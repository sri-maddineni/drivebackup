package com.example.activitylifecycle

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }


    override fun onStart() {
        super.onStart()
        println("On start is called;")
    }

    override fun onRestart() {
        super.onRestart()
        println("On start is called;")
    }


    override fun onPause() {
        super.onPause()
        println("On pause is called;")
    }

    override fun onResume() {
        super.onResume()
        println("On resume is called;")
    }

    override fun onStop() {
        super.onStop()
        println("On stop is called;")
    }

    override fun onDestroy() {
        super.onDestroy()
        println("On destroy is called;")
    }

}