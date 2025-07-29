package com.yourcompany.yourapp;

import android.app.Activity;
import android.nfc.NfcAdapter;
import android.nfc.Tag;
import android.content.Intent;
import android.util.Log;

import java.util.HashMap;
import java.util.Map;

import io.flutter.embedding.engine.FlutterEngine;
import io.flutter.plugin.common.MethodCall;
import io.flutter.plugin.common.MethodChannel;

public class NfcPlugin implements MethodChannel.MethodCallHandler {
    private final Activity activity;

    public static void registerWith(FlutterEngine flutterEngine, Activity activity) {
        MethodChannel channel = new MethodChannel(flutterEngine.getDartExecutor(), "flet_nfc_channel");
        NfcPlugin instance = new NfcPlugin(activity);
        channel.setMethodCallHandler(instance);
    }

    private NfcPlugin(Activity activity) {
        this.activity = activity;
    }

    @Override
    public void onMethodCall(MethodCall call, MethodChannel.Result result) {
        if (call.method.equals("scanNfc")) {
            // Aqui você precisa implementar a lógica de leitura NFC
            // Exemplo: retornar dummy data para teste
            Map<String, String> data = new HashMap<>();
            data.put("uid", "04:A2:34:56:78");
            data.put("payload", "NFC");
            result.success(data);
        } else {
            result.notImplemented();
        }
    }
}
