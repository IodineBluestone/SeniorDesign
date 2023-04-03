//
//  SpotView.swift
//  ParkWise
//
//  Created by Parker Muery on 3/27/23.
//

import SwiftUI

struct SpotView: View {
        var spotData: CarSpot
        var body: some View {
            VStack{
                HStack{
                    Text("#\(spotData.spotNumber)")
                }
                
                HStack{
                    if(!spotData.spotOpen) {
                        Image("Image")
                            .resizable()
                            .scaledToFit()
                            .clipShape(RoundedRectangle(cornerRadius: 30))
                    }
                    else {
                        Image(systemName: "arrow.up")
                            .font(.largeTitle)
                            .foregroundColor(.green)
                    }
                }.frame(width:75,height: 50)
                HStack{
                    Text(spotData.spotOpen ? "Open" : "Taken")
                }
            }
            .padding(20)
            .background(.white)
            .cornerRadius(15)
            .overlay(
                RoundedRectangle(cornerRadius: 15)
                    .stroke(style: StrokeStyle(lineWidth: 1, dash: [4.0]))
            )
            
        }
    }

//struct SpotView_Previews: PreviewProvider {
//    static var previews: some View {
//        SpotView()
//    }
//}
