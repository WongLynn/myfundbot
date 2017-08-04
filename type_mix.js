db.getCollection('MixFunds').aggregate([
  {
    $match: {
      ftype: {
        $eq: '混合型'
      },
      manage_fund_number: {
        $lte: 3
      }
    }
  },
  {
    $sort: {
      last_1year: -1
    }
  }
])