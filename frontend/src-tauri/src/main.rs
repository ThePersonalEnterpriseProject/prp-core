// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use tauri::api::process::{Command, CommandEvent};

fn main() {
  tauri::Builder::default()
    .setup(|app| {
      let (mut rx, child) = Command::new_sidecar("api")
        .expect("failed to create `api` binary command")
        .spawn()
        .expect("Failed to spawn sidecar");

      tauri::async_runtime::spawn(async move {
        // read events such as stdout
        while let Some(event) = rx.recv().await {
          if let CommandEvent::Stdout(line) = event {
            println!("API: {}", line);
          } else if let CommandEvent::Stderr(line) = event {
             eprintln!("API ERR: {}", line);
          }
        }
      });

      Ok(())
    })
    .run(tauri::generate_context!())
    .expect("error while running tauri application");
}
