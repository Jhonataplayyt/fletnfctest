import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter_nfc_kit/flutter_nfc_kit.dart';

class NfcfletControl extends StatelessWidget {
  final Control? parent;
  final Control control;

  const NfcfletControl({
    super.key,
    required this.parent,
    required this.control,
  });

  @override
  _NFCState createState() => _NFCState();
}

class _NFCState extends State<NfcfletControl> {
  dynamic _lastRequest;

  @override
  void didUpdateWidget(covariant NfcfletControl oldWidget) {
    super.didUpdateWidget(oldWidget);

    final req = widget.control.attrDynamic("request_payload");
    if (req != null && widget.control.attrDynamic("request_payload")) {
      _lastRequest = req;

      final result = _readNFC(req);

      widget.control.backend.triggerControlEvent(
        widget.control.id,
        "response",
        {'value': result},
      );

      widget.control.backend.setControlAttr(
        widget.control.id,
        "request_payload",
        null,
      );
    }
  }

  Future<String?> _readNFC async {
    try {
      NFCTag tag = await FlutterNfcKit.poll();

      return tag.id ?? tag.ndefMessage?.toString();
    } catch (e) {
      print('Erro ao ler o NFC: $e');

      return null;
    } finally {
      await FlutterNfcKit.finish()
    }
  }
}
