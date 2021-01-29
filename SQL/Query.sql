SELECT Event1.EventId as Event1Id, Event2.EventId as Event2Id 
    FROM Events as Event1 join Events as Event2 ON Event1.ResourceID = Event2.ResourceID 
    WHERE 
        (Event2.StartedAt > Event1.StartedAt and Event2.StartedAt < Event1.EndedAt)
        or 
        (Event1.StartedAt > Event2.StartedAt and Event1.StartedAt < Event2.EndedAt);
