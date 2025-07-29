import 'dart:async';
import 'package:flutter/services.dart';

class FletNfc {
  static const MethodChannel _channel = MethodChannel('flet_nfc');
  static const EventChannel _eventChannel = EventChannel('flet_nfc/events');

  static Stream<String>? _onTagDiscovered;
  
  /// Inicia o modo leitor NFC.
  static Future<void> startSession() async {
    await _channel.invokeMethod('startSession');
  }
  
  /// Encerra o modo leitor NFC.
  static Future<void> stopSession() async {
    await _channel.invokeMethod('stopSession');
  }
  
  /// Fluxo de eventos com o ID (UID) da tag lida.
  static Stream<String> get onTagDiscovered {
    _onTagDiscovered ??= _eventChannel
      .receiveBroadcastStream()
      .map((event) => event.toString());
    return _onTagDiscovered!;
  }
}
