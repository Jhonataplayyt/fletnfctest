// lib/nfcflet.dart

library nfcflet;

// exporte apenas o createControl;  
// NÃO exporte seu stub de ensureInitialized
export "src/create_control.dart" show createControl;

// importe e reexporte o ensureInitialized de dentro do Flet
export "package:flet/flet.dart" show ensureInitialized;
