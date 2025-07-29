package com.example.flet_nfc;

import android.app.Activity;
import android.app.PendingIntent;
import android.content.Intent;
import android.nfc.NfcAdapter;
import android.nfc.Tag;
import android.os.Build;
import android.os.Bundle;
import androidx.annotation.NonNull;
import io.flutter.embedding.engine.plugins.activity.ActivityAware;
import io.flutter.embedding.engine.plugins.activity.ActivityPluginBinding;
import io.flutter.embedding.engine.plugins.FlutterPlugin;
import io.flutter.plugin.common.EventChannel;
import io.flutter.plugin.common.MethodCall;
import io.flutter.plugin.common.MethodChannel;

public class FletNfcPlugin implements FlutterPlugin, MethodChannel.MethodCallHandler,
        ActivityAware, EventChannel.StreamHandler {

    private MethodChannel methodChannel;
    private EventChannel eventChannel;
    private EventChannel.EventSink eventSink;
    private Activity activity;
    private NfcAdapter nfcAdapter;
    private PendingIntent pendingIntent;

    @Override
    public void onAttachedToEngine(@NonNull FlutterPluginBinding binding) {
        methodChannel = new MethodChannel(binding.getBinaryMessenger(), "flet_nfc");
        methodChannel.setMethodCallHandler(this);

        eventChannel = new EventChannel(binding.getBinaryMessenger(), "flet_nfc/events");
        eventChannel.setStreamHandler(this);
    }

    // ActivityAware callbacks
    @Override
    public void onAttachedToActivity(ActivityPluginBinding binding) {
        activity = binding.getActivity();
        nfcAdapter = NfcAdapter.getDefaultAdapter(activity);

        Intent intent = new Intent(activity, activity.getClass())
                .addFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP);
        int flags = Build.VERSION.SDK_INT >= Build.VERSION_CODES.S
                    ? PendingIntent.FLAG_MUTABLE
                    : 0;
        pendingIntent = PendingIntent.getActivity(activity, 0, intent, flags);

        binding.addOnNewIntentListener(this::onNewIntent);
    }

    private boolean onNewIntent(Intent intent) {
        String action = intent.getAction();
        if (action != null && (action.equals(NfcAdapter.ACTION_TAG_DISCOVERED)
            || action.equals(NfcAdapter.ACTION_NDEF_DISCOVERED)
            || action.equals(NfcAdapter.ACTION_TECH_DISCOVERED))) {

            Tag tag = intent.getParcelableExtra(NfcAdapter.EXTRA_TAG);
            if (tag != null && eventSink != null) {
                byte[] id = tag.getId();
                // Transforma em hex
                StringBuilder sb = new StringBuilder();
                for (byte b : id) {
                    sb.append(String.format("%02X", b));
                }
                eventSink.success(sb.toString());
            }
        }
        return true;
    }

    @Override
    public void onDetachedFromActivityForConfigChanges() { }
    @Override
    public void onReattachedToActivityForConfigChanges(ActivityPluginBinding binding) { }
    @Override
    public void onDetachedFromActivity() { }

    // MethodChannel handler
    @Override
    public void onMethodCall(MethodCall call, MethodChannel.Result result) {
        switch (call.method) {
            case "startSession":
                nfcAdapter.enableForegroundDispatch(activity, pendingIntent, null, null);
                result.success(null);
                break;
            case "stopSession":
                nfcAdapter.disableForegroundDispatch(activity);
                result.success(null);
                break;
            default:
                result.notImplemented();
        }
    }

    // EventChannel handler
    @Override
    public void onListen(Object args, EventChannel.EventSink sink) {
        this.eventSink = sink;
    }

    @Override
    public void onCancel(Object args) {
        this.eventSink = null;
    }

    @Override
    public void onDetachedFromEngine(@NonNull FlutterPluginBinding binding) {
        methodChannel.setMethodCallHandler(null);
        eventChannel.setStreamHandler(null);
    }
}
