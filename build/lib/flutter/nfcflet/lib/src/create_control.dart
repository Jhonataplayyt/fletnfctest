// lib/src/create_control.dart

import 'package:flutter/widgets.dart';
import 'package:flet/src/control_factory.dart';
import 'package:flet/flet.dart';            // <-- para usar o ensureInitialized “de verdade”
import 'nfcflet_control.dart';

Widget? createControl(CreateControlArgs args) {
  final control = args.control;
  final parent  = args.parent;
  if (control.type == 'nfcflet') {
    return NfcfletControl(parent: parent, control: control);
  }
  return null;
}
