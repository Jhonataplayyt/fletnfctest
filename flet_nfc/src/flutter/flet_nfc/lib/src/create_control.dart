import 'package:nfc_manager/nfc_manager.dart';
import 'package:flet/flet.dart';
import 'package:flutter/widgets.dart';

Widget createControl(Control control, Control? parent) {
  switch (control.type) {
    case "nfc_reader":
      return _NfcReaderWidget(parent: parent, control: control);
    // outros cases…
  }
}
