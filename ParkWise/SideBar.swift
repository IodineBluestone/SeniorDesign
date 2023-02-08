////
////  SideBar.swift
////  ParkWise
////
////  Created by Parker Muery on 2/6/23.
////
//
//import SwiftUI
//
//struct SideBar: View {
//  @Binding var isSideBarVisible: Bool
//    var sideBarWidth = UIScreen.main.bounds.size.width * 0.7
//    var bgColor: Color =
//              Color(.init(
//                      red: 52 / 255,
//                      green: 70 / 255,
//                      blue: 182 / 255,
//                      alpha: 1))
//
//    var body: some View {
//        ZStack{
//            GeometryReader { _ in
//                EmptyView()
//            }
//            .background(.black.opacity(0.6))
//                       .opacity(isSideBarVisible ? 1 : 0)
//                       .animation(.easeInOut.delay(0.2), value: isSideBarVisible)
//                       .onTapGesture {
//                           isSideBarVisible.toggle()
//                       }
//                       content
//                   }
//                   .edgesIgnoringSafeArea(.all)
//        }
//
//               var content: some View {
//                   HStack(alignment: .top) {
//                       ZStack(alignment: .top) {
//                           bgColor
//                       }
//                       .frame(width: sideBarWidth)
//                       .offset(x: isSideBarVisible ? 0 : -sideBarWidth)
//                       .animation(.default, value: isSideBarVisible)
//
//                       Spacer()
//                   }
//               }
//        }
//struct SideBar_Previews: PreviewProvider {
//    static var previews: some View {
//        SideBar(isSideBarVisible: Binding<Bool>)
//    }
//}
