import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:nfc_manager/nfc_manager.dart';          // <= seu plugin
import 'package:flet/flet.dart';

void registerPlugins(Registrar registrar) {
  NfcManager.instance;                                  // inicializa o plugin
  // outros plugins…
  registrar.registerMessageCodec();
}