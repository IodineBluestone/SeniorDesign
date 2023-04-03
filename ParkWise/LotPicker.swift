//
//  LotPicker.swift
//  ParkWise
//
//  Created by Parker Muery on 3/27/23.
//

import SwiftUI

struct LotPicker: View {
    @ObservedObject var model: DataModel
    var body: some View {
        HStack{
            Text("\(model.selectedLotDisplay)")
            Spacer()
            Menu {
                ForEach(model.lotNames, id: \.self) { lotName in
                    Button(action:{
                        model.selectInitialLot(lotName)
                    })
                    {
                        Text("\(lotName)")
                    }
                }
                
            } label: {
                Image(systemName:"chevron.down")
            }
        } .foregroundColor(.black)
            .padding()
            .background(RoundedRectangle(cornerRadius: 10).fill(.white))
    }
}

struct LotPicker_Previews: PreviewProvider {
    static var previews: some View {
        LotPicker(model:DataModel())
    }
}
