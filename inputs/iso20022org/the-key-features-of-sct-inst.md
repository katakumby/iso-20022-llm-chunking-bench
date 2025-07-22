The key features of SCT Inst
----------------------------

With this article, I want to start the description of the SCT Inst scheme, which became operational in November 2017.

More about SEPA  pan-European

SCT Inst means two things:

* SCT is SEPA Credit Transfer – it means that the scheme covers only credit transfers.
* Inst means that this scheme is related to the Instant payments. the transfer of money is immediate and available 24/7/365.

eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52020DC0592&from=EN

P131021-2.pdf (fsb.org)

**An optional scheme**  
PSPs operating within SEPA are not obliged to adhere to the SCT Inst scheme. If a PSP wishes to adhere, it must at least be reachable in the role of the beneficiary’s PSP.

**Availability**

**Availability 24/7/365**  
The services based on the SCT Inst scheme are available 24 hours a day and on all calendar days of the year. All adhering scheme participants have to be technically capable to process the SCT Inst transactions on a 24/7/365 basis. 

**Maximum duration time**

**An initial maximum duration is ten seconds**

When the payer’s payment service provider (PSP) is certain that all mandatory attributes for processing the transaction are valid, it marks this starting point with a **timestamp**.

In other words, the maximum execution time of ten seconds of an SCT Inst transaction starts once the originator’s PSP is ready for inter-bank processing

Within ten seconds, the beneficiary’s PSP has to report to the payer’s PSP either that the money has been made available to the beneficiary or that the transaction has been rejected. If the maximum execution time of ten seconds cannot be met due to exceptional processing circumstances, the SCT Inst rulebook foresees a hard time-out deadline of 20 seconds. The payer’s PSP cannot unilaterally reject the transaction until the moment it receives a negative confirmation message reporting its failure.

SCT Inst scheme participants are free to agree on either a bilateral or multilateral basis on a **shorter execution time**. The EPC provides the list of SCT Inst scheme participants using these options.

Note that this parameter can only be changed in a more ambitious direction.

they can agree bilaterally or multilaterally to change these parameters for SCT Inst transactions exchanged among themselves.

The money is available in the account of the payee within ten seconds. It means that within ten seconds, the PSP of the person receiving the payment (the beneficiary PSP) will report to the PSP sending the payment (the originator PSP) either that the funds have been made available on the beneficiary’s account, or that the SCT Inst transaction has been rejected.

**Maximum amount**

**A maximum amount of 100.000,00 EUR**  
Any SCT Inst transaction higher than this maximum amount is rejected by the inter-PSP parties involved in the process chain (unless otherwise previously agreed between the participants).

It is important to know that the maximum amount is not described in SCT Inst Scheme Rulebook. However, in section 2.5, Rulebook refers to the document which forms binding supplement to the SCT Inst Scheme Rulebook, and sets sets the maximum amount per instruction that can be processed under the SEPA Instant Credit Transfer (SCT Inst) . This is published on ecb website here: Maximum Amount for Instructions under the SCT Inst Scheme Rulebook

SCT Inst scheme participants are free to agree on either a bilateral or multilateral basis on a **higher maximum amount**.

The EPC will review the maximum amount annually (as of 2018).

The EPC provides the list of SCT Inst scheme participants using these options.   

Note that this parameter can only be changed in a more ambitious direction.

they can agree bilaterally or multilaterally to change this parameter for SCT Inst transactions exchanged among themselves.

One thing to note is that TIPS as the platform does not validate this amount.

**Currency of the transfer**

SCT Inst transactions must be made in euros.

  

**Currency of the accounts held at PSPs**

Though the transaction must be made in**euros**, the payment accounts held at PSPs operating in SEPA do not have to be denominated in euros.

The payment accounts held at PSPs operating within SEPA for sending or receiving an SCT Inst transaction do not have to be denominated in euro. Any currency conversion is executed in the originator bank or beneficiary bank and is not governed by the SCT Inst scheme.

**Messages used**

The SCT Inst scheme is based on ISO 20022 XML messages

**Clearing and settlement**

Here it is important to see the difference to SCT scheme.

Classic SCT transactions are processed in batches. All individual SCT transactions received during a specific period of time during a business working day are grouped into a single (batch) file. This file is then submitted for further clearing and settlement usually at the end of the day.

The processing of SCT Inst is different as the processing, clearing (and potentially settlement) of SCT Inst take place on a transaction-by-transaction basis as soon as they reach a PSP system, i.e. in real-time end-to-end.

Note that as for the existing EPC SEPA schemes, the clearing and settlement layer of SCT Inst transactions lies outside of the scope of the SCT Inst scheme.   
The SCT Inst scheme provides a single set of rules, practices and standards which are to be respected by individual PSPs and infrastructure providers, including clearing and settlement mechanisms (CSMs) on behalf of their PSP customers.

|  |  |
| --- | --- |
| << previous page | next page >> |