//
//  DataModel.swift
//  ParkWise
//
//  Created by Parker Muery on 2/15/23.
//

import SwiftUI

@MainActor
class DataModel: ObservableObject {
    
    @Published var selectedLotDisplay = "Pharmacy Lot"
    @Published var selectedLot: [CarSpot] = []
    
    let lotNames = ["Pharmacy Lot", "Northern Lot", "Rec Lot", "Arena Lot"]
    
    var pharmacyLot : [CarSpot] =
    [
        CarSpot(spotOpen: false,spotNumber: 20),
        CarSpot(spotOpen: true,spotNumber: 200),
        CarSpot(spotOpen: false,spotNumber: 35),
        CarSpot(spotOpen: false,spotNumber: 21),
        CarSpot(spotOpen: true,spotNumber: 201),
        CarSpot(spotOpen: false,spotNumber: 36),
        CarSpot(spotOpen: false,spotNumber: 22),
        CarSpot(spotOpen: true,spotNumber: 222),
        CarSpot(spotOpen: false,spotNumber: 39),
        CarSpot(spotOpen: false,spotNumber: 40)
        
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
        CarSpot(spotOpen: true,spotNumber: 19),
        CarSpot(spotOpen: true,spotNumber: 30),
        CarSpot(spotOpen: false,spotNumber: 35)
    ]
    func openSpots() -> Double {
        var count: Double = 0.0
        for (index,_) in selectedLot.enumerated() {
            if(selectedLot[index].spotOpen == true) {
                count = count + 1
            }
        }
        return count
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

struct CarSpot: Identifiable {
    var id: Int {
        return spotNumber
    }
    var spotOpen = true
    var spotNumber = 100
}
