//
//  ParkWiseApp.swift
//  ParkWise
//
//  Created by Parker Muery on 2/6/23.
//


import SwiftUI
import Firebase

@main
struct ParkWiseApp: App {
    init() {
        FirebaseApp.configure()
    }
    @StateObject var model = DataModel()
    
    var body: some Scene {
        WindowGroup {
            ContentView(model: model)
        }
    }
}
