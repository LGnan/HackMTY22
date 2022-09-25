//
//  ViewControllertres.swift
//  food4allapp
//
//  Created by José Armando Benvenuto Valerdi  on 25/09/22.
//

import UIKit

class ViewControllertres: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    var papa:Int = 0;
    var pollos:Int = 0;
    @IBOutlet weak var papas: UITextField!
    
    @IBOutlet weak var pollo: UITextField!
    
    @IBAction func maspapas(_ sender: Any) {
        papa=papa+1;
        papas.text=String(papa);
    }
    
    @IBAction func menospapas(_ sender: Any) {
        if papa != 0
        {
            papa-=1;
            papas.text=String(papa);
        }
        
        
    }
    
    @IBAction func maspollo(_ sender: Any) {
        pollos+=1;
        pollo.text=String(pollos);
    }
    
    @IBAction func menospollo(_ sender: Any) {
        if pollos != 0
        {
            pollos-=1;
            pollo.text=String(pollos);
        }
    }
    
    @IBAction func retro(_ sender: Any) {
        dismiss(animated: true, completion: nil)
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
