// import 'package:flutter/material.dart';
// import 'package:flet/flet.dart';
// import 'package:flutter_nfc_kit/flutter_nfc_kit.dart';

// class NfcfletControl extends StatelessWidget {
//   final Control? parent;
//   final Control control;

//   const NfcfletControl({
//     super.key,
//     required this.parent,
//     required this.control,
//   });

//   @override
//   Future<Widget> build(BuildContext context) async {
//     String text = control.attrString("text", "")!;
//     String x = control.attrString("x", "")!;
//     late final Widget content;

//     if (text == "readNFC") {
//       try {
//         NFCTag tag = await FlutterNfcKit.poll(timeout: Duration(seconds: 2));
//         if (tag.ndefAvailable == true) {
//           NDEFMessage? message = await FlutterNfcKit.readNDEF();
//           message?.records.forEach((r) {
//             final tagtext = r.payload.length > 3
//               ? String.fromCharCodes(r.payload.sublist(3))
//               : '';
//             content = Text(text);
//           ''});
//         }
//       } catch e {
//         content = Text("Error: $e")
//       } finally {
//         await FlutterNfcKit.finish();
//       }
//     } else if (text == "") {
//       try {
//         NFCTag tag = await FlutterNfcKit.poll(timeout: Duration(seconds: 2));
//           await FlutterNfcKit.writeNDEFRecords([
//           NDEFRecord.text(x),
//         ]);
//       }  catch e {
//         content = Text("Error: $e")
//       } finally {
//         await FlutterNfcKit.finish();
//       }
//     } else {
//       return const SizedBox.shrink();
//     }

//     return constrainedControl(
//       context,
//       content,
//       parent,
//       control,
//     );
//   }
// }

import 'dart:typed_data';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flet/flet.dart';
import 'package:flutter_nfc_kit/flutter_nfc_kit.dart'
import 'package:nfc_manager/nfc_manager.dart';
import 'dart:async';

class NfcfletControl extends StatelessWidget {
  final Control? parent;
  final Control control;

  const NfcfletControl({
    super.key,
    required this.parent,
    required this.control,
  });

  Future<String> readTag() {
    final completer = Completer<String>();

    NfcManager.instance.startSession(
      onDiscovered: (NfcTag tag) {
        final ndef = Ndef.from(tag);
        if (ndef == null || ndef.cachedMessage == null) {
          completer.completeError('Tag não formatada');
          NfcManager.instance.stopSession(errorMessage: 'NDEF esperado');
          return;
        }
        final record = ndef.cachedMessage!.records.first;
      // payload[0–2] = status + language code (per NDEF spec)
        final raw = record.payload;
        final text = String.fromCharCodes(raw.sublist(3));
        completer.complete(text);
        NfcManager.instance.stopSession();
      },
      onError: (e) {
        completer.completeError(e);
      },
    );

    return completer.future;
  }

  Future<bool> writeTag(String text) async {
    if (!await NfcManager.instance.isAvailable()) return false;

    final message = NdefMessage([
      NdefRecord.createText(text)
    ]);

    final completer = Completer<bool>();

    NfcManager.instance.startSession(
      onDiscovered: (NfcTag tag) async {
        final ndef = Ndef.from(tag);
        if (ndef == null || !ndef.isWritable) {
          completer.complete(false);
          NfcManager.instance.stopSession(errorMessage: 'Error');
          return;
        }
        try {
          await ndef.write(message);
          completer.complete(true);
          NfcManager.instance.stopSession(alertMessage: 'Tag writed with success.');
        } catch (e) {
          completer.complete(false);
          NfcManager.instance.stopSession(errorMessage: e.toString());
        }
      },
      onError: (error) {
        if (!completer.isCompleted) {
          completer.complete(false);
        }
      },
    );

    return completer.future;
  }


  @override
  Widget build(BuildContext context) {
    final text = control.attrString("text", "")!;
    final x = control.attrString("x", "")!;

    if (text == "readNFC") {
      return FutureBuilder<String>(
        future: readNfc(),
        builder: (ctx, snap) {
          Widget content;

          if (snap.hasData) {
            content = Text('${snap.data!}');
          } else {
            content = Text('Error on NFC read.');
          }

          return constrainedControl(context, content, parent, control);
        },
      );
    } else if (text == "writeNFC") {
      return FutureBuilder<bool>(
        future: writeNfc(x),
        builder: (ctx, snap) {
          Widget content;

          if (snap.hasData) {
            content = Text("Success NFC write.");
          } else {
            content = Text("Error on NFC write.");
          }

          return constrainedControl(context, content, parent, control);
        },
      );
    } else {
      return const SizedBox.shrink();
    }
  }
}
