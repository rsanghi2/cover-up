//
//  ContentView.swift
//  CoverUp!!
//
//  Created by Harini Kolluru on 2/8/25.
//

import SwiftUI

struct ContentView: View {
    
    @StateObject var locationManager = LocationManager()
    var body: some View {
        VStack {
            
            if let location = locationManager.location{
                Text("we know where u live")
            }
            else {
                if locationManager.isLoading{
                    ProgressView()
                    
                }
                else{
                    WelcomeView()
                        .environmentObject(locationManager)
                }
            }
            WelcomeView()
                .environmentObject(locationManager)
        }
        .background(Color(hue: 0.643, saturation: 0.343, brightness: 0.87))
        preferredColorScheme(.light)
        
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
