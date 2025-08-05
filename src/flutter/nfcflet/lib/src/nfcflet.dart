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

// lib/src/nfcflet.dart

import 'dart:async';
import 'package:flutter/material.dart';
import 'package:nfc_manager/nfc_manager.dart';
import 'package:flet/flet.dart';

/// Um Control Flet para ler e escrever em tags NFC.
/// Dispara eventos "nfc-result" com payload {"value": String} ou {"error": String}.
class NfcfletControl extends StatelessWidget {
  final Control? parent;
  final Control control;
  static bool _isProcessing = false;

  const NfcfletControl({
    Key? key,
    required this.parent,
    required this.control,
  }) : super(key: key);

  /// Inicia sessão NFC para leitura, completa com o texto lido ou erro.
  Future<String> readTag({Duration timeout = const Duration(seconds: 20)}) {
    final completer = Completer<String>();
    // timeout
    Timer(timeout, () {
      if (!completer.isCompleted) {
        completer.completeError('Timeout on NFC read');
        NfcManager.instance.stopSession(errorMessage: 'Timeout NFC');
      }
    });

    NfcManager.instance.startSession(
      onDiscovered: (tag) async {
        try {
          final ndef = Ndef.from(tag);
          if (ndef == null || ndef.cachedMessage == null) {
            throw 'Tag not formatted';
          }
          final record = ndef.cachedMessage!.records.first;
          final payload = record.payload.sublist(3);
          final text = String.fromCharCodes(payload);
          completer.complete(text);
        } catch (e) {
          completer.completeError(e);
        } finally {
          await NfcManager.instance.stopSession();
        }
      },
      onError: (error) async {
        if (!completer.isCompleted) {
          completer.completeError(error);
        }
        await NfcManager.instance.stopSession(errorMessage: error.toString());
      },
    );

    return completer.future;
  }

  /// Inicia sessão NFC para escrita, completa com true ou erro.
  Future<bool> writeTag(
    String text, {
    Duration timeout = const Duration(seconds: 20),
  }) async {
    if (!await NfcManager.instance.isAvailable()) {
      throw 'NFC not available';
    }

    final completer = Completer<bool>();
    // timeout
    Timer(timeout, () {
      if (!completer.isCompleted) {
        completer.completeError('Timeout on NFC write');
        NfcManager.instance.stopSession(errorMessage: 'Timeout NFC');
      }
    });

    final message = NdefMessage([NdefRecord.createText(text)]);

    NfcManager.instance.startSession(
      onDiscovered: (tag) async {
        try {
          final ndef = Ndef.from(tag);
          if (ndef == null || !ndef.isWritable) {
            throw 'Cannot write to tag';
          }
          await ndef.write(message);
          completer.complete(true);
        } catch (e) {
          completer.completeError(e);
        } finally {
          await NfcManager.instance.stopSession();
        }
      },
      onError: (error) async {
        if (!completer.isCompleted) {
          completer.completeError(error);
        }
        await NfcManager.instance.stopSession(errorMessage: error.toString());
      },
    );

    return completer.future;
  }

  /// Dispara evento Flet "nfc-result" para o frontend Python/JS
  void _dispatchResult(Map<String, dynamic> payload) {
    dispatchControlEvent(control, "nfc-result", payload);
  }

  @override
  Widget build(BuildContext context) {
    final cmd = control.attrString("text", "")!;
    final value = control.attrString("x", "")!;

    // Executa apenas uma vez por comando
    if (!_isProcessing && cmd.isNotEmpty) {
      _isProcessing = true;

      if (cmd == "read") {
        readTag().then((tag) {
          _dispatchResult({"value": tag});
        }).catchError((e) {
          _dispatchResult({"error": e.toString()});
        }).whenComplete(() {
          _isProcessing = false;
        });
      } else if (cmd == "write") {
        writeTag(value).then((_) {
          _dispatchResult({"value": value});
        }).catchError((e) {
          _dispatchResult({"error": e.toString()});
        }).whenComplete(() {
          _isProcessing = false;
        });
      } else {
        // comando desconhecido
        _dispatchResult({"error": "Unknown command: $cmd"});
        _isProcessing = false;
      }
    }

    // Retorna um container vazio pois toda a interação é via evento
    return const SizedBox.shrink();
  }
}
