//
//  WelcomeView.swift
//  CoverUp!!
//
//  Created by Harini Kolluru on 2/8/25.
//

import Foundation
import SwiftUI
import CoreLocation
import CoreLocationUI
import UIKit


struct WelcomeView: View {
    @EnvironmentObject var locationManager: LocationManager
    
    var body: some View {
        VStack {
            VStack(spacing:20 ){
                Text("welcome to coverup!")
                    .bold().font(.title)
                Text("please share your current lcocation to get the weather")
                    .padding()
            }
            .multilineTextAlignment(.center)
            .padding()
            LocationButton(.shareCurrentLocation) {
                locationManager.requestUserLoc()
            }
            .cornerRadius(30)
            .symbolVariant(.fill)
            .foregroundColor(.white)
            

            
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}
               
struct WelcomeView_Previews: PreviewProvider {
    static var previews: some View {
        WelcomeView()
    }
}
