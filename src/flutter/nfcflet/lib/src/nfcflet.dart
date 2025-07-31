import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

/// 1. Declare your factory
class NFCFletControlFactory implements ControlFactory {
  @override
  String get controlName => "nfcflet";

  @override
  ControlDefinition create() {
    return FletControl(
      name: controlName,
      createWidget: (ctr) => _NFCFletWidget(ctr),
    );
  }
}

/// 2. Your stateful widget
class _NFCFletWidget extends StatefulWidget {
  final Control ctr;
  const _NFCFletWidget(this.ctr, {Key? key}) : super(key: key);

  @override
  State<_NFCFletWidget> createState() => _NFCFletState();
}

/// 3. The State implementation
class _NFCFletState extends State<_NFCFletWidget> {
  late final MethodChannel _channel;

  @override
  void initState() {
    super.initState();
    _channel = MethodChannel(widget.ctr.id);
    _channel.setMethodCallHandler(_handleCalls);
  }

  Future<dynamic> _handleCalls(MethodCall call) async {
    switch (call.method) {
      case "readNFC":
        return _readNFCAsync();
      case "writeNFC":
        return _writeNFCAsync(call.arguments);
      default:
        throw MissingPluginException();
    }
  }

  Future<String> _readNFCAsync() async {
    await Future.delayed(const Duration(milliseconds: 500));
    return "mock‐tag‐payload";
  }

  Future<String> _writeNFCAsync(dynamic data) async {
    await Future.delayed(const Duration(milliseconds: 500));
    return data.toString();
  }

  @override
  Widget build(BuildContext context) => const SizedBox.shrink();
}

void ensureInitialized() {
  Flet.registerControl(NFCFletControlFactory());
}
