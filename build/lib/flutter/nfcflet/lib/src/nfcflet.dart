import 'package:flutter/material.dart';
import 'package:flet/flet.dart';

class NfcfletControl extends StatelessWidget {
  final Control? parent;
  final Control control;

  const NfcfletControl({
    Key? key,
    required this.parent,
    required this.control,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Puxa o valor atual de 'text' do lado Python
    final text = control.attrString('text') ?? '';

    // Cria o widget de texto
    final content = Text(
      text,
      style: const TextStyle(fontSize: 16),
    );

    // Envolve no constrainedControl para posicionamento e eventos
    return constrainedControl(
      context,
      content,
      parent,
      control,
    );
  }
}
