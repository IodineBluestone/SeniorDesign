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
                        HStack{
                            lotPicker(model: model)
                        }
                    }
                    .padding()
                    .cornerRadius(10)
                    ScrollView{
                        LazyVGrid(
                            columns: [
                                GridItem(spacing: 4),
                                GridItem(spacing: 4),
                                GridItem(spacing: 4)
                            ], spacing: 10) {
                                
                                ForEach(model.selectedLot, id: \.id) { spot in
                                    CardView(cardData: spot)
                                }
                                
                            }.padding(3)
                        
                        Spacer(minLength:125)
                        
                    }
                    .background(.white)
                    .padding(1)
                }
                .padding(1)
                .edgesIgnoringSafeArea(.bottom)
                VStack{
                    Spacer()
                    floatingBar(model:model)
                        .cornerRadius(40)
                        .frame(maxHeight:70)
                        .padding(10)
                }
            }
            .background(LinearGradient(gradient: Gradient(colors: [.gradientPurple, .gradientPink]), startPoint: .leading, endPoint: .trailing))
            .navigationTitle("ParkWise")
            .toolbar {
                Button(){
                }label:{
                    Image(systemName: "magnifyingglass").foregroundColor(.black).font(.headline)
                }
            }
            
        }
        .onAppear(){
            model.doSomething("Pharmacy Lot")
        }
    }
}

struct CardView: View {
    var cardData: CarSpot
    
    var body: some View {
        VStack{
            HStack{
                Text("#\(cardData.spotNumber)")
            }
            
            HStack{
                if(!cardData.spotOpen) {
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
            }.frame(width:75,height: 75)
            HStack{
                Text(cardData.spotOpen ? "Open" : "Taken")
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

struct lotPicker : View {
    @ObservedObject var model: DataModel
    var body: some View {
        HStack{
            Text("\(model.selectedLotDisplay)")
            Spacer()
            Menu {
                ForEach(model.lotNames, id: \.self) { lotName in
                    Button(action:{
                        model.doSomething(lotName)
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

struct floatingBar : View {
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
            progressBar(model:model, progress: (model.openSpots()/Double(model.selectedLot.count) ))
                .animation(.spring())
            
            Spacer()
        }
        .padding()
        .background(RoundedRectangle(cornerRadius: 15).fill(.black))
        .foregroundColor(.white)
    }
}

struct progressBar : View {
    @ObservedObject var model : DataModel
    var progress: Double
    var body: some View {
        ZStack {
            Circle()
                .stroke(
                    Color.gradientPink.opacity(0.5),
                    lineWidth: 7
                )
            Circle()
                .trim(from: 0, to: progress)
                .stroke(
                    Color.gradientPink,
                    style: StrokeStyle(
                        lineWidth: 7,
                        lineCap: .round
                    )
                )
                .rotationEffect(.degrees(-90))
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView(model: DataModel())
    }
}


