SCT Inst & TIPS
---------------

Introduction to TIPS
--------------------

**What is TIPS?**

TARGET Instant Payment Settlement (TIPS) is a market infrastructure service launched by the Eurosystem in November 2018. 

TIPS settles instant payments in central bank money, in real-time and around the clock, every day of the year (24/7/365). 

**Scheme used**

TIPS is compliant with the SEPA Instant Credit Transfer (SCT Inst), the scheme for pan-European instant payments.

As SCT Inst compliant service, TIPS follows the ISO 20022 standard.

**Currency**

Multi-currency capability is a core principle of TIPS and an integral part of its design.

At the time of writing this article (May 2024) TIPS settles payment transfers in euro and, as of February 2024, in Swedish kronor. Sveriges Riksbank is the first non-euro area central bank to join the service with its currency.

In this context it’s important to differenciate multi-currency capability from cross-currency settlement.

For the time being TIPS offers the multi-currency functionality. This means that payments processed can:

* debit the TIPS account in EUR and credit TIPS account in EUR or
* debit the TIPS account in SEK and credit TIPS account in SEK.

There is currently no possibility of cross-curency settlement.

However, ECB is working also on this functionality that may be implemented in the future.

Sveriges Riksbank was the first to join TIPS, however, there are other CBs interested in onboarding. Based on the public information, Danmarks Nationalbank is also preparing to migrate to TIPS, and Norway has shown interest in joining.

Other thing worth heightening is that, the above points relate to the accounts held in TIPS.

Accounts of the end originator and beneficiary, which are kept in the books of the PSPs, may be denominated in different currencies.

**Part of the TARGET Services**

TIPS is part of the TARGET Services.

This means that it is fully integrated with other services provided by the Eurosystem for large-value payments, securities settlement, and collateral management.

The TARGET Services architecture is described in the following articles:

* Short history of TARGET system
* TARGET Services Infrastructure

Being part of TARGET Services means i.a. that:

* the settlement in TIPS in done in central bank money (CeBM),
* for connectivity purposes ESMIG is used with SWIFT and Nexi-Colt (formerly SIA-Colt) being authorized Network Service Providers,
* reference data is kept in CRDM,
* TIPS adheres to the same participation rules as T2,
* TIPS shares the same logic and tools of liquidity management as other services,
* there are monetary policy benefits, like the fact that TIPS account balances count towards minimum reserve requirements.

**Business day (euro)**

TIPS processes instructions continuously without any scheduled service downtime.

TIPS change of business day is synchronized with other TARGET Services.

The new business day starts at 18:00 in normal situations (without any interruption to the service).

It is important to keep in mind, that regardless of the TIPS business day which starts at 18:00, the recommended value dating of SEPA Instant Credit Transfers is to apply the calendar date.

This is presented in the following Ami-Pay document: Value dating SEPA Instant Credit Transfers

  

**Pan-European reachability**

As described in my previous article (Instant payment Regulation in a nutshell) the instant payments landscape in Europe is going to change significantly.

However, it is worth noticing, that already in 2020, the ECB took steps to ensure the Pan-European reachability in TIPS (more information here).

One of the requirements is that all payment service providers that adhere to the SCT Inst scheme and are reachable in T2 become reachable in a TIPS.

**High performance**

TIPS is an efficient and reliable service.

TIPS is built to secure an end-to-end processing time of ten seconds or less (with TIPS in practice much less).

With a processing time measured in milliseconds, TIPS can settle up to 2,000 transactions per second.

**Maintenance and deployment windows**

This technical solution is designed to secure availability around the clock without maintenance windows and enable a deployment process with no interruption in the service.

**Flexible ways to access TIPS**

Flexible ways to join TIPS refers to both:

* the account structure (PSP may have their own TIPS account or settle via another participant’s account)
* connectivity (PSP can either be in control of the messaging exchange themselves or delegate it to an “instructing party” of their choice).

**Value added functionalities**

As an example of Value added serice , PSPs using TIPS have the option to offer their clients Mobile Proxy Lookup (MPL)

MPL makes it easier for customers to send and receive instant payments where the receiver is identified only by a proxy – a mobile number.

**Pricing**

The current pricing structure for the TIPS platform is applicable as of 1 January 2024.

The new Pricing structure is described in more detail here. 

The price per instant payment transaction is fixed at 0.2 cent (€0.002), which is shared equally between the sending participant and the receiving participant in TIPS (i.e. €0.001 for the Originator and €0.001 for the Beneficiary).

Of course, the above is the price applied for PSPs in TIPS.

The fees charged by PSP to their customers are at their discretion.

However, it is worth mentioning that according to the new IPR, the price of instant credit transfers (if any) must not be higher than the charges that apply for credit transfers of the corresponding type.

**Interesting materials**

As TIPS is a Eurosystem service, the most important information is available on the ECB website.

The basic Facts and Figures are described here.

An interesting ECB Focus session related to TIPS took place in March 2024. Recordings and presentations are available here.

|  |  |
| --- | --- |
| << Instant payment Regulation in a nutshell | TIPS Parties & Accounts >> |