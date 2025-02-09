//
//  ViewController.swift
//  CoverUp!
//
//  Created by Harini Kolluru on 2/8/25.
//

import UIKit

class ViewController: UIViewController, UIImagePickerControllerDelegate & UINavigationControllerDelegate {
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func ImagePicker(_ sender: Any) {
        let imagePickerController = UIImagePickerController()
        imagePickerController.delegate = self
        imagePickerController.sourceType = .photoLibrary
        self.present(imagePickerController, animated: false, completion: nil)
    }
    
    
   // func imagePickerController(_ picker:UIImagePickerController, )
}

