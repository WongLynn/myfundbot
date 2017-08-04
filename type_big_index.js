db.getCollection('MixFunds').aggregate([
  {
    $match: {
      ftype: {
        $eq: '指数型大盘型'
      },
      size: {
        $gte: 10
      }
    }
  },
  {
    $sort: {
      size: -1
    }
  }
])