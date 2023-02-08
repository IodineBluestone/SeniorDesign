//
//  ContentView.swift
//  ParkWise
//
//  Created by Parker Muery on 2/6/23.
//

import SwiftUI

extension Color {
    static let navy = Color(red: 0, green: 0, blue: 199/255)
}

struct ContentView: View {
    @State private var selectedLot = "Pharmacy Lot"
    let lotNames = ["Pharmacy Lot", "Northern Lot", "Rec Lot", "Arena Lot"]
    var spotOne = CarSpot(spotOpen: false,spotNumber: 20)
    var spotTwo = CarSpot(spotOpen: false,spotNumber: 20)
    var spotThree = CarSpot(spotOpen: false,spotNumber: 20)
    @State private var pharmacyLot : [CarSpot] = []
    
    init() {
        UINavigationBar.appearance().largeTitleTextAttributes = [.foregroundColor: UIColor( .white) ]
        UINavigationBar.appearance().titleTextAttributes = [.foregroundColor: UIColor( .white)]
          }
    
    var body: some View {
        NavigationView {
            VStack{
                HStack{
                    Text("\(selectedLot)")
                    Spacer()
                    Menu("Select Lot"){
                        ForEach(lotNames, id: \.self) { lotName in
                            Button(action:{
                                doSomething(lotName)
                            })
                            {
                                Text("\(lotName)")
                            }
                        }
                        
                    }
                }.foregroundColor(.white)
                .padding()
                .frame(maxWidth: .infinity)
                .background(RoundedRectangle(cornerRadius: 10).fill(.black))
                
                    Spacer()
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
                Spacer()
                
            }
            .padding()
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .background(Color.navy)
            .navigationTitle("ParkWise")
        }
        }
    
    func doSomething(_ pressedLot: String) {
        selectedLot = pressedLot
    }
    struct CarSpot: View {
        @State var spotOpen = true
        @State var spotNumber = 100
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
    }




struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}


