//
//  FloatingBar.swift
//  ParkWise
//
//  Created by Parker Muery on 3/27/23.
//

import SwiftUI

struct FloatingBar: View {
    @ObservedObject var model : DataModel
    var body: some View {
        HStack(){
            Spacer()
            VStack(spacing:2){
                withAnimation(){
                    Text("\(model.selectedLot.count)")
                        .font(.system(size:30))
                        .animation(.spring())
                }
                Text("Spaces")
            }
            Spacer()
            VStack{
                Text("\(Int(model.openSpots()))")
                    .font(.system(size:30))
                    .animation(.spring())
                Text("Open")
            }
            Spacer()
            ProgressBar(model:model, progress: (model.openSpots()/Double(model.selectedLot.count) ))
                .animation(.spring())
                .frame(maxWidth:50)
            
            Spacer()
        }
        .padding()
        .background(RoundedRectangle(cornerRadius: 15).fill(.black))
        .foregroundColor(.white)
    }
}

struct FloatingBar_Previews: PreviewProvider {
    static var previews: some View {
        FloatingBar(model: DataModel())
    }
}
