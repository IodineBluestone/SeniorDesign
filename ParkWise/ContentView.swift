//
//  ContentView.swift
//  ParkWise
//
//  Created by Parker Muery on 2/6/23.
//

import SwiftUI

extension Color {
    static let navy = Color(red: 0, green: 0, blue: 128/255)
}

struct ContentView: View {
    @State private var spot_one = false
    @State private var spot_two = false
    @State private var spot_three = false
    let spotOne = CarSpot(spotOpen: false,spotNumber: 20)
    let navy = Color(red: 0, green: 0, blue: 128/255)
    init() {
        UINavigationBar.appearance().largeTitleTextAttributes = [.foregroundColor: UIColor( .white) ]
        UINavigationBar.appearance().titleTextAttributes = [.foregroundColor: UIColor( .white)]
          }
    
    var body: some View {
        NavigationView {
                Grid{
                    GridRow{
                        spotOne
                        spotOne
                        spotOne
                    }
                    GridRow{
                        spotOne
                        spotOne
                        spotOne
                    }
                    GridRow{
                        spotOne
                        spotOne
                        spotOne
                    }
                }
            .padding()
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .background(.blue)
            .navigationTitle("ParkWise")
        }
        }
    }

struct CarSpot: View {
    @State  var spotOpen = true
    @State  var spotNumber = 100
    var body: some View {
            VStack{
                HStack{
                    Spacer()
                    Text("#\(spotNumber)")
                }
                
                HStack{
                    Text(spotOpen ?" 🟢" : " 🚗")
                        .font(.title)
                }
                .padding()
                HStack{
                    Text(spotOpen ? "Open" : "Taken")
                    Spacer()
                }
            }
            .padding()
            .background(.white)
            .cornerRadius(10)
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}


