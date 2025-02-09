//
//  LocationManager.swift
//  CoverUp!!
//
//  Created by Harini Kolluru on 2/8/25.
//

import Foundation
import CoreLocation
class LocationManager: NSObject, ObservableObject, CLLocationManagerDelegate {
    
    let manager = CLLocationManager()
    // question mark represents that this can be false at any moment
    @Published var location: CLLocationCoordinate2D?
    @Published var isLoading = false
    override init() {
        super.init()
        manager.delegate = self
    }
    
    func requestUserLoc() {
        isLoading = true
        manager.requestLocation()
    }
    
    
    
    func locationManager(_ manager:CLLocationManager, didUpdateLocation locations:[CLLocation]) {
        location = locations.first?.coordinate
        isLoading = false
    }
    
    func locationManager(_ manager: CLLocationManager, didFailWithError error: Error ){
        print("Sorry, we can't find your location... Try again later :)", error)
        isLoading = false
    }
    
//    struct definingObservableObject: View {
//        @ObservableObject var observeMe: LocationManager = LocationManager()
//
//        var body: some View {
//
//        }
//    }
}
