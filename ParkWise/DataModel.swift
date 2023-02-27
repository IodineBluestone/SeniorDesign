//
//  DataModel.swift
//  ParkWise
//
//  Created by Parker Muery on 2/15/23.
//

import SwiftUI
import FirebaseDatabase


struct ParkWise: Identifiable, Codable {
    var id: String
    var spot1: Bool
    var spot2: Bool
    var spot3: Bool
    var time: String
    
}


@MainActor
class DataModel: ObservableObject {


    
    @Published var selectedLotDisplay = "Pharmacy Lot"
    @Published var selectedLot: [CarSpot] = []
    let lotNames = ["Pharmacy Lot", "Northern Lot", "Rec Lot", "Arena Lot", "Model Lot"]
    @Published var testPark: ParkWise = ParkWise(id: "1", spot1: true, spot2: true, spot3: true, time: "2")
    @Published var parking: [ParkWise] = [
        ParkWise(id: "1", spot1: true, spot2: true, spot3: true, time: "2")
        ]

    private lazy var databasePath: DatabaseReference? = {
        let ref = Database.database().reference().child("AUParking/parking")  //Change to AU Parking Pharmacy
        return ref
    }()

    //private let encoder = JSONEncoder()
    private let decoder = JSONDecoder()

    func listentoRealtimeDatabase() {
        guard let databasePath = databasePath else {
            return
        }

        databasePath.observe(.value) { [weak self] snapshot in
                guard
                    let self = self,
                    var json = snapshot.value as? [String: Any]
                else {
                    return
                }
                json["id"] = snapshot.key
                do {
                    let parkingData = try JSONSerialization.data(withJSONObject: json)
                    let park = try self.decoder.decode(ParkWise.self, from: parkingData)
                    self.testPark = park
                    self.parking.append(park)
                } catch {
                    print("an error occurred", error)
                }            }
       
    }


//    func stopListening() {
//        databasePath?.removeAllObservers()
//    }
    
    var pharmacyLot : [CarSpot] =
    [
      //  CarSpot(spotOpen: testPark.spot1,spotNumber: 20),
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
    var modelLot : [CarSpot] =
    [
        CarSpot(spotOpen: true,spotNumber: 1),
        CarSpot(spotOpen: true,spotNumber: 2),
        CarSpot(spotOpen: false,spotNumber: 3),
        CarSpot(spotOpen: true,spotNumber: 4),
        CarSpot(spotOpen: true,spotNumber: 5),
        CarSpot(spotOpen: false,spotNumber: 6)
        
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
        case "Model Lot":
            selectedLot = modelLot
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
