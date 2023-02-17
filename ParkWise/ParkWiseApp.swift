//
//  ParkWiseApp.swift
//  ParkWise
//
//  Created by Parker Muery on 2/6/23.
//

import SwiftUI

@main
struct ParkWiseApp: App {
    @StateObject var model = DataModel()
    
    var body: some Scene {
        WindowGroup {
            ContentView(model: model)
        }
    }
}
