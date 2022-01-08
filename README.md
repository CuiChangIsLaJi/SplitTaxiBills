# SplitTaxiBills
Having trouble with how to split the taxi bill when multiple partners hang out together? Now let's explore a convenient way to transfer the money.
The taxi payment is always processed by one or some of guys on his/her/their cellphone applications. If we want to split the taxi bill afterwards, what is the convenient way to get this done?

Well, some of our partners did not even touch the app, and they need to make it up; some might have paid a bit, and still need to pay for the rest part; some might have paid a lot, and they might even acquire some money from other guys! This program is aimed at a convenient payment on each person that could be automatically calculated.

You can run this python script easily with the following command line

<code>python SplitTaxiBills.py --payers-info payers.json --names-info names.txt --output-bill bill.json [--intermediate name]</code>

 and all partner names recorded in <code>names.txt<\code> and all payers' information recorded in <code>payers.json</code>. This command will generate a bill <code>bill.json</code> which contains all the information you need.
  
  The intermediate is the one who processes all the ins and outs of money. If it is not assigned with a name, or is assigned with a name that is not on the partner list, we would get exactly the net change of money on everyone. Otherwise, we get how much we should pay to this intermediate.
