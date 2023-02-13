//
//  ContentView.swift
//  ParkWise
//
//  Created by Parker Muery on 2/6/23.
//

import SwiftUI

extension Color {
    static let wholeBackground = Color(red: 244/255, green: 239/255, blue: 238/255)
}

struct ContentView: View {
    @State private var selectedLotDisplay = "Pharmacy Lot"
    @State private var selectedLot : [CarSpot] = []
    let lotNames = ["Pharmacy Lot", "Northern Lot", "Rec Lot", "Arena Lot"]
    var pharmacyLot : [CarSpot] =
    [
        CarSpot(spotOpen: false,spotNumber: 20),
        CarSpot(spotOpen: true,spotNumber: 200),
        CarSpot(spotOpen: false,spotNumber: 35)
    ]
    var northernLot : [CarSpot] =
    [
        CarSpot(spotOpen: false,spotNumber: 80),
        CarSpot(spotOpen: true,spotNumber: 81),
        CarSpot(spotOpen: false,spotNumber: 82)
    ]
    var recLot : [CarSpot] =
    [
        CarSpot(spotOpen: false,spotNumber: 10),
        CarSpot(spotOpen: true,spotNumber: 55),
        CarSpot(spotOpen: false,spotNumber: 44)
    ]
    var arenaLot : [CarSpot] =
    [
        CarSpot(spotOpen: false,spotNumber: 19),
        CarSpot(spotOpen: true,spotNumber: 30),
        CarSpot(spotOpen: false,spotNumber: 35)
    ]
    init() {
        UINavigationBar.appearance().largeTitleTextAttributes = [.foregroundColor: UIColor( .black) ]
        UINavigationBar.appearance().titleTextAttributes = [.foregroundColor: UIColor( .black)]
    }
    
    var body: some View {
        NavigationView {
            VStack{
                HStack{
                    Text("\(selectedLotDisplay)")
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
                
                ScrollView{
                    Grid{
                        GridRow{
                            ForEach(0..<selectedLot.count, id: \.self) { lot in
                                CardView(cardData: selectedLot[lot])
                                
                            }
                        }
                        Rectangle()
                             .frame(maxWidth:.infinity,minHeight:30)
                             .foregroundColor(.gray)
                             .ignoresSafeArea()
                      
                        

                        GridRow{
                            ForEach(0..<selectedLot.count, id: \.self) { lot in
                                CardView(cardData: selectedLot[lot])
                                
                            }
                        }
                        GridRow{
                            ForEach(0..<selectedLot.count, id: \.self) { lot in
                                CardView(cardData: selectedLot[lot])
                                
                            }
                        }
                        
                        GridRow{
                            ForEach(0..<selectedLot.count, id: \.self) { lot in
                                CardView(cardData: selectedLot[lot])
                                
                            }
                        }
                        GridRow{
                            ForEach(0..<selectedLot.count, id: \.self) { lot in
                                CardView(cardData: selectedLot[lot])
                            }
                        }
                    }
                }
                Spacer()
                
            }
            .ignoresSafeArea()
            .padding()
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .background(Color.wholeBackground)
            .navigationTitle("ParkWise")
        }
        .onAppear(){
            doSomething("Pharmacy Lot")
        }
    }
    
    func doSomething(_ pressedLot: String) {
        selectedLotDisplay = pressedLot
        switch pressedLot {
        case "Pharmacy Lot":
            selectedLot = pharmacyLot
        case "Northern Lot":
            selectedLot = northernLot
        case "Rec Lot":
            selectedLot = recLot
        case "Arena Lot":
            selectedLot = arenaLot
        default:
            selectedLot = pharmacyLot
        }
    }
    
}
struct CarSpot {
    var spotOpen = true
    var spotNumber = 100
    
}
struct CardView: View {
    
    var cardData: CarSpot
    
    var body: some View {
        VStack{
            HStack{
                Spacer()
                Text("#\(cardData.spotNumber)")
            }
            
            HStack{
                Text(cardData.spotOpen ?" 🟢" : " 🚗")
                    .font(.title)
            }
            .padding()
            HStack{
                Text(cardData.spotOpen ? "Open" : "Taken")
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


