class _NfcReaderWidget extends StatefulWidget {
  final Control? parent;
  final Control control;
  const _NfcReaderWidget({this.parent, required this.control});

  @override
  State<_NfcReaderWidget> createState() => _NfcReaderWidgetState();
}

class _NfcReaderWidgetState extends State<_NfcReaderWidget> {
  @override
  void initState() {
    super.initState();
    NfcManager.instance.startSession(onDiscovered: (tag) {
      widget.backend.triggerControlEvent(
        widget.control.id,
        "tag_discovered",
        {"id": tag.id},
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return constrainedControl(
      context,
      Text("Aproxime o cartão…"),
      widget.parent,
      widget.control,
    );
  }

  @override
  void dispose() {
    NfcManager.instance.stopSession();
    super.dispose();
  }
}
