import Foundation
import CoreData

class FetchedResultsControllerManager: NSObject, NSFetchedResultsControllerDelegate {
    var fetchedResultsController: NSFetchedResultsController< NSFetchRequestResult >?
    var blockOperations = [BlockOperation]()
    
    init( friend: Friend ) {
        super.init()
        let fetchRequest = NSFetchRequest<NSFetchRequestResult>(entityName: "ChatMessage")
        fetchRequest.sortDescriptors = [NSSortDescriptor(key: "date", ascending: true)]
        let friend_name = friend.name
        fetchRequest.predicate = NSPredicate(format: "friend.name = %@", friend_name!)
        let context = mLibrary.LibraryDelegate.sharedInstance().getContext()
        fetchedResultsController = NSFetchedResultsController(fetchRequest: fetchRequest, managedObjectContext: context, sectionNameKeyPath: nil, cacheName: nil)
        fetchedResultsController?.delegate = self
    }
    
    func performFetch() {
        do {
            try fetchedResultsController?.performFetch()
        } catch let error {
            print("Failed to perform fetch: \(error)")
        }
    }
    
    func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>, didChange anObject: Any, at indexPath: IndexPath?, for type: NSFetchedResultsChangeType, newIndexPath: IndexPath?) {
        print( "didChange in FetchedResultsControllerManager... " )
        // ... rest of the code ...
    }
    
    func controllerDidChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {
        print( "controllerDidChangeContent called in FetchedResultController... " )
        // ... rest of the code ...
    }
    
    func numberOfObjects() -> Int {
        return fetchedResultsController?.sections?[0].numberOfObjects ?? 0
    }
    
    func object(at indexPath: IndexPath) -> ChatMessage {
        return fetchedResultsController?.object(at: indexPath) as! ChatMessage
    }
    
    // ... rest of the code ...
}