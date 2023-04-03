//
//  ProgressBar.swift
//  ParkWise
//
//  Created by Parker Muery on 3/27/23.
//

import SwiftUI

struct ProgressBar: View {
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

struct ProgressBar_Previews: PreviewProvider {
    static var previews: some View {
        ProgressBar(model: DataModel(),progress:60.0)
    }
}
