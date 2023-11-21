package com.udocoin.udocoin_wallet

import android.annotation.SuppressLint
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.udocoin.udocoin_wallet.modules.KeyManager

class MainActivity : AppCompatActivity() {
    private val TAG = "[MAIN ACTIVITY]"
    lateinit var keyManager: KeyManager

    @SuppressLint("SetTextI18n")
    override fun onCreate(savedInstanceState: Bundle?) {
        Log.d(TAG,"HELLO FROM MAIN ACTIVITY ON CREATE")
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        keyManager = KeyManager.getInstance()

        /** go to login activity if there are no keys */
        if(!keyManager.hasValidKeys(this)){
            Log.d(TAG,"No keys found. Returning to Login Activity")
            Toast.makeText(this, "No keys found.",Toast.LENGTH_SHORT).show()
            val intent = Intent(this, LoginActivity::class.java)
            startActivity(intent)
            finish()
        }
        val privKey = keyManager.getPrivateKey(this)
        val pubKey = keyManager.getPublicKey(this)
        findViewById<TextView>(R.id.text1).text = privKey
        findViewById<TextView>(R.id.text2).text = pubKey

        findViewById<Button>(R.id.reset_keys).setOnClickListener { resetKeys() }
        findViewById<Button>(R.id.create_transaction).setOnClickListener { startTransaction() }
    }

    private fun resetKeys(){
        keyManager.setPrivateKey(this,"")
        keyManager.setPublicKey(this,"")
        val intent = Intent(this, LoginActivity::class.java)
        startActivity(intent)
    }

    private fun startTransaction(){
        val intent = Intent(this, CodeScannerActivity::class.java)
        intent.putExtra("redirectActivity","TransactionActivity")
        startActivity(intent)
    }
}