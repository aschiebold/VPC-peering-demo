let s = {
   $source: {
      connectionName: "confluent-vpc",
      topic: "allan-vpc"
   }
}

let g = {
   $group: {
      _id: "$group_id",
      sum_temp: {
         $sum: "$temp"
      }
   }
}

 let t = {
 $tumblingWindow: {
   interval: {
     size: NumberInt(10),
     unit: "second"
   },
    pipeline: [g]
  }
}

let m = {
   $merge: {
      into: {
         connectionName: "toDB",
         db: "streams",
         coll: "streams"
      }
   }
}

sp.createStreamProcessor("test1", [s, t, m])

sp.test1.start()

sp.process([{"$source": {
   "connectionName": "confluent-vpc",
   "topic": "allan-vpc"
}}])