static func removeId(idArg: String, contextArg: NSManagedObjectContext, controller: UICollectionViewController) -> Void {
    let request = NSFetchRequest<NSFetchRequestResult>(entityName: "ChatMessage")
    request.predicate = NSPredicate(format: "id = %@", idArg)
    do {
        let result = try contextArg.fetch(request)
        for data in result as! [NSManagedObject] {
            print("found \(data.value(forKey: "id") as! String)")
            contextArg.perform {
                do {
                    try(contextArg.delete(data))
                    print ("deleted object with id: \(idArg)")
                    
                    try(contextArg.save())
                    //controller.collectionView.reloadData()
                    
                } catch let err {
                    print(err)
                }
            }
        }
    } catch {
        print("*** ERROR: didn't find id: \(idArg) to delete from current context ***")
    }
} // </ func>