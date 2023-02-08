////
////  CarSpot.swift
////  ParkWise
////
////  Created by Parker Muery on 2/6/23.
////
//
//import SwiftUI
//
//struct CarSpot: View {
//    @State  var spotOpen = false
// //   @State private var lot = ""
//    @State  var spotNumber = 100
//    var body: some View {
//            VStack{
//                HStack{
//                    Spacer()
//                    Text("#\(spotNumber)")
//                }
//                HStack{
//                    Text(spotOpen ?" 🟢" : " 🚗")
//                        .font(.title)
//                        .padding(10)
//                }
//                HStack{
//                    Text(spotOpen ? "Open" : "Taken")
//                    Spacer()
//                }
//               
//            }.background(RoundedRectangle(cornerRadius: 15)
//                .fill(.white)
//                .frame(width:135,height:200))
//            
//        
//       // .frame(maxWidth: .infinity, maxHeight: .infinity)
//      //  .background(.blue)
//    }
//}
//
//struct CarSpot_Previews: PreviewProvider {
//    static var previews: some View {
//        CarSpot()
//    }
//}
