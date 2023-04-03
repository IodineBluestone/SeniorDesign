//
//  ContentView.swift
//  ParkWise
//
//  Created by Parker Muery on 2/6/23.
//

import SwiftUI

struct ContentView: View {
    @ObservedObject var model: DataModel
    var body: some View {
        NavigationView {
            ZStack{
                VStack(spacing:0){
                    VStack{
                        LotPicker(model: model)
                    }
                    .padding()
                    .cornerRadius(10)
                    ScrollView{
                        LazyVGrid(
                            columns: [
                                GridItem(spacing: 20),
                                GridItem(spacing: 20),
                                GridItem(spacing: 20)
                            ], spacing: 10) {
                                ForEach(model.selectedLot, id: \.id) { spot in
                                    SpotView(spotData: spot)
                                }
                            }
                            .padding()
                        Spacer(minLength:120)
                    }
                    .background(.white)
                }
                .padding(1)
                .edgesIgnoringSafeArea(.bottom)
                VStack{
                    Spacer()
                    FloatingBar(model:model)
                        .cornerRadius(40)
                        .padding(10)
                }
            }
            .background(LinearGradient(gradient: Gradient(colors: [.gradientPurple, .gradientPink]), startPoint: .leading, endPoint: .trailing))
            .navigationTitle("ParkWise")
            
        }
        .onAppear(){
            model.listentoRealtimeDatabase()
            model.selectInitialLot("Model Lot")
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        
        ContentView(model: DataModel())
    }
}


