//
//  ShortSleevesViewController.swift
//  CoverUp!
//
//  Created by Harini Kolluru on 2/8/25.
//

import UIKit

class ShortSleevesViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    
    @IBOutlet weak var theTable: UITableView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        theTable.register(ViewCell.self, forCellReuseIdentifier: "ViewCell")
        theTable.dataSource = self
        theTable.delegate = self
        // Do any additional setup after loading the view.
    }
    
    
    
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int)-> Int{
        return 1
    }
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath)-> UITableViewCell{
        let cell = tableView.dequeueReusableCell(withIdentifier: "ViewCell") as!ViewCell
        return cell
    }
    func tableView(_tableView: UITableView, heightForRowAt indexPath: IndexPath)->CGFloat{
        return 500
    }

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
