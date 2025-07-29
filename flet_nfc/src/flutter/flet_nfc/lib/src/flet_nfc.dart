import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter_nfc_kit/flutter_nfc_kit.dart';
import 'package:flet/flet.dart';

class FletNfcExtControl extends StatelessWidget {
  final Control control;
  final Control? parent;

  const FletNfcExtControl({
    super.key,
    required this.parent,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () async {
        // exemplo simples: lê ID da tag
        NFCTag tag = await FlutterNfcKit.poll();
        await FlutterNfcKit.finish();
        // envia de volta para Python
        control.backend.triggerControlEvent(
          control.id,
          jsonEncode({'id': tag.id}),
        );
      },
      child: Container(
        width: control.attrDouble('width'),
        height: control.attrDouble('height'),
        color: Colors.grey.shade200,
        alignment: Alignment.center,
        child: Text('Toque para ler NFC'),
      ),
    );
  }
}
