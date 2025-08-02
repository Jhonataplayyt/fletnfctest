import 'package:flutter/material.dart';
import 'package:flet/flet.dart';

class NfcfletControl extends StatelessWidget {
  final Control? parent;
  final Control control;

  const NfcfletControl({
    super.key,
    required this.parent,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    String text = control.attrString("text", "")!;
    String x = control.attrString("x", "")!;
    late final Widget content;

    if (text == "readNFC") {
      content = Text(text);
    } else if (text == "writeNFC") {
      content = Text(x);
    } else {
      return const SizedBox.shrink();
    }

    return constrainedControl(
      context,
      content,
      parent,
      control,
    );
  }
}
