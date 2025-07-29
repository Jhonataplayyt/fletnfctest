import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'flet_nfc_ext.dart';

Control createControl(ControlArgs args) {
  switch (args.control.type) {
    case 'flet_nfc_ext':
      return FletNfcExtControl(
        parent: args.parentControl,
        control: args.control,
      );
    default:
      return UnimplementedControl();
  }
}

void ensureInitialized() {
  // qualquer inicialização global
}

final extension = Extension(
  id: 'flet_nfc_ext',
  createControl: createControl,
  ensureInitialized: ensureInitialized,
);
