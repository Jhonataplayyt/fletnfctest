import 'package:flutter/material.dart';
import 'package:flet/flet.dart';
import 'package:nfcflet/nfcflet.dart';

void main() {
    WidgetsFlutterBinding.ensureInitialized();

  // registra a fábrica de controles e inicializa o Python embutido
    registerUserExtensions(
        createControl,      // de src/create_control.dart
        ensureInitialized,  // reexportado de package:flet/flet.dart
    );

    runApp(
        FletView(),         // ou configure host/port se for remoto
    );
}