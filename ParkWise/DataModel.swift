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
    var spot10: Bool
    var spot11: Bool
    var spot12: Bool
    var spot2: Bool
    var spot3: Bool
    var spot4: Bool
    var spot5: Bool
    var spot6: Bool
    var spot7: Bool
    var spot8: Bool
    var spot9: Bool
    var time: String
    
}


@MainActor
class DataModel: ObservableObject {

    @Published var selectedLotDisplay = "Pharmacy Lot"
    @Published var selectedLot: [CarSpot] = [
        CarSpot(spotOpen:true,spotNumber:1)]
    @Published var testPark: ParkWise = ParkWise(
        id: "1", spot1: true, spot10: true, spot11: true, spot12: true , spot2: true  ,spot3: true, spot4: true,
        spot5: true, spot6: true, spot7: true, spot8: true, spot9: true , time: "2")
    var modelLot : [CarSpot] = []
    let lotNames = ["Pharmacy Lot", "Northern Lot", "Rec Lot", "Arena Lot", "Model Lot"]
    private lazy var databasePath: DatabaseReference? = {
        let ref = Database.database().reference().child("AUParking/parking")  //Change to AU Parking Pharmacy
        return ref
    }()
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
                    if self.selectedLotDisplay == "Model Lot" {
                        self.modelLot =
                        [
                            CarSpot(spotOpen: park.spot1,spotNumber: 1),
                            CarSpot(spotOpen: park.spot2,spotNumber: 2),
                            CarSpot(spotOpen: park.spot3,spotNumber: 3),
                            CarSpot(spotOpen: park.spot4,spotNumber: 4),
                            CarSpot(spotOpen: park.spot5,spotNumber: 5),
                            CarSpot(spotOpen: park.spot6,spotNumber: 6),
                            CarSpot(spotOpen: park.spot7,spotNumber: 7),
                            CarSpot(spotOpen: park.spot8,spotNumber: 8),
                            CarSpot(spotOpen: park.spot5,spotNumber: 9),
                            CarSpot(spotOpen: park.spot6,spotNumber: 10),
                            CarSpot(spotOpen: park.spot7,spotNumber: 11),
                            CarSpot(spotOpen: park.spot8,spotNumber: 12)
                            
                        ]
                        self.selectedLot = self.modelLot
                    }
                } catch {
                    print("an error occurred", error)
                }
            
        }
       
    }
//    func stopListening() {
//        databasePath?.removeAllObservers()
//    }
    func openSpots() -> Double {
        var count: Double = 0.0
        for (index,_) in selectedLot.enumerated() {
            if(selectedLot[index].spotOpen == true) {
                count = count + 1
            }
        }
        return count
    }
   
    func selectInitialLot(_ pressedLot: String) {
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
    
    var pharmacyLot : [CarSpot] =
    [
        CarSpot(spotOpen: false,spotNumber: 1),
        CarSpot(spotOpen: false,spotNumber: 2),
        CarSpot(spotOpen: true,spotNumber: 3),
        CarSpot(spotOpen: false,spotNumber: 4),
        CarSpot(spotOpen: false,spotNumber: 5),
        CarSpot(spotOpen: true,spotNumber: 6),
        CarSpot(spotOpen: false,spotNumber: 7),
        CarSpot(spotOpen: false,spotNumber: 8),
        CarSpot(spotOpen: false,spotNumber: 9),
        CarSpot(spotOpen: false,spotNumber: 10),
        CarSpot(spotOpen: true,spotNumber: 11),
        CarSpot(spotOpen: false,spotNumber: 12),
        CarSpot(spotOpen: false,spotNumber: 13),
        CarSpot(spotOpen: true,spotNumber: 14),
        CarSpot(spotOpen: false,spotNumber: 15),
        CarSpot(spotOpen: false,spotNumber: 16)
    ]
    var northernLot : [CarSpot] =
    [
        CarSpot(spotOpen: false,spotNumber: 1),
        CarSpot(spotOpen: true,spotNumber: 2),
        CarSpot(spotOpen: false,spotNumber: 3),
        CarSpot(spotOpen: false,spotNumber: 4),
        CarSpot(spotOpen: true,spotNumber: 5),
        CarSpot(spotOpen: true,spotNumber: 6),
        CarSpot(spotOpen: false,spotNumber: 7),
        CarSpot(spotOpen: true,spotNumber: 8),
        CarSpot(spotOpen: true,spotNumber: 9),
        CarSpot(spotOpen: true,spotNumber: 10),
        CarSpot(spotOpen: false,spotNumber: 11)
    ]
    var recLot : [CarSpot] =
    [
        CarSpot(spotOpen: false,spotNumber: 1),
        CarSpot(spotOpen: true,spotNumber: 2),
        CarSpot(spotOpen: false,spotNumber: 3),
        CarSpot(spotOpen: false,spotNumber: 4),
        CarSpot(spotOpen: false,spotNumber: 5),
        CarSpot(spotOpen: false,spotNumber: 6),
        CarSpot(spotOpen: false,spotNumber: 7),
        CarSpot(spotOpen: false,spotNumber: 8),
        CarSpot(spotOpen: true,spotNumber: 9),
        CarSpot(spotOpen: false,spotNumber: 10),
        CarSpot(spotOpen: false,spotNumber: 11)
    ]
    var arenaLot : [CarSpot] =
    [
        CarSpot(spotOpen: true,spotNumber: 1),
        CarSpot(spotOpen: true,spotNumber: 2),
        CarSpot(spotOpen: false,spotNumber: 3),
        CarSpot(spotOpen: false,spotNumber: 4),
        CarSpot(spotOpen: true,spotNumber: 5),
        CarSpot(spotOpen: false,spotNumber: 6),
        CarSpot(spotOpen: false,spotNumber: 7),
        CarSpot(spotOpen: true,spotNumber: 8),
        CarSpot(spotOpen: false,spotNumber: 9),
        CarSpot(spotOpen: false,spotNumber: 10)
    ]
}

struct CarSpot: Identifiable {
    var id: Int {
        return spotNumber
    }
    var spotOpen = false
     var spotNumber = 100
    
//    init(spotOpen:Bool, spotNumber: Int) {
//        self.spotOpen = spotOpen
//        self.spotNumber = spotNumber
//    }
}
