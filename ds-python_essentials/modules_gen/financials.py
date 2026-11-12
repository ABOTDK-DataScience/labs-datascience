def target_sell_prompt():

  def get_float(prompt:str, name:str):
    """Getting the inputs for the various parameters"""
    try:
      return float(input(prompt))
    except ValueError:
      print(f"Number for {name} incorrect. Please try again")

  cost_price = get_float("Enter Cost Price:","Cost price")
  commission_rate = get_float("Enter the commission rate for Buy/Sell in decimals:","Commission rate")
  target_profit = get_float("Enter your target profit:","Profit")

  if 0 > commission_rate > 1:
    raise ValueError("Check and enter the commission rate again")

  selling_price = (target_profit + cost_price*(1+commission_rate))/(1-commission_rate)

  print(f"{'-'*70}")
  print(f"Selling price should be: ${selling_price:,.2f}")
  print(f"{'-'*70}")
  print(f"{'-'*70}")
  print(f"With Buying commission of: ${commission_rate*cost_price:,.2f} and Selling commission of: ${commission_rate*selling_price:,.2f}")
  print(f"{'-'*70}")
