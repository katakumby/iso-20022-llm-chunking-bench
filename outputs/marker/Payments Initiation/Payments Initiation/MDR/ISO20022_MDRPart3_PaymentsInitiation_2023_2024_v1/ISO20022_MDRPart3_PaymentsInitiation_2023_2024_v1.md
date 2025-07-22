## **Introduction**

|                                                                                                                                               |                |                                                                                                                                                                      |  |  |  | Introduction |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--------------|--|
|                                                                                                                                               |                |                                                                                                                                                                      |  |  |  |              |  |
| This document describes the Business<br>Model Components and Elements used by<br>the Payments Initiation message<br>definitions.              |                |                                                                                                                                                                      |  |  |  |              |  |
|                                                                                                                                               |                |                                                                                                                                                                      |  |  |  |              |  |
| In the "Business Model" tab, the cells with<br>text in green indicate the business<br>concepts used by the Payments Initiation<br>message set |                |                                                                                                                                                                      |  |  |  |              |  |
|                                                                                                                                               |                |                                                                                                                                                                      |  |  |  |              |  |
| The "Traces" tab shows to which business<br>concepts the Payments Initiation message<br>components and message elements trace.                |                |                                                                                                                                                                      |  |  |  |              |  |
|                                                                                                                                               |                |                                                                                                                                                                      |  |  |  |              |  |
| Notes:                                                                                                                                        |                |                                                                                                                                                                      |  |  |  |              |  |
|                                                                                                                                               | Specialisation | Some components inherit from a parent. In this<br>illustration, the AccountContract is a specialisation (a<br>child) of Contract and inherits from all its elements. |  |  |  |              |  |
|                                                                                                                                               |                | CashAccountContract inherits AccountContract and<br>indirectly from Contract.                                                                                        |  |  |  |              |  |

## **FullBusinessModel**

| Asset |                        |
|-------|------------------------|
| Asset | ExpiryDate             |
|       |                        |
|       |                        |
| Asset | MaturityDate           |
|       |                        |
| Asset | Derivative             |
| Asset | AssetValue             |
| Asset | AssetClassification    |
| Asset | FinancialAssetCategory |
| Asset | AssetPartyRole         |
| Asset | Issuance               |
| Asset | Portfolio              |
| Asset | InvestmentAmount       |

| Asset    | InvestmentRate                  |       |
|----------|---------------------------------|-------|
| Asset    | EffectiveDate                   |       |
| Asset    | FinancialInstrumentSubStructure |       |
| Asset    | InvestmentPlan                  |       |
| Asset    | Trade                           |       |
| Asset    | Tranche                         |       |
| Asset    | LegAdditionalInformation        |       |
| Asset    | StandingSettlementInstruction   |       |
| Asset    | GenericAssetIdentification      |       |
| Security |                                 | Asset |
| Security | Identification                  |       |
| Security | RegisteredDistributionCountry   |       |
| Security | DenominationCurrency            |       |

| Security | RegistrationForm        |  |
|----------|-------------------------|--|
| Security | DematerialisedIndicator |  |
| Security | EUSavingsDirective      |  |
| Security | SecuritiesQuantity      |  |
| Security | Fees                    |  |
| Security | Pricing                 |  |
| Security | SecuritiesAccount       |  |
| Security | TradingMarket           |  |
| Security | PlaceOfListing          |  |
| Security | Registration            |  |
| Security | Restriction             |  |
| Security | CorporateEvent          |  |

| Security | TemporaryFinancialInstrumentIndicator |  |
|----------|---------------------------------------|--|
| Security | AvailableDate                         |  |
| Security | DeclarationDetails                    |  |
| Security | Spread                                |  |
| Security | Dividend                              |  |
| Security | Balance                               |  |
| Security | FungibleIndicator                     |  |
| Security | Appearance                            |  |
| Security | NearTermPositionLimit                 |  |
| Security | ContractSettlementMonth               |  |
| Security | MinimumTradingPricingIncrement        |  |
|          |                                       |  |

| Security | Rating                    |  |
|----------|---------------------------|--|
| Security | CouponAttached            |  |
| Security | Sector                    |  |
| Security | WarrantAttachedOnDelivery |  |
| Security | StrippableIndicator       |  |
| Security | FirstDealingDate          |  |
| Security | TaxDetails                |  |
| Security | SecuritiesTrade           |  |
| Security | RegistrationJurisdiction  |  |
| Security | PartyRole                 |  |
| Security | SecurityStatus            |  |

| Security | Modification                        |  |
|----------|-------------------------------------|--|
| Security | RedemptionSchedule                  |  |
| Security | SecuritiesSettlement                |  |
| Security | SecuritiesTransfer                  |  |
| Security | CorporateActionStandingInstructions |  |
| Security | Quote                               |  |
| Security | SecuritiesOrder                     |  |
| Security | RelatedVariableInterest             |  |
| Security | Conversion                          |  |
| Security | ComponentSecurity                   |  |
| Security | RecompositionIndicator              |  |

| Security | Series                         |  |
|----------|--------------------------------|--|
| Security | PercentageOfDebtClaim          |  |
| Security | CoverRate                      |  |
| Security | MaturityRedemption             |  |
| Security | RelatedMarginCall              |  |
| Security | CloseLink                      |  |
| Security | PotentialEuroSystemEligibility |  |
| Security | MinimumQuantity                |  |

| Security            | RestrictedIndicator  |          |
|---------------------|----------------------|----------|
| InvestmentFundClass |                      | Security |
| InvestmentFundClass | ClassType            |          |
| InvestmentFundClass | DistributionPolicy   |          |
| InvestmentFundClass | DividendPolicy       |          |
| InvestmentFundClass | DualFundIndicator    |          |
| InvestmentFundClass | RequestedNAVCurrency |          |

| InvestmentFundClass | TradingCurrency                    |  |
|---------------------|------------------------------------|--|
| InvestmentFundClass | InvestmentFund                     |  |
| InvestmentFundClass | PhysicalBearerSecurities           |  |
| InvestmentFundClass | DematerialisedBearerSecurities     |  |
| InvestmentFundClass | PhysicalRegisteredSecurities       |  |
| InvestmentFundClass | DematerialisedRegisteredSecurities |  |
| InvestmentFundClass | ProcessingCharacteristics          |  |
| InvestmentFundClass | ProductGroup                       |  |
| InvestmentFundClass | InvestmentAccount                  |  |
| InvestmentFundClass | NetAssetValueCalculation           |  |
| InvestmentFundClass | InvestmentFundTransaction          |  |
|                     |                                    |  |

| InvestmentFundClass | SeriesIssueIdentificationDate | Date that identifies the issue of a<br>fund series. Typically applicable<br>to a redemption or order<br>ISODate<br>confirmation, but may be<br>specified in the subscription, if<br>known.                     |
|---------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| InvestmentFundClass | SeriesName                    | Identifies the name of a fund<br>series. Typically applicable to a<br>redemption or order<br>Max35Text<br>confirmation, but may be<br>specified in the subscription, if<br>known.                              |
| InvestmentFundClass | NewIssueIndicator             | Indicates that the financial<br>instrument and/or series included<br>YesNoIndicator<br>in the message is a new issue.                                                                                          |
| InvestmentFundClass | Equalisation                  | Part of an investor's subscription<br>amount that is held by the fund<br>in order to pay incentive /<br>Equalisation<br>RelatedInvestmentFundTransaction<br>performance fees at the end of<br>the fiscal year. |
| InvestmentFundClass | TopUpAmount                   | Additional amount of money<br>(top-up amount) required to<br>CurrencyAndAmount<br>meet the minimum subscription<br>amount.                                                                                     |
| InvestmentFundClass | HoldBackAmount                | Value of the redemption amount<br>CurrencyAndAmount<br>subject to hold back.                                                                                                                                   |
| InvestmentFundClass | HoldBackReleaseDate           | Date on which the hold back<br>ISODate<br>amount is to be released.                                                                                                                                            |
| InvestmentFundClass | LotDescription                | Description of the lot.<br>Max350Text                                                                                                                                                                          |
| InvestmentFundClass | FundClassification            | Method of classifying a fund.<br>GenericIdentification<br>IdentificationForInvestmentFundClass                                                                                                                 |

| InvestmentFundClass      | UnderlyingAssetType    |  |
|--------------------------|------------------------|--|
| InvestmentFundClass      | InvestorType           |  |
| InvestmentFundClass      | Reinvestment           |  |
| InvestmentFundClass      | OutstandingUnits       |  |
| InvestmentFundClass      | FundEndDate            |  |
| SecuritiesIdentification |                        |  |
| SecuritiesIdentification | IdentifiedSecurity     |  |
| SecuritiesIdentification | SecurityIdentification |  |
| SecuritiesIdentification | RIC                    |  |

| SecuritiesIdentification | TickerSymbol |  |
|--------------------------|--------------|--|
| SecuritiesIdentification | Bloomberg    |  |
| SecuritiesIdentification | CTA          |  |
| SecuritiesIdentification | Common       |  |
| SecuritiesIdentification | Name         |  |
| SecuritiesIdentification | SEDOL        |  |

| SecuritiesIdentification | CUSIP      |  |
|--------------------------|------------|--|
| SecuritiesIdentification | QUICK      |  |
| SecuritiesIdentification | Wertpapier |  |
| SecuritiesIdentification | Dutch      |  |
| SecuritiesIdentification | Valoren    |  |
| SecuritiesIdentification | Sicovam    |  |

| SecuritiesIdentification | Belgian                    |  |
|--------------------------|----------------------------|--|
| SecuritiesIdentification | IdentificationSuffix       |  |
| SecuritiesIdentification | GenericIdentification      |  |
| SecuritiesIdentification | ValidityPeriod             |  |
| SecuritiesIdentification | ApplicableTradingMarket    |  |
| SecuritiesIdentification | PrimeIdentification        |  |
| SecuritiesIdentification | RelatedOtherIdentification |  |
| SecuritiesIdentification | TradingIdentification      |  |
| Role                     |                            |  |
| Role                     | Player                     |  |
| Role                     | ContactPersonRole          |  |
| Role                     | PartyRole                  |  |
| Role                     | CounterpartyRisk           |  |
|                          |                            |  |

| Role                     | Entry                 |                      |
|--------------------------|-----------------------|----------------------|
| InformationPartyRole     |                       | Role                 |
| InformationPartyRole     | GenericIdentification |                      |
| InformationPartyRole     | HaircutValuation      |                      |
| InformationPartyRole     | Price                 |                      |
| InformationPartyRole     | Scheme                |                      |
| InformationPartyRole     | Quote                 |                      |
| InformationPartyRole     | TreasuryTrade         |                      |
| IdentificationIssuerRole |                       | InformationPartyRole |
| IdentificationIssuerRole | Country               |                      |
| IdentificationIssuerRole | EntityName            |                      |
| IdentificationIssuerRole | OwnerCode             |                      |
|                          |                       |                      |

| Information related to a non<br>standardised identification, such<br>GenericIdentification<br>as a proprietary party<br>identification or account<br>identification.<br>Name or number assigned by an<br>entity to enable recognition of<br>that entity, for example account<br>GenericIdentification<br>Identification<br>Max35Text<br>identifier, identification assigned<br>by a provider to identify its<br>customers.<br>Contact point which uses a<br>GenericIdentification<br>IdentificationForContactPoint<br>generic identification as<br>ContactPoint<br>Identification<br>identification.<br>Account Identification which uses<br>GenericIdentification<br>IdentificationForAccount<br>a generic identification as<br>AccountIdentification<br>ProprietaryIdentification<br>proprietary identification.<br>GenericIdentification<br>RelatedPartyIdentification<br>Party identified with a scheme.<br>PartyIdentificationInformation<br>OtherIdentification<br>Date at which the identification<br>GenericIdentification<br>IssueDate<br>ISODate<br>was issued.<br>Date at which the identification<br>GenericIdentification<br>ExpiryDate<br>ISODate<br>expires.<br>Information regarding an<br>GenericIdentification<br>Scheme<br>enumerated code list and its<br>Scheme<br>Identification<br>owner.<br>Securities certificate which uses<br>GenericIdentification<br>IdentificationForSecuritiesCertificate<br>a generic identification as<br>SecuritiesCertificate<br>Number<br>certificate number.<br>Lot breakdown which uses a<br>GenericIdentification<br>IdentificationForLot<br>generic identification as lot<br>LotBreakdown<br>LotNumber<br>number. |  |  |  |  |  |  |  |  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |  |  |  |  |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |  |  |  |  |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |  |  |  |  |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |  |  |  |  |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |  |  |  |  |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |  |  |  |  |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |  |  |  |  |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |  |  |  |  |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |  |  |  |  |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |  |  |  |  |  |  |  |  |

| GenericIdentification | PartyRole                                    |  |
|-----------------------|----------------------------------------------|--|
| GenericIdentification | IdentificationForCashProceedsIncome          |  |
| GenericIdentification | RelatedStatusReason                          |  |
| GenericIdentification | IdentificationForBankTransaction             |  |
| GenericIdentification | IdentificationForAccountCostReferencePattern |  |
| GenericIdentification | Account                                      |  |
| GenericIdentification | RelatedSystemIdentification                  |  |
| GenericIdentification | IdentificationForInterestName                |  |
| GenericIdentification | RelatedCashAccountService                    |  |
| GenericIdentification | IdentificationForInvestmentFundClass         |  |
| GenericIdentification | IdentifiedLocation                           |  |

| GenericIdentification | RelatedSecuritiesIdentification |  |
|-----------------------|---------------------------------|--|
| GenericIdentification | IdentifiedDocument              |  |
| GenericIdentification | RelatedPurchaseOrder            |  |
| GenericIdentification | RelatedCertificate              |  |
| LocalName             |                                 |  |
| LocalName             | FullName                        |  |
| LocalName             | RelatedSecurity                 |  |
| LocalName             | ShortName                       |  |
| LocalName             | Language                        |  |
| UmbrellaFund          |                                 |  |

| UmbrellaFund   | Name                 |                  |
|----------------|----------------------|------------------|
| UmbrellaFund   | SubFund              |                  |
| InvestmentFund |                      | FinancialProduct |
| InvestmentFund | DomicileCountry      |                  |
| InvestmentFund | OrderDesk            |                  |
| InvestmentFund | InvestmentFundClass  |                  |
| InvestmentFund | FundType             |                  |
| InvestmentFund | TreasuryTradingParty |                  |
| InvestmentFund | Identification       |                  |
| InvestmentFund | Custodian            |                  |
| InvestmentFund | PartyRole            |                  |

| InvestmentFund | Family                     |  |
|----------------|----------------------------|--|
| InvestmentFund | Structure                  |  |
| InvestmentFund | LegalForm                  |  |
| InvestmentFund | SubFundIndicator           |  |
| InvestmentFund | EndOfFiscalYear            |  |
| InvestmentFund | AccountingYearEndDate      |  |
| InvestmentFund | FirstAccountingYearEndDate |  |
| InvestmentFund | UmbrellaFund               |  |
| InvestmentFund | AuthorisedCountry          |  |
| Country        |                            |  |
| Country        | DomiciledFunds             |  |
| Country        | Code                       |  |
|                |                            |  |

| Country | Citizen                                |  |
|---------|----------------------------------------|--|
| Country | Tax                                    |  |
| Country | CountryForSafekeepingPlace             |  |
| Country | CountryForBeneficialOwner              |  |
| Country | ProducedProducts                       |  |
| Country | NationalRegulatoryAuthority            |  |
| Country | RelatedCardPayment                     |  |
| Country | Name                                   |  |
| Country | PostalAddressSpecification             |  |
| Country | CountryRelatedInvestmentFundProcessing |  |
| Country | Market                                 |  |
| Country | RelatedPaymentCard                     |  |

| Dividend | NetDividend                   | Cash dividend amount per equity<br>after deductions or allowances<br>RateAndAmount<br>have been made.                                                                                                                                                    |
|----------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dividend | ProvisionalDividend           | Dividend is provisional.<br>RateAndAmount                                                                                                                                                                                                                |
| Dividend | DividendRankingDate           | Date on which a security will be<br>ISODateTime<br>entitled to a dividend.                                                                                                                                                                               |
| Dividend | ManufacturedDividendAmount    | Amount of money that the<br>borrower pays to the lender as a<br>compensation. It does not entitle<br>the lender to reclaim any tax<br>CurrencyAndAmount<br>credit and is sometimes treated<br>differently by the local tax<br>authorities of the lender. |
| Dividend | UnfrankedAmount               | Amount resulting from an<br>unfranked dividend paid by a<br>company; the amount does not<br>CurrencyAndAmount<br>include tax credit and is subject<br>to withholding tax.                                                                                |
| Dividend | NotionalDividendPayableAmount | Amount of cash that would have<br>been payable if the dividend had<br>CurrencyAndAmount<br>been taken in the form of cash<br>rather than shares.                                                                                                         |
| Dividend | Rate                          | Planned dividend rate, for<br>PercentageRate<br>example, for preferred shares.                                                                                                                                                                           |
| Dividend | ExDividendDate                | Date/time as from which trading<br>(including exchange and OTC<br>ISODateTime<br>trading) occurs on the underlying<br>security without the benefit.                                                                                                      |
| Dividend | Security                      | Security for which a dividend is<br>Security<br>specified.                                                                                                                                                                                               |
| Dividend | Type                          | Nature of the dividend.<br>DividendTypeCode                                                                                                                                                                                                              |

| Dividend | CashProceeds          |  |
|----------|-----------------------|--|
| Dividend | Obligation            |  |
| Dividend | Tax                   |  |
| Dividend | RelatedDistribution   |  |
| Dividend | DividendFrequenceType |  |
| Dividend | DividendRatio         |  |
| Dividend | PaymentDate           |  |
| Dividend | PaymentFrequency      |  |
| Dividend | ReinvestmentDate      |  |
| Dividend | Value                 |  |
| Dividend | DeemedAmount          |  |
| Dividend | DeemedRate            |  |

| Dividend                                     | ConduitForeignIncomeAmount |  |
|----------------------------------------------|----------------------------|--|
| InvestmentFundClassProcessingCharacteristics |                            |  |
| InvestmentFundClassProcessingCharacteristics | ReinvestmentFrequency      |  |
| InvestmentFundClassProcessingCharacteristics | FrontEndLoadIndicator      |  |
| InvestmentFundClassProcessingCharacteristics | BackEndLoadIndicator       |  |
| InvestmentFundClassProcessingCharacteristics | SwitchingFeeIndicator      |  |
| InvestmentFundClassProcessingCharacteristics | LimitedSubscriptionPeriod  |  |
| InvestmentFundClassProcessingCharacteristics | LimitedRedemptionPeriod    |  |
| InvestmentFundClassProcessingCharacteristics | Decimalisation             |  |

| InvestmentFundClassProcessingCharacteristics | HoldingTransferableIndicator |  |
|----------------------------------------------|------------------------------|--|
| InvestmentFundClassProcessingCharacteristics | ApplicationForm              |  |
| InvestmentFundClassProcessingCharacteristics | SignatureRequired            |  |
| InvestmentFundClassProcessingCharacteristics | AmountIndicator              |  |
| InvestmentFundClassProcessingCharacteristics | UnitsIndicator               |  |
| InvestmentFundClassProcessingCharacteristics | OrderCutOffDateTime          |  |
| InvestmentFundClassProcessingCharacteristics | SettlementCycle              |  |
| InvestmentFundClassProcessingCharacteristics | FundClass                    |  |
|                                              |                              |  |

| InvestmentFundClassProcessingCharacteristics | HoldingTransferable                   |  |
|----------------------------------------------|---------------------------------------|--|
| InvestmentFundClassProcessingCharacteristics | DealingFrequency                      |  |
| InvestmentFundClassProcessingCharacteristics | LimitedPeriod                         |  |
| InvestmentFundClassProcessingCharacteristics | SettlementAccount                     |  |
| InvestmentFundClassProcessingCharacteristics | Country                               |  |
| InvestmentFundClassProcessingCharacteristics | LocalMarketAnnex                      |  |
| InvestmentFundClassProcessingCharacteristics | EffectiveDate                         |  |
| InvestmentFundClassProcessingCharacteristics | SubsequentSubscriptionApplicationForm |  |
| InvestmentFundClassProcessingCharacteristics | RedemptionForm                        |  |
| InvestmentFundClassProcessingCharacteristics | DealingCurrency                       |  |
|                                              |                                       |  |

| InvestmentFundClassProcessingCharacteristics | DealingCutOffTimeFrame           |  |
|----------------------------------------------|----------------------------------|--|
| InvestmentFundClassProcessingCharacteristics | MinimumHoldingAmount             |  |
| InvestmentFundClassProcessingCharacteristics | MaximumRedemptionUnits           |  |
| InvestmentFundClassProcessingCharacteristics | MinimumHoldingUnits              |  |
| InvestmentFundClassProcessingCharacteristics | MinimumRemainingHoldingAmount    |  |
| InvestmentFundClassProcessingCharacteristics | MaximumRedemptionPercentage      |  |
| InvestmentFundClassProcessingCharacteristics | MaximumRedemptionAmount          |  |
| InvestmentFundClassProcessingCharacteristics | MinimumInitialSubscriptionUnits  |  |
| InvestmentFundClassProcessingCharacteristics | MinimumSubscriptionAmount        |  |
| InvestmentFundClassProcessingCharacteristics | MinimumInitialSubscriptionAmount |  |
|                                              |                                  |  |

| InvestmentFundClassProcessingCharacteristics | MinimumSubscriptionUnits    |  |
|----------------------------------------------|-----------------------------|--|
| InvestmentFundClassProcessingCharacteristics | MinimumHoldingPeriod        |  |
| InvestmentFundClassProcessingCharacteristics | MinimumRedemptionPercentage |  |
| NetAssetValueCalculation                     |                             |  |
| NetAssetValueCalculation                     | ValuationFrequency          |  |
| NetAssetValueCalculation                     | ValuationDateTime           |  |
| NetAssetValueCalculation                     | NetAssetValue               |  |
| NetAssetValueCalculation                     | RelatedFund                 |  |
| NetAssetValueCalculation                     | ValuationType               |  |
| NetAssetValueCalculation                     | SuspendedIndicator          |  |

| NetAssetValueCalculation | ForExecutionIndicator            |
|--------------------------|----------------------------------|
| NetAssetValueCalculation | TaxLiability                     |
| NetAssetValueCalculation | TaxRefund                        |
| NetAssetValueCalculation | OfficialValuationIndicator       |
| NetAssetValueCalculation | EstimatedPriceIndicator          |
| NetAssetValueCalculation | ValuationStatistics              |
| NetAssetValueCalculation | InvestmentFundPerformanceFactors |
| NetAssetValueCalculation | Price                            |
| NetAssetValueCalculation | SecuritiesQuantity               |
| NetAssetValueCalculation | Interest                         |
| NetAssetValueCalculation | FundsCashFlow                    |

| NetAssetValueCalculation | DeclarationChannel                 |  |
|--------------------------|------------------------------------|--|
| NetAssetValueCalculation | DeclarationDate                    |  |
| NetAssetValueCalculation | FirstValuationDate                 |  |
| NetAssetValueCalculation | HistoricPricingIndicator           |  |
| SecuritiesPricing        |                                    |  |
| SecuritiesPricing        | PriceMethod                        |  |
| SecuritiesPricing        | PriceType                          |  |
| SecuritiesPricing        | CumDividendIndicator               |  |
| SecuritiesPricing        | CalculationBasis                   |  |
| SecuritiesPricing        | PriceChangeRelatedStatistics       |  |
| SecuritiesPricing        | Rate                               |  |
| SecuritiesPricing        | HighestPriceValueRelatedStatistics |  |
|                          |                                    |  |

| SecuritiesPricing | LowestPriceValueRelatedStatistics              | Valuation statistics for which a<br>ValuationStatistics<br>lowest price value is specified.                                                    |
|-------------------|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| SecuritiesPricing | Security                                       | Identifies the security for which a<br>Security<br>price is given.                                                                             |
| SecuritiesPricing | SecuritiesTradeExecution                       | Trade execution for which a deal<br>SecuritiesTradeExecution<br>price is specified.                                                            |
| SecuritiesPricing | Yielded                                        | Indicates whether the price is<br>expressed as a yield (yield is the<br>YesNoIndicator<br>annual rate of return expressed<br>as a percentage). |
| SecuritiesPricing | TypeOfRate                                     | Type of value in which the price<br>PriceValueTypeCode<br>(as a rate) is expressed.                                                            |
| SecuritiesPricing | Derivative                                     | Derivative for which an exercise<br>Derivative<br>price is specified.                                                                          |
| SecuritiesPricing | RelatedWarrant                                 | Warrant for which a subscription<br>Warrant<br>price is provided.                                                                              |
| SecuritiesPricing | RelatedSecuritiesConversion                    | Securities conversion process for<br>which a conversion price is<br>SecuritiesConversion<br>specified.                                         |
| SecuritiesPricing | LotBreakdown                                   | Lot for which a price is specified.<br>LotBreakdown                                                                                            |
| SecuritiesPricing | TypeOfAmount                                   | Type of value in which the price<br>AmountPriceTypeCode<br>(as a rate) is expressed.                                                           |
| SecuritiesPricing | ExercisePriceRelatedEvent                      | Corporate action event for which<br>an exercise price is provided.                                                                             |
| SecuritiesPricing | GenericCashPriceReceivedPerProductRelatedEvent | Corporate action event for which<br>a generic cash price received per<br>product is provided.                                                  |

| SecuritiesPricing | AmountPricePerFinancialInstrumentQuantity  |  |
|-------------------|--------------------------------------------|--|
| SecuritiesPricing | AmountPricePerAmount                       |  |
| SecuritiesPricing | GenericCashPricePaidPerProductRelatedEvent |  |
| SecuritiesPricing | PriceCalculationPeriod                     |  |
| SecuritiesPricing | CashInLieuOfSharePriceRelatedEvent         |  |
| SecuritiesPricing | OverSubscriptionDepositPriceRelatedEvent   |  |
| SecuritiesPricing | CashValueForTaxRelatedEvent                |  |
| SecuritiesPricing | MaximumPriceBiddingConditions              |  |
| SecuritiesPricing | MinimumPriceBiddingConditions              |  |
| SecuritiesPricing | QuotationDate                              |  |
| SecuritiesPricing | YieldCalculation                           |  |
| SecuritiesPricing | RelatedSecuritiesFinancing                 |  |

| SecuritiesPricing | FundOrderRelatedToExecutedPrice    |
|-------------------|------------------------------------|
| SecuritiesPricing | FundOrderRelatedToInformativePrice |
| SecuritiesPricing | TaxVoucher                         |
| SecuritiesPricing | SecuritiesTrade                    |
| SecuritiesPricing | NetAssetValueCalculation           |
| SecuritiesPricing | RelatedBuyIn                       |
| SecuritiesPricing | Index                              |
| SecuritiesPricing | InformationPartyRole               |
| SecuritiesPricing | PriceFactPeriod                    |
| SecuritiesPricing | AnalyticsCalculation               |
| SecuritiesPricing | DurationCalculation                |
| SecuritiesPricing | LifeCalculation                    |
| SecuritiesPricing | Date                               |

| SecuritiesPricing | Spread                                          |  |
|-------------------|-------------------------------------------------|--|
| SecuritiesPricing | Order                                           |  |
| SecuritiesPricing | StopPriceOrder                                  |  |
| SecuritiesPricing | Allocation                                      |  |
| SecuritiesPricing | RelatedOrder                                    |  |
| SecuritiesPricing | Issuance                                        |  |
| SecuritiesPricing | Entitlement                                     |  |
| SecuritiesPricing | CashFractionsPriceRelatedSecuritiesDistribution |  |
| SecuritiesPricing | SuscriptionPriceRelatedSecuritiesDistribution   |  |
| SecuritiesPricing | ReinvestmentPriceRelatedSecuritiesDistribution  |  |
| SecuritiesPricing | RelatedFuture                                   |  |
| SecuritiesPricing | Distribution                                    |  |
| SecuritiesPricing | PriceChangeRedemptionSchedule                   |  |
|                   |                                                 |  |

| SecuritiesPricing | RelatedRedemptionSchedule                 |  |
|-------------------|-------------------------------------------|--|
| SecuritiesPricing | PreviousClosingPriceRelatedQuote          |  |
| SecuritiesPricing | RequestedPriceRelatedQuote                |  |
| SecuritiesPricing | PriceRelatedQuote                         |  |
| SecuritiesPricing | MarketPriceRelatedQuote                   |  |
| SecuritiesPricing | Price                                     |  |
| SecuritiesPricing | RelatedCorporateActionPrice               |  |
| SecuritiesPricing | RelatedPosition                           |  |
| SecuritiesPricing | MinimumCashToInstructRelatedEvent         |  |
| SecuritiesPricing | MaximumCashToInstructRelatedEvent         |  |
| SecuritiesPricing | MinimumMultipleCashToInstructRelatedEvent |  |
| RolePlayer        |                                           |  |
| RolePlayer        | Role                                      |  |
| RolePlayer        | ValidityPeriod                            |  |

| Party | RolePlayer           |  |
|-------|----------------------|--|
| Party | ContactPoint         |  |
| Party | Identification       |  |
| Party | MoneyLaunderingCheck |  |
| Party | TaxationConditions   |  |
| Party | Domicile             |  |
| Party | Residence            |  |
| Party | PowerOfAttorney      |  |
| Party | Location             |  |
| Party | CloseLinkSecurity    |  |
| Party | CreditQuality        |  |

| Party<br>ShareholdingType<br>Party<br>RelatedCareOf<br>Organisation<br>Party<br>Organisation<br>Purpose<br>Organisation<br>RegistrationDate<br>Organisation<br>OrganisationIdentification<br>Organisation<br>ParentOrganisation<br>Organisation<br>Branch<br>Organisation<br>SecuritiesModification |  |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                     |  |  |

| Organisation | PlaceOfOperation            |  |
|--------------|-----------------------------|--|
| Organisation | PlaceOfRegistration         |  |
| Organisation | Description                 |  |
| Organisation | LegalStructure              |  |
| Organisation | Sector                      |  |
| Organisation | RelatedIndicationOfInterest |  |
| Organisation | Strategy                    |  |
| Organisation | OrganisationHierarchy       |  |
| Organisation | RepresentativeOfficer       |  |
| Organisation | EstablishmentDate           |  |
| Organisation | EntityExpirationDate        |  |

| Organisation | EntityExpirationReason                   |
|--------------|------------------------------------------|
| Organisation | EntityStatus                             |
| Organisation | MerchantCategory                         |
| Organisation | Logo                                     |
| Organisation | RelatedUltimateCreditrorEnrolmentService |
| Organisation | RelatedCreditrorEnrolmentService         |
| Organisation | RelatedPostTradeRiskReduction            |
| PartyName    |                                          |
| PartyName    | Name                                     |

| PartyName    | PartyIdentification         |  |
|--------------|-----------------------------|--|
| ContactPoint |                             |  |
| ContactPoint | Identification              |  |
| ContactPoint | RelatedInvestmentFund       |  |
| ContactPoint | BICAddress                  |  |
| ContactPoint | RelatedParty                |  |
| ContactPoint | RelatedCorporateActionEvent |  |
| ContactPoint | RelatedReportingService     |  |
| ContactPoint | StoredDocument              |  |
| ContactPoint | RemittanceRelatedPayment    |  |
| ContactPoint | RelatedProxyAppointment     |  |
| ContactPoint | ContactPointForMeeting      |  |
| ContactPoint | ContactPointForVote         |  |

| ContactPoint  | MainContact                   |              |
|---------------|-------------------------------|--------------|
| ContactPoint  | ReturnAddress                 |              |
|               |                               |              |
| ContactPoint  | RelatedPayment                |              |
| ContactPoint  | TemporaryIndicator            |              |
| ContactPoint  | DeliveredAttendanceCard       |              |
| ContactPoint  | InvestmentFundClassProcessing |              |
| PostalAddress |                               | ContactPoint |
| PostalAddress | AddressType                   |              |
| PostalAddress | StreetName                    |              |
| PostalAddress | StreetBuildingIdentification  |              |
| PostalAddress | PostCodeIdentification        |              |
|               |                               |              |

| TownName               |
|------------------------|
| BuildingName           |
| Floor                  |
| PostOfficeBox          |
| Department             |
| SubDepartment          |
| Location               |
| ChequeIssue            |
| Country                |
| ValidityPeriod         |
| SuiteIdentification    |
| BuildingIdentification |
|                        |

| PostalAddress | MailDeliverySubLocation |              |
|---------------|-------------------------|--------------|
| PostalAddress | Block                   |              |
| PostalAddress | Lot                     |              |
| PostalAddress | MailingInstructions     |              |
| PostalAddress | PhysicalDelivery        |              |
| PostalAddress | UnitNumber              |              |
| PostalAddress | CareOf                  |              |
| PhoneAddress  |                         | ContactPoint |
| PhoneAddress  | PhoneNumber             |              |

| PhoneAddress                   | FaxNumber           |              |
|--------------------------------|---------------------|--------------|
| PhoneAddress                   | MobileNumber        |              |
| ElectronicAddress              |                     | ContactPoint |
| ElectronicAddress              | EmailAddress        |              |
| ElectronicAddress              | URLAddress          |              |
| ElectronicAddress              | TelexAddress        |              |
| ElectronicAddress              | RelatedPresentation |              |
| ElectronicAddress              | TeletextAddress     |              |
| ElectronicAddress              | ISDNAddress         |              |
| PartyIdentificationInformation |                     |              |

| PartyIdentificationInformation | OtherIdentification           |  |
|--------------------------------|-------------------------------|--|
| PartyIdentificationInformation | IdentifiedParty               |  |
| PartyIdentificationInformation | TaxIdentificationNumber       |  |
| PartyIdentificationInformation | NationalRegistrationNumber    |  |
| PartyIdentificationInformation | TypeOfIdentification          |  |
| PartyIdentificationInformation | Declaration                   |  |
| PartyIdentificationInformation | PartyType                     |  |
| PartyIdentificationInformation | PartyName                     |  |
| PartyIdentificationInformation | ValidityPeriod                |  |
| PartyIdentificationInformation | IdentifiedMarket              |  |
| PartyIdentificationInformation | RelatedApprovedBenchmark      |  |
| PartyIdentificationInformation | RelatedAdministratedBenchmark |  |

| RegistrationAuthorityIdentification    |
|----------------------------------------|
| PartyIdentificationInformation         |
| BICFI                                  |
| AnyBIC                                 |
| OrganisationName                       |
| Organisation                           |
| ClearingSystemMemberIdentificationType |
|                                        |

| OrganisationIdentification | BICNonFI                 |  |
|----------------------------|--------------------------|--|
| OrganisationIdentification | EANGLN                   |  |
| OrganisationIdentification | CHIPSUniversalIdentifier |  |
| OrganisationIdentification | DUNS                     |  |

| OrganisationIdentification | BankPartyIdentification |           |
|----------------------------|-------------------------|-----------|
| OrganisationIdentification | MIC                     |           |
| OrganisationIdentification | LEI                     |           |
| OrganisationIdentification | ELF                     |           |
| OrganisationIdentification | AdditionalLEIAttributes |           |
| PersonName                 |                         | PartyName |
| PersonName                 | BirthName               |           |
| PersonName                 | NamePrefix              |           |
| PersonName                 | GivenName               |           |
| PersonName                 | MiddleName              |           |

| PersonName<br>NameSuffix<br>PersonName<br>Identification<br>TimeFrame<br>TimeFrame<br>TradeMinus<br>TimeFrame<br>RenunciationMinus<br>TimeFrame<br>SubscriptionSettlementRelatedFundProcessing<br>TimeFrame<br>TradePlus |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |

| TimeFrame | RenunciationPlus                 |  |
|-----------|----------------------------------|--|
| TimeFrame | Prepayment                       |  |
| TimeFrame | OtherTimeFrameDescription        |  |
| TimeFrame | RelatedProcessingCharacteristics |  |
| Account   |                                  |  |
| Account   | BaseCurrency                     |  |
| Account   | Identification                   |  |
| Account   | ParentAccount                    |  |
| Account   | SubAccount                       |  |

| Account | RelatedFundProcessingCharacteristics |  |
|---------|--------------------------------------|--|
| Account | Status                               |  |
| Account | Language                             |  |
| Account | PartyRole                            |  |
| Account | TradePartyRole                       |  |
| Account | ReportingCurrency                    |  |
| Account | AccountRestriction                   |  |
| Account | SettlementPartyRole                  |  |
| Account | Purpose                              |  |
| Account | ClosingDate                          |  |
| Account | LiveDate                             |  |
|         |                                      |  |

| Account | ReportedPeriod                  |  |
|---------|---------------------------------|--|
| Account | InvestmentFundPartyRole         |  |
| Account | RelatedCollateralProcess        |  |
| Account | Type                            |  |
| Account | RelatedProceedsDelivery         |  |
| Account | RelatedCorporateActionPartyRole |  |
| Account | DefaultFundAccountOwner         |  |
| Account | System                          |  |
| Account | Balance                         |  |
| Account | Entry                           |  |
| Account | AccountContract                 |  |
|         |                                 |  |

| Account     | OpeningDate             |         |
|-------------|-------------------------|---------|
| Account     | CurrencyExchange        |         |
| Account     | DefaultFundContribution |         |
| Account     | SystemMember            |         |
| Account     | CollateralAccountType   |         |
| Account     | AccountService          |         |
| Account     | Reconciliation          |         |
| Account     | ManagedAccountProduct   |         |
| CashAccount |                         | Account |
| CashAccount | CashAccountType         |         |

| CashAccount | RelatedInvestmentAccount       |  |
|-------------|--------------------------------|--|
| CashAccount | CashEntry                      |  |
| CashAccount | CashBalance                    |  |
| CashAccount | PaymentPartyRole               |  |
| CashAccount | RelatedCreditStandingOrder     |  |
| CashAccount | RelatedDebitStandingOrder      |  |
| CashAccount | CashAccountContract            |  |
| CashAccount | RelatedCorporateActionElection |  |
| CashAccount | Charges                        |  |
|             |                                |  |

| CashAccount | Tax                              | Tax charged on a cash account.<br>Tax                                                                                                                       |
|-------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CashAccount | RelatedSettlementInstruction     | Settlement process which uses<br>CashSettlement<br>specific cash accounts.                                                                                  |
| CashAccount | CashSettlementPartyRole          | Specifies each role linked to a<br>payment settlement and using a<br>CashSettlementInstructionPartyRole<br>specific cash account in the<br>payment context. |
| CashAccount | UltimateObligor                  | Party for which different types of<br>UndertakingUltimateObligor<br>cash accounts are specified.                                                            |
| CashAccount | RelatedPaymentCard               | Payment card for which an<br>PaymentCard<br>account is specified.                                                                                           |
| CashAccount | SecuritiesPartyRole              | Specifies the role which uses a<br>SecuritiesPartyRole<br>cash account.                                                                                     |
| CashAccount | RelatedInvoiceFinancingPartyRole | Specifies each role using a<br>specific account in the context of<br>InvoiceFinancingPartyRole<br>invoice financing.                                        |
| CashAccount | RelatedCommercialTrade           | Commercial trade for which a<br>CommercialTrade<br>purchase account is specified.                                                                           |
| CashAccount | Level                            | Defines the level of an account<br>AccountLevelCode<br>within the account hierarchy.                                                                        |
| CashAccount | SettlementCurrency               | Specifies the currency used for<br>settlement, if different from the<br>CurrencyCode<br>account currency.                                                   |
| CashAccount | ReportedMovements                | Provides statistical information<br>on the number of movements<br>AccountReportedMovement<br>and their value for a particular<br>account.                   |

| CashAccount           | ClosedAccountContract |  |
|-----------------------|-----------------------|--|
| CashAccount           | AccountLink           |  |
| CashAccount           | CashStandingOrder     |  |
| CashAccount           | Cheque                |  |
| CashAccount           | CashAccountService    |  |
| CashAccount           | Payment               |  |
| CashAccount           | Commission            |  |
| AccountIdentification |                       |  |
| AccountIdentification | Account               |  |

| AccountIdentification | IBAN                      |  |
|-----------------------|---------------------------|--|
| AccountIdentification | BBAN                      |  |
| AccountIdentification | UPIC                      |  |
| AccountIdentification | ProprietaryIdentification |  |

| AccountIdentification | Name                  |              |
|-----------------------|-----------------------|--------------|
| AccountIdentification | CostReferencePattern  |              |
| AccountIdentification | Number                |              |
| FinancialInstitution  |                       | Organisation |
| FinancialInstitution  | RelatedPaymentTracker |              |
|                       |                       |              |
| Location              |                       |              |
| Location              | NativePerson          |              |
| Location              | System                |              |
| Location              | DomiciledParty        |              |
| Location              | OperatingOrganisation |              |

| Location | Address                        | Information that locates and<br>PostalAddress<br>identifies a specific address.                                                                                                                      |  |
|----------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Location | IssuedDocument                 | Document which was issued at a<br>Document<br>specific location.                                                                                                                                     |  |
| Location | Incoterms                      | Incoterms associated with a<br>Incoterms<br>location.                                                                                                                                                |  |
| Location | DepartureTransportParameters   | Transport parameters linked to a<br>Transport<br>place of departure.                                                                                                                                 |  |
| Location | DestinationTransportParameters | Transport parameters linked to a<br>Transport<br>place of destination.                                                                                                                               |  |
| Location | InsuranceCertificate           | Insurance for which the claims<br>InsuranceCertificate<br>are payable at a specific location.                                                                                                        |  |
| Location | Party                          | Party which resides in a specific<br>Party<br>location.                                                                                                                                              |  |
| Location | RelatedExpiry                  | Expiry information which<br>Expiry<br>contains an expiry location.                                                                                                                                   |  |
| Location | RelatedJurisdiction            | Jurisdiction of the location.<br>Jurisdiction                                                                                                                                                        |  |
| Location | Identification                 | Identifies the location, for<br>instance, the name of an airport,<br>a county, a state, a province or a<br>GenericIdentification<br>city by a code or a text. eg LHR<br>for London Heathrow airport. |  |
| Location | TaxableParty                   | Party which is taxable at a<br>Party<br>specific location                                                                                                                                            |  |
| Location | RegisteredOrganisation         | Organisation which is registered<br>Organisation<br>at that location.                                                                                                                                |  |
| Location | RelatedTransport               | Transport process for which a<br>Transport<br>transit location is specified.                                                                                                                         |  |

| Location           | TimeZone              |  |
|--------------------|-----------------------|--|
| UTCOffset          |                       |  |
| UTCOffset          | Sign                  |  |
| UTCOffset          | NumberOfHours         |  |
| UTCOffset          | Location              |  |
| RedemptionSchedule |                       |  |
| RedemptionSchedule | BusinessDayConvention |  |
| RedemptionSchedule | EffectivePeriod       |  |
| RedemptionSchedule | PriceChange           |  |
| RedemptionSchedule | Price                 |  |
| RedemptionSchedule | PartyType             |  |
| RedemptionSchedule | AmountFulfilType      |  |

| RedemptionSchedule | MinimumNoticeDays    |        |
|--------------------|----------------------|--------|
| RedemptionSchedule | MaximumNoticeDays    |        |
| RedemptionSchedule | FinancialCenter      |        |
| RedemptionSchedule | NoticePeriodType     |        |
| RedemptionSchedule | PriceChangeFrequency |        |
| RedemptionSchedule | PriceFrequency       |        |
| RedemptionSchedule | Security             |        |
| TradingMarket      |                      | Market |
| TradingMarket      | TradedSecurity       |        |

| TradingMarket | Type                         |  |
|---------------|------------------------------|--|
| TradingMarket | ListedSecurity               |  |
| TradingMarket | SourceOfPrice                |  |
| TradingMarket | TradeLotSize                 |  |
| TradingMarket | MinimumTradedNominalQuantity |  |
| TradingMarket | ListingDate                  |  |
| TradingMarket | RelatedOrder                 |  |
| TradingMarket | TradingCurrency              |  |
| TradingMarket | MaximumTradedNominalQuantity |  |
| TradingMarket | StockExchange                |  |
| TradingMarket | QuoteLot                     |  |

| TradingMarket | RoundLot                            |  |
|---------------|-------------------------------------|--|
| TradingMarket | TradingSession                      |  |
| TradingMarket | ListedSecurityTradingIdentification |  |
| TradingMarket | DefaultCurrency                     |  |
| TradingMarket | FirstTradingDate                    |  |
| TradingMarket | LastTradingDate                     |  |
| TradingMarket | Issuance                            |  |
| TradingMarket | RelatedPlaceOfSettlement            |  |
| Trade         |                                     |  |
| Trade         | TradeDateTime                       |  |

| Trade | TradeCommission             |  |
|-------|-----------------------------|--|
| Trade | ValueDate                   |  |
| Trade | EndDate                     |  |
| Trade | TradeRelatedIdentifications |  |
| Trade | AllocationIndicator         |  |
| Trade | CollateralisationType       |  |
| Trade | BlockIndicator              |  |
| Trade | SettlementNetting           |  |
| Trade | TradePartyRole              |  |
| Trade | Obligation                  |  |
| Trade | RelatedNegotiation          |  |
| Trade | GoverningDocument           |  |
|       |                             |  |

| Trade  | StartDate            |  |
|--------|----------------------|--|
| Trade  | System               |  |
| Trade  | Asset                |  |
| Trade  | Market               |  |
| Trade  | Guarantee            |  |
| Trade  | Settlement           |  |
| Trade  | Order                |  |
| Trade  | Leg                  |  |
| Trade  | FinancialTransaction |  |
| Trade  | Reconciliation       |  |
| Scheme |                      |  |
| Scheme | NameShort            |  |

| Scheme | Code                     |  |
|--------|--------------------------|--|
| Scheme | Identification           |  |
| Scheme | Rating                   |  |
| Scheme | CreditorRole             |  |
| Scheme | InformationPartyRole     |  |
| Scheme | Version                  |  |
| Scheme | AssessmentValidityPeriod |  |
| Scheme | NameLong                 |  |
| Scheme | Description              |  |
| Scheme | DomainValueCode          |  |
| Scheme | DomainValueName          |  |
| Scheme | Sector                   |  |
|        |                          |  |

| Scheme         | AssetClassification            |  |
|----------------|--------------------------------|--|
| DateTimePeriod |                                |  |
| DateTimePeriod | FromDateTime                   |  |
| DateTimePeriod | ToDateTime                     |  |
| DateTimePeriod | RelatedStandingOrder           |  |
| DateTimePeriod | PaymentInstruction             |  |
| DateTimePeriod | NumberOfDays                   |  |
| DateTimePeriod | ValuationStatistics            |  |
| DateTimePeriod | PerformanceFactors             |  |
| DateTimePeriod | Status                         |  |
| DateTimePeriod | PriceCalculationRelatedPricing |  |
| DateTimePeriod | CorporateActionOption          |  |
|                |                                |  |

| DateTimePeriod | ParallelTradingProceedsDefinition       |  |
|----------------|-----------------------------------------|--|
| DateTimePeriod | PrivilegeSuspensionCorporateAction      |  |
| DateTimePeriod | WithdrawalSuspensionRelatedEvent        |  |
| DateTimePeriod | RelatedInterestCalculation              |  |
| DateTimePeriod | BiddingConditions                       |  |
| DateTimePeriod | ClassAction                             |  |
| DateTimePeriod | BookEntryTransferSuspensionRelatedEvent |  |
| DateTimePeriod | DepositAtAgentSuspensionRelatedEvent    |  |
| DateTimePeriod | DepositSuspensionRelatedEvent           |  |
| DateTimePeriod | PledgeSuspensionRelatedEvent            |  |
|                |                                         |  |

| DateTimePeriod | SegregationPeriodRelatedEvent                 |  |
|----------------|-----------------------------------------------|--|
| DateTimePeriod | WithdrawalAtAgentSuspensionRelatedEvent       |  |
| DateTimePeriod | WithdrawalInNomineeNameSuspensionRelatedEvent |  |
| DateTimePeriod | WithdrawalInStreetNameSuspensionRelatedEvent  |  |
| DateTimePeriod | BookClosureCorporateAction                    |  |
| DateTimePeriod | CoDepositoriesSuspensionRelatedEvent          |  |
| DateTimePeriod | ExtendiblePeriodDebt                          |  |
| DateTimePeriod | SecuritiesConversion                          |  |
| DateTimePeriod | YieldCalculation                              |  |
| DateTimePeriod | CustomDateDebt                                |  |
|                |                                               |  |

| DateTimePeriod | TaxPeriod                            |  |
|----------------|--------------------------------------|--|
| DateTimePeriod | Account                              |  |
| DateTimePeriod | RelatedAgreement                     |  |
| DateTimePeriod | AssentedLinePeriodProceedsDefinition |  |
| DateTimePeriod | SellThruIssuerProceedsDefinition     |  |
| DateTimePeriod | RelatedProductDelivery               |  |
| DateTimePeriod | RelatedInvoice                       |  |
| DateTimePeriod | TradeCertificate                     |  |
| DateTimePeriod | RelatedPortfolioValuation            |  |
| DateTimePeriod | System                               |  |
| DateTimePeriod | AccountRestriction                   |  |
| DateTimePeriod | BankOperation                        |  |
| DateTimePeriod | RelatedCorporateAction               |  |
|                |                                      |  |

| DateTimePeriod | RelatedLimit               |  |
|----------------|----------------------------|--|
| DateTimePeriod | RelatedIdentification      |  |
| DateTimePeriod | AssessmentValidityScheme   |  |
| DateTimePeriod | ExercisePeriodDistribution |  |
| DateTimePeriod | OfferPeriodDistribution    |  |
| DateTimePeriod | TradingPeriodDistribution  |  |
| DateTimePeriod | BlockingPeriodDistribution |  |
| DateTimePeriod | Guarantee                  |  |
| DateTimePeriod | PriceFactRelatedPricing    |  |
| DateTimePeriod | CashDistribution           |  |
| DateTimePeriod | ComponentSecurity          |  |
| DateTimePeriod | TradingSession             |  |
|                |                            |  |

| DateTimePeriod | FinancialInstrumentSwap              | Swap for which a maturity period<br>FinancialInstrumentSwap<br>is specified.                             |
|----------------|--------------------------------------|----------------------------------------------------------------------------------------------------------|
| DateTimePeriod | RelatedPostalAddress                 | Postal address for which a<br>PostalAddress<br>validity period is specified.                             |
| DateTimePeriod | RedemptionSchedule                   | Redemption schedule for which a<br>RedemptionSchedule<br>notice period is provided.                      |
| DateTimePeriod | RelatedAccountLink                   | Link between two accounts for<br>which a validity period is<br>AccountLink<br>specified.                 |
| DateTimePeriod | RelatedAdjustment                    | Adjustment for which a validity<br>Adjustment<br>period is provided.                                     |
| DateTimePeriod | RelatedSecuritiesIdentification      | Securities identification for which<br>SecuritiesIdentification<br>a validity period is specified.       |
| DateTimePeriod | RelatedStandingSettlementInstruction | SSI for which a validity period is<br>StandingSettlementInstruction<br>specified.                        |
| DateTimePeriod | RelatedSecuritiesRegistration        | Securities registration process for<br>BasicSecuritiesRegistration<br>which a split period is specified. |
| DateTimePeriod | Amount                               | Relationship with an amount.<br>AmountAndPeriod                                                          |
| DateTimePeriod | RelatedInvestmentPlan                | InvestmentPlan for which an<br>InvestmentPlan<br>investment period is specified.                         |
| DateTimePeriod | Issuance                             | Issuance for which subscription<br>Issuance<br>information is provided.                                  |
| DateTimePeriod | RelatedPaymentTerms                  | Payment terms for which a<br>PaymentTerms<br>period is specified.                                        |
| DateTimePeriod | Percentage                           | Relationship with a percentage.<br>PercentageAndPeriod                                                   |
| DateTimePeriod | RelatedRolePlayer                    | Role player for which a validity<br>RolePlayer<br>period is specified.                                   |
|                |                                      |                                                                                                          |

| DateTimePeriod    | RelatedSystemAvailability |         |
|-------------------|---------------------------|---------|
| SecuritiesAccount |                           | Account |
| SecuritiesAccount | SecuritiesAccountType     |         |
| SecuritiesAccount | RelatedInvestmentAccount  |         |
| SecuritiesAccount | RelatedTransfer           |         |
| SecuritiesAccount | SecuritiesPartyRole       |         |
| SecuritiesAccount | Security                  |         |
| SecuritiesAccount | RelatedRegistrar          |         |
| SecuritiesAccount | SafekeepingPlace          |         |
| SecuritiesAccount | SecuritiesBalance         |         |
| SecuritiesAccount | CorporateActionServicing  |         |
| SecuritiesAccount | RelatedAllocation         |         |

| SecuritiesAccount | SecuritiesEntry           |                  |
|-------------------|---------------------------|------------------|
| SecuritiesAccount | ClearingAccountOwner      |                  |
| SecuritiesAccount | MarginAccountOwner        |                  |
| SecuritiesAccount | DeliveryAccountOwner      |                  |
| SecuritiesAccount | RelatedPowerOfAttorney    |                  |
| SecuritiesAccount | RelatedMeetingInstruction |                  |
| SecuritiesAccount | ClearingAccountType       |                  |
| SecuritiesAccount | RelatedOrder              |                  |
| SecuritiesAccount | DisclosedListTrading      |                  |
| SecuritiesAccount | AccountLink               |                  |
| AccountPartyRole  |                           | Role             |
| AccountPartyRole  | Account                   |                  |
| AccountOwnerRole  |                           | AccountPartyRole |

| Product |                       |  |
|---------|-----------------------|--|
| Product | CardPayment           |  |
| Product | UnitPrice             |  |
| Product | ProductCategory       |  |
| Product | LineItem              |  |
| Product | ProductIdentification |  |
| Product | Name                  |  |
| Product | Description           |  |
| Product | Origin                |  |
| Product | Characteristics       |  |
| Product | NetPrice              |  |
| Product | Quantity              |  |
| Product | GrossPrice            |  |
| Product | Quality               |  |
| Product | Delivery              |  |

| Product        | PurchaseOrder   |                  |
|----------------|-----------------|------------------|
| Product        | Tax             |                  |
| Service        |                 | Product          |
| Service        | Amount          |                  |
| Service        | Type            |                  |
| Service        | TaxDesignation  |                  |
| Service        | Rate            |                  |
| AccountService |                 | FinancialService |
| AccountService | AccountContract |                  |
| AccountService | Reservation     |                  |
| AccountService | Account         |                  |
|                |                 |                  |

| AccountService<br>AccountAdministrationCharge<br>ReportingService<br>AccountService<br>ReportingService<br>StatementFrequency<br>ReportingService<br>FloorNotificationAmount<br>ReportingService<br>CeilingNotificationAmount<br>ReportingService<br>ReportingChannel<br>ReportingService<br>RelatedInvestmentAccountService |  |  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                              |  |  |
|                                                                                                                                                                                                                                                                                                                              |  |  |

| InvestmentAccount |                       | Account |
|-------------------|-----------------------|---------|
| InvestmentAccount | InvestmentAccountType |         |
| InvestmentAccount | OwnershipType         |         |
| InvestmentAccount | Designation           |         |
| InvestmentAccount | ReferenceCurrency     |         |
| InvestmentAccount | InvestmentFundClass   |         |
| InvestmentAccount | CashAccount           |         |
|                   |                       |         |

| InvestmentAccount | SecuritiesAccount                  | Part of the investment account to<br>or from which securities entries<br>are made.               |
|-------------------|------------------------------------|--------------------------------------------------------------------------------------------------|
| InvestmentAccount | InvestmentFundTax                  | Taxes specific to the account.                                                                   |
| InvestmentAccount | InvestmentFundTransaction          | Investment fund transaction<br>which uses the investment<br>account.                             |
| InvestmentAccount | SidePocket                         | Separate account containing<br>illiquid assets of a hedge fund<br>portfolio.                     |
| InvestmentAccount | InvestmentAccountPartyRole         | Specifies each role linked to an<br>investment account and played<br>by a party in that context. |
| InvestmentAccount | DebitPortfolioTransfer             | Transfer process for which a<br>debit investment account is<br>specified.                        |
| InvestmentAccount | CreditPortfolioTransfer            | Transfer process for which a<br>beneficiary investment account is<br>specified.                  |
| InvestmentAccount | AccountForInvestmentFundProcessing | Order desk for which an account<br>is specified.                                                 |
| InvestmentAccount | InvestmentAccountContract          | Contract defining the related<br>account                                                         |
| InvestmentAccount | AccountUsageType                   | Specifies whether the account is<br>used for investment or for<br>settlement purpose.            |
| InvestmentAccount | Category                           | Specifies the investment account<br>category.                                                    |
| InvestmentAccount | Portfolio                          | Portfolio held on an account.                                                                    |

| InvestmentAccount | RelatedPortfolioTransfer     |  |
|-------------------|------------------------------|--|
| InvestmentAccount | UsufructPercentage           |  |
| InvestmentAccount | OwnershipPercentage          |  |
| Tax               |                              |  |
| Tax               | ExemptionReason              |  |
| Tax               | Country                      |  |
| Tax               | TaxLiabilityValueCalculation |  |
| Tax               | Type                         |  |
| Tax               | Amount                       |  |
| Tax               | Rate                         |  |
| Tax               | TaxableParty                 |  |
| Tax               | TaxRefundValueCalculation    |  |
|                   |                              |  |

| Tax | Basis                     |  |
|-----|---------------------------|--|
| Tax | SecuritiesTransfer        |  |
| Tax | TaxRateType               |  |
| Tax | TaxAccount                |  |
| Tax | TaxationConditions        |  |
| Tax | Adjustment                |  |
| Tax | Interest                  |  |
| Tax | Identification            |  |
| Tax | RelatedPaymentSettlement  |  |
| Tax | TaxableBaseAmount         |  |
| Tax | TaxDate                   |  |
| Tax | CertificateIdentification |  |
| Tax | AdministrationZone        |  |

| Tax | Method                             |  |
|-----|------------------------------------|--|
| Tax | Record                             |  |
| Tax | Product                            |  |
| Tax | CurrencyExchange                   |  |
| Tax | Currency                           |  |
| Tax | PartyRole                          |  |
| Tax | TaxDeduction                       |  |
| Tax | RelatedCorporateActionDistribution |  |
| Tax | CalculationDate                    |  |
| Tax | Dividend                           |  |
| Tax | WithholdingTaxType                 |  |
| Tax | CorporateActionEvent               |  |
| Tax | TaxIdentificationType              |  |
| Tax | TaxRateMarker                      |  |
|     |                                    |  |

| InvestmentAccountService |                                    | AccountService |
|--------------------------|------------------------------------|----------------|
| InvestmentAccountService | IncomePreference                   |                |
| InvestmentAccountService | TaxWithholdingMethod               |                |
| InvestmentAccountService | RoundingMethod                     |                |
| InvestmentAccountService | BeneficiaryCertificationIndicator  |                |
| InvestmentAccountService | BeneficiaryCertificationCompletion |                |
| InvestmentAccountService | SystematicInvestmentPlan           |                |

| InvestmentAccountService | InvestmentAccountContract    |  |
|--------------------------|------------------------------|--|
| InvestmentAccountService | ReportingService             |  |
| InvestmentAccountService | Reinvestment                 |  |
| Status                   |                              |  |
| Status                   | StatusReason                 |  |
| Status                   | StatusDateTime               |  |
| Status                   | ValidityTime                 |  |
| Status                   | StatusDescription            |  |
| Status                   | InstructionProcessingStatus  |  |
| Status                   | PartyRole                    |  |
| Status                   | SettlementStatus             |  |
| Status                   | CancellationProcessingStatus |  |
| Status                   | TransactionProcessingStatus  |  |
|                          |                              |  |

| Status        | ModificationProcessingStatus |        |
|---------------|------------------------------|--------|
| AccountStatus |                              | Status |
| AccountStatus | Account                      |        |
| AccountStatus | Status                       |        |
| AccountStatus | Blocked                      |        |
| AccountStatus | ManagementStatus             |        |
| AccountStatus | EntryStatus                  |        |
| AccountStatus | BalanceStatus                |        |
| AccountStatus | BlockedReason                |        |
| Agreement     |                              |        |
| Agreement     | DateSigned                   |        |
| Agreement     | Description                  |        |

| Agreement       | Version           |           |
|-----------------|-------------------|-----------|
| Agreement       | ValidityPeriod    |           |
| Agreement       | Document          |           |
| Agreement       | Trade             |           |
| Agreement       | Jurisdiction      |           |
| Contract        |                   | Agreement |
| Contract        | MasterAgreement   |           |
| AccountContract |                   | Contract  |
| AccountContract | TargetClosingDate |           |
| AccountContract | UrgencyFlag       |           |
|                 |                   |           |

| AccountContract           | RemovalIndicator     |                 |
|---------------------------|----------------------|-----------------|
| AccountContract           | TargetGoLiveDate     |                 |
| AccountContract           | AccountService       |                 |
| AccountContract           | Account              |                 |
| AccountContract           | Interest             |                 |
| AccountContract           | RequestDate          |                 |
| AccountContract           | AccountAuthorisation |                 |
| AccountContract           | TransactionChannel   |                 |
| InvestmentAccountContract |                      | AccountContract |

| InvestmentAccountContract | LetterIntentReference      |  |
|---------------------------|----------------------------|--|
| InvestmentAccountContract | AccumulationRightReference |  |
| InvestmentAccountContract | InvestmentAccount          |  |
| InvestmentAccountContract | Services                   |  |
| InvestmentAccountContract | ModeledAccount             |  |
| SignatureCondition        |                            |  |
|                           |                            |  |

| SignatureCondition   | RequiredSignatureNumber |  |
|----------------------|-------------------------|--|
| SignatureCondition   | SignatoryRightIndicator |  |
| SignatureCondition   | Mandate                 |  |
| SignatureCondition   | SignatureOrderIndicator |  |
| SignatureCondition   | SignatureOrder          |  |
| SignatureCondition   | Signature               |  |
| InvestmentFundFamily |                         |  |
| InvestmentFundFamily | FundFamilyName          |  |
| InvestmentFundFamily | InvestmentFund          |  |

| RoundingParameters         |                            |                  |
|----------------------------|----------------------------|------------------|
| RoundingParameters         | InvestmentAccountService   |                  |
| RoundingParameters         | RoundingModulus            |                  |
| RoundingParameters         | RoundingDirection          |                  |
| RoundingParameters         | RelatedPegOrderInstruction |                  |
| InvestmentAccountPartyRole |                            | AccountPartyRole |
| InvestmentAccountPartyRole | OwnershipBeneficiaryRate   |                  |
| InvestmentAccountPartyRole | InvestmentAccount          |                  |
| InvestmentAccountPartyRole | FATCAFormType              |                  |

| InvestmentAccountPartyRole | FATCAStatus                  |                            |
|----------------------------|------------------------------|----------------------------|
| InvestmentAccountPartyRole | CRSStatus                    |                            |
| PrimaryOwner               |                              | InvestmentAccountPartyRole |
| OrganisationName           |                              | PartyName                  |
| OrganisationName           | Organisation                 |                            |
| OrganisationName           | LegalName                    |                            |
| OrganisationName           | TradingName                  |                            |
| OrganisationName           | ShortName                    |                            |
| MailingInstructions        |                              |                            |
| MailingInstructions        | MailingIndicator             |                            |
| MailingInstructions        | RegistrationAddressIndicator |                            |

| MailingInstructions | RelatedPostalAddress  |       |
|---------------------|-----------------------|-------|
| Person              |                       | Party |
| Person              | Gender                |       |
| Person              | Language              |       |
| Person              | BirthDate             |       |
| Person              | PlaceOfBirth          |       |
| Person              | Profession            |       |
| Person              | ResidentialStatus     |       |
| Person              | Nationality           |       |
| Person              | MinorIndicator        |       |
| Person              | BusinessFunctionTitle |       |

| Person               | PersonIdentification   |                                |
|----------------------|------------------------|--------------------------------|
| Person               | EmployingParty         |                                |
| Person               | MeetingAttendee        |                                |
| Person               | RelatedRole            |                                |
| Person               | PreAssignedProxyPerson |                                |
| Person               | PersonProfile          |                                |
| Person               | ContactPersonRole      |                                |
| Person               | Household              |                                |
| Person               | CivilStatus            |                                |
| Person               | DeathDate              |                                |
| Person               | CitizenshipEndDate     |                                |
| Person               | CitizenshipStartDate   |                                |
| PersonIdentification |                        | PartyIdentificationInformation |

| PersonIdentification<br>SocialSecurityNumber         |
|------------------------------------------------------|
| PersonIdentification<br>Person                       |
| PersonIdentification<br>PersonName                   |
| PersonIdentification<br>DriversLicenseNumber         |
| PersonIdentification<br>AlienRegistrationNumber      |
| PersonIdentification<br>PassportNumber               |
| PersonIdentification<br>IdentityCardNumber           |
| PersonIdentification<br>EmployerIdentificationNumber |
| EmployingPartyRole<br>Role                           |
| EmployingPartyRole<br>Employee                       |

| Document |                   |  |
|----------|-------------------|--|
| Document | IssueDate         |  |
| Document | CopyDuplicate     |  |
| Document | PlaceOfStorage    |  |
| Document | PaymentObligation |  |
| Document | Type              |  |
| Document | Amount            |  |
| Document | Agreement         |  |
| Document | PlaceOfIssue      |  |
| Document | DocumentVersion   |  |
| Document | Status            |  |
|          |                   |  |

| Document | Reconciliation         |  |
|----------|------------------------|--|
| Document | LetterOfCredit         |  |
| Document | PartyRole              |  |
| Document | DataSetType            |  |
| Document | Transport              |  |
| Document | SignedIndicator        |  |
| Document | RemittedAmount         |  |
| Document | Guarantee              |  |
| Document | Language               |  |
| Document | Purpose                |  |
| Document | DocumentIdentification |  |
| Document | Evidence               |  |
|          |                        |  |

| Document           | CommercialTrade        |          |
|--------------------|------------------------|----------|
| Document           | Presentation           |          |
| Document           | RelatedContract        |          |
| PrivateCertificate |                        | Document |
| PrivateCertificate | CertificateType        |          |
| PrivateCertificate | CertificationIndicator |          |
| PrivateCertificate | CheckingDate           |          |
| PrivateCertificate | CheckingFrequency      |          |
| PrivateCertificate | NextRevisionDate       |          |
| PrivateCertificate | Person                 |          |
| DocumentPartyRole  |                        | Role     |
| DocumentPartyRole  | Document               |          |
|                    |                        |          |

| ValidatingPartyRole  |                                 | DocumentPartyRole |
|----------------------|---------------------------------|-------------------|
| CheckingPartyRole    |                                 | DocumentPartyRole |
| ResponsiblePartyRole |                                 | DocumentPartyRole |
| SecuritiesTax        |                                 | Tax               |
| SecuritiesTax        | TaxableIncomePerShare           |                   |
| SecuritiesTax        | TaxableIncomePerShareCalculated |                   |
| SecuritiesTax        | EUCapitalGain                   |                   |

| SecuritiesTax<br>EUDividendStatus<br>SecuritiesTax<br>TaxableIncomePerDividend<br>SecuritiesTax<br>StampDutyType<br>SecuritiesTax<br>StampDutyTaxBasis<br>SecuritiesTax<br>TaxVoucher<br>SecuritiesTax<br>TaxableIncomePerDividendShare<br>SecuritiesTax<br>RelatedTax |  |  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                        |  |  |
|                                                                                                                                                                                                                                                                        |  |  |

| SecuritiesTax     | TaxLotNumber           |               |
|-------------------|------------------------|---------------|
| SecuritiesTax     | Security               |               |
| SecuritiesTax     | TaxRuleExemptIndicator |               |
| SecuritiesTax     | EffectivePeriod        |               |
| SecuritiesTax     | FrankedRate            |               |
| SecuritiesTax     | TEFRARule              |               |
| SecuritiesTax     | Jurisdiction           |               |
| InvestmentFundTax |                        | SecuritiesTax |
| InvestmentFundTax | FiscalExemption        |               |
| InvestmentFundTax | InvestmentAccount      |               |
|                   |                        |               |

| InvestmentFundTax | PercentageOfDebtClaim       |                            |
|-------------------|-----------------------------|----------------------------|
| InvestmentFundTax | PercentageGrandfatheredDebt |                            |
| InvestmentFundTax | ExemptionIndicator          |                            |
| InvestmentFundTax | Transaction                 |                            |
| TrusteeRole       |                             | InvestmentAccountPartyRole |
| CustodianForMinor |                             | InvestmentAccountPartyRole |
| Nominee           |                             | InvestmentAccountPartyRole |

| JointOwner        |         | InvestmentAccountPartyRole |
|-------------------|---------|----------------------------|
| SecondaryOwner    |         | InvestmentAccountPartyRole |
| MandatePartyRole  |         | Role                       |
| MandatePartyRole  | Mandate |                            |
| MandateHolder     |         | MandatePartyRole           |
| LegalGuardianRole |         | InvestmentAccountPartyRole |
| SuccessorOnDeath  |         | InvestmentAccountPartyRole |
| AdministratorRole |         | InvestmentAccountPartyRole |
|                   |         |                            |

| IntermediaryRole |                   | AccountPartyRole |
|------------------|-------------------|------------------|
| Adjustment       |                   |                  |
| Adjustment       | Amount            |                  |
| Adjustment       | ChargeRate        |                  |
| Adjustment       | CalculationMethod |                  |
| Adjustment       | Payment           |                  |
| Adjustment       | Direction         |                  |
| Adjustment       | Reason            |                  |
| Adjustment       | RelatedLineItem   |                  |

| Adjustment | AllowanceChargeIndicator |  |
|------------|--------------------------|--|
| Adjustment | Price                    |  |
| Adjustment | ChargeIndicator          |  |
| Adjustment | Type                     |  |
| Adjustment | CollateralManagement     |  |
| Adjustment | AdjustedBalance          |  |
| Adjustment | ChargesPartyRole         |  |
| Adjustment | EffectivePeriod          |  |
| Adjustment | CurrencyExchange         |  |
| Adjustment | SecuritiesOrder          |  |
|            |                          |  |

| Adjustment | Tax                          |            |
|------------|------------------------------|------------|
| Commission |                              | Adjustment |
| Commission | CommissionWaiving            |            |
| Commission | Trade                        |            |
| Commission | CommissionType               |            |
| Commission | Basis                        |            |
| Commission | CommercialAgreementReference |            |
| Commission | CalculationDate              |            |
| Commission | Rate                         |            |
| Commission | CommissionAmount             |            |

| Commission       | Broker                        |  |
|------------------|-------------------------------|--|
| Commission       | CommissionPartyRole           |  |
| Commission       | Account                       |  |
| Commission       | RelatedQuote                  |  |
| Commission       | SplitRate                     |  |
| Commission       | Currency                      |  |
| Commission       | CorporateActionFeesAndCharges |  |
| CommissionWaiver |                               |  |
| CommissionWaiver | Commission                    |  |
| CommissionWaiver | InstructionBasis              |  |
| CommissionWaiver | WaivedRate                    |  |
| CommissionWaiver | NonWaivedRate                 |  |
|                  |                               |  |

| InvestmentPlan |                |  |
|----------------|----------------|--|
| InvestmentPlan | Frequency      |  |
| InvestmentPlan | Amount         |  |
| InvestmentPlan | Asset          |  |
| InvestmentPlan | Instalment     |  |
| InvestmentPlan | RelatedService |  |
| InvestmentPlan | Insurance      |  |
| InvestmentPlan | StandingOrder  |  |
| InvestmentPlan | MultiCurrency  |  |
| InvestmentPlan | Currency       |  |

| InvestmentPlan      | Portfolio            |                 |
|---------------------|----------------------|-----------------|
| InvestmentPlan      | InvestmentPeriod     |                 |
| InvestmentPlan      | PlanStatus           |                 |
| InvestmentPlan      | Pension              |                 |
| InvestmentPlan      | TaxEfficientProduct  |                 |
| InvestmentFundOrder |                      | SecuritiesOrder |
| InvestmentFundOrder | GrossAmountIndicator |                 |
| InvestmentFundOrder | RelatedTransaction   |                 |
| InvestmentFundOrder | OrderType            |                 |
|                     |                      |                 |

| InvestmentFundOrder | GrossAmount                  |  |
|---------------------|------------------------------|--|
| InvestmentFundOrder | UnitsNumber                  |  |
| InvestmentFundOrder | InvestmentFundOrderExecution |  |
| InvestmentFundOrder | NetAmount                    |  |
| InvestmentFundOrder | OrderDateTime                |  |
| InvestmentFundOrder | ExpiryDateTime               |  |
| InvestmentFundOrder | CancellationRight            |  |
| InvestmentFundOrder | RequestedSettlementCurrency  |  |
| InvestmentFundOrder | RequestedExecutionDateTime   |  |
| InvestmentFundOrder | FinancialAdvice              |  |
|                     |                              |  |

| InvestmentFundOrder | NegotiatedTrade       |  |
|---------------------|-----------------------|--|
| InvestmentFundOrder | HoldingsRate          |  |
| InvestmentFundOrder | OrderWaiverReason     |  |
| InvestmentFundOrder | InitialOrderIndicator |  |
| InvestmentFundOrder | OrderBookingDate      |  |
| InvestmentFundOrder | InvestmentPlan        |  |
| InvestmentFundOrder | OrderStatus           |  |
| InvestmentFundOrder | TotalAmount           |  |
| Obligation          |                       |  |

| Obligation<br>RequestedSettlementDate   |  |
|-----------------------------------------|--|
| Obligation<br>RequestedSettlementAmount |  |
| Obligation<br>Priority                  |  |
| Obligation<br>Trade                     |  |
| Obligation<br>TransactionRisk           |  |
| Obligation<br>ParentObligation          |  |
| Obligation<br>SubObligation             |  |

| Obligation        | Offset                    |            |
|-------------------|---------------------------|------------|
| Obligation        | OriginalObligationProcess |            |
| Obligation        | ExposureType              |            |
| PaymentObligation |                           | Obligation |
| PaymentObligation | PaymentOffset             |            |
| PaymentObligation | Purpose                   |            |
| PaymentObligation | RemittanceDeliveryMethod  |            |
| PaymentObligation | AssociatedDocument        |            |
| PaymentObligation | Amount                    |            |

| PaymentObligation | RemittanceLocation        |  |
|-------------------|---------------------------|--|
| PaymentObligation | Interest                  |  |
| PaymentObligation | CommercialTrade           |  |
| PaymentObligation | Percentage                |  |
| PaymentObligation | MaximumAmount             |  |
| PaymentObligation | ExpiryDate                |  |
| PaymentObligation | ApplicableLaw             |  |
| PaymentObligation | PaymentSourceBuyIn        |  |
| PaymentObligation | RelatedCorporateAction    |  |
| PaymentObligation | RelatedCollateralMovement |  |
|                   |                           |  |

| PaymentObligation | PaymentSourceUndertakingDemand |  |
|-------------------|--------------------------------|--|
| PaymentObligation | PartyRole                      |  |
| PaymentObligation | ExecutedSecuritiesTrade        |  |
| PaymentObligation | RelatedAccountClosingTerms     |  |
| PaymentObligation | PaymentSourcePortfolioTransfer |  |
| PaymentObligation | PaymentSourceCurrencyOption    |  |
| PaymentObligation | ExchangeRateInformation        |  |
| PaymentObligation | Dividend                       |  |
| PaymentObligation | RepurchaseAgreement            |  |
| PaymentObligation | RelatedAssignment              |  |
|                   |                                |  |

| PaymentObligation | BankingTransaction        |                   |
|-------------------|---------------------------|-------------------|
| PaymentObligation | PaymentTerms              |                   |
| PaymentObligation | PaymentDueDate            |                   |
| Instalment        |                           | PaymentObligation |
| Instalment        | InitialNumberOfInstalment |                   |
| Instalment        | TotalNumberOfInstalment   |                   |
| Instalment        | PeriodUnit                |                   |
| Instalment        | NumberOfUnits             |                   |
| Instalment        | SequenceIdentification    |                   |
| Instalment        | InvestmentPlan            |                   |
| Instalment        | InstalmentPlanType        |                   |

| Instalment           | FirstPaymentAmount  |                      |
|----------------------|---------------------|----------------------|
| Instalment           | FirstPaymentDate    |                      |
| ObligationFulfilment |                     |                      |
| ObligationFulfilment | Date                |                      |
| ObligationFulfilment | ObligationOffset    |                      |
| ObligationFulfilment | ResultingObligation |                      |
| Payment              |                     | ObligationFulfilment |
| Payment              | PaymentObligation   |                      |
| Payment              | CurrencyOfTransfer  |                      |
| Payment              | CreditMethod        |                      |
| Payment              | Type                |                      |
|                      |                     |                      |

| Payment | InstructedAmount      | Amount of money to be moved<br>between the debtor and creditor,<br>before deduction of charges,<br>CurrencyAndAmount<br>expressed in the currency as<br>ordered by the initiating party.                                                    |
|---------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Payment | Priority              | Urgency or order of importance<br>that the originator would like the<br>PriorityCode<br>recipient of the payment to apply<br>to its processing.                                                                                             |
| Payment | ValueDate             | Date on which a payment must<br>ISODate<br>be executed                                                                                                                                                                                      |
| Payment | PaymentStatus         | Specifies the status of a payment<br>PaymentStatus<br>at a specified time.                                                                                                                                                                  |
| Payment | PartyRole             | Specifies each role linked to a<br>payment and played by a party<br>PaymentPartyRole<br>Payment<br>at that step in a payment flow.                                                                                                          |
| Payment | TaxOnPayment          | Payment levy tax.<br>Tax<br>RelatedPaymentSettlement                                                                                                                                                                                        |
| Payment | PaymentExecution      | Describes the processes<br>PaymentExecution<br>Payment<br>necessary to execute a payment.                                                                                                                                                   |
| Payment | PoolingAdjustmentDate | Date used for the correction of<br>the value date of a cash pool<br>ISODate<br>movement that has been posted<br>with a different value date.                                                                                                |
| Payment | EquivalentAmount      | Amount of money to be<br>transferred between debtor and<br>creditor, before deduction of<br>charges, expressed in the<br>ImpliedCurrencyAndAmount<br>currency of the debtor's account,<br>and to be transferred in a<br>different currency. |

| Payment | CurrencyExchange              |  |
|---------|-------------------------------|--|
| Payment | InstructionForCreditorAgent   |  |
| Payment | InstructionForDebtorAgent     |  |
| Payment | PaymentRelatedIdentifications |  |
| Payment | RelatedInvestigationCase      |  |
| Payment | SettlementTimeRequest         |  |
| Payment | Amount                        |  |

| Payment | TradeSettlement                    |  |
|---------|------------------------------------|--|
| Payment | StandardSettlementInstructions     |  |
| Payment | RelatedDebitAuthorisation          |  |
| Payment | RelatedInvestigationCaseResolution |  |
| Payment | OriginalPayment                    |  |
| Payment | ReturnPayment                      |  |
| Payment | RelatedSecuritiesSettlement        |  |
| Payment | InvoiceReconciliation              |  |
| Payment | PaymentInstrument                  |  |
| Payment | Account                            |  |
| Payment | Adjustments                        |  |
| Payment | ContractRegistration               |  |

| IndividualPayment |                      | Payment           |
|-------------------|----------------------|-------------------|
| IndividualPayment | BulkPayment          |                   |
| ChequePayment     |                      | IndividualPayment |
| ChequePayment     | Cheque               |                   |
| CardPayment       |                      | IndividualPayment |
| CardPayment       | PaymentCard          |                   |
| CardPayment       | Product              |                   |
| CardPayment       | DetailedAmount       |                   |
| CardPayment       | AmountQualifier      |                   |
| CardPayment       | CardPaymentAcquiring |                   |
| CardPayment       | PaymentCardPartyRole |                   |
| CardPayment       | CardPaymentStatus    |                   |
| CardPayment       | DetailedAmountLabel  |                   |
|                   |                      |                   |

| CardPayment | Reconciliation       |  |
|-------------|----------------------|--|
| CardPayment | TransactionCategory  |  |
| CardPayment | CashBackAmount       |  |
| CardPayment | Gratuity             |  |
| CardPayment | DebitCreditDirection |  |
| CardPayment | ATMTotal             |  |
| PaymentCard |                      |  |
| PaymentCard | Payment              |  |
| PaymentCard | Type                 |  |
| PaymentCard | Number               |  |
| PaymentCard | StartDate            |  |
| PaymentCard | ExpiryDate           |  |

| PaymentCard | SecurityCode           |  |
|-------------|------------------------|--|
| PaymentCard | SequenceNumber         |  |
| PaymentCard | ServiceCode            |  |
| PaymentCard | TrackValue             |  |
| PaymentCard | SecurityCodeManagement |  |
| PaymentCard | CardBrand              |  |
| PaymentCard | RelatedAccount         |  |
| PaymentCard | ProfileNumber          |  |
| PaymentCard | RelatedAccountType     |  |
| PaymentCard | CreditAvailableAmount  |  |
| PaymentCard | Limit                  |  |
| PaymentCard | CardCurrencyCode       |  |
| PaymentCard | Interest               |  |
| PaymentCard | CardCountryCode        |  |
|             |                        |  |

| PaymentCard          | CardProgramme              |                      |
|----------------------|----------------------------|----------------------|
| CardPaymentPartyRole |                            | Role                 |
| CardPaymentPartyRole | CardPayment                |                      |
| CardPaymentPartyRole | PartyType                  |                      |
| CardholderRole       |                            | CardPaymentPartyRole |
| CardholderRole       | Authentication             |                      |
| DirectDebit          |                            | IndividualPayment    |
| DirectDebit          | RegistrationIdentification |                      |
| DirectDebit          | DirectDebitMandate         |                      |
|                      |                            |                      |

| DirectDebit              | PreNotificationIdentification |  |
|--------------------------|-------------------------------|--|
| DirectDebit              | PreNotificationDate           |  |
| CashClearingSystemMember |                               |  |
| CashClearingSystemMember | OrganisationIdentification    |  |

| CashClearingSystemMember | CHIPSUniversalIdentification |  |
|--------------------------|------------------------------|--|
| CashClearingSystemMember | NewZealandNCC                |  |
| CashClearingSystemMember | IrishNSC                     |  |
| CashClearingSystemMember | UKSortCode                   |  |

| CashClearingSystemMember | CHIPSParticipantIdentification       |  |
|--------------------------|--------------------------------------|--|
| CashClearingSystemMember | SwissBC                              |  |
| CashClearingSystemMember | FedwireRoutingNumber                 |  |
| CashClearingSystemMember | PortugueseNCC                        |  |
| CashClearingSystemMember | RussianCentralBankIdentificationCode |  |
| CashClearingSystemMember | ItalianDomesticIdentificationCode    |  |

| CashClearingSystemMember | AustrianBankleitzahl                     |  |
|--------------------------|------------------------------------------|--|
| CashClearingSystemMember | CanadianPaymentsAssociationRoutingNumber |  |
| CashClearingSystemMember | SwissSIC                                 |  |
| CashClearingSystemMember | GermanBankleitzahl                       |  |
| CashClearingSystemMember | SpanishDomesticInterbankingCode          |  |
| CashClearingSystemMember | SouthAfricanNCC                          |  |

| CashClearingSystemMember    | HongKongBankCode               |  |
|-----------------------------|--------------------------------|--|
| CashClearingSystemMember    | ClearingMember                 |  |
| CashClearingSystemMember    | IndianFinancialSystemCode      |  |
| CashClearingSystemMember    | HellenicBankIdentificationCode |  |
| CashClearingSystemMember    | PolishNationalClearingCode     |  |
| CashClearingSystemMember    | AustralianBSBCode              |  |
| AustralianBSBIdentification |                                |  |

| AustralianBSBIdentification | ExtensiveBranchNetworkIdentification   |  |
|-----------------------------|----------------------------------------|--|
| AustralianBSBIdentification | SmallNetworkIdentification             |  |
| AustralianBSBIdentification | ClearingSystemMemberIdentificationType |  |
| AustralianBSBIdentification | ClearingSystemMember                   |  |
| Entry                       |                                        |  |
| Entry                       | CreditDebitIndicator                   |  |
| Entry                       | EntryDate                              |  |
| Entry                       | Identification                         |  |

| Entry | AccountOwnerTransactionIdentification    |  |
|-------|------------------------------------------|--|
| Entry | AccountServicerTransactionIdentification |  |
| Entry | ReversalIndicator                        |  |
| Entry | ValueDate                                |  |
| Entry | BankTransactionCode                      |  |
| Entry | CommissionWaiverIndicator                |  |
| Entry | Role                                     |  |
| Entry | Account                                  |  |
| Entry | Balance                                  |  |
| Entry | EntryType                                |  |
|       |                                          |  |

| CashEntry |                  | Entry |
|-----------|------------------|-------|
| CashEntry | CashAccount      |       |
| CashEntry | Amount           |       |
| CashEntry | RelatedBookEntry |       |
| CashEntry | CashBalance      |       |
| CashEntry | CurrencyExchange |       |
| CashEntry | Charges          |       |
| CashEntry | Availability     |       |
| CashEntry | Interest         |       |

| CashEntry        | DebitRelatedBookEntry              |  |
|------------------|------------------------------------|--|
| CashEntry        | CreditRelatedBookEntry             |  |
| CashEntry        | RelatedInvoiceFinancingTransaction |  |
| CashEntry        | RelatedInvestigationCase           |  |
| CashEntry        | RelatedInvestigationCaseResolution |  |
| CashEntry        | ChargesIncluded                    |  |
| CreditInstrument |                                    |  |
| CreditInstrument | RelatedPayment                     |  |
| CreditInstrument | Method                             |  |
| CreditInstrument | CreditInstrumentIdentification     |  |
| CreditInstrument | NetAmount                          |  |
| CreditInstrument | Deadline                           |  |
|                  |                                    |  |

| ChequeIssue         |                       | CreditInstrument |
|---------------------|-----------------------|------------------|
| ChequeIssue         | Cheque                |                  |
| ChequeIssue         | DeliveryMethod        |                  |
| ChequeIssue         | DeliverTo             |                  |
| ChequeIssue         | PrintLocation         |                  |
| TradeIdentification |                       |                  |
| TradeIdentification | CounterpartyReference |                  |
| TradeIdentification | Identification        |                  |
| TradeIdentification | CommonIdentification  |                  |
| TradeIdentification | MatchingReference     |                  |
|                     |                       |                  |

| TradeIdentification<br>Trade<br>TradeIdentification<br>UniqueTradeIdentifier   |
|--------------------------------------------------------------------------------|
|                                                                                |
|                                                                                |
| TradeIdentification<br>ClearingBrokerIdentification                            |
| TradeIdentification<br>RelatedPostTradeRiskReduction                           |
| TradeIdentification<br>RelatedEventIdentifier                                  |
| SecuritiesTradeIdentification<br>TradeIdentification                           |
| SecuritiesTradeIdentification<br>IdentifiedTrade                               |
| SecuritiesTradeIdentification<br>MarketInfrastructureTransactionIdentification |

| SecuritiesTradeIdentification<br>ProcessorTransactionIdentification                |
|------------------------------------------------------------------------------------|
| SecuritiesTradeIdentification<br>PoolIdentification                                |
| SecuritiesTradeIdentification<br>CollateralTransactionIdentification               |
| SecuritiesTradeIdentification<br>ClientTripartyCollateralTransactionIdentification |
| SecuritiesTradeIdentification<br>TripartyAgentCollateralTransactionIdentification  |
| SecuritiesTradeIdentification<br>BasketIdentification                              |
| SecuritiesTradeIdentification<br>ProgramIdentification                             |
| SecuritiesTradeIdentification<br>BlockIdentification                               |
| SecuritiesTradeIdentification<br>AllocationIdentification                          |
| SecuritiesTradeIdentification<br>ComplianceIdentification                          |

| SecuritiesTradeIdentification | CSDTransactionIdentification                              |                         |
|-------------------------------|-----------------------------------------------------------|-------------------------|
| SecuritiesTradeIdentification | CentralCounterpartyTransactionIdentification              |                         |
| SecuritiesTradeIdentification | CancellationRequestIdentification                         |                         |
| SecuritiesTradeIdentification | CounterpartyMarketInfrastructureTransactionIdentification |                         |
| InvestmentFundPartyRole       |                                                           | Role                    |
| InvestmentFundPartyRole       | Account                                                   |                         |
| InvestmentFundPartyRole       | InvestmentFund                                            |                         |
| Grantor                       |                                                           | InvestmentFundPartyRole |
| Settlor                       |                                                           | InvestmentFundPartyRole |
|                               |                                                           |                         |

| TradePartyRole |                      | Role           |
|----------------|----------------------|----------------|
| TradePartyRole | Account              |                |
| TradePartyRole | TradingPartyCapacity |                |
| TradePartyRole | BuyerOrSeller        |                |
| TradePartyRole | Trade                |                |
| InvestorRole   |                      | TradePartyRole |
| InvestorRole   | IndividualInvestor   |                |
| InvestorRole   | CorporateInvestor    |                |
| InvestorRole   | Capacity             |                |
|                |                      |                |

| InvestorRole        | InvestorProtectionAssociationMembership |                  |
|---------------------|-----------------------------------------|------------------|
| InvestorRole        | Type                                    |                  |
| AccountServicerRole |                                         | AccountPartyRole |
| AccountServicerRole | RelatedPTRR                             |                  |
| SecuritiesQuantity  |                                         |                  |
| SecuritiesQuantity  | Unit                                    |                  |
| SecuritiesQuantity  | SecuritiesTransfer                      |                  |
| SecuritiesQuantity  | SecurityIdentification                  |                  |
| SecuritiesQuantity  | Order                                   |                  |
| SecuritiesQuantity  | Group1Or2Units                          |                  |
| SecuritiesQuantity  | RelatedOrderExecution                   |                  |

| SecuritiesQuantity | SecuritiesSettlement                                   |  |
|--------------------|--------------------------------------------------------|--|
| SecuritiesQuantity | MinimumQuantityDebt                                    |  |
| SecuritiesQuantity | LotBreakdown                                           |  |
| SecuritiesQuantity | MinimumExercisableQuantitySecuritiesConversion         |  |
| SecuritiesQuantity | MinimumExercisableMultipleQuantitySecuritiesConversion |  |
| SecuritiesQuantity | AggregateQuantityBalance                               |  |
| SecuritiesQuantity | SecuritiesProceedsDefinition                           |  |
| SecuritiesQuantity | ConditionalQuantitySecuritiesProceeds                  |  |
| SecuritiesQuantity | OverAndAboveQuantitySecuritiesProceeds                 |  |
| SecuritiesQuantity | Entry                                                  |  |
| SecuritiesQuantity | Code                                                   |  |
|                    |                                                        |  |

| SecuritiesQuantity | ExpectedQuantitySecuritiesProceeds             |  |
|--------------------|------------------------------------------------|--|
| SecuritiesQuantity | StatusRelatedSecuritiesProceeds                |  |
| SecuritiesQuantity | CorporateActionDistribution                    |  |
| SecuritiesQuantity | RelatedEventForFractionalQuantity              |  |
| SecuritiesQuantity | MaximumExercisableQuantitySecuritiesConversion |  |
| SecuritiesQuantity | BoardLotSecuritiesProceeds                     |  |
| SecuritiesQuantity | NewDenominationSecuritiesProceeds              |  |
| SecuritiesQuantity | BackEndOddLotBiddingConditions                 |  |
| SecuritiesQuantity | SecuritiesEntitlement                          |  |
| SecuritiesQuantity | CorporateActionEvent                           |  |
| SecuritiesQuantity | BiddingConditions                              |  |

| SecuritiesQuantity<br>Lottery<br>SecuritiesQuantity<br>RelatedSubBalance<br>SecuritiesQuantity<br>AvailableQuantityBalance<br>SecuritiesQuantity<br>Trade<br>SecuritiesQuantity<br>RatioDenominatorSecuritiesConversion<br>SecuritiesQuantity<br>RatioNumeratorSecuritiesConversion<br>SecuritiesQuantity<br>MinimumTradedQuantityMarket<br>SecuritiesQuantity<br>MinimumDenominationDebt<br>SecuritiesQuantity<br>MinimumIncrementDebt<br>SecuritiesQuantity<br>RelatedOrder<br>SecuritiesQuantity<br>Allocation |  |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |

| SecuritiesQuantity | Amount                      |  |
|--------------------|-----------------------------|--|
| SecuritiesQuantity | DenominatorRatio            |  |
| SecuritiesQuantity | NumeratorRatio              |  |
| SecuritiesQuantity | SecuritiesTradeExecution    |  |
| SecuritiesQuantity | RelatedCorporateActionEvent |  |
| SecuritiesQuantity | CorporateActionElection     |  |
| SecuritiesQuantity | TaxVoucher                  |  |
| SecuritiesQuantity | RelatedBuyIn                |  |
| SecuritiesQuantity | PreviousDayOrder            |  |
| SecuritiesQuantity | Liquidity                   |  |

| SecuritiesQuantity<br>Rate<br>SecuritiesQuantity<br>MinimumQuantityOrderParameters<br>SecuritiesQuantity<br>MaximumQuantityRelatedQuote<br>SecuritiesQuantity<br>UnavailableQuantityBalance<br>SecuritiesQuantity<br>MatchIncrementOrderParameters<br>SecuritiesQuantity<br>RelatedIssuance<br>SecuritiesQuantity<br>Pairoff<br>SecuritiesQuantity<br>Issuance<br>SecuritiesQuantity<br>IntermediateToUnderlyingDenominatorDistributionInformation |  |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |

| SecuritiesQuantity | MaximumHoldingDistributionInformation                     |  |
|--------------------|-----------------------------------------------------------|--|
| SecuritiesQuantity | MaximumExercisableQuantityDistributionInformation         |  |
| SecuritiesQuantity | MinimumExercisableQuantityDistributionInformation         |  |
| SecuritiesQuantity | DistributedToUnderlyingDenominatorDistributionInformation |  |
| SecuritiesQuantity | IntermediateToUnderlyingNumeratorDistributionInformation  |  |
| SecuritiesQuantity | MinimumHoldingDistributionInformation                     |  |
| SecuritiesQuantity | DistributedToUnderlyingNumeratorDistributionInformation   |  |
| SecuritiesQuantity | MaximumHoldingRelatedSecuritiesDistribution               |  |

| SecuritiesQuantity | IntermediateToUnderlyingNumeratorRelatedSecuritiesDistribution   |  |
|--------------------|------------------------------------------------------------------|--|
| SecuritiesQuantity | IntermediateToUnderlyingDenominatorRelatedSecuritiesDistribution |  |
| SecuritiesQuantity | DistributedToUnderlyingDenominatorRelatedSecuritiesDistribution  |  |
| SecuritiesQuantity | DistributedToUnderlyingNumeratorRelatedSecuritiesDistribution    |  |
| SecuritiesQuantity | MinimumHoldingRelatedSecuritiesDistribution                      |  |
| SecuritiesQuantity | MaximumTradedQuantityMarket                                      |  |
| SecuritiesQuantity | QuantityRelatedQuote                                             |  |
| SecuritiesQuantity | MinimumQuantityRelatedQuote                                      |  |
| SecuritiesQuantity | NetAssetValueCalculation                                         |  |
| SecuritiesQuantity | SidePocket                                                       |  |
|                    |                                                                  |  |

| SecuritiesQuantity<br>Netting<br>SecuritiesQuantity<br>RelatedOrderStatus<br>SecuritiesQuantity<br>SecuritiesOrderStatus<br>SecuritiesQuantity<br>RelatedTurnaroundSettlement<br>SecuritiesQuantity<br>RelatedCashFlow<br>SecuritiesQuantity<br>Position<br>SecuritiesQuantity<br>MaximumQuantityBiddingConditions<br>SecuritiesQuantity<br>FrontEndOddLotBiddingConditions<br>SecuritiesQuantity<br>MinimumQuantityBiddingConditions<br>SecuritiesQuantity<br>RelatedCorporateActionProtectProcess<br>SecuritiesQuantity<br>DigitalTokenUnit |  |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |

| SecuritiesTrade |                                       | Trade |
|-----------------|---------------------------------------|-------|
| SecuritiesTrade | SecuritiesTradeRelatedIdentifications |       |
| SecuritiesTrade | TradeAmount                           |       |
| SecuritiesTrade | OpeningClosingIndicator               |       |
| SecuritiesTrade | TradeTransactionCondition             |       |
| SecuritiesTrade | SecuritiesTradeStatus                 |       |
| SecuritiesTrade | Activity                              |       |
| SecuritiesTrade | TradeQuantity                         |       |

| SecuritiesTrade | TradeOriginationDate           |  |
|-----------------|--------------------------------|--|
| SecuritiesTrade | ClearingFeeType                |  |
| SecuritiesTrade | Security                       |  |
| SecuritiesTrade | TradePrice                     |  |
| SecuritiesTrade | PartyRole                      |  |
| SecuritiesTrade | SecuritiesFinancingClosingData |  |
| SecuritiesTrade | TradingExecution               |  |
| SecuritiesTrade | TradeAllocation                |  |
| SecuritiesTrade | RelatedOrder                   |  |
| SecuritiesTrade | SecuritiesFinancingOpeningData |  |
| SecuritiesTrade | TransactionType                |  |

| SecuritiesTrade           | LegalFramework            |                 |
|---------------------------|---------------------------|-----------------|
| SecuritiesTrade           | SecuritiesTransactionType |                 |
| InvestmentFundTransaction |                           | SecuritiesTrade |
| InvestmentFundTransaction | InvestmentFundOrder       |                 |
| InvestmentFundTransaction | ClientReference           |                 |
| InvestmentFundTransaction | Type                      |                 |
| InvestmentFundTransaction | TransactionCharge         |                 |
| InvestmentFundTransaction | InvestmentAccount         |                 |
| InvestmentFundTransaction | InvestmentFundClass       |                 |
| InvestmentFundTransaction | TransactionTax            |                 |
| InvestmentFundTransaction | CreditDebitIndicator      |                 |
|                           |                           |                 |

| Status<br>Reason<br>NoSpecifiedReason<br>DataSourceScheme<br>RejectedStatusReason<br>FailingReason<br>CancellationReason<br>PendingReason<br>RejectionReason<br>AcknowledgedAcceptedReason | InvestmentFundTransaction | InvestmentFundOrderExecution |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------|--|
|                                                                                                                                                                                            | StatusReason              |                              |  |
|                                                                                                                                                                                            | StatusReason              |                              |  |
|                                                                                                                                                                                            | StatusReason              |                              |  |
|                                                                                                                                                                                            | StatusReason              |                              |  |
|                                                                                                                                                                                            | StatusReason              |                              |  |
|                                                                                                                                                                                            | StatusReason              |                              |  |
|                                                                                                                                                                                            | StatusReason              |                              |  |
|                                                                                                                                                                                            | StatusReason              |                              |  |
|                                                                                                                                                                                            | StatusReason              |                              |  |
|                                                                                                                                                                                            | StatusReason              |                              |  |
|                                                                                                                                                                                            | StatusReason              |                              |  |

| StatusReason | RelatedClosureReason |                   |
|--------------|----------------------|-------------------|
| Cheque       |                      | FinancialDocument |
| Cheque       | ChequeDelivery       |                   |
| Cheque       | Number               |                   |
| Cheque       | ChequeType           |                   |
| Cheque       | MaturityDate         |                   |
| Cheque       | FormsCode            |                   |
| Cheque       | MemoField            |                   |
| Cheque       | RegionalClearingZone |                   |

| Cheque               | RelatedPayment      |          |
|----------------------|---------------------|----------|
| Cheque               | ChequePartyRole     |          |
| Cheque               | CashAccount         |          |
| InsuranceCertificate |                     | Document |
| InsuranceCertificate | EffectiveDate       |          |
| InsuranceCertificate | InsuredAmount       |          |
| InsuranceCertificate | InsuranceConditions |          |
| InsuranceCertificate | InsuranceClauses    |          |
| InsuranceCertificate | ClaimsPayableAt     |          |
| InsuranceCertificate | ClaimsPayableIn     |          |
| InsuranceCertificate | InsurancePartyRole  |          |

| InsuranceCertificate | ProductDelivery             |                      |
|----------------------|-----------------------------|----------------------|
| InsuranceCertificate | InsuranceType               |                      |
| InsuranceCertificate | RelatedInvestmentPlan       |                      |
| SecuritiesTransfer   |                             | ObligationFulfilment |
| SecuritiesTransfer   | Identification              |                      |
| SecuritiesTransfer   | TransferredQuantity         |                      |
| SecuritiesTransfer   | Account                     |                      |
| SecuritiesTransfer   | TransferType                |                      |
| SecuritiesTransfer   | RelatedSettlement           |                      |
| SecuritiesTransfer   | OwnAccountTransferIndicator |                      |
| SecuritiesTransfer   | PhysicalDelivery            |                      |

| SecuritiesTransfer | LateDeliveryDate             |  |
|--------------------|------------------------------|--|
| SecuritiesTransfer | TransferTax                  |  |
| SecuritiesTransfer | TransferReason               |  |
| SecuritiesTransfer | PartialSettlementType        |  |
| SecuritiesTransfer | SecuritiesDeliveryObligation |  |
| SecuritiesTransfer | BookEntry                    |  |
| SecuritiesTransfer | TransactionIdentification    |  |
| SecuritiesTransfer | Security                     |  |
| SecuritiesTransfer | Status                       |  |
| PortfolioTransfer  |                              |  |

| PortfolioTransfer | TransferredYear              |  |
|-------------------|------------------------------|--|
| PortfolioTransfer | CashComponentIndicator       |  |
| PortfolioTransfer | AccountFrom                  |  |
| PortfolioTransfer | AccountTo                    |  |
| PortfolioTransfer | PaymentObligation            |  |
| PortfolioTransfer | TransferredPortfolio         |  |
| PortfolioTransfer | SecuritiesDeliveryObligation |  |
| PortfolioTransfer | TransferredAmount            |  |
| PortfolioTransfer | TransferredPercentage        |  |
| PortfolioTransfer | TransferDate                 |  |
|                   |                              |  |

| PortfolioTransfer            | NomineeAccount                   |
|------------------------------|----------------------------------|
| PortfolioTransfer            | PEPOrISAPlan                     |
| PortfolioTransfer            | CurrentYearISAType               |
| InvestmentFundOrderExecution | SecuritiesTradeExecution         |
| InvestmentFundOrderExecution | UnitsNumber                      |
| InvestmentFundOrderExecution | NonStandardSettlementInformation |
| InvestmentFundOrderExecution | Order                            |
| InvestmentFundOrderExecution | DealIdentification               |
| InvestmentFundOrderExecution | ExecutedTradePrice               |
| InvestmentFundOrderExecution | PartiallyExecutedIndicator       |

| InvestmentFundOrderExecution | InterimProfitAmount       | Part of the price deemed as<br>accrued income or profit rather<br>than capital. The interim profit<br>amount is used for tax purposes. | CurrencyAndAmount         |                                    |
|------------------------------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------|
| InvestmentFundOrderExecution | InformativePrice          | Other quoted price than the one<br>at which the order was executed.                                                                    | SecuritiesPricing         | FundOrderRelatedToInformativePrice |
| InvestmentFundOrderExecution | BestExecution             | Specifies that the execution was<br>subject to best execution rules as<br>defined by MiFID.                                            | BestExecutionCode         |                                    |
| InvestmentFundOrderExecution | PartialSettlementOfUnits  | Percentage of units partially<br>settled.                                                                                              | PercentageRate            |                                    |
| InvestmentFundOrderExecution | PartialSettlementOfCash   | Percentage of cash partially<br>settled.                                                                                               | PercentageRate            |                                    |
| InvestmentFundOrderExecution | LateReport                | Specifies whether the order<br>execution confirmation is late.                                                                         | LateReportCode            |                                    |
| InvestmentFundOrderExecution | SettledIndicator          | Indicates whether the cash<br>payment with respect to the<br>executed order is settled.                                                | YesNoIndicator            |                                    |
| InvestmentFundOrderExecution | RegisteredIndicator       | Indicates whether the executed<br>order has a registered status on<br>the books of the transfer agent.                                 | YesNoIndicator            |                                    |
| InvestmentFundOrderExecution | ExecutedAmount            | Amount of money invested or<br>redeemed as a result of an<br>investment fund order.                                                    | CurrencyAndAmount         |                                    |
| InvestmentFundOrderExecution | InvestmentFundTransaction | Transaction which is executed.                                                                                                         | InvestmentFundTransaction | InvestmentFundOrderExecution       |
| InvestmentFundOrderExecution | CashFlow                  | Specifies the cash flow resulting<br>from the execution of an order.                                                                   | FundsCashFlow             | RelatedOrder                       |
| InvestmentFundOrderExecution | SourceOfCash              | Source of cash used for the<br>settlement of the execution.                                                                            | SourceOfCashCode          |                                    |
|                              |                           |                                                                                                                                        |                           |                                    |

| SubscriptionExecution |                      | InvestmentFundOrderExecution |
|-----------------------|----------------------|------------------------------|
| SubscriptionExecution | EquityComponent      |                              |
| SubscriptionExecution | CashComponent        |                              |
| SubscriptionExecution | InvestedNetAmount    |                              |
| SubscriptionExecution | Refund               |                              |
| SubscriptionExecution | SubscriptionInterest |                              |
| SubscriptionExecution | TaxEfficientProduct  |                              |
| Portfolio             |                      |                              |
| Portfolio             | Valuation            |                              |
| Portfolio             | Transfer             |                              |
| Portfolio             | AssetDescription     |                              |
| Portfolio             | Name                 |                              |
|                       |                      |                              |

| Portfolio    | Identification     |  |
|--------------|--------------------|--|
| Portfolio    | Strategy           |  |
| Portfolio    | Benchmark          |  |
| Portfolio    | InvestmentPlan     |  |
| Portfolio    | Account            |  |
| AssetHolding |                    |  |
| AssetHolding | HoldingValue       |  |
| AssetHolding | BookValue          |  |
| AssetHolding | FaceAmount         |  |
| AssetHolding | AmortisedFaceValue |  |
| AssetHolding | MarketValue        |  |

| AssetHolding | Balance                 |  |
|--------------|-------------------------|--|
| AssetHolding | UnrealisedGainOrLoss    |  |
| AssetHolding | Asset                   |  |
| AssetHolding | Haircut                 |  |
| AssetHolding | EligibleCollateralValue |  |
| AssetHolding | ExchangeRate            |  |
| AssetHolding | CapValue                |  |
| AssetHolding | RiskAdjustedValue       |  |
| AssetHolding | RealisedGainOrLoss      |  |
|              |                         |  |

| AssetHolding     | UnrealisedType              |  |
|------------------|-----------------------------|--|
| AssetHolding     | PostHaircutValue            |  |
| AssetHolding     | Interest                    |  |
| AssetHolding     | Collateral                  |  |
| AssetHolding     | FinancialAssetType          |  |
| AssetHolding     | VariationMarginCollateral   |  |
| AssetHolding     | IndependentAmountCollateral |  |
| AssetHolding     | HoldingType                 |  |
| AssetHolding     | GuaranteeAmount             |  |
| PaymentExecution |                             |  |
|                  |                             |  |

| PaymentExecution | CreditDebitIndicator               |  |
|------------------|------------------------------------|--|
| PaymentExecution | CreationDate                       |  |
| PaymentExecution | AcceptanceDateTime                 |  |
| PaymentExecution | Payment                            |  |
| PaymentExecution | ProcessingInstructions             |  |
| PaymentExecution | RequestedExecutionDate             |  |
| PaymentExecution | RelatedInvestigationCase           |  |
| PaymentExecution | RelatedInvestigationCaseResolution |  |
|                  |                                    |  |

| PaymentExecution   | Next                    |                  |
|--------------------|-------------------------|------------------|
| PaymentExecution   | CurrencyExchange        |                  |
| PaymentInstruction |                         | PaymentExecution |
| PaymentInstruction | ProcessingValidityTime  |                  |
| PaymentInstruction | InstructionForNextAgent |                  |
| PaymentInstruction | SettlementInstruction   |                  |

| PaymentInstruction | ClearingChargeAmount |            |
|--------------------|----------------------|------------|
| PaymentInstruction | StandingOrder        |            |
| PaymentInstruction | Previous             |            |
| System             |                      | RolePlayer |
| System             | SystemIdentification |            |
| System             | Location             |            |
| System             | Reconciliation       |            |
| System             | Availability         |            |
|                    |                      |            |

| System | Event                      |
|--------|----------------------------|
| System | PartyRole                  |
| System | Status                     |
| System | SystemGeneratedInformation |
| System | VersionValidityPeriod      |
| System | SystemDateTime             |
| System | Negotiation                |
| System | Account                    |
| System | Trade                      |
| System | Assessment                 |
| System | TradesPosition             |

| System               | SystemLanguage              |        |
|----------------------|-----------------------------|--------|
| SystemIdentification |                             |        |
| SystemIdentification | IdentificationForSystem     |        |
| SystemIdentification | Model                       |        |
| SystemIdentification | SerialNumber                |        |
| SystemIdentification | ApprovalNumber              |        |
| SystemIdentification | SystemVersion               |        |
| SystemIdentification | SystemName                  |        |
| SystemIdentification | Identification              |        |
| ClearingSystem       |                             | System |
| ClearingSystem       | Clearing                    |        |
| ClearingSystem       | CentralClearingCounterparty |        |
| ClearingSystem       | DefaultFund                 |        |

| ClearingSystem     | CollateralManagement     |                 |
|--------------------|--------------------------|-----------------|
| CashClearingSystem |                          | ClearingSystem  |
| CashClearingSystem | Identification           |                 |
| CashClearingSystem | TransactionAdministrator |                 |
| CashClearingSystem | SystemRole               |                 |
| CashClearingSystem | Type                     |                 |
| CashClearingSystem | CashSettlementSystem     |                 |
| SystemPartyRole    |                          | Role            |
| SystemPartyRole    | RelatedSystem            |                 |
| SystemMemberRole   |                          | SystemPartyRole |
| SystemMemberRole   | CashBalance              |                 |
| SystemMemberRole   | Type                     |                 |
| SystemMemberRole   | MemberStatus             |                 |
|                    |                          |                 |

| SystemMemberRole   | Limit                              |                 |
|--------------------|------------------------------------|-----------------|
| SystemMemberRole   | Account                            |                 |
| ClearingMemberRole |                                    | SystemPartyRole |
| ClearingMemberRole | ClearingSystemMemberIdentification |                 |
| ClearingMemberRole | Side                               |                 |
| ClearingMemberRole | ClearingAccount                    |                 |

| ClearingMemberRole<br>MarginAccount<br>ClearingMemberRole<br>DeliveryAccount<br>ClearingMemberRole<br>DefaultFundAccount<br>ClearingMemberRole<br>ClearingSegment<br>ClearingMemberRole<br>RelatedClearingMemberRole<br>PaymentIdentification<br>TradeIdentification<br>PaymentIdentification<br>ExecutionIdentification |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                                                                                                                          |  |  |

| PaymentIdentification | EndToEndIdentification    |  |
|-----------------------|---------------------------|--|
| PaymentIdentification | InstructionIdentification |  |
| PaymentIdentification | TransactionIdentification |  |
| PaymentIdentification | ClearingSystemReference   |  |
| PaymentIdentification | CreditorReference         |  |
| PaymentIdentification | Payment                   |  |
| PaymentIdentification | UETR                      |  |

| Settlement     |                                         |            |
|----------------|-----------------------------------------|------------|
| Settlement     | CentralCounterpartyEligibilityIndicator |            |
| Settlement     | StandingSettlementInstruction           |            |
| Settlement     | SettlementPartyRole                     |            |
| Settlement     | Trade                                   |            |
| CashSettlement |                                         | Settlement |
| CashSettlement | InterbankSettlementAmount               |            |
| CashSettlement | InterbankSettlementDate                 |            |
| CashSettlement | RTGS                                    |            |

| CashSettlement | CreditDateTime                  |  |
|----------------|---------------------------------|--|
| CashSettlement | RelatedPaymentInstruction       |  |
| CashSettlement | SettlementMethod                |  |
| CashSettlement | SettlementAccount               |  |
| CashSettlement | DebitDateTime                   |  |
| CashSettlement | PartyRole                       |  |
| CashSettlement | RelatedTransactionAdministrator |  |
| CashSettlement | BookEntry                       |  |
| CashSettlement | RelatedInvestigationCase        |  |

| CashSettlement       | Reservation          |                  |
|----------------------|----------------------|------------------|
| PaymentPartyRole     |                      | Role             |
| PaymentPartyRole     | CashAccount          |                  |
| PaymentPartyRole     | Payment              |                  |
| InstructingAgentRole |                      | PaymentPartyRole |
| InstructingAgentRole | Previous             |                  |
| InstructedAgentRole  |                      | PaymentPartyRole |
| Limit                |                      |                  |
| Limit                | Type                 |                  |
| Limit                | Amount               |                  |
| Limit                | CreditDebitIndicator |                  |
|                      |                      |                  |

| Limit | UsedAmount                 |
|-------|----------------------------|
| Limit | UsedPercentage             |
| Limit | Currency                   |
| Limit | LimitStatus                |
| Limit | Percentage                 |
| Limit | RelatedDebitCreditFacility |
| Limit | Periodicity                |
| Limit | Quantity                   |
| Limit | ValidityPeriod             |
| Limit | RelatedPaymentCard         |
| Limit | AvailableAmount            |
|       |                            |

| RiskManagementLimit      |                       | Limit           |
|--------------------------|-----------------------|-----------------|
| RiskManagementLimit      | CashManagementService |                 |
| RiskManagementLimit      | Counterparty          |                 |
| TransactionAdministrator |                       | SystemPartyRole |
| TransactionAdministrator | CashClearingSystem    |                 |
| TransactionAdministrator | Currency              |                 |

| TransactionAdministrator | CurrencyExchange             |       |
|--------------------------|------------------------------|-------|
| TransactionAdministrator | CashManagementService        |       |
| TransactionAdministrator | SettlementInstruction        |       |
| Reservation              |                              | Limit |
| Reservation              | ReservationType              |       |
| Reservation              | RelatedIntraPositionTransfer |       |
| Reservation              | SettlementInstruction        |       |
| Reservation              | AccountService               |       |
| Balance                  |                              |       |
| Balance                  | Type                         |       |
| Balance                  | ValueDate                    |       |
|                          |                              |       |

| Balance     | CreditDebitIndicator  |         |
|-------------|-----------------------|---------|
| Balance     | AssetHolding          |         |
| Balance     | CalculationDate       |         |
| Balance     | Adjustment            |         |
| Balance     | Account               |         |
| Balance     | Interest              |         |
| Balance     | BalanceEntry          |         |
| Balance     | ProcessingRestriction |         |
| Balance     | OpeningClosingCode    |         |
| CashBalance |                       | Balance |

| CashBalance | CashAccount                         |  |
|-------------|-------------------------------------|--|
| CashBalance | CalculationType                     |  |
| CashBalance | Counterparty                        |  |
| CashBalance | Amount                              |  |
| CashBalance | Availability                        |  |
| CashBalance | CashBalanceEntry                    |  |
| CashBalance | BalanceAdjustmentCode               |  |
| CashBalance | RelatedCardPaymentValidationProcess |  |

| CashBalance            | CutOffDate                |  |
|------------------------|---------------------------|--|
| CashBalance            | RelatedRegisteredContract |  |
| SystemEventInformation |                           |  |
| SystemEventInformation | Type                      |  |
| SystemEventInformation | Time                      |  |
| SystemEventInformation | System                    |  |
| AmountRange            |                           |  |
| AmountRange            | FromAmount                |  |
| AmountRange            | ToAmount                  |  |
|                        |                           |  |

| AmountRange         | EqualAmount          |  |
|---------------------|----------------------|--|
| AmountRange         | NotEqualAmount       |  |
| AmountRange         | CreditDebitIndicator |  |
| AmountRange         | Currency             |  |
| AmountRange         | RelatedInterest      |  |
| AmountRangeBoundary |                      |  |
| AmountRangeBoundary | FromAmountRange      |  |
| AmountRangeBoundary | BoundaryAmount       |  |
| AmountRangeBoundary | Included             |  |
| AmountRangeBoundary | ToAmountRange        |  |
| StandingOrder       |                      |  |
| StandingOrder       | Identification       |  |
| StandingOrder       | Type                 |  |
|                     |                      |  |

| StandingOrder | ValidityPeriod        |  |
|---------------|-----------------------|--|
| StandingOrder | LinkSetIdentification |  |
| StandingOrder | StandingOrderSequence |  |
| StandingOrder | Amount                |  |
| StandingOrder | CreditAccount         |  |
| StandingOrder | DebitAccount          |  |
| StandingOrder | Frequency             |  |
| StandingOrder | EventDescription      |  |
| StandingOrder | Day                   |  |
|               |                       |  |

| StandingOrder     | TimeSpecification         |               |
|-------------------|---------------------------|---------------|
| StandingOrder     | PaymentInstructionTrigger |               |
| StandingOrder     | IncludedStandingOrder     |               |
| StandingOrder     | LinkSet                   |               |
| CashStandingOrder |                           | StandingOrder |
| CashStandingOrder | ZeroSweepIndicator        |               |
| CashStandingOrder | RelatedCashServices       |               |
| CashStandingOrder | CreditDebitIndicator      |               |

| CashStandingOrder           | CreditTransfer        |                             |
|-----------------------------|-----------------------|-----------------------------|
| CashStandingOrder           | FloorAmount           |                             |
| CashStandingOrder           | CashAccount           |                             |
| AccountResponsiblePartyRole |                       | AccountPartyRole            |
| StandingOrderResponsible    |                       | AccountResponsiblePartyRole |
| PaymentStatus               |                       | Status                      |
| PaymentStatus               | Status                |                             |
| PaymentStatus               | Payment               |                             |
| PaymentStatus               | UnmatchedStatusReason |                             |
| PaymentStatus               | SuspendedStatusReason |                             |
| PaymentStatus               | PendingSettlement     |                             |
|                             |                       |                             |

| PaymentStatus<br>InstructionStatus<br>PaymentStatus<br>TransactionRejectionReason<br>PaymentStatus<br>RelatedInvestigationCase<br>PaymentStatus<br>NotificationStatus<br>PaymentStatus<br>TransactionStatus<br>PaymentStatus<br>CashPaymentStatus<br>PaymentStatus<br>UnsuccessfulStatusReason<br>PaymentStatus<br>CancellationReason<br>PaymentStatus<br>MandateRejectionReason<br>PaymentStatus<br>PendingFailingSettlement<br>DebtorRole<br>PaymentPartyRole |  |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |

| PaymentProcessing |                  |  |
|-------------------|------------------|--|
| PaymentProcessing | Priority         |  |
| PaymentProcessing | ServiceLevel     |  |
| PaymentProcessing | ClearingChannel  |  |
| PaymentProcessing | LocalInstrument  |  |
| PaymentProcessing | CategoryPurpose  |  |
| PaymentProcessing | PaymentExecution |  |
| PaymentProcessing | SequenceType     |  |
| PaymentProcessing | RelatedMandate   |  |
|                   |                  |  |

| PaymentProcessing   | BankTransaction   |                |
|---------------------|-------------------|----------------|
| PaymentProcessing   | ContactPoint      |                |
| PaymentProcessing   | AdviceType        |                |
| AssetPartyRole      |                   | Role           |
| AssetPartyRole      | Asset             |                |
| SecuritiesPartyRole |                   | AssetPartyRole |
| SecuritiesPartyRole | SecuritiesAccount |                |
| SecuritiesPartyRole | CashAccount       |                |
| SecuritiesPartyRole | Security          |                |
|                     |                   |                |

| SettlementPartyRole           |                            | Role                          |
|-------------------------------|----------------------------|-------------------------------|
| SettlementPartyRole           | SettlementAccount          |                               |
| SettlementPartyRole           | Settlement                 |                               |
| SecuritiesSettlementPartyRole |                            | SettlementPartyRole           |
| SecuritiesSettlementPartyRole | SecuritiesSettlement       |                               |
| SecuritiesSettlementPartyRole | SecuritiesSettlementSystem |                               |
| SecuritiesSettlementPartyRole | SettlingCapacity           |                               |
| SecuritiesSettlementPartyRole | TaxCapacity                |                               |
| ReceivingSettlementParty      |                            | SecuritiesSettlementPartyRole |
| ReceivingSettlementParty      | ReceivingSettlementParty   |                               |
| ReceivingSettlementParty      | NextParty                  |                               |

| SecuritiesSettlement |                        | Settlement |
|----------------------|------------------------|------------|
| SecuritiesSettlement | TransferOperation      |            |
| SecuritiesSettlement | SettlementDate         |            |
| SecuritiesSettlement | PartyRole              |            |
| SecuritiesSettlement | SettlementAmount       |            |
| SecuritiesSettlement | HoldingsPlanType       |            |
| SecuritiesSettlement | SecuritiesMovementType |            |
| SecuritiesSettlement | SettlementQuantity     |            |
|                      |                        |            |

| SecuritiesSettlement<br>SecuritiesTradeExecution<br>SecuritiesSettlement<br>CurrencyToBuy<br>SecuritiesSettlement<br>CurrencyToSell<br>SecuritiesSettlement<br>DenominationChoice<br>SecuritiesSettlement<br>SettlementTransactionCondition<br>SecuritiesSettlement<br>BeneficialOwnershipIndicator<br>SecuritiesSettlement<br>MarketClientSide<br>SecuritiesSettlement<br>Tracking<br>SecuritiesSettlement<br>LetterOfGuarantee |  |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |

| SecuritiesSettlement | EligibleForCollateral             |  |
|----------------------|-----------------------------------|--|
| SecuritiesSettlement | AccruedInterestIndicator          |  |
| SecuritiesSettlement | PreConfirmation                   |  |
| SecuritiesSettlement | SecuritiesRealTimeGrossSettlement |  |
| SecuritiesSettlement | BlockTrade                        |  |
| SecuritiesSettlement | SettlementSystemMethod            |  |
| SecuritiesSettlement | AutomaticBorrowing                |  |
| SecuritiesSettlement | PartialSettlementIndicator        |  |
| SecuritiesSettlement | HoldIndicator                     |  |
| SecuritiesSettlement | RequestedSafekeepingPlace         |  |
|                      |                                   |  |

| SecuritiesSettlement | PairOff                         | Buy and sell trades are settled in<br>cash, based on the difference in<br>the prices between the off<br>setting trades.      |
|----------------------|---------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| SecuritiesSettlement | AccruedInterest                 | Interest included in the<br>settlement.                                                                                      |
| SecuritiesSettlement | SecuritiesClearing              | Clearing process which triggers<br>the settlement process.                                                                   |
| SecuritiesSettlement | Payment                         | Specifies the cash payment<br>information of a securities<br>settlement.                                                     |
| SecuritiesSettlement | SettledAllocation               | Allocation which is settled.                                                                                                 |
| SecuritiesSettlement | RelatedForeignExchangeOperation | Entry details related to currency<br>exchange information.                                                                   |
| SecuritiesSettlement | Security                        | Security which is settled.                                                                                                   |
| SecuritiesSettlement | Position                        | Information on the quantities and<br>amounts to be settled in a<br>position.                                                 |
| SecuritiesSettlement | Rollover                        | Process whereby a financial<br>instrument is reinvested at<br>maturity.                                                      |
| SecuritiesSettlement | TurnedQuantity                  | Relates to a turnaround: the<br>same security is bought and sold<br>to settle the same day, to or<br>from different brokers. |
| SecuritiesSettlement | SettlementReason                | Specifies the reason for the<br>settlement related to the type of<br>underlying trade.                                       |

| SecuritiesSettlement | SettlementType         | Specifies how the transaction is<br>to be settled, eg, against<br>DeliveryReceiptTypeCode<br>payment.                                                                          |
|----------------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SecuritiesSettlement | BuyInState             | Status of the buy-in transaction.<br>BuyInStateCode                                                                                                                            |
| SecuritiesSettlement | BuyInDeferral          | Specifies if the buy-in transaction<br>BuyInDeferralCode<br>was deferred or not.                                                                                               |
| SecuritiesSettlement | CashCompensationAmount | Amount of money that has to be<br>paid by the failing trading party<br>in case of an unsuccessful or<br>ActiveCurrencyAndAmount<br>partially successful buy-in<br>transaction. |
| LotBreakdown         |                        | Number of securities purchased<br>or sold in one transaction. In<br>terms of options, a lot represents<br>the number of contracts<br>contained in one derivative<br>security.  |
| LotBreakdown         | LotUnit                | Quantity of securities included in<br>DecimalNumber<br>the lot.                                                                                                                |
| LotBreakdown         | SecuritiesQuantity     | Number of securities included in<br>SecuritiesQuantity<br>LotBreakdown<br>a lot.                                                                                               |
| LotBreakdown         | LotNumber              | Specifies the number of the lot.<br>GenericIdentification<br>IdentificationForLot                                                                                              |
| LotBreakdown         | LotDateTime            | Date and time at which the lot<br>ISODateTime<br>was purchased.                                                                                                                |
| LotBreakdown         | LotPrice               | Specifies the price of the lot.<br>SecuritiesPricing<br>LotBreakdown                                                                                                           |
| LotBreakdown         | LotIdentifier          | Identifies the lot constituting an<br>asset backed or mortgage<br>Max35Text<br>backed security issue.                                                                          |

| LotBreakdown | TradeLotMarket    |  |
|--------------|-------------------|--|
| LotBreakdown | QuoteLotMarket    |  |
| LotBreakdown | RoundLotMarket    |  |
| Price        |                   |  |
| Price        | Amount            |  |
| Price        | Option            |  |
| Price        | UnitPriceProduct  |  |
| Price        | NetPriceProduct   |  |
| Price        | PriceAdjustment   |  |
| Price        | GrossPriceProduct |  |
| Price        | UnitOfMeasure     |  |
| Price        | PriceTolerance    |  |
| Price        | Currency          |  |
|              |                   |  |

| Price          | Factor               |            |
|----------------|----------------------|------------|
| Price          | Netting              |            |
| Price          | SecuritiesPricing    |            |
| Price          | RelatedEnergy        |            |
| AmountAndPrice |                      |            |
| AmountAndPrice | Amount               |            |
| AmountAndPrice | Price                |            |
| Charges        |                      | Adjustment |
| Charges        | ChargeType           |            |
| Charges        | CalculationBasis     |            |
| Charges        | BearerType           |            |
| Charges        | ChargesDebitAccount  |            |
| Charges        | CashEntry            |            |
| Charges        | CreditDebitIndicator |            |

| Charges | MaximumAmount             |  |
|---------|---------------------------|--|
| Charges | InvestmentFundTransaction |  |
| Charges | LogisticsChargeLineItem   |  |
| Charges | Transport                 |  |
| Charges | Services                  |  |
| Charges | RelatedUndertaking        |  |
| Charges | LineItem                  |  |
| Charges | NetPriceChargeLineItem    |  |
| Charges | BaseAmount                |  |
| Charges | MaximumRate               |  |
| Charges | MinimumRate               |  |

| Charges               | MinimumAmount        |         |
|-----------------------|----------------------|---------|
| Charges               | RelatedInterest      |         |
| Charges               | ChargePaymentMethod  |         |
| SecuritiesRelatedFees |                      | Charges |
| SecuritiesRelatedFees | Security             |         |
| SecuritiesRelatedFees | PostageFeeAmount     |         |
| SecuritiesRelatedFees | RegulatoryFeesAmount |         |
| SecuritiesRelatedFees | ShippingFeesAmount   |         |
| SecuritiesRelatedFees | ResearchFee          |         |
| ValuationStatistics   |                      |         |
| ValuationStatistics   | Currency             |         |

| ValuationStatistics<br>PriceChange<br>ValuationStatistics<br>Yield<br>ValuationStatistics<br>HighestPriceValue<br>ValuationStatistics<br>LowestPriceValue<br>ValuationStatistics<br>Period<br>ValuationStatistics<br>NetAssetValueCalculation<br>ValuationStatistics<br>NetAssetValueChangeRate | ValuationStatistics | PriceTypeChangeBasis |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|----------------------|--|
|                                                                                                                                                                                                                                                                                                 |                     |                      |  |
|                                                                                                                                                                                                                                                                                                 |                     |                      |  |
|                                                                                                                                                                                                                                                                                                 |                     |                      |  |
|                                                                                                                                                                                                                                                                                                 |                     |                      |  |
|                                                                                                                                                                                                                                                                                                 |                     |                      |  |
|                                                                                                                                                                                                                                                                                                 |                     |                      |  |
|                                                                                                                                                                                                                                                                                                 |                     |                      |  |

| FundManagerRole    |                                 | InvestmentFundPartyRole |
|--------------------|---------------------------------|-------------------------|
| PerformanceFactors |                                 |                         |
| PerformanceFactors | NetAssetValueCalculation        |                         |
| PerformanceFactors | CorporateActionFactor           |                         |
| PerformanceFactors | CumulativeCorporateActionFactor |                         |
| PerformanceFactors | AccumulationPeriod              |                         |
| PerformanceFactors | NormalPerformance               |                         |
|                    |                                 |                         |

| CashAccountContract<br>CashAccount<br>CashAccountContract<br>TransferCashAccount<br>CashAccountContract<br>Services<br>CashAccountContract<br>BalanceTransfer<br>CashAccountContract<br>CashAccountMandate | CashAccountContract | AccountContract |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|-----------------|
|                                                                                                                                                                                                            |                     |                 |
|                                                                                                                                                                                                            |                     |                 |
|                                                                                                                                                                                                            |                     |                 |
|                                                                                                                                                                                                            |                     |                 |
|                                                                                                                                                                                                            |                     |                 |

| CashAccountService |                     | AccountService |
|--------------------|---------------------|----------------|
| CashAccountService | CashAccountMandate  |                |
| CashAccountService | CompensationMethod  |                |
| CashAccountService | BillingCurrency     |                |
| CashAccountService | BillingChargeMethod |                |
| CashAccountService | PaymentMethod       |                |
| CashAccountService | CashAccountContract |                |
| CashAccountService | Identification      |                |
| CashAccountService | CashAccount         |                |
|                    |                     |                |

| CashManagementService |                                 | CashAccountService |
|-----------------------|---------------------------------|--------------------|
| CashManagementService | RiskManagementLimit             |                    |
| CashManagementService | StandingOrder                   |                    |
| CashManagementService | RelatedTransactionAdministrator |                    |
| CashManagementService | LiquidityManagementLimit        |                    |
| CashManagementService | CallInType                      |                    |
| AccountRestriction    |                                 |                    |

| AccountRestriction | Account                |
|--------------------|------------------------|
| AccountRestriction | RestrictionType        |
| AccountRestriction | ValidityPeriod         |
| SystemStatus       | Status                 |
| SystemStatus       | Status                 |
| SystemStatus       | MemberStatus           |
| SystemStatus       | System                 |
| SystemStatus       | SystemMemberRole       |
| SystemAvailability |                        |
| SystemAvailability | AvailableSessionPeriod |
| SystemAvailability | System                 |
| SystemAvailability | ClosureInformation     |
| SystemAvailability | Date                   |

| SystemAvailability        | ClosurePeriod      |  |
|---------------------------|--------------------|--|
| TimePeriod                |                    |  |
| TimePeriod                | SystemAvailability |  |
| TimePeriod                | FromTime           |  |
| TimePeriod                | ToTime             |  |
| SystemClosureInformation  |                    |  |
| SystemClosureInformation  | Period             |  |
| SystemClosureInformation  | SystemAvailability |  |
| SystemClosureInformation  | ClosureReason      |  |
| SystemBusinessInformation |                    |  |
| SystemBusinessInformation | Qualifier          |  |

| SystemBusinessInformation | Subject                   |        |
|---------------------------|---------------------------|--------|
| SystemBusinessInformation | SubjectDetails            |        |
| SystemBusinessInformation | Identification            |        |
| SystemBusinessInformation | Reference                 |        |
| SystemBusinessInformation | System                    |        |
| InformationQualifier      |                           |        |
| InformationQualifier      | SystemBusinessInformation |        |
| InformationQualifier      | IsFormatted               |        |
| InformationQualifier      | Priority                  |        |
| LimitStatus               |                           | Status |
| LimitStatus               | Limit                     |        |
| LimitStatus               | Status                    |        |
|                           |                           |        |

| BookEntry       |                              | CreditInstrument |
|-----------------|------------------------------|------------------|
| BookEntry       | CashEntry                    |                  |
| BookEntry       | DebitEntry                   |                  |
| BookEntry       | CreditEntry                  |                  |
| BookEntry       | TransferAdvice               |                  |
| BookEntry       | FundSubscriptionCashInFlow   |                  |
| BookEntry       | FundRedemptionCashOutFlow    |                  |
| BookEntry       | RelatedSettlementInstruction |                  |
| SecuritiesEntry |                              | Entry            |

| SecuritiesEntry       | AcquisitionDate              | Date upon which the investor<br>purchased the financial<br>ISODate<br>instrument.                                                                                            |
|-----------------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SecuritiesEntry       | FinancialInstrumentQuantity  | Quantity of financial instrument.<br>SecuritiesQuantity                                                                                                                      |
| SecuritiesEntry       | SecuritiesAccount            | Securities account on which the<br>quantity of the entry is debited<br>or credited. It is derived from the<br>SecuritiesAccount<br>association between Entry and<br>Account. |
| SecuritiesEntry       | SecuritiesBalance            | Amount that is the result of the<br>sum of the entries from or to an<br>account. It is derived from the<br>SecuritiesBalance<br>association between Entry and<br>Balance.    |
| SecuritiesEntry       | TriggeringSecuritiesTransfer | Transfer which is at the origin of<br>the entry in the securities<br>SecuritiesTransfer<br>account.                                                                          |
| SecuritiesCertificate |                              | Physical representation of a<br>security.                                                                                                                                    |
| SecuritiesCertificate | Number                       | Identifier of a certificate assigned<br>by the issuer.                                                                                                                       |
| SecuritiesCertificate | BasicRegistration            | Registration process which<br>BasicSecuritiesRegistration<br>requires a securities certificate.                                                                              |
| SecuritiesCertificate | RelatedDelivery              | Delivery parameters which<br>specify the certificate<br>parameters.                                                                                                          |
|                       |                              |                                                                                                                                                                              |

| Interest |                               |  |
|----------|-------------------------------|--|
| Interest | AccruedInterestAmount         |  |
| Interest | InterestCalculation           |  |
| Interest | Amount                        |  |
| Interest | Rate                          |  |
|          |                               |  |
| Interest | RelatedCashProceedsDefinition |  |
| Interest | SecuritiesFinancing           |  |
| Interest | InterestTax                   |  |
| Interest | CreditDebitIndicator          |  |
| Interest | CashEntry                     |  |

| Interest | RelatedInterestManagement       |  |
|----------|---------------------------------|--|
| Interest | RelatedUndertakingAmount        |  |
| Interest | RelatedDebitCreditFacility      |  |
| Interest | SecuritiesSettlement            |  |
| Interest | InterestName                    |  |
| Interest | RelatedAssetHolding             |  |
| Interest | Deposit                         |  |
| Interest | AccountBalance                  |  |
| Interest | RelatedAccountContract          |  |
| Interest | RelatedNetAssetValueCalculation |  |
| Interest | TypeOfInterest                  |  |
| Interest | RelatedPaymentCard              |  |
|          |                                 |  |

| SafekeepingPlace |                            | SecuritiesPartyRole |
|------------------|----------------------------|---------------------|
| SafekeepingPlace | SafekeepingPlaceType       |                     |
| SafekeepingPlace | Country                    |                     |
| SafekeepingPlace | RelatedSecuritiesAccount   |                     |
| SafekeepingPlace | SecuritiesBalance          |                     |
| SafekeepingPlace | SecuritiesSettlement       |                     |
| PhysicalDelivery |                            |                     |
| PhysicalDelivery | RelatedTransfer            |                     |
| PhysicalDelivery | RegisteredAddressIndicator |                     |
| PhysicalDelivery | IssuedCertificateNumber    |                     |
| PhysicalDelivery | Address                    |                     |
| PhysicalDelivery | Type                       |                     |

| SecuritiesTradeExecution |                       |  |
|--------------------------|-----------------------|--|
| SecuritiesTradeExecution | StampDutyIndicator    |  |
| SecuritiesTradeExecution | ProcessingPosition    |  |
| SecuritiesTradeExecution | SecuritiesSettlement  |  |
| SecuritiesTradeExecution | DealPrice             |  |
| SecuritiesTradeExecution | MarginAmount          |  |
| SecuritiesTradeExecution | ExecutedTradeQuantity |  |
|                          |                       |  |

| SecuritiesTradeExecution | OffMarketReason              |      |
|--------------------------|------------------------------|------|
| SecuritiesTradeExecution | RelatedTrade                 |      |
| SecuritiesTradeExecution | DealExecutionAmount          |      |
| SecuritiesTradeExecution | PaymentObligation            |      |
| SecuritiesTradeExecution | SecuritiesDeliveryObligation |      |
| SecuritiesTradeExecution | ReportingType                |      |
| ContactPersonRole        |                              | Role |
| ContactPersonRole        | Role                         |      |
| ContactPersonRole        | Meeting                      |      |
| ContactPersonRole        | Person                       |      |
|                          |                              |      |

| DeliveringSettlementParty  |                             | SecuritiesSettlementPartyRole |
|----------------------------|-----------------------------|-------------------------------|
| DeliveringSettlementParty  | DeliveringSettlementParty   |                               |
| DeliveringSettlementParty  | NextParty                   |                               |
| SecuritiesSettlementSystem |                             | System                        |
| SecuritiesSettlementSystem | SettlementParty             |                               |
| SecuritiesTradeStatus      |                             | Status                        |
| SecuritiesTradeStatus      | MatchingStatus              |                               |
| SecuritiesTradeStatus      | AffirmationStatus           |                               |
| SecuritiesTradeStatus      | Reason                      |                               |
| SecuritiesTradeStatus      | SecuritiesTrade             |                               |
| SecuritiesTradeStatus      | TransactionStatus           |                               |
| SecuritiesTradeStatus      | ReplacementProcessingStatus |                               |
|                            |                             |                               |

| SecuritiesTradeStatus       | CancellationStatus                    |              |
|-----------------------------|---------------------------------------|--------------|
| SecuritiesTradeStatus       | CancellationRight                     |              |
| SecuritiesTradeStatus       | TransferStatus                        |              |
| SecuritiesTradeStatus       | AllegedStatus                         |              |
| SecuritiesTradeStatus       | CollateralAllocationStatus            |              |
| SecuritiesTradeStatus       | RepoCallRequestStatus                 |              |
| SecuritiesTradeStatus       | SettlementConditionModificationStatus |              |
| SecuritiesTradeStatus       | MatchingProcess                       |              |
| SecuritiesTradeStatus       | RelatedSecuritiesTransfer             |              |
| SecuritiesTradeStatus       | TradeConfirmationStatus               |              |
| SecuritiesTradeStatusReason |                                       | StatusReason |

| SecuritiesTradeStatusReason | UnmatchedReason               |        |
|-----------------------------|-------------------------------|--------|
| SecuritiesTradeStatusReason | DeniedReason                  |        |
| SecuritiesTradeStatusReason | SecuritiesTradeStatus         |        |
| SecuritiesTradeStatusReason | GeneratedReason               |        |
| SecuritiesTradeStatusReason | AllegementReason              |        |
| SecuritiesTradeStatusReason | PendingSettlementReason       |        |
| SecuritiesTradeStatusReason | RepoCallAcknowledgementReason |        |
| SecuritiesTradeStatusReason | RepairReason                  |        |
| SecuritiesTradeStatusReason | DeliveryReturnReason          |        |
| SecuritiesTradeStatusReason | CounterpartyStatusReason      |        |
| SecuritiesTradeStatusReason | ModifiedStatusReason          |        |
| CorporateActionStatus       |                               | Status |

| CorporateActionStatus | AgentStandingInstructionStatus             |  |
|-----------------------|--------------------------------------------|--|
| CorporateActionStatus | ProcessingStatus                           |  |
| CorporateActionStatus | EventProcessingStatus                      |  |
| CorporateActionStatus | CorporateActionStatusReason                |  |
| CorporateActionStatus | InstructionCancellationStatus              |  |
| CorporateActionStatus | CorporateActionInstructionProcessingStatus |  |
| CorporateActionStatus | RateStatus                                 |  |
| CorporateActionStatus | OptionAvailabilityStatus                   |  |
| CorporateActionStatus | CorporateActionEvent                       |  |
| CorporateActionStatus | EventStatus                                |  |
| CorporateActionStatus | RelatedInstructionProcessedStatus          |  |
| CorporateActionStatus | DeactivationDateAndTime                    |  |
|                       |                                            |  |

| CorporateActionStatus        | EventConfirmationStatus   |            |
|------------------------------|---------------------------|------------|
| CorporateActionStatus        | EventCompletenessStatus   |            |
| SecuritiesDeliveryObligation |                           | Obligation |
| SecuritiesDeliveryObligation | CCPEligibility            |            |
| SecuritiesDeliveryObligation | NettingEligibility        |            |
| SecuritiesDeliveryObligation | TransferInstructionDate   |            |
| SecuritiesDeliveryObligation | TransferCurrency          |            |
| SecuritiesDeliveryObligation | RelatedCorporateAction    |            |
| SecuritiesDeliveryObligation | RelatedCollateralMovement |            |
| SecuritiesDeliveryObligation | SecuritiesTradeExecution  |            |
| SecuritiesDeliveryObligation | RelatedPortfolioTransfer  |            |
|                              |                           |            |

| SecuritiesDeliveryObligation<br>SecuritiesTransfer<br>SecuritiesDeliveryObligation<br>SettlementInstructionGeneration<br>SecuritiesDeliveryObligation<br>SettlementDateCode<br>SecuritiesDeliveryObligation<br>SecuritiesLending<br>CurrencyExchange<br>CurrencyExchange<br>OriginalAmount<br>CurrencyExchange<br>CurrencyExchangeForForeignExchangeTrade<br>CurrencyExchange<br>UnitCurrency<br>CurrencyExchange<br>QuotedCurrency |  |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |  |  |

| CurrencyExchange | ExchangeRate                         |  |
|------------------|--------------------------------------|--|
| CurrencyExchange | ResultingAmount                      |  |
| CurrencyExchange | RelatedCorporateActionEvent          |  |
| CurrencyExchange | CurrencyExchangeForSecuritiesBalance |  |
| CurrencyExchange | QuotationDate                        |  |
| CurrencyExchange | CalculatedAssetValue                 |  |
| CurrencyExchange | SourceCurrency                       |  |
| CurrencyExchange | TargetCurrency                       |  |
| CurrencyExchange | CurrencyExchangeForCashEntry         |  |
|                  |                                      |  |

| CurrencyExchange | RelatedPayment                                    |  |
|------------------|---------------------------------------------------|--|
| CurrencyExchange | RateType                                          |  |
| CurrencyExchange | RelatedLimitManagement                            |  |
| CurrencyExchange | FixingConditions                                  |  |
| CurrencyExchange | Tax                                               |  |
| CurrencyExchange | RelatedInvoice                                    |  |
| CurrencyExchange | CurrencyExchangeForTransactionAdministrator       |  |
| CurrencyExchange | ReportedAccount                                   |  |
| CurrencyExchange | CurrencyExchangeForCorporateActionCashEntitlement |  |
| CurrencyExchange | PaymentExecution                                  |  |
| CurrencyExchange | CurrencyExchangeForSecuritiesQuote                |  |
|                  |                                                   |  |

| CurrencyExchange                 | CurrencyExchangeForSecuritiesConversion    |  |
|----------------------------------|--------------------------------------------|--|
| CurrencyExchange                 | CurrencyExchangeForCashDistribution        |  |
| CurrencyExchange                 | Adjustment                                 |  |
| CurrencyExchange                 | RelatedPaymentTracker                      |  |
| CurrencyExchange                 | ExchangeRateBase                           |  |
| CorporateActionEventRegistration |                                            |  |
| CorporateActionEventRegistration | CorporateActionEventIdentification         |  |
| CorporateActionEventRegistration | OfficialCorporateActionEventIdentification |  |
| CorporateActionEventRegistration | OfficialAnnouncementPublicationDate        |  |
| CorporateActionEventRegistration | CorporateActionEvent                       |  |
|                                  |                                            |  |

| TradeOriginatorRole  |                               | TradePartyRole |
|----------------------|-------------------------------|----------------|
| TradeOriginatorRole  | OriginatorRole                |                |
| TreasuryTrade        |                               | Trade          |
| TreasuryTrade        | TreasuryTradeSettlementStatus |                |
| TreasuryTrade        | InformationPartyRole          |                |
| TreasuryTrade        | TreasurySettlementPartyRole   |                |
| TreasuryTrade        | PartyRole                     |                |
| ForeignExchangeTrade |                               | TreasuryTrade  |
| ForeignExchangeTrade | AgreedRate                    |                |
| ForeignExchangeTrade | TypeOfProduct                 |                |

| ForeignExchangeTrade | BuyAmount                               |  |
|----------------------|-----------------------------------------|--|
| ForeignExchangeTrade | SellAmount                              |  |
| ForeignExchangeTrade | ResultingSettlement                     |  |
| ForeignExchangeTrade | CurrencyExchangeForSecuritiesSettlement |  |
| ForeignExchangeTrade | OpeningLegRelatedNonDeliverableTrade    |  |
| ForeignExchangeTrade | ClosingLegRelatedNonDeliverableTrade    |  |
| ForeignExchangeTrade | RelatedSwap                             |  |
| ForeignExchangeTrade | RelatedOption                           |  |
| ForeignExchangeTrade | CurrencyExchangeForTaxVoucher           |  |
|                      |                                         |  |

| ForeignExchangeTrade | ExchangeForwardPoint |  |
|----------------------|----------------------|--|
| InterestCalculation  |                      |  |
| InterestCalculation  | DayCountBasis        |  |
| InterestCalculation  | Rate                 |  |
| InterestCalculation  | Interest             |  |
| InterestCalculation  | RateType             |  |
| InterestCalculation  | InterestPeriod       |  |
| InterestCalculation  | RelatedIndex         |  |
|                      |                      |  |

| InterestCalculation | InterestAccrualDate  | date.          | Start date used for calculating<br>accrued interest on debt<br>instruments which are being sold<br>between interest payment dates.<br>Often but not always the same as<br>the issue date and the dated | ISODateTime           |                     |
|---------------------|----------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|---------------------|
| InterestCalculation | CalculationMethod    |                | Specifies whether the interest is<br>simple or compounded.                                                                                                                                             | CalculationMethodCode |                     |
| InterestCalculation | VariableInterest     | payments.      | Specifies the parameters to be<br>used for variable interest                                                                                                                                           | VariableInterest      | InterestCalculation |
| InterestCalculation | InterestType         |                | Specifies the type of interest.                                                                                                                                                                        | InterestCode          |                     |
| InterestCalculation | RateValidityRange    | applicable.    | Specifies the amount range for<br>which the interest rate is                                                                                                                                           | AmountRange           |                     |
| InterestCalculation | InterestMethod       |                | Indicates whether the interest<br>will be settled in cash or rolled in<br>the existing collateral balance.                                                                                             | InterestMethodCode    |                     |
| InterestCalculation | CalculationFrequency |                | Specifies the periodicity of the<br>calculation of the interest.                                                                                                                                       | FrequencyCode         |                     |
| InterestCalculation | CalculationDate      |                | Indicates the calculation date of<br>the interest amount.                                                                                                                                              | ISODate               |                     |
| InterestCalculation | Charges              |                | Specifies the charges on interest.                                                                                                                                                                     | Charges               |                     |
| InterestCalculation | DebtInstrument       | specified.     | Debt for which a next interest is                                                                                                                                                                      | Debt                  |                     |
| InterestCalculation | Spread               | two interests. | Specifies the difference between                                                                                                                                                                       | Spread                |                     |
|                     |                      |                |                                                                                                                                                                                                        |                       |                     |

| InterestCalculation | PaymentFrequency          |          |
|---------------------|---------------------------|----------|
| InterestCalculation | RelatedInterestManagement |          |
| Debt                |                           | Security |
| Debt                | PaymentDirectionIndicator |          |
| Debt                | NextCallableDate          |          |
| Debt                | PutableDate               |          |
| Debt                | DatedDate                 |          |
| Debt                | FirstPaymentDate          |          |
|                     |                           |          |

| Debt | Factor                |  |
|------|-----------------------|--|
| Debt | PoolNumber            |  |
| Debt | VariableRateIndicator |  |
| Debt | CallableIndicator     |  |
| Debt | PutableIndicator      |  |
| Debt | YieldToMaturityRate   |  |

| Debt | AccruedCapitalisationAmount |  |
|------|-----------------------------|--|
| Debt | NextCouponDate              |  |
| Debt | NextFactorDate              |  |
| Debt | OddCouponIndicator          |  |
| Debt | CPProgram                   |  |
| Debt | CPRegistrationType          |  |
| Debt | ConvertibleIndicator        |  |
| Debt | PreFundedIndicator          |  |

| Debt | EscrowedIndicator     |  |
|------|-----------------------|--|
| Debt | PerpetualIndicator    |  |
| Debt | SubordinatedIndicator |  |
| Debt | ExtendibleIndicator   |  |
| Debt | ExtendiblePeriod      |  |
| Debt | OverAllotmentAmount   |  |
| Debt | OverAllotmentRate     |  |
| Debt | AmortisableIndicator  |  |
|      |                       |  |

| Debt | CapitalisedInterest       |  |
|------|---------------------------|--|
| Debt | ActualDenominationAmount  |  |
| Debt | Pieces                    |  |
| Debt | PoolsMaximum              |  |
| Debt | PoolsPerMillion           |  |
| Debt | PoolsPerLot               |  |
| Debt | PoolsPerTrade             |  |
| Debt | ConstantPrePaymentPenalty |  |
|      |                           |  |

| Debt | PrePaymentSpeed         |  |
|------|-------------------------|--|
| Debt | ConstantPrePaymentYield |  |
| Debt | WeightedAverageCoupon   |  |
| Debt | WeightedAverageLife     |  |
| Debt | WeightedAverageLoan     |  |
| Debt | WeightedAverageMaturity |  |
| Debt | InsuredIndicator        |  |
| Debt | BankQualified           |  |

| Debt<br>AutoReinvestment<br>Debt<br>CustomDate<br>Debt<br>LookBack<br>Debt<br>MinimumDenomination<br>Debt<br>MaximumSubstitution<br>Debt<br>MinimumIncrement<br>Debt<br>Production<br>Debt<br>Restricted |  |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                          |  |  |

| Debt<br>PriceFrequency<br>Debt<br>SubstitutionFrequency<br>Debt<br>SubstitutionLeft<br>Debt<br>WholePool<br>Debt<br>AlternativeMinimumTax<br>Debt<br>NextInterest<br>Debt<br>ExtendibleDate<br>Debt<br>SinkableIndicator |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |
|                                                                                                                                                                                                                          |  |  |

| Debt             | Insured            |        |
|------------------|--------------------|--------|
| Debt             | Geographics        |        |
| Debt             | PaymentCurrency    |        |
| Debt             | DirtyPrice         |        |
| Debt             | DebtSeniority      |        |
| SecuritiesStatus |                    | Status |
| SecuritiesStatus | PaymentStatus      |        |
| SecuritiesStatus | Status             |        |
| SecuritiesStatus | RegistrationStatus |        |
| SecuritiesStatus | Security           |        |
|                  |                    |        |

| VariableInterest |                             |  |
|------------------|-----------------------------|--|
| VariableInterest | VariableRateChangeFrequency |  |
| VariableInterest | FixingDate                  |  |
| VariableInterest | InterestCalculation         |  |
| VariableInterest | ReportingDate               |  |
| VariableInterest | ResetDate                   |  |
| VariableInterest | Arrears                     |  |
| VariableInterest | Index                       |  |
| VariableInterest | YieldCalculation            |  |
|                  |                             |  |

| VariableInterest | BenchmarkReference    |          |
|------------------|-----------------------|----------|
| VariableInterest | EstimatedInterestRate |          |
| VariableInterest | VariableRateValueDate |          |
| VariableInterest | LifeCalculation       |          |
| VariableInterest | DurationCalculation   |          |
| Equity           |                       | Security |

| Equity              | PreferenceToIncome   |  |
|---------------------|----------------------|--|
| Equity              | ConvertibleIndicator |  |
| Equity              | NonPaidAmount        |  |
| Equity              | ParValue             |  |
| Equity              | VotingRightsPerShare |  |
| AssetClassification |                      |  |
| AssetClassification | ClassificationType   |  |
| AssetClassification | Asset                |  |
| AssetClassification | Language             |  |

| AssetClassification | AssetClassScheme          |       |
|---------------------|---------------------------|-------|
| AssetClassification | ProductType               |       |
| AssetClassification | Strategy                  |       |
| AssetClassification | ClassificationSubType     |       |
| Derivative          |                           | Asset |
| Derivative          | UnderlyingAsset           |       |
| Derivative          | NotionalCurrencyAndAmount |       |
| Derivative          | DerivativeCovered         |       |
| Derivative          | ExerciseDate              |       |
| Derivative          | InterestIncludedInPrice   |       |
| Derivative          | Tick                      |       |

| Derivative | ExercisePrice              |            |
|------------|----------------------------|------------|
| Derivative | NotionalCurrency           |            |
| Derivative | VersionNumber              |            |
| Derivative | Event                      |            |
| Option     |                            | Derivative |
| Option     | InstrumentAssignmentMethod |            |
| Option     | SettleStyle                |            |

| Option | Standardisation             |  |
|--------|-----------------------------|--|
| Option | PositionLimit               |  |
| Option | UnderlyingType              |  |
| Option | CoverIndicator              |  |
| Option | OptionConversionInformation |  |
| Option | OptionRatio                 |  |
| Option | SecuritiesOptionTrade       |  |
| Option | SettlementType              |  |
|        |                             |  |

| Option | StrikeMultiplier     |  |
|--------|----------------------|--|
| Option | ExpiryLocation       |  |
| Option | FinalSettlementDate  |  |
| Option | OptionStyle          |  |
| Option | CurrencyOption       |  |
| Option | EarliestExerciseDate |  |
| Option | SettlementDays       |  |
| Option | StrikePrice          |  |
| Option | OptionStartDate      |  |
| Option | ExpiryDateAndTime    |  |

| Option         | OptionType           |  |
|----------------|----------------------|--|
| Option         | StrikeValue          |  |
| Option         | SettlementPeriodType |  |
| CouponAttached |                      |  |
| CouponAttached | Date                 |  |
| CouponAttached | Number               |  |
| CouponAttached | Security             |  |
| CouponAttached | CouponClippingDate   |  |
| CouponAttached | Identification       |  |
| Issuance       |                      |  |

| Issuance | IssueDate              |  |
|----------|------------------------|--|
| Issuance | IssueDiscountAllowance |  |
| Issuance | InterestShortfall      |  |
| Issuance | RealisedLoss           |  |
| Issuance | Purpose                |  |
| Issuance | IssueSize              |  |
| Issuance | IssueNominalAmount     |  |
| Issuance | EventInformation       |  |
| Issuance | IssuedAsset            |  |
| Issuance | OriginalIssueDiscount  |  |
|          |                        |  |

| Issuance | IssuePlace         |  |
|----------|--------------------|--|
| Issuance | GlobalNoteType     |  |
| Issuance | CapitalRaised      |  |
| Issuance | SubscriptionPeriod |  |
| Issuance | Minimum            |  |
| Issuance | IssuePrice         |  |
| Index    |                    |  |
| Index    | IndexRateBasis     |  |
| Index    | IndexFactor        |  |
|          |                    |  |

| Index | IndexPoints         |  |
|-------|---------------------|--|
| Index | IndexFixingDate     |  |
| Index | Identification      |  |
| Index | ReferenceSource     |  |
| Index | IndexRateCurrency   |  |
| Index | IndexRateFrequency  |  |
| Index | IndexRateMultiplier |  |
| Index | Spread              |  |
| Index | PortfolioBenchmark  |  |
| Index | VariableInterest    |  |
| Index | SecuritiesPricing   |  |
|       |                     |  |

| Future |                  | Derivative |
|--------|------------------|------------|
| Future | FutureDate       |            |
| Future | MinimumSize      |            |
| Future | UnitOfMeasure    |            |
| Future | LastDeliveryDate |            |
| Future | Standardisation  |            |
| Future | UnderlyingType   |            |
| Future | FutureRule       |            |

| Warrant              |                            | Security |
|----------------------|----------------------------|----------|
| Warrant              | SubscriptionPrice          |          |
| Warrant              | Multiplier                 |          |
| Warrant              | Style                      |          |
| Warrant              | WarrantParity              |          |
| SecuritiesConversion |                            |          |
| SecuritiesConversion | ConversionPrice            |          |
| SecuritiesConversion | ConversionDate             |          |
| SecuritiesConversion | MinimumExercisableQuantity |          |
|                      |                            |          |

| SecuritiesConversion | MinimumExercisableMultipleQuantity |  |
|----------------------|------------------------------------|--|
| SecuritiesConversion | MaximumExercisableQuantity         |  |
| SecuritiesConversion | ConversionType                     |  |
| SecuritiesConversion | ConversionPeriod                   |  |
| SecuritiesConversion | ConversionRatioDenominator         |  |
| SecuritiesConversion | ConversionRatioNumerator           |  |
| SecuritiesConversion | Ratio                              |  |
| SecuritiesConversion | ConversionUnitCurrency             |  |
| SecuritiesConversion | RelatedOption                      |  |
| SecuritiesConversion | BusinessDayConvention              |  |

| SecuritiesConversion | ConversionChoice                   |  |
|----------------------|------------------------------------|--|
| SecuritiesConversion | ConversionFixedExchangeRate        |  |
| SecuritiesConversion | ConversionMarginAmount             |  |
| SecuritiesConversion | ConversionOption                   |  |
| SecuritiesConversion | ConversionQuotedCurrency           |  |
| SecuritiesConversion | FinancialCenter                    |  |
| SecuritiesConversion | MinimumNoticeDays                  |  |
| SecuritiesConversion | NoticePeriodType                   |  |
| SecuritiesConversion | ProtectionAgainstDilutionIndicator |  |
| SecuritiesConversion | ReverseConversionIndicator         |  |
|                      |                                    |  |

| SecuritiesConversion               | SecurityIdentification |                                    |
|------------------------------------|------------------------|------------------------------------|
| SecuritiesConversion               | PartyType              |                                    |
| SecuritiesConversion               | ContractSize           |                                    |
| CashSettlementInstructionPartyRole |                        | SettlementPartyRole                |
| CashSettlementInstructionPartyRole | CashAccount            |                                    |
| CashSettlementInstructionPartyRole | SettlementInstruction  |                                    |
| SettlementInstructionSystemRole    |                        | CashSettlementInstructionPartyRole |
| SettlementInstructionSystemRole    | System                 |                                    |
| ExposureTerm                       |                        |                                    |
| ExposureTerm                       | ExposureType           |                                    |
|                                    |                        |                                    |

| ExposureTerm                  | MinimumTransferAmount      |  |
|-------------------------------|----------------------------|--|
| ExposureTerm                  | RoundingAmount             |  |
| ExposureTerm                  | RoundingMethod             |  |
| ExposureTerm                  | RelatedCollateralAgreement |  |
| ExposureTerm                  | MinimumRequirementDeposit  |  |
| StandingSettlementInstruction |                            |  |
| StandingSettlementInstruction | Settlement                 |  |
| StandingSettlementInstruction | FXStandingInstruction      |  |

| StandingSettlementInstruction | SettlementStandingInstructionDatabase |  |
|-------------------------------|---------------------------------------|--|
| StandingSettlementInstruction | Identification                        |  |
| StandingSettlementInstruction | RelatedCollateralAgreement            |  |
| StandingSettlementInstruction | SSIDatabaseName                       |  |
| StandingSettlementInstruction | SSIDatabaseProvider                   |  |
| StandingSettlementInstruction | ValidityPeriod                        |  |
| StandingSettlementInstruction | Currency                              |  |
| StandingSettlementInstruction | Asset                                 |  |
| BasicSecuritiesRegistration   |                                       |  |
| BasicSecuritiesRegistration   | Security                              |  |
| BasicSecuritiesRegistration   | RegistrationInstruction               |  |
|                               |                                       |  |

| BasicSecuritiesRegistration | CertificationIdentification   |  |
|-----------------------------|-------------------------------|--|
| BasicSecuritiesRegistration | CertificationDate             |  |
| BasicSecuritiesRegistration | SecuritiesCertificate         |  |
| BasicSecuritiesRegistration | SplitPeriod                   |  |
| SecuritiesRestriction       |                               |  |
| SecuritiesRestriction       | Security                      |  |
| SecuritiesRestriction       | LegalRestrictionType          |  |
| SecuritiesRestriction       | Jurisdiction                  |  |
| SecuritiesRestriction       | RestrictionType               |  |
| SecuritiesRestriction       | InvestorStatusRestrictionType |  |
| SecuritiesRestriction       | EffectivePeriod               |  |

| SecuritiesRestriction | Rate                 |                 |
|-----------------------|----------------------|-----------------|
| SecuritiesRestriction | InvestorType         |                 |
| SecuritiesFinancing   |                      | SecuritiesTrade |
| SecuritiesFinancing   | ReturnLegInstruction |                 |
| SecuritiesFinancing   | Type                 |                 |
| SecuritiesFinancing   | TerminationDateTime  |                 |
| SecuritiesFinancing   | RateChangeDateTime   |                 |
| SecuritiesFinancing   | RevaluationIndicator |                 |

| SecuritiesFinancing | InterestPayment                     |  |
|---------------------|-------------------------------------|--|
| SecuritiesFinancing | VariableRateSupport                 |  |
| SecuritiesFinancing | RepurchaseRate                      |  |
| SecuritiesFinancing | StockLoanMargin                     |  |
| SecuritiesFinancing | Interest                            |  |
| SecuritiesFinancing | RepurchaseSpread                    |  |
| SecuritiesFinancing | TransactionCallDelay                |  |
| SecuritiesFinancing | TotalNumberOfCollateralInstructions |  |
| SecuritiesFinancing | DealAmount                          |  |
| SecuritiesFinancing | ForfeitRepurchaseAmount             |  |
|                     |                                     |  |

| SecuritiesFinancing<br>PremiumAmount<br>SecuritiesFinancing<br>TerminationAmountPerPieceOfCollateral<br>SecuritiesFinancing<br>TerminationTransactionAmount<br>SecuritiesFinancing<br>MaturityDateModification<br>SecuritiesFinancing<br>EarliestCallBackDate<br>SecuritiesFinancing<br>OpeningSettlementDate<br>SecuritiesFinancing<br>RepurchaseType<br>SecuritiesFinancing<br>EndPrice<br>SecuritiesFinancing<br>SpreadTransaction<br>SecuritiesFinancing<br>FinancingAgreement |  |  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |

| SecuritiesFinancing | OpeningSettlementAmount     |  |
|---------------------|-----------------------------|--|
| SecuritiesFinancing | ClosingLegExecution         |  |
| SecuritiesFinancing | OpeningLegExecution         |  |
| SecuritiesFinancing | RelatedIndicationOfInterest |  |
| SecuritiesFinancing | Identification              |  |
| SecuritiesFinancing | TerminationOption           |  |
| ProceedsDefinition  |                             |  |
| ProceedsDefinition  | SpecialConcessionAmount     |  |
| ProceedsDefinition  | CreditDebitIndicator        |  |

| ProceedsDefinition | EarliestPaymentDate              |  |
|--------------------|----------------------------------|--|
| ProceedsDefinition | ValueDate                        |  |
| ProceedsDefinition | NonEligibleProceedsIndicator     |  |
| ProceedsDefinition | IssuerOfferorTaxabilityIndicator |  |
| ProceedsDefinition | OfferPriceFixingDate             |  |
| ProceedsDefinition | Option                           |  |
| ProceedsDefinition | CorporateAction                  |  |
| ProceedsDefinition | CountryOfIncomeSource            |  |

| SecuritiesBalance |                                     | Balance |
|-------------------|-------------------------------------|---------|
| SecuritiesBalance | NetGainLoss                         |         |
| SecuritiesBalance | SecuritiesAccount                   |         |
| SecuritiesBalance | EligibleBalanceRelatedEntitlement   |         |
| SecuritiesBalance | ShortLong                           |         |
| SecuritiesBalance | AggregateQuantity                   |         |
| SecuritiesBalance | CorporateActionEntitlement          |         |
| SecuritiesBalance | InstructedBalanceRelatedEntitlement |         |
|                   |                                     |         |

| SecuritiesBalance | UninstructedBalanceRelatedEntitlement |  |
|-------------------|---------------------------------------|--|
| SecuritiesBalance | MainSecuritiesBalance                 |  |
| SecuritiesBalance | SecuritiesSubBalance                  |  |
| SecuritiesBalance | SecuritiesBalanceType                 |  |
| SecuritiesBalance | SubBalanceQuantity                    |  |
| SecuritiesBalance | Security                              |  |
| SecuritiesBalance | ExchangeRate                          |  |
| SecuritiesBalance | AvailabilityIndicator                 |  |
| SecuritiesBalance | AvailableQuantity                     |  |

| SecuritiesBalance | RelatedMeetingEntitlement            |  |
|-------------------|--------------------------------------|--|
| SecuritiesBalance | UnavailableQuantity                  |  |
| SecuritiesBalance | SafekeepingPlace                     |  |
| SecuritiesBalance | SecuritiesEntry                      |  |
| SecuritiesBalance | NotEligibleBalanceRelatedEntitlement |  |
| SecuritiesBalance | RelatedIntraPositionTransfer         |  |
| SecuritiesBalance | CostAdjustment                       |  |
| SecuritiesBalance | Pledgee                              |  |
| Collateral        |                                      |  |
| Collateral        | CollateralAmount                     |  |
| Collateral        | Valuation                            |  |
|                   |                                      |  |

| Collateral | CollateralType              |  |
|------------|-----------------------------|--|
| Collateral | BaseCurrencyAmount          |  |
| Collateral | CollateralPurpose           |  |
| Collateral | CollateralBalance           |  |
| Collateral | CollateralAccount           |  |
| Collateral | CollateralManagement        |  |
| Collateral | CollateralPartyRole         |  |
| Collateral | Status                      |  |
| Collateral | AssetHolding                |  |
| Collateral | VariationMarginAssetHolding |  |

| Collateral    | SegregatedIndependentAmountAssetHolding |                     |
|---------------|-----------------------------------------|---------------------|
| Collateral    | CollateralAgreement                     |                     |
| Collateral    | CollateralOwnership                     |                     |
| Collateral    | RelatedCollateralSubstitution           |                     |
| Collateral    | CollateralDeliveryMethod                |                     |
| Collateral    | CollateralQualityType                   |                     |
| Collateral    | DeliveryByValue                         |                     |
| Collateral    | CollateralReinvestment                  |                     |
| Collateral    | CollateralTransactionType               |                     |
| RegistrarRole |                                         | SecuritiesPartyRole |

| RegistrarRole               | RegistrarAccount                          |                |
|-----------------------------|-------------------------------------------|----------------|
| RegistrarRole               | RegisterName                              |                |
| IssuerRole                  |                                           | AssetPartyRole |
| CorporateActionNotification |                                           |                |
| CorporateActionNotification | RelatedServicing                          |                |
| CorporateActionNotification | CorporateActionNotificationIdentification |                |
| CorporateActionNotification | NotificationType                          |                |
| CorporateActionNotification | CreationDateTime                          |                |
| CorporateActionStatusReason |                                           | StatusReason   |
| CorporateActionStatusReason | CorporateActionCancellationReason         |                |
| CorporateActionStatusReason | CorporateActionStatus                     |                |
| CorporateActionStatusReason | AcceptedReason                            |                |
| CorporateActionStatusReason | ReversalReason                            |                |
|                             |                                           |                |

| CorporateActionStatusReason | MovementFailureReason       |  |
|-----------------------------|-----------------------------|--|
| CorporateActionStatusReason | MovementRejectionReason     |  |
| CorporateActionEvent        |                             |  |
| CorporateActionEvent        | Type                        |  |
| CorporateActionEvent        | MandatoryVoluntaryEventType |  |
| CorporateActionEvent        | UnderlyingSecurity          |  |
| CorporateActionEvent        | CorporateActionPrice        |  |
| CorporateActionEvent        | ExchangeRate                |  |
| CorporateActionEvent        | RegistrationDetails         |  |
| CorporateActionEvent        | BasketOrIndexInformation    |  |
| CorporateActionEvent        | Deadline                    |  |
|                             |                             |  |

| CorporateActionEvent | AdditionalBusinessProcess |  |
|----------------------|---------------------------|--|
| CorporateActionEvent | TradingDate               |  |
| CorporateActionEvent | CorporateActionCharge     |  |
| CorporateActionEvent | PariPassuDate             |  |
| CorporateActionEvent | InformationConditions     |  |
| CorporateActionEvent | FractionalQuantity        |  |
| CorporateActionEvent | EventProcessingType       |  |
| CorporateActionEvent | CorporateActionStatus     |  |
| CorporateActionEvent | AnnouncementDate          |  |
|                      |                           |  |

| CorporateActionEvent | EffectiveDate                  |  |
|----------------------|--------------------------------|--|
| CorporateActionEvent | FurtherDetailsAnnouncementDate |  |
| CorporateActionEvent | MarginFixingDate               |  |
| CorporateActionEvent | ResultPublicationDate          |  |
| CorporateActionEvent | UnconditionalDate              |  |
| CorporateActionEvent | WhollyUnconditionalDate        |  |
| CorporateActionEvent | LapsedDate                     |  |
| CorporateActionEvent | BookClosurePeriod              |  |
| CorporateActionEvent | SecuritiesQuantity             |  |
|                      |                                |  |

| CorporateActionEvent | RestrictionIndicator     |
|----------------------|--------------------------|
| CorporateActionEvent | EventStage               |
| CorporateActionEvent | DocumentationLocation    |
| CorporateActionEvent | SecuritiesQuantitySought |
| CorporateActionEvent | PartialElectionIndicator |
| CorporateActionEvent | CorporateActionPartyRole |
| CorporateActionEvent | MarketClaim              |

| CorporateActionEvent | BiddingConditions                | Specifies the conditions under<br>which securities can be acquired<br>BiddingConditions<br>as part of a corporate action.                                                                                         |
|----------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CorporateActionEvent | RelatedClassAction               | Specifies the underlying class<br>ClassAction<br>action related to the event.                                                                                                                                     |
| CorporateActionEvent | CorporateActionEventRegistration | Official registration of the event.<br>CorporateActionEventRegistration                                                                                                                                           |
| CorporateActionEvent | SuspensionPeriod                 | Period defining the last date for<br>which an action will be accepted<br>and the date on which the<br>SuspensionPeriod<br>suspension will be released and<br>normal processing will resume.                       |
| CorporateActionEvent | Lottery                          | Organisation of draws for cash<br>prizes on bonds (instead of<br>coupon payments). Every issued<br>Lottery<br>bond (similar to a lottery ticket)<br>has an equal opportunity at<br>winning payments in the draws. |
| CorporateActionEvent | MarginType                       | Specifies the margin type for a<br>RemarketingMarginTypeCode<br>remarketing procedure.                                                                                                                            |
| CorporateActionEvent | RelatedMeeting                   | Provides information on the<br>meeting related to the corporate<br>Meeting<br>event.                                                                                                                              |
| CorporateActionEvent | Services                         | Specifies the different services<br>linked to a corporate action<br>CorporateActionServicing<br>event.                                                                                                            |
| CorporateActionEvent | Issuance                         | Information specified when the<br>corporate event relates to the<br>Issuance<br>issuance of securities.                                                                                                           |
| CorporateActionEvent | SecuritiesModification           | Modification of the reference data<br>of a security or of the<br>SecuritiesModification<br>organisation that issued it.                                                                                           |

| CorporateActionEvent<br>TradingPeriod<br>CorporateActionEvent<br>TransactionTax<br>CorporateActionEvent<br>ConsentType<br>CorporateActionEvent<br>ProceedsDefinition<br>CorporateActionEvent<br>TaxOnNonDistributedProceedsIndicator<br>ClassAction<br>ClassAction<br>ClassActionNumber<br>ClassAction<br>LeadPlaintiffDeadline<br>ClassAction<br>CourtApprovalDate |  |  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                                                                                     |  |  |

| ClassAction                | ClaimPeriod         |  |
|----------------------------|---------------------|--|
| ClassAction                | FilingDate          |  |
| ClassAction                | HearingDate         |  |
| ClassAction                | CorporateEvent      |  |
| CorporateActionEntitlement |                     |  |
| CorporateActionEntitlement | EligibleBalance     |  |
| CorporateActionEntitlement | SecuritiesBalance   |  |
| CorporateActionEntitlement | InstructedBalance   |  |
| CorporateActionEntitlement | UninstructedBalance |  |
|                            |                     |  |

| CorporateActionEntitlement | EligibleBalanceIndicator |                     |
|----------------------------|--------------------------|---------------------|
| CorporateActionEntitlement | RelatedServicing         |                     |
| CorporateActionEntitlement | NotEligibleBalance       |                     |
| BeneficialOwner            |                          | SecuritiesPartyRole |
| BeneficialOwner            | CertificationType        |                     |
| BeneficialOwner            | NonDomicileCountry       |                     |
| BeneficialOwner            | CertificationIndicator   |                     |

| BeneficialOwner       | CertificationFormat             |  |
|-----------------------|---------------------------------|--|
| BeneficialOwner       | ERISAEligibility                |  |
| BeneficialOwner       | ERISARate                       |  |
| BeneficialOwner       | BenefitPlanDeclarationIndicator |  |
| CorporateActionOption |                                 |  |
| CorporateActionOption | OptionNumber                    |  |
| CorporateActionOption | OptionType                      |  |
| CorporateActionOption | FractionDisposition             |  |
| CorporateActionOption | CurrencyOption                  |  |
|                       |                                 |  |

| CorporateActionOption | RelatedChoiceCorporateAction   |  |
|-----------------------|--------------------------------|--|
| CorporateActionOption | CorporateActionElection        |  |
| CorporateActionOption | OptionFeatures                 |  |
| CorporateActionOption | ActionPeriod                   |  |
| CorporateActionOption | OfferType                      |  |
| CorporateActionOption | ChargesAppliedIndicator        |  |
| CorporateActionOption | WithdrawalAllowedIndicator     |  |
| CorporateActionOption | ChangeAllowedIndicator         |  |
| CorporateActionOption | CorporateActionOptionServicing |  |
| CorporateActionOption | ProceedsDefinition             |  |
| CorporateActionOption | Distribution                   |  |
| CorporateActionOption | Default                        |  |

| SecuritiesModification<br>ChangeType<br>SecuritiesModification<br>NewOrganisationInformation<br>SecuritiesModification<br>RelatedCorporateEvent<br>SecuritiesModification<br>NewSecurityReferenceData<br>SecuritiesModification<br>NumberOfSharesIssued<br>SecuritiesModification<br>LastTradingDate<br>SecuritiesProceedsDefinition<br>ProceedsDefinition<br>SecuritiesProceedsDefinition<br>SecuritiesQuantity | SecuritiesModification |  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                  |                        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |                        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |                        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |                        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |                        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |                        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |                        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |                        |  |

| SecuritiesProceedsDefinition | ConditionalQuantity                                |  |
|------------------------------|----------------------------------------------------|--|
| SecuritiesProceedsDefinition | OverAndAboveNormalEnsuredEntitlementQuantity       |  |
| SecuritiesProceedsDefinition | QuantityToReceive                                  |  |
| SecuritiesProceedsDefinition | StatusQuantity                                     |  |
| SecuritiesProceedsDefinition | ParallelTradingPeriod                              |  |
| SecuritiesProceedsDefinition | AdditionalQuantityForSubscribedResultantSecurities |  |
| SecuritiesProceedsDefinition | AdditionalQuantityForExistingSecurities            |  |

| SecuritiesProceedsDefinition | NewToOld                                |  |
|------------------------------|-----------------------------------------|--|
| SecuritiesProceedsDefinition | NewSecuritiesToUnderlyingSecurities     |  |
| SecuritiesProceedsDefinition | ReinvestmentAmount                      |  |
| SecuritiesProceedsDefinition | IntermediateSecuritiesDistributionType  |  |
| SecuritiesProceedsDefinition | BoardLotSecuritiesQuantity              |  |
| SecuritiesProceedsDefinition | NewDenominationSecuritiesQuantity       |  |
| SecuritiesProceedsDefinition | IntermediateSecuritiesToUnderlyingRatio |  |
| SecuritiesProceedsDefinition | ReinvestmentDiscountToMarket            |  |
|                              |                                         |  |

| SecuritiesProceedsDefinition | RedemptionDate             |  |
|------------------------------|----------------------------|--|
| SecuritiesProceedsDefinition | AssentedLinePeriod         |  |
| SecuritiesProceedsDefinition | SellThruIssuerPeriod       |  |
| SecuritiesProceedsDefinition | ShareRanking               |  |
| CorporateActionElection      |                            |  |
| CorporateActionElection      | ExecutionRequestedDateTime |  |
| CorporateActionElection      | Option                     |  |
| CorporateActionElection      | CashAccount                |  |
| CorporateActionElection      | ElectionType               |  |

| CorporateActionElection | Quantity                        |                          |
|-------------------------|---------------------------------|--------------------------|
| CorporateActionElection | AmendmentReason                 |                          |
| CorporateActionElection | RelatedServicing                |                          |
| CorporateActionElection | ProtectProcess                  |                          |
| ChoiceCorporateAction   |                                 | MandatoryCorporateAction |
| ChoiceCorporateAction   | CorporateActionOptionDefinition |                          |
| BiddingConditions       |                                 |                          |
| BiddingConditions       | ProposedRate                    |                          |
| BiddingConditions       | OversubscriptionRate            |                          |
| BiddingConditions       | InformationToComplyWith         |                          |
|                         |                                 |                          |

| BiddingConditions | SubscriptionCostDebitDate      |  |
|-------------------|--------------------------------|--|
| BiddingConditions | MaximumAllowedOverSubscription |  |
| BiddingConditions | ProrationRate                  |  |
| BiddingConditions | ApplicableRate                 |  |
| BiddingConditions | FrontEndOddLotQuantity         |  |
| BiddingConditions | BackEndOddLotQuantity          |  |
| BiddingConditions | TransformationRate             |  |

| BiddingConditions | ProrationDate            |  |
|-------------------|--------------------------|--|
| BiddingConditions | CompulsoryPurchasePeriod |  |
| BiddingConditions | PercentageSought         |  |
| BiddingConditions | BidInterval              |  |
| BiddingConditions | MaximumPrice             |  |
| BiddingConditions | MinimumPrice             |  |
| BiddingConditions | MaximumQuantity          |  |
| BiddingConditions | MinimumQuantitySought    |  |

| BiddingConditions | BaseDenomination           |  |
|-------------------|----------------------------|--|
| BiddingConditions | CalculationMethod          |  |
| BiddingConditions | AdditionalSubscriptionCost |  |
| BiddingConditions | Event                      |  |
| TaxVoucher        |                            |  |
| TaxVoucher        | RequestedTaxationRate      |  |
| TaxVoucher        | CreditRate                 |  |
| TaxVoucher        | RelatedSecurityTax         |  |
|                   |                            |  |

| TaxVoucher | SundryOrOtherAmount      |  |
|------------|--------------------------|--|
| TaxVoucher | CreditAmount             |  |
| TaxVoucher | CashAmountBroughtForward |  |
| TaxVoucher | CashAmountCarriedForward |  |
| TaxVoucher | NotionalTaxAmount        |  |
| TaxVoucher | Distribution             |  |
| TaxVoucher | Identification           |  |
| TaxVoucher | BargainDate              |  |
| TaxVoucher | BargainSettlementDate    |  |
| TaxVoucher | TaxVoucherRate           |  |
| TaxVoucher | RecordDateHolding        |  |
|            |                          |  |

| TaxVoucher           | ScripDividendReinvestmentPricePerShare |  |
|----------------------|----------------------------------------|--|
| TaxVoucher           | AllotedSharesCost                      |  |
| TaxVoucher           | ForeignExchangeTransaction             |  |
| CorporateActionPrice |                                        |  |
| CorporateActionPrice | CorporateActionEvent                   |  |
| CorporateActionPrice | CorporateActionExercisePrice           |  |
| CorporateActionPrice | GenericCashPriceReceivedPerProduct     |  |
| CorporateActionPrice | GenericCashPricePaidPerProduct         |  |

| CorporateActionPrice | CashInLieuOfSharePrice        |  |
|----------------------|-------------------------------|--|
| CorporateActionPrice | OverSubscriptionDepositPrice  |  |
| CorporateActionPrice | CashValueForTax               |  |
| CorporateActionPrice | PricingCalculation            |  |
| CorporateActionPrice | MinimumMultipleCashToInstruct |  |
| CorporateActionPrice | MaximumCashToInstruct         |  |
| CorporateActionPrice | MinimumCashToInstruct         |  |
| AmountAndQuantity    |                               |  |
| AmountAndQuantity    | SecuritiesPricing             |  |
| AmountAndQuantity    | Amount                        |  |
| AmountAndQuantity    | Quantity                      |  |
| AmountRatio          |                               |  |
|                      |                               |  |

| AmountRatio              | SecuritiesPricing                |                  |
|--------------------------|----------------------------------|------------------|
| AmountRatio              | Amount1                          |                  |
| AmountRatio              | Amount2                          |                  |
| CorporateActionServicing |                                  | FinancialService |
| CorporateActionServicing | SecuritiesAccount                |                  |
| CorporateActionServicing | CorporateActionEventNotification |                  |
| CorporateActionServicing | CorporateActionDistribution      |                  |
| CorporateActionServicing | CorporateActionOptionServicing   |                  |
| CorporateActionServicing | Event                            |                  |
| CorporateActionServicing | CorporateActionElection          |                  |
| CorporateActionServicing | CorporateActionEntitlement       |                  |
|                          |                                  |                  |

| CorporateActionProceedsDeliveryInstruction |                                    | Specifies the delivery instructions<br>for the securities and cash<br>proceeds at any stage of the<br>Corporate Action process. |
|--------------------------------------------|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| CorporateActionProceedsDeliveryInstruction | RelatedDistribution                | Parameters of the distribution of<br>the proceeds of a CA event.                                                                |
| CorporateActionProceedsDeliveryInstruction | SecuritiesProceedsMovement         | Instructions for the movement of<br>securities related to a corporate<br>SecuritiesDeliveryObligation<br>action.                |
| CorporateActionProceedsDeliveryInstruction | CashProceedsMovement               | Instructions for the movement of<br>cash related to a corporate<br>PaymentObligation<br>action.                                 |
| CorporateActionProceedsDeliveryInstruction | SettlementAccount                  | Information relative to the<br>account(s) to be used for the<br>Account<br>delivery of the proceeds (cash or<br>securities)     |
| CorporateActionProceedsDeliveryInstruction | CorporateActionStandingInstruction | Standing instruction related to a<br>corporate action.                                                                          |
| Deadline                                   |                                    | Specifies the different deadlines<br>available for the different<br>processes related to corporate<br>action processes.         |
| Deadline                                   | RelatedCorporateActionEvent        | Related corporate action event.<br>CorporateActionEvent                                                                         |
| Deadline                                   | MarketDeadline                     | Date by which the action should<br>have been completed. This<br>ISODateTime<br>deadline is set by the issuer.                   |
| Deadline                                   | IntermediaryDeadline               | Date by which the action should<br>have been completed. This<br>ISODateTime<br>deadline is set by an<br>intermediary.           |

| Deadline                      | STPDeadline              |         |
|-------------------------------|--------------------------|---------|
| Deadline                      | RelatedMeeting           |         |
| CorporateActionFeesAndCharges |                          | Charges |
| CorporateActionFeesAndCharges | CorporateAction          |         |
| CorporateActionFeesAndCharges | SolicitationFee          |         |
| CorporateActionFeesAndCharges | EarlySolicitationFeeRate |         |
| CorporateActionFeesAndCharges | Commission               |         |
| RateAndAmount                 |                          |         |
| RateAndAmount                 | FinalDividendParameters  |         |
|                               |                          |         |

| RateAndAmount<br>GrossDividendParameters<br>RateAndAmount<br>Amount<br>RateAndAmount<br>Index<br>RateAndAmount<br>NetDividendParameters<br>RateAndAmount<br>MaximumAllowedBiddingConditions<br>RateAndAmount<br>ProvisionalDividendParameters<br>RateAndAmount<br>SolicitationFeeCorporateActionParameters<br>RateAndAmount<br>Rate<br>RateAndAmount<br>RateBiddingConditions<br>RateAndAmount<br>SecuritiesTax<br>RateAndAmount<br>EarlySolicitationFeeCorporateActionParameters<br>RateAndAmount<br>InterestRelatedIssuance | RateAndAmount | FullyFrankedRateAndAmountDividendParameters |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|---------------------------------------------|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |               |                                             |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |               |                                             |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |               |                                             |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |               |                                             |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |               |                                             |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |               |                                             |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |               |                                             |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |               |                                             |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |               |                                             |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |               |                                             |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |               |                                             |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |               |                                             |  |

| RateAndAmount          | LossRelatedIssuance                          |                    |
|------------------------|----------------------------------------------|--------------------|
| RateAndAmount          | AbsoluteValue                                |                    |
| RateAndAmount          | Operator                                     |                    |
| RateAndAmount          | RelatedYieldCalculation                      |                    |
| RateAndAmount          | ConduitForeignIncomeAmountDividendParameters |                    |
| RateAndAmount          | DeemedAmountDividendParameters               |                    |
| CashProceedsDefinition |                                              | ProceedsDefinition |
| CashProceedsDefinition | CashIncentiveRate                            |                    |
| CashProceedsDefinition | ContractualPaymentIndicator                  |                    |
|                        |                                              |                    |

| CashProceedsDefinition | IncomeType              |  |
|------------------------|-------------------------|--|
| CashProceedsDefinition | IndemnityAmount         |  |
| CashProceedsDefinition | CashIncentiveAmount     |  |
| CashProceedsDefinition | PrincipalOrCorpus       |  |
| CashProceedsDefinition | RedemptionPremiumAmount |  |
| CashProceedsDefinition | IncomePortion           |  |
| CashProceedsDefinition | Interest                |  |
| CashProceedsDefinition | Amount                  |  |
|                        |                         |  |

| CashProceedsDefinition      | Dividend         |  |
|-----------------------------|------------------|--|
| CashProceedsDefinition      | PaymentCurrency  |  |
| CashProceedsDefinition      | StatusCashAmount |  |
| CorporateActionDistribution |                  |  |
| CorporateActionDistribution | PostingQuantity  |  |
| CorporateActionDistribution | PostingDateTime  |  |
| CorporateActionDistribution | MovementDate     |  |
| CorporateActionDistribution | PostingAmount    |  |
| CorporateActionDistribution | TaxVoucher       |  |
| CorporateActionDistribution | RelatedServicing |  |
|                             |                  |  |

| CorporateActionDistribution | OrderType                                  |  |
|-----------------------------|--------------------------------------------|--|
| CorporateActionDistribution | MovementType                               |  |
| CorporateActionDistribution | HighPriorityIndicator                      |  |
| CorporateActionDistribution | RequestedExecutionDate                     |  |
| CorporateActionDistribution | FractionTreatment                          |  |
| CorporateActionDistribution | CreditDebitIndicator                       |  |
| CorporateActionDistribution | Option                                     |  |
| CorporateActionDistribution | NetAmount                                  |  |
| CorporateActionDistribution | GrossAmount                                |  |
| CorporateActionDistribution | FinancialTransaction                       |  |
| CorporateActionDistribution | CorporateActionProceedsDeliveryInstruction |  |
| QuantityRatio               |                                            |  |
|                             |                                            |  |

| QuantityRatio                  | AdditionalQuantityForResultantSecuritiesProceedsDefinition  |                            |
|--------------------------------|-------------------------------------------------------------|----------------------------|
| QuantityRatio                  | Quantity1                                                   |                            |
| QuantityRatio                  | Quantity2                                                   |                            |
| QuantityRatio                  | AdditionalQuantityForSubscribedSecuritiesProceedsDefinition |                            |
| QuantityRatio                  | NewToOldProceedsDefinition                                  |                            |
| QuantityRatio                  | NewToUnderlyingProceedsDefinition                           |                            |
| QuantityRatio                  | IntermediateSecuritiesProceedsDefinition                    |                            |
| QuantityRatio                  | Warrant                                                     |                            |
| CorporateActionCashEntitlement |                                                             | CorporateActionEntitlement |
| CorporateActionCashEntitlement | GrossCashAmount                                             |                            |
|                                |                                                             |                            |

| CorporateActionCashEntitlement | NetCashAmount              |  |
|--------------------------------|----------------------------|--|
| CorporateActionCashEntitlement | CashInLieuOfShare          |  |
| CorporateActionCashEntitlement | CapitalGain                |  |
| CorporateActionCashEntitlement | EntitledCashAmount         |  |
| CorporateActionCashEntitlement | ExchangeRate               |  |
| MarketClaim                    |                            |  |
| MarketClaim                    | MarketClaimAmount          |  |
| MarketClaim                    | MarketClaimTrackingEndDate |  |

| MarketClaim     | RelatedCorporateEvent |  |
|-----------------|-----------------------|--|
| FixingCondition |                       |  |
| FixingCondition | FixingDateTime        |  |
| FixingCondition | NonDeliverableTrade   |  |
| FixingCondition | FixingRate            |  |
| FixingCondition | SettlementRateOption  |  |
| FixingCondition | FinancialCenter       |  |
| FixingCondition | DisruptionFallback    |  |
| FixingCondition | BusinessDayConvention |  |
|                 |                       |  |

| Equalisation |                                  |  |
|--------------|----------------------------------|--|
| Equalisation | Amount                           |  |
| Equalisation | Date                             |  |
| Equalisation | Rate                             |  |
| Equalisation | RelatedInvestmentFundTransaction |  |
| Equalisation | CreditDebitIndicator             |  |
| Equalisation | DepreciationDepositPerUnit       |  |

| Equalisation | CreditPerUnit   |  |
|--------------|-----------------|--|
| Equalisation | MethodologyType |  |
| Equalisation | HighWatermark   |  |
| Equalisation | GrossAssetValue |  |

| Equalisation     | ContingentLiquidationPerUnit                   |  |
|------------------|------------------------------------------------|--|
| SuspensionPeriod |                                                |  |
| SuspensionPeriod | PrivilegeSuspensionPeriod                      |  |
| SuspensionPeriod | DepositorySuspensionPeriodForWithdrawal        |  |
| SuspensionPeriod | DepositorySuspensionPeriodForBookEntryTransfer |  |

| SuspensionPeriod | DepositorySuspensionPeriodForDepositAtAgent    |  |
|------------------|------------------------------------------------|--|
| SuspensionPeriod | DepositorySuspensionPeriodForDeposit           |  |
| SuspensionPeriod | DepositorySuspensionPeriodForPledge            |  |
| SuspensionPeriod | DepositorySuspensionPeriodForSegregation       |  |
| SuspensionPeriod | DepositorySuspensionPeriodForWithdrawalAtAgent |  |

| SuspensionPeriod                     | DepositorySuspensionPeriodForWithdrawalInNomineeName |                            |
|--------------------------------------|------------------------------------------------------|----------------------------|
| SuspensionPeriod                     | DepositorySuspensionPeriodForWithdrawalInStreetName  |                            |
| SuspensionPeriod                     | CoDepositoriesSuspensionPeriod                       |                            |
| SuspensionPeriod                     | CorporateActionEvent                                 |                            |
| CorporateActionSecuritiesEntitlement |                                                      | CorporateActionEntitlement |
| CorporateActionSecuritiesEntitlement | EntitledSecuritiesQuantity                           |                            |

| CorporateActionSecuritiesEntitlement | RenounceableEntitlementStatusType |  |
|--------------------------------------|-----------------------------------|--|
| Lottery                              |                                   |  |
| Lottery                              | LotteryDate                       |  |
| Lottery                              | IncrementalDenomination           |  |
| Lottery                              | LotteryType                       |  |
| Lottery                              | RelatedCorporateEvent             |  |
| Meeting                              |                                   |  |
| Meeting                              | DateAndTime                       |  |
| Meeting                              | DateStatus                        |  |
| Meeting                              | MeetingLocation                   |  |

| Meeting | Identification     |  |
|---------|--------------------|--|
| Meeting | Deadline           |  |
| Meeting | MeetingServicing   |  |
| Meeting | Person             |  |
| Meeting | PartyRole          |  |
| Meeting | Status             |  |
| Meeting | CorporateEvent     |  |
| Meeting | Quorum             |  |
| Meeting | VotingCondition    |  |
| Meeting | AttendanceRequired |  |

| Meeting | AttendanceConfirmation       |  |
|---------|------------------------------|--|
| Meeting | IncentivePremium             |  |
| Meeting | Participation                |  |
| Meeting | ResolutionProposalConditions |  |
| Meeting | AgendaItem                   |  |
| Meeting | ProxyAppointmentConditions   |  |
| Meeting | AdditionalRight              |  |
| Meeting | Type                         |  |
| Meeting | PowerOfAttorneyRequirements  |  |
| Meeting | MeetingEventClassification   |  |

| Meeting                    | AttendanceAdmissionConditions |          |
|----------------------------|-------------------------------|----------|
| SecuritiesBlockingDeadline |                               | Deadline |
| SecuritiesBlockingDeadline | BlockingPeriod                |          |
| Spread                     |                               |          |
| Spread                     | BenchmarkSecurity             |          |
| Spread                     | SecuritiesFinancing           |          |
| Spread                     | SpreadRate                    |          |
| Spread                     | BasisPointSpread              |          |
| Spread                     | Index                         |          |
| Spread                     | BenchmarkPrice                |          |
| Spread                     | RelatedIndicationOfInterest   |          |
|                            |                               |          |

| Spread                | IndicationOfInterest |                      |
|-----------------------|----------------------|----------------------|
| Spread                | RelatedInterest      |                      |
| Spread                | BenchmarkCurve       |                      |
| Spread                | PriceOffset          |                      |
| IntraPositionTransfer |                      | SecuritiesTransfer   |
| IntraPositionTransfer | Reservation          |                      |
| IntraPositionTransfer | CollateralAmount     |                      |
| IntraPositionTransfer | SecuritiesBalance    |                      |
|                       |                      |                      |
| SourceOfPrice         |                      | InformationPartyRole |

| SourceOfPrice    | Type               |       |
|------------------|--------------------|-------|
| HaircutValuation |                    |       |
| HaircutValuation | AssetHolding       |       |
| HaircutValuation | Haircut            |       |
| HaircutValuation | Sign               |       |
| HaircutValuation | PartyRole          |       |
| SecuritiesOrder  |                    | Order |
| SecuritiesOrder  | OrderEffectiveDate |       |
| SecuritiesOrder  | OrderExpiryDate    |       |
| SecuritiesOrder  | Identification     |       |
|                  |                    |       |

| SecuritiesOrder | CashMargin       |  |
|-----------------|------------------|--|
| SecuritiesOrder | Side             |  |
| SecuritiesOrder | SolicitedOrder   |  |
| SecuritiesOrder | CustomerCapacity |  |
| SecuritiesOrder | PositionEffect   |  |

| SecuritiesOrder<br>SettlementCurrency<br>SecuritiesOrder<br>OrderOriginatorEligibility<br>SecuritiesOrder<br>OrderedQuantity<br>SecuritiesOrder<br>BusinessProcessType<br>SecuritiesOrder<br>PlaceOfTrade<br>SecuritiesOrder<br>OrderedAmount<br>SecuritiesOrder<br>GiveUpNumberOfDays<br>SecuritiesOrder<br>TradeRegulatoryConditionsType | SecuritiesOrder | ForeignExchangeExecutionRequested |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-----------------------------------|--|
|                                                                                                                                                                                                                                                                                                                                            |                 |                                   |  |
|                                                                                                                                                                                                                                                                                                                                            |                 |                                   |  |
|                                                                                                                                                                                                                                                                                                                                            |                 |                                   |  |
|                                                                                                                                                                                                                                                                                                                                            |                 |                                   |  |
|                                                                                                                                                                                                                                                                                                                                            |                 |                                   |  |
|                                                                                                                                                                                                                                                                                                                                            |                 |                                   |  |
|                                                                                                                                                                                                                                                                                                                                            |                 |                                   |  |
|                                                                                                                                                                                                                                                                                                                                            |                 |                                   |  |

| SecuritiesOrder | DayOrderQuantity          | For good till orders, the order<br>quantity less all quantity<br>SecuritiesQuantity<br>PreviousDayOrder<br>(adjusted for stock splits) that<br>traded on previous days. |
|-----------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SecuritiesOrder | SecuritiesOrderPartyRole  | Specifies the party which plays a<br>role in the process of ordering<br>SecuritiesOrderPartyRole<br>SecuritiesOrder<br>securities.                                      |
| SecuritiesOrder | Status                    | Indicates the status of an order<br>SecuritiesOrderStatus<br>SecuritiesOrder<br>at a specific point in time.                                                            |
| SecuritiesOrder | RelatedNegotiation        | Negotiation which resulted in an<br>Negotiation<br>SecuritiesOrder<br>order.                                                                                            |
| SecuritiesOrder | Adjustments               | Charges and commissions<br>associated with a securities<br>Adjustment<br>SecuritiesOrder<br>order.                                                                      |
| SecuritiesOrder | LegalParameters           | Legal parameters required in a<br>securities order for regulatory<br>SecuritiesRegulatoryDetails<br>RelatedOrder<br>purposes.                                           |
| SecuritiesOrder | OrderPrice                | Indicates the requested price for<br>the order. This can be a "stop"<br>SecuritiesPricing<br>Order<br>price a "limit" price or a "deal"<br>price.                       |
| SecuritiesOrder | StopPrice                 | Indicates the stop price in case<br>of a stop order or a stop limit<br>SecuritiesPricing<br>StopPriceOrder<br>order.                                                    |
| SecuritiesOrder | SecuritiesOrderAllocation | Information about the pre<br>Allocation<br>SecuritiesOrder<br>allocation of an order.                                                                                   |
| SecuritiesOrder | OrderExecutionParameters  | Conditions under which a<br>securities order must be<br>SecuritiesOrderParameters<br>RelatedSecuritiesOrder<br>executed.                                                |
| SecuritiesOrder | OrderExecution            | Result of a securities order.<br>SecuritiesTrade<br>RelatedOrder                                                                                                        |

| SecuritiesOrder | OrderingAccount                   |  |
|-----------------|-----------------------------------|--|
| SecuritiesOrder | Quote                             |  |
| SecuritiesOrder | FundTransactionDirectionIndicator |  |
| SecuritiesOrder | OrderDate                         |  |
| SecuritiesOrder | PegDifference                     |  |
| SecuritiesOrder | SecuritiesOrderTradingSession     |  |
| SecuritiesOrder | RelatedOrderBook                  |  |
| SecuritiesOrder | ListTrading                       |  |
| SecuritiesOrder | BuySideRelatedCrossTrade          |  |
| SecuritiesOrder | SellSideRelatedCrossTrade         |  |
| SecuritiesOrder | OrderedSecurity                   |  |
| SecuritiesOrder | BookingInstructions               |  |
|                 |                                   |  |

| SecuritiesOrder | ExchangeForPhysicalTrade   |  |
|-----------------|----------------------------|--|
| SecuritiesOrder | QuantityType               |  |
| SecuritiesOrder | ClientOrderIdentification  |  |
| SecuritiesOrder | ExecutionInstructions      |  |
| SecuritiesOrder | Type                       |  |
| SecuritiesOrder | LiquidityProvisionActivity |  |
| SecuritiesOrder | EventType                  |  |

| SecuritiesOrder | PegPrice            |  |
|-----------------|---------------------|--|
| SecuritiesOrder | LimitPrice          |  |
| ListTrading     |                     |  |
| ListTrading     | ListIdentification  |  |
| ListTrading     | SecuritiesListOrder |  |
| ListTrading     | ListTradingSession  |  |

| ListTrading | ListName               |  |
|-------------|------------------------|--|
| ListTrading | BasisPriceType         |  |
| ListTrading | StrikeTime             |  |
| ListTrading | GrossAmountIndicator   |  |
| ListTrading | SellSideIdentification |  |
| ListTrading | BuySideIdentification  |  |
| ListTrading | Liquidity              |  |
| ListTrading | BidType                |  |
|             |                        |  |

| Clearing                 |                            | ObligationFulfilment |
|--------------------------|----------------------------|----------------------|
| Clearing                 | ClearingThresholdIndicator |                      |
| Clearing                 | ClearedIdentification      |                      |
| Clearing                 | GuaranteedTrade            |                      |
| Clearing                 | TradePostingType           |                      |
| Clearing                 | ClearingSystem             |                      |
| SecuritiesTradePartyRole |                            | TradePartyRole       |
| SecuritiesTradePartyRole | SecuritiesTrade            |                      |
|                          |                            |                      |

| AffirmingPartyRole |                    | SecuritiesTradePartyRole |
|--------------------|--------------------|--------------------------|
| BuyerRole          |                    | TradePartyRole           |
| Borrower           |                    | TradePartyRole           |
| SellerRole         |                    | TradePartyRole           |
| Lender             |                    | TradePartyRole           |
| TradingSession     |                    |                          |
| TradingSession     | TradingSessionName |                          |
| TradingSession     | TimeBracket        |                          |
| TradingSession     | Market             |                          |
| TradingSession     | Quote              |                          |

| TradingSession  | SecuritiesOrder         |                |
|-----------------|-------------------------|----------------|
| TradingSession  | TradingSessionIndicator |                |
| TradingSession  | TradingSessionPhase     |                |
| TradingSession  | USFuturesTradingSession |                |
| TradingSession  | ListTrading             |                |
| TradeRegulator  |                         | TradePartyRole |
| PrePaymentSpeed |                         |                |
| PrePaymentSpeed | Type                    |                |

| PrePaymentSpeed  | Rate                 |  |
|------------------|----------------------|--|
| YieldCalculation |                      |  |
| YieldCalculation | RedemptionPrice      |  |
| YieldCalculation | Value                |  |
| YieldCalculation | CalculationType      |  |
| YieldCalculation | ValueDate            |  |
| YieldCalculation | ValuePeriod          |  |
| YieldCalculation | YieldCalculationDate |  |
| YieldCalculation | YieldRange           |  |
| YieldCalculation | VariableInterest     |  |
| FutureRule       |                      |  |
| FutureRule       | TimeType             |  |
|                  |                      |  |

| FutureRule | RelatedFutureInstrument |  |
|------------|-------------------------|--|
| FutureRule | MaximumTimeToMaturity   |  |
| FutureRule | MinimumTimeToMaturity   |  |
| FutureRule | BaseInterestRate        |  |
| Rating     |                         |  |
| Rating     | Security                |  |
| Rating     | RatingScheme            |  |
| Rating     | ValueDate               |  |
| Rating     | Value                   |  |
| Leg        |                         |  |
| Leg        | RelatedAsset            |  |
| Leg        | RatioQuantity           |  |

| Leg        | Currency           |  |
|------------|--------------------|--|
| Leg        | SwapType           |  |
| Leg        | Pool               |  |
| Leg        | Trade              |  |
| Allocation |                    |  |
| Allocation | Percentage         |  |
| Allocation | AllocatedQuantity  |  |
| Allocation | SettlementCurrency |  |
| Allocation | AllocationAccount  |  |
| Allocation | AllocatedPrice     |  |

| Allocation          | AllocationAmount              |
|---------------------|-------------------------------|
| Allocation          | Method                        |
| Allocation          | AveragePricePrecision         |
| Allocation          | SettlementExecutionParameters |
| Allocation          | SecuritiesOrder               |
| Allocation          | SecuritiesTrade               |
| Allocation          | Identification                |
| CollateralValuation |                               |
| CollateralValuation | Collateral                    |
| CollateralValuation | CollateralValuationDate       |
| CollateralValuation | RelatedManagementProcess      |
| CollateralValuation | ReportedCurrencyAndAmount     |

| CollateralValuation                 | MarketValueAmount           |  |
|-------------------------------------|-----------------------------|--|
| CollateralValuation                 | AdjustedRate                |  |
| CollateralValuation                 | CollateralValuationCurrency |  |
| Sector                              |                             |  |
| Sector                              | Security                    |  |
| Sector                              | Scheme                      |  |
| Sector                              | Organisation                |  |
| Sector                              | Identification              |  |
| Sector                              | Strategy                    |  |
| SecuritiesOrderExecutionInstruction |                             |  |

| SecuritiesOrderExecutionInstruction | AllOrNone        |  |
|-------------------------------------|------------------|--|
| SecuritiesOrderExecutionInstruction | CallFirst        |  |
| SecuritiesOrderExecutionInstruction | Cross            |  |
| SecuritiesOrderExecutionInstruction | CustomerDisplay  |  |
| SecuritiesOrderExecutionInstruction | Hold             |  |
| SecuritiesOrderExecutionInstruction | Increase         |  |
| SecuritiesOrderExecutionInstruction | InstitutionsOnly |  |
|                                     |                  |  |

| SecuritiesOrderExecutionInstruction | NonNegotiable           |  |
|-------------------------------------|-------------------------|--|
| SecuritiesOrderExecutionInstruction | OverTheDay              |  |
| SecuritiesOrderExecutionInstruction | ParticipateDontInitiate |  |
| SecuritiesOrderExecutionInstruction | PercentOfVolume         |  |
| SecuritiesOrderExecutionInstruction | Scale                   |  |
| SecuritiesOrderExecutionInstruction | StayOnSide              |  |
| SecuritiesOrderExecutionInstruction | Work                    |  |
| SecuritiesOrderExecutionInstruction | GoAlong                 |  |
|                                     |                         |  |

| SecuritiesOrderExecutionInstruction | TryScale              |  |
|-------------------------------------|-----------------------|--|
| SecuritiesOrderExecutionInstruction | DoNotReduce           |  |
| SecuritiesOrderExecutionInstruction | CancelOnSystemFailure |  |
| SecuritiesOrderExecutionInstruction | CancelOnTradingHalt   |  |

| SecuritiesOrderExecutionInstruction | TradeAlong                |  |
|-------------------------------------|---------------------------|--|
| SecuritiesOrderExecutionInstruction | StrictLimit               |  |
| SecuritiesOrderExecutionInstruction | IgnorePriceValidityChecks |  |
| SecuritiesOrderExecutionInstruction | ReinstateOnSystemFailure  |  |
| SecuritiesOrderExecutionInstruction | ReinstateOnTradingHalt    |  |
| SecuritiesOrderExecutionInstruction | CancelIfNotBest           |  |

| SecuritiesOrderExecutionInstruction | ExternalRoutingAllowed    |  |
|-------------------------------------|---------------------------|--|
| SecuritiesOrderExecutionInstruction | ExternalRoutingNotAllowed |  |
| SecuritiesOrderExecutionInstruction | ImbalanceOnly             |  |

| Indicates that the party sending<br>the order has taken responsibility<br>for price protection, and the<br>recipient of the order should<br>execute it, if possible, without<br>regard to protection of other<br>SecuritiesOrderExecutionInstruction<br>IntermarketSweep<br>marketsÂ' prices. While the term<br>YesNoIndicator<br>"Intermarket sweep" is specific<br>to the United States, it may be<br>used in other markets, where<br>appropriate, to indicate an order<br>that should be executed without<br>regard to price protection.<br>Used when sending multiple<br>SecuritiesOrderExecutionInstruction<br>Netting<br>orders indicating that you would<br>be 'netting' the F/X later.<br>SecuritiesOrderExecutionInstruction<br>RelatedOrder<br>Order which is executed.<br>Reduction of transfers of cash<br>(resulting of a foreign exchange<br>SecuritiesOrderExecutionInstruction<br>ForeignExchangeNetting<br>operation between subsidiaries or<br>separate companies) to a net<br>amount.<br>Order to buy (sell) a security that<br>strictly specifies the total amount<br>to be bought (sold) and the<br>amount to be bought (sold) at<br>SecuritiesOrderExecutionInstruction<br>StrictScale<br>successively decreasing<br>(increasing) price intervals; often<br>placed in order to average the<br>price.<br>Used in specialist driven markets<br>SecuritiesOrderExecutionInstruction<br>Suspend<br>to direct the specialist to try to<br>suspend the order. |  |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| YesNoIndicator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |
| SecuritiesOrder                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
| YesNoIndicator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |
| YesNoIndicator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |
| YesNoIndicator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |

| SecuritiesOrderExecutionInstruction | TryToStop           |                |
|-------------------------------------|---------------------|----------------|
| SecuritiesOrderExecutionInstruction | OrderPriceStrategy  |                |
| SecuritiesPostTradeBooking          |                     |                |
| SecuritiesPostTradeBooking          | DayBooking          |                |
| SecuritiesPostTradeBooking          | BookingUnit         |                |
| SecuritiesPostTradeBooking          | PreAllocationMethod |                |
| SecuritiesPostTradeBooking          | BookingType         |                |
| SecuritiesPostTradeBooking          | RelatedOrder        |                |
| Broker                              |                     | TradePartyRole |
| Broker                              | RemunerationAmount  |                |
| Broker                              | Commission          |                |

| SecuritiesOrderPartyRole |                 | Role                     |
|--------------------------|-----------------|--------------------------|
|                          |                 |                          |
| SecuritiesOrderPartyRole | SecuritiesOrder |                          |
|                          |                 |                          |
| IntroducingFirm          |                 | SecuritiesOrderPartyRole |
|                          |                 |                          |
| StepInBroker             |                 | Broker                   |
| StepOutBroker            |                 | Broker                   |
| ClearingBroker           |                 | Broker                   |
| ExecutingBrokerRole      |                 | Broker                   |
| ExecutingBrokerRole      | ExecutingTrader |                          |

| SecuritiesLending |                          | SecuritiesFinancing |
|-------------------|--------------------------|---------------------|
| SecuritiesLending | BorrowingFee             |                     |
| SecuritiesLending | CallableTradeIndicator   |                     |
| SecuritiesLending | LendingTransactionMethod |                     |
| SecuritiesLending | BorrowingReason          |                     |
| SecuritiesLending | Reversible               |                     |
| SecuritiesLending | SecuritiesLendingType    |                     |
| SecuritiesLending | LendingWithCollateral    |                     |
|                   |                          |                     |

| SecuritiesLending            | MinimumDateForCallBack        |           |
|------------------------------|-------------------------------|-----------|
| SecuritiesLending            | NumberOfDaysLendingBorrowing  |           |
| SecuritiesLending            | PeriodicPayment               |           |
| SecuritiesLending            | Rollover                      |           |
| SecuritiesLending            | BorrowingRate                 |           |
| SecuritiesLending            | SecuritiesDeliveryObligation  |           |
| UnderlyingRatio              |                               |           |
| UnderlyingRatio              | SecuritiesConversion          |           |
| UnderlyingRatio              | UnderlyingQuantityDenominator |           |
| UnderlyingRatio              | UnderlyingQuantityNumerator   |           |
| SecuritiesFinancingAgreement |                               | Agreement |

| SecuritiesFinancingAgreement | SecuritiesFinancingTrade      |  |
|------------------------------|-------------------------------|--|
| SecuritiesFinancingAgreement | Currency                      |  |
| SecuritiesFinancingAgreement | TerminationType               |  |
| SecuritiesFinancingAgreement | DeliveryType                  |  |
| SecuritiesFinancingAgreement | MarginRatio                   |  |
| RegulatoryReport             |                               |  |
| RegulatoryReport             | DebitCreditReportingIndicator |  |
| RegulatoryReport             | Authority                     |  |
| RegulatoryReport             | Code                          |  |

| RegulatoryReport | Amount              |  |
|------------------|---------------------|--|
| RegulatoryReport | Description         |  |
| RegulatoryReport | Type                |  |
| RegulatoryReport | Date                |  |
| RegulatoryReport | ReportedTransaction |  |
| RegulatoryReport | UnderlyingProduct   |  |
| RegulatoryReport | NonStandardFlag     |  |
| RegulatoryReport | ReportingPartyRole  |  |
| Undertaking      |                     |  |

| Undertaking | ElectronicSignature  |  |
|-------------|----------------------|--|
| Undertaking | UndertakingStatus    |  |
| Undertaking | Identification       |  |
| Undertaking | Demand               |  |
| Undertaking | TerminationDate      |  |
| Undertaking | UndertakingAmount    |  |
| Undertaking | Expiry               |  |
| Undertaking | PartyRole            |  |
| Undertaking | UndertakingAmendment |  |
| Undertaking | SpecifiedDocument    |  |
| Undertaking | DateOfAdvice         |  |

| Undertaking<br>Purpose<br>Undertaking<br>UndertakingName<br>Undertaking<br>Type<br>Undertaking<br>ConfirmationIndicator<br>Undertaking<br>CounterUndertakingIndicator<br>Undertaking<br>RelatedChargesPayableBy<br>Undertaking<br>StandardClaimDocumentIndicator<br>Undertaking<br>UnderlyingTransaction<br>Undertaking<br>ModelForm |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |
|                                                                                                                                                                                                                                                                                                                                      |  |  |

| Undertaking | MultipleDemandIndicator |          |
|-------------|-------------------------|----------|
| Undertaking | PartialDemandIndicator  |          |
| Undertaking | TransferIndicator       |          |
| Undertaking | PredefinedVariation     |          |
| Undertaking | Charges                 |          |
| Undertaking | Presentation            |          |
| Undertaking | UndertakingExtension    |          |
| Signature   |                         | Evidence |
| Signature   | Conditions              |          |
| Signature   | CardPaymentValidation   |          |
|             |                         |          |

| ElectronicSignature     |                            | Signature        |
|-------------------------|----------------------------|------------------|
| ElectronicSignature     | Undertaking                |                  |
| ElectronicSignature     | RelatedSecurityCertificate |                  |
| RepresentativeOfficer   |                            | AccountPartyRole |
| RepresentativeOfficer   | Organisation               |                  |
| TreasuryManager         |                            | AccountPartyRole |
| AccountReportedMovement |                            |                  |
| AccountReportedMovement | MonthlyPaymentValue        |                  |
| AccountReportedMovement | MonthlyReceivedValue       |                  |
| AccountReportedMovement | MonthlyTransactionNumber   |                  |
|                         |                            |                  |

| AccountReportedMovement | AverageBalance        |          |
|-------------------------|-----------------------|----------|
| AccountReportedMovement | ReportedCashAccount   |          |
| Mandate                 |                       | Contract |
| Mandate                 | SignatureConditions   |          |
| Mandate                 | MandateIdentification |          |
| Mandate                 | OriginalMandate       |          |
| Mandate                 | Amendment             |          |
| Mandate                 | MandatePartyRole      |          |
| Mandate                 | MandateStatus         |          |
| Mandate                 | AccountContract       |          |
| Mandate                 | Authentication        |          |
| Mandate                 | TrackingDays          |          |

| Mandate             | TrackingIndicator            |          |
|---------------------|------------------------------|----------|
| Mandate             | Rate                         |          |
| Mandate             | Frequency                    |          |
| Mandate             | MandatePaymentType           |          |
| CashAccountMandate  |                              | Mandate  |
| CashAccountMandate  | Services                     |          |
| CashAccountMandate  | CashAccountContract          |          |
| SecurityCertificate |                              | Document |
| SecurityCertificate | ElectronicSignature          |          |
| SecurityCertificate | SecurityCertificatePartyRole |          |
| SecurityCertificate | NetworkAccess                |          |
|                     |                              |          |

| SecurityCertificate | CertificateType             |                    |
|---------------------|-----------------------------|--------------------|
|                     |                             |                    |
| BankOperation       |                             | CashAccountService |
| BankOperation       | OperationThreshold          |                    |
| BankOperation       | OperationType               |                    |
| BankOperation       | ApplicablePeriod            |                    |
| OperationThreshold  |                             |                    |
| OperationThreshold  | BankOperation               |                    |
| OperationThreshold  | MininumAmountPerTransaction |                    |
| OperationThreshold  | MaximumAmount               |                    |
| BankTransaction     |                             |                    |
| BankTransaction     | Domain                      |                    |
| BankTransaction     | Family                      |                    |

| BankTransaction | SubFamily                     |  |
|-----------------|-------------------------------|--|
| BankTransaction | ProprietaryIdentification     |  |
| BankTransaction | BankOperation                 |  |
| BankTransaction | RelatedEntry                  |  |
| BankTransaction | RelatedPayment                |  |
| Presentation    |                               |  |
| Presentation    | CommunicationMethod           |  |
| Presentation    | PresentedUndertaking          |  |
| Presentation    | Medium                        |  |
| Presentation    | PresentedDocument             |  |
| Presentation    | ElectronicPresentationAddress |  |
| Presentation    | PresentationDate              |  |
| Presentation    | ApplicableChannel             |  |
|                 |                               |  |

| SecurityCertificatePartyRole  |                      | Role                         |
|-------------------------------|----------------------|------------------------------|
| SecurityCertificatePartyRole  | SecurityCertificate  |                              |
| SecurityCertificateHolderRole |                      | SecurityCertificatePartyRole |
| DebitCreditFacility           |                      | CashAccountService           |
| DebitCreditFacility           | CreditLine           |                              |
| DebitCreditFacility           | CashAccountInterest  |                              |
| DebitCreditFacility           | CreditDebitIndicator |                              |
| CashAvailability              |                      |                              |
| CashAvailability              | CashBalance          |                              |
| CashAvailability              | Date                 |                              |
| CashAvailability              | NumberOfDays         |                              |
| CashAvailability              | Amount               |                              |

| CashAvailability<br>CashEntry<br>CashAvailability<br>CreditDebitIndicator<br>DocumentIssuer<br>DocumentPartyRole<br>Discount<br>Adjustment<br>Discount<br>DiscountAppliedAmount<br>Discount<br>DiscountType<br>Discount<br>DiscountBasisAmount<br>Invoice<br>FinancialDocument |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                |  |  |

| Invoice | CreditDebitNoteAmount |  |
|---------|-----------------------|--|
| Invoice | TotalTaxAmount        |  |
| Invoice | TotalInvoiceAmount    |  |
| Invoice | InvoiceCurrency       |  |
| Invoice | PeriodCovered         |  |
| Invoice | TradeSettlement       |  |
| Invoice | TotalCharge           |  |
| Invoice | TotalPrepaidAmount    |  |
| Invoice | LineItem              |  |
| Invoice | TotalNetAmount        |  |
|         |                       |  |

| Invoice | CurrencyExchange                          |  |
|---------|-------------------------------------------|--|
| Invoice | BillingCompensationType                   |  |
| Invoice | InvoicePartyRole                          |  |
| Invoice | OriginalInvoice                           |  |
| Invoice | RelatedInvoice                            |  |
| Invoice | InvoiceFinancingTransaction               |  |
| Invoice | BillingCompensationAmount                 |  |
| Invoice | InvoiceStatus                             |  |
| Invoice | Payment                                   |  |
| Invoice | CreditDebitIndicator                      |  |
| Invoice | LimitedPresentmentIndicator               |  |
| Invoice | RelatedElectronicInvoiceProcessingService |  |

| Invoice             | ActivationRequestDeliveryParty |                  |
|---------------------|--------------------------------|------------------|
| InvoicePartyRole    |                                | Role             |
| InvoicePartyRole    | Invoice                        |                  |
| InvoiceeRole        |                                | InvoicePartyRole |
| TaxPartyRole        |                                | Role             |
| TaxPartyRole        | Tax                            |                  |
| TaxPartyRole        | VATRegistrationNumber          |                  |
| CreditSideTaxDebtor |                                | TaxPartyRole     |
| TaxPayer            |                                | TaxPartyRole     |
| DebitSideTaxDebtor  |                                | TaxPartyRole     |
| TaxRecord           |                                |                  |
| TaxRecord           | Tax                            |                  |

| TaxRecord | TaxRecordType       |  |
|-----------|---------------------|--|
| TaxRecord | Category            |  |
| TaxRecord | Status              |  |
| TaxRecord | FormsCode           |  |
| TaxRecord | Period              |  |
| TaxRecord | Amount              |  |
| TaxRecord | CategoryDescription |  |
| TaxPeriod |                     |  |
| TaxPeriod | TaxRecord           |  |
| TaxPeriod | Year                |  |
| TaxPeriod | Type                |  |

| TaxPeriod            | FromToDate                |  |
|----------------------|---------------------------|--|
| TaxPeriod            | EndOfFiscalYear           |  |
| CardPaymentAcquiring |                           |  |
| CardPaymentAcquiring | PointOfInteraction        |  |
| CardPaymentAcquiring | CardPaymentService        |  |
| CardPaymentAcquiring | TransactionIdentification |  |
| CardPaymentAcquiring | TransactionDateTime       |  |
| CardPaymentAcquiring | ICCRelatedData            |  |
| CardPaymentAcquiring | RelatedCardPayment        |  |
| CardPaymentAcquiring | CardPresent               |  |
| CardPaymentAcquiring | CardholderPresent         |  |
|                      |                           |  |

| CardPaymentAcquiring<br>OnLineContext                  |
|--------------------------------------------------------|
| CardPaymentAcquiring<br>AttendanceContext              |
| CardPaymentAcquiring<br>TransactionEnvironment         |
| CardPaymentAcquiring<br>TransactionChannel             |
| CardPaymentAcquiring<br>AttendantMessageCapable        |
| CardPaymentAcquiring<br>AttendantLanguage              |
| CardPaymentAcquiring<br>CardDataEntryMode              |
| CardPaymentAcquiring<br>FallbackIndicator              |
| CardPaymentAcquiring<br>TMSTrigger                     |
| CardPaymentAcquiring<br>InitiatorTransactionIdentifier |

| CardPaymentAcquiring | Reversal                           |
|----------------------|------------------------------------|
| CardPaymentAcquiring | InterchangeData                    |
| CardPaymentAcquiring | UnattendedLevelCategory            |
| CardPaymentAcquiring | Validation                         |
| CardPaymentAcquiring | CompletionRequired                 |
| CardPaymentAcquiring | ActionType                         |
| CardPaymentAcquiring | ActionMessage                      |
| CardPaymentAcquiring | CaptureIndicator                   |
| CardPaymentAcquiring | RecipientTransactionIdentification |
| CardPaymentAcquiring | Location                           |

| CardPaymentAcquiring | Country                            |        |
|----------------------|------------------------------------|--------|
| CardPaymentAcquiring | ReSubmissionCounter                |        |
| CardPaymentAcquiring | BusinessArea                       |        |
| PointOfInteraction   |                                    | System |
| PointOfInteraction   | CardPaymentAcquiring               |        |
| PointOfInteraction   | CardReadingCapabilities            |        |
| PointOfInteraction   | CardholderVerificationCapabilities |        |
| PointOfInteraction   | OnLineCapabilities                 |        |

| PointOfInteraction<br>DisplayCapabilities<br>PointOfInteraction<br>PrintLineWidth<br>PointOfInteraction<br>Component<br>PointOfInteraction<br>ComponentIdentification<br>PointOfInteraction<br>GroupIdentifier<br>PointOfInteraction<br>LineWidth<br>PointOfInteraction<br>NumberOfLines<br>PointOfInteraction<br>ErrorLog<br>PointOfInteraction<br>ComponentVersionNumber<br>PointOfInteraction<br>ControllingTerminalManagementSystem<br>SystemName<br>SystemName<br>Name |  |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |

| SystemName                | SystemIdentification      |                        |
|---------------------------|---------------------------|------------------------|
| InvestigationPartyRole    |                           | Role                   |
| InvestigationPartyRole    | InvestigationCase         |                        |
| InvestigationPartyRole    | Status                    |                        |
| StatusOriginator          |                           | InvestigationPartyRole |
| CashDeposit               |                           | IndividualPayment      |
| CashDeposit               | NoteDenomination          |                        |
| CashDeposit               | NumberOfNotes             |                        |
| CashDeposit               | DepositAmount             |                        |
| CashDeposit               | RelatedBankingTransaction |                        |
| ReconciliationTransaction |                           | Reconciliation         |
|                           |                           |                        |

| ReconciliationTransaction | ReconciliationIdentification |  |
|---------------------------|------------------------------|--|
| ReconciliationTransaction | Currency                     |  |
| ReconciliationTransaction | TransactionType              |  |
| ReconciliationTransaction | TotalNumber                  |  |
| ReconciliationTransaction | CumulativeAmount             |  |
| ReconciliationTransaction | ClosePeriod                  |  |
| ReconciliationTransaction | CardPaymentTotal             |  |
| ProductIdentification     |                              |  |
| ProductIdentification     | Identifier                   |  |
| ProductIdentification     | Product                      |  |
| ProductIdentification     | Type                         |  |

| ProductIdentification | GlobalSerialIdentifier            |  |
|-----------------------|-----------------------------------|--|
| ProductQuantity       |                                   |  |
| ProductQuantity       | UnitOfMeasure                     |  |
| ProductQuantity       | Value                             |  |
| ProductQuantity       | Product                           |  |
| ProductQuantity       | Factor                            |  |
| ProductQuantity       | NetWeightRelatedLineItem          |  |
| ProductQuantity       | BilledQuantityRelatedLineItem     |  |
| ProductQuantity       | RelatedPackaging                  |  |
| ProductQuantity       | PackagingForUnitQuantity          |  |
| ProductQuantity       | ChargeFreeQuantityRelatedLineItem |  |

| ProductQuantity | MeasureQuantityStart              |
|-----------------|-----------------------------------|
| ProductQuantity | MeasureQuantityEnd                |
| ProductQuantity | QuantityTolerance                 |
| ProductQuantity | PackagingForConsignmentlQuantity  |
| ProductQuantity | PackagingForVolume                |
| ProductQuantity | PackagingForWeight                |
| ProductQuantity | GrossPriceQuantityRelatedLineItem |
| ProductQuantity | NetPriceQuantityRelatedLineItem   |
| ProductQuantity | GrossWeightRelatedLineItem        |
| ProductQuantity | TimeUnit                          |
| ServiceLevel    |                                   |

| ServiceLevel               | PaymentProcessing |                            |
|----------------------------|-------------------|----------------------------|
|                            |                   |                            |
| ServiceLevel               | Code              |                            |
| ServiceLevel               | Other             |                            |
|                            |                   |                            |
| ServiceLevel               | Bilateral         |                            |
|                            |                   |                            |
| DebtorAgentRole            |                   | PaymentPartyRole           |
| PaymentObligationPartyRole |                   | Role                       |
| PaymentObligationPartyRole | PaymentObligation |                            |
| UltimateDebtorRole         |                   | PaymentObligationPartyRole |
| ChargePartyRole            |                   | Role                       |
| ChargePartyRole            | Adjustment        |                            |
| ChargeAccountAgent         |                   | ChargePartyRole            |
|                            |                   |                            |

| CreditTransfer          |                      | IndividualPayment          |
|-------------------------|----------------------|----------------------------|
| CreditTransfer          | StandingOrder        |                            |
| CreditTransfer          | RelatedStandingOrder |                            |
| RegulatoryAuthorityRole |                      | Role                       |
| RegulatoryAuthorityRole | RegulatoryReport     |                            |
| RegulatoryAuthorityRole | Country              |                            |
| UltimateCreditorRole    |                      | PaymentObligationPartyRole |
| DirectDebitMandate      |                      | Mandate                    |
| DirectDebitMandate      | RelatedDirectDebit   |                            |
| DirectDebitMandate      | FinalCollectionDate  |                            |
| DirectDebitMandate      | FirstCollectionDate  |                            |
|                         |                      |                            |

| DirectDebitMandate | CollectionAmount         |                  |
|--------------------|--------------------------|------------------|
| DirectDebitMandate | MaximumAmount            |                  |
| DirectDebitMandate | PreNotification          |                  |
| DirectDebitMandate | PreNotificationThreshold |                  |
| DirectDebitMandate | Classification           |                  |
| DirectDebitMandate | PointInTime              |                  |
| CreditorRole       |                          | PaymentPartyRole |
| CreditorRole       | SchemeIdentification     |                  |
| InvestigationCase  |                          |                  |
| InvestigationCase  | AssignmentIdentification |                  |
| InvestigationCase  | CreationDateTime         |                  |
| InvestigationCase  | Identification           |                  |
|                    |                          |                  |

| InvestigationCase | Status                               |  |
|-------------------|--------------------------------------|--|
| InvestigationCase | InvestigationPartyRole               |  |
| InvestigationCase | DuplicateCaseResolution              |  |
| InvestigationCase | InvestigationResolution              |  |
| InvestigationCase | OriginalInvestigationCase            |  |
| InvestigationCase | LinkedCase                           |  |
| InvestigationCase | Reassignment                         |  |
| InvestigationCase | EIR                                  |  |
| InvestigationCase | RequestorInvestigationIdentification |  |

| InvestigationCase<br>InvestigationType<br>InvestigationCase<br>ResponderInvestigationIdentification<br>PaymentInvestigationCase<br>InvestigationCase<br>PaymentInvestigationCase<br>PaymentStatus<br>PaymentInvestigationCase<br>CancellationReason<br>PaymentInvestigationCase<br>UnderlyingPayment<br>PaymentInvestigationCase<br>MissingCoverIndication | InvestigationCase | InvestigationSubType |  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|----------------------|--|
|                                                                                                                                                                                                                                                                                                                                                            |                   |                      |  |
|                                                                                                                                                                                                                                                                                                                                                            |                   |                      |  |
|                                                                                                                                                                                                                                                                                                                                                            |                   |                      |  |
|                                                                                                                                                                                                                                                                                                                                                            |                   |                      |  |
|                                                                                                                                                                                                                                                                                                                                                            |                   |                      |  |
|                                                                                                                                                                                                                                                                                                                                                            |                   |                      |  |
|                                                                                                                                                                                                                                                                                                                                                            |                   |                      |  |

| PaymentInvestigationCase     | UnderlyingInstruction      |                                    |
|------------------------------|----------------------------|------------------------------------|
| PaymentInvestigationCase     | UnderlyingCashEntry        |                                    |
| PaymentInvestigationCase     | IncorrectInformationReason |                                    |
| PaymentInvestigationCase     | MissingInformationReason   |                                    |
| PaymentInvestigationCase     | CaseType                   |                                    |
| InstructedReimbursementAgent |                            | CashSettlementInstructionPartyRole |
| UndertakingStatusReason      |                            | StatusReason                       |
| UndertakingStatusReason      | Discrepancy                |                                    |
| UndertakingStatusReason      | UndertakingStatus          |                                    |
|                              |                            |                                    |

| UndertakingStatusReason | TerminationReason         |                      |
|-------------------------|---------------------------|----------------------|
| UndertakingStatusReason | DemandRefusalStatusReason |                      |
| UndertakingStatusReason | SettlementReason          |                      |
| UndertakingStatus       |                           | Status               |
| UndertakingStatus       | Undertaking               |                      |
| UndertakingStatus       | DemandStatus              |                      |
| UndertakingStatus       | Status                    |                      |
| UndertakingStatus       | UndertakingStatusReason   |                      |
| UndertakingStatus       | StatusCategory            |                      |
| UndertakingStatus       | PresentationStatus        |                      |
| UndertakingPartyRole    |                           | Role                 |
| UndertakingPartyRole    | Undertaking               |                      |
| UndertakingIssuer       |                           | UndertakingPartyRole |

| Demand      |                         |  |
|-------------|-------------------------|--|
| Demand      | Undertaking             |  |
| Demand      | SubmissionDateTime      |  |
| Demand      | DemandAmount            |  |
| Demand      | Type                    |  |
| Demand      | TotalClaimAmount        |  |
| Demand      | Payment                 |  |
| Demand      | AssociatedDocument      |  |
| Discrepancy |                         |  |
| Discrepancy | UndertakingStatusReason |  |
| Discrepancy | Type                    |  |
| Discrepancy | Description             |  |
| Expiry      |                         |  |
|             |                         |  |

| Expiry                | ExpiryDateTime     |                   |
|-----------------------|--------------------|-------------------|
| Expiry                | Undertaking        |                   |
| Expiry                | ExpiryCondition    |                   |
| Expiry                | OpenEndedIndicator |                   |
| Expiry                | ExpiryPlace        |                   |
| UndertakingDocument   |                    | FinancialDocument |
| UndertakingDocument   | DocumentType       |                   |
| UndertakingDocument   | Format             |                   |
| UndertakingDocument   | Undertaking        |                   |
| UndertakingDocument   | CopyIndicator      |                   |
| UndertakingDocument   | Demand             |                   |
| SettlementTimeRequest |                    |                   |
| SettlementTimeRequest | Payment            |                   |
|                       |                    |                   |

| SettlementTimeRequest | CLSTime               |                        |
|-----------------------|-----------------------|------------------------|
| SettlementTimeRequest | TillTime              |                        |
| SettlementTimeRequest | FromTime              |                        |
| SettlementTimeRequest | RejectTime            |                        |
| Assigner              |                       | InvestigationPartyRole |
| Assignee              |                       | InvestigationPartyRole |
| IntermediaryAgentRole |                       | PaymentPartyRole       |
| IntermediaryAgentRole | IntermediaryAgentRole |                        |
| IntermediaryAgentRole | NextParty             |                        |
| IntermediaryAgentRole | Position              |                        |
| MandateStatus         |                       | Status                 |
|                       |                       |                        |

| MandateStatus          | Accepted                           |  |
|------------------------|------------------------------------|--|
| MandateStatus          | RejectReason                       |  |
| MandateStatus          | Mandate                            |  |
| MandateStatus          | MandateReason                      |  |
| AmendmentOfUndertaking |                                    |  |
| AmendmentOfUndertaking | DateOfIssuance                     |  |
| AmendmentOfUndertaking | ChangeOfAmount                     |  |
| AmendmentOfUndertaking | Undertaking                        |  |
| AmendmentOfUndertaking | BeneficiaryConsentRequestIndicator |  |
| AmendmentOfUndertaking | AmendmentIdentification            |  |
| UndertakingAmount      |                                    |  |
| UndertakingAmount      | Undertaking                        |  |
|                        |                                    |  |

| UndertakingAmount<br>Tolerance<br>UndertakingAmount<br>BalanceAmount<br>UndertakingAmount<br>Type<br>UndertakingAmount<br>Interest<br>UndertakingExtension<br>UndertakingExtension<br>Undertaking<br>UndertakingExtension<br>AutoExtensionPeriod<br>UndertakingExtension<br>AutoExtensionFinalExpiryDate<br>UndertakingExtension<br>NonExtensionNoticePeriod<br>UndertakingExtension<br>NonExtensionIndicator | UndertakingAmount | Amount |  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--------|--|
|                                                                                                                                                                                                                                                                                                                                                                                                               |                   |        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                               |                   |        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                               |                   |        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                               |                   |        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                               |                   |        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                               |                   |        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                               |                   |        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                               |                   |        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                               |                   |        |  |
|                                                                                                                                                                                                                                                                                                                                                                                                               |                   |        |  |

| UndertakingExtension<br>AutoExtensionNotificationPeriod |                      |
|---------------------------------------------------------|----------------------|
| UndertakingExtension<br>NotificationRecipientType       |                      |
| UndertakingDeliveryToParty                              | UndertakingPartyRole |
| UndertakingAdvisingParty                                | UndertakingPartyRole |
| UndertakingBeneficiary                                  | UndertakingPartyRole |
| UndertakingUltimateObligor                              | UndertakingPartyRole |
| UndertakingUltimateObligor<br>CashAccount               |                      |
| UndertakingApplicant                                    | UndertakingPartyRole |

| UndertakingConfirmer |                          | UndertakingPartyRole |
|----------------------|--------------------------|----------------------|
| Tolerance            |                          |                      |
| Tolerance            | RelatedUndertakingAmount |                      |
| Tolerance            | Quantity                 |                      |
| Tolerance            | PlusPercent              |                      |
| Tolerance            | MinusPercent             |                      |
| Tolerance            | Price                    |                      |
| ModelForm            |                          |                      |
| ModelForm            | GovernanceRules          |                      |
| ModelForm            | Undertaking              |                      |
| ModelForm            | Identification           |                      |
| ModelForm            | Version                  |                      |
| ModelForm            | RequestedWordingLanguage |                      |
|                      |                          |                      |

| ModelForm       | EffectiveDate        |  |
|-----------------|----------------------|--|
| GovernanceRules |                      |  |
| GovernanceRules | ModelForm            |  |
| GovernanceRules | Identification       |  |
| GovernanceRules | ApplicableLaw        |  |
| GovernanceRules | Jurisdiction         |  |
| GovernanceRules | PublicationAgency    |  |
| Jurisdiction    |                      |  |
| Jurisdiction    | GovernanceRules      |  |
| Jurisdiction    | Identification       |  |
| Jurisdiction    | RegisteredSecurities |  |
| Jurisdiction    | AssociatedStrategy   |  |
|                 |                      |  |

| Jurisdiction          | SecuritiesRestriction    |  |
|-----------------------|--------------------------|--|
| Jurisdiction          | RelatedSecuritiesTax     |  |
| Jurisdiction          | RelatedMarket            |  |
| Jurisdiction          | RelatedAgreement         |  |
| UnderlyingTransaction |                          |  |
| UnderlyingTransaction | Undertaking              |  |
| UnderlyingTransaction | Type                     |  |
| UnderlyingTransaction | Identification           |  |
| UnderlyingTransaction | IssueDate                |  |
| UnderlyingTransaction | TenderClosingDate        |  |
| UnderlyingTransaction | TotalAmount              |  |
| UnderlyingTransaction | ContractAmountPercentage |  |
|                       |                          |  |

| UnderlyingTransaction          | CommercialTrade    |                      |
|--------------------------------|--------------------|----------------------|
| AutomaticVariation             |                    |                      |
| AutomaticVariation             | Undertaking        |                      |
| AutomaticVariation             | Type               |                      |
| AutomaticVariation             | VariationAmount    |                      |
| AutomaticVariation             | Trigger            |                      |
| Trigger                        |                    |                      |
| Trigger                        | AutomaticVariation |                      |
| Trigger                        | TriggerDate        |                      |
| Trigger                        | TriggerEvent       |                      |
| UndertakingPresenter           |                    | UndertakingPartyRole |
| UndertakingPlaceOfPresentation |                    | UndertakingPartyRole |
|                                |                    |                      |

| UndertakingPlaceOfPresentation | PresentationUnderConfirmation |                      |
|--------------------------------|-------------------------------|----------------------|
| UndertakingInstructingParty    |                               | UndertakingPartyRole |
| TreasuryTradeSettlementStatus  |                               | Status               |
| TreasuryTradeSettlementStatus  | TradeStatus                   |                      |
| TreasuryTradeSettlementStatus  | AllegedTrade                  |                      |
| TreasuryTradeSettlementStatus  | TreasuryTrade                 |                      |
| TreasuryTradeSettlementStatus  | Settlement                    |                      |
| TreasuryTradeSettlementStatus  | RejectedAmount                |                      |
| TreasuryTradeSettlementStatus  | SettlementSuspended           |                      |
| TreasuryTradeSettlementStatus  | PendingSettlement             |                      |
| TreasuryTradeSettlementStatus  | SettlementDate                |                      |
| TreasuryTradeSettlementStatus  | WithdrawalReason              |                      |

| ProductCategory              |                              |               |
|------------------------------|------------------------------|---------------|
| ProductCategory              | Product                      |               |
| ProductCategory              | Type                         |               |
| ProductCategory              | Category                     |               |
| ProductCategory              | RelatedCardPaymentValidation |               |
| ClearingBrokerIdentification |                              |               |
| ClearingBrokerIdentification | RelatedTradeIdentification   |               |
| ClearingBrokerIdentification | SideIndicator                |               |
| ClearingBrokerIdentification | Identification               |               |
| ForeignExchangeSwap          |                              | TreasuryTrade |
|                              |                              |               |

| ForeignExchangeSwap    | LinkSwapIdentification |                               |
|------------------------|------------------------|-------------------------------|
| ForeignExchangeSwap    | SwapLeg                |                               |
| SubmittingPartyRole    |                        | SystemPartyRole               |
| TreasuryTradePartyRole |                        | TradePartyRole                |
| TreasuryTradePartyRole | TreasuryTrade          |                               |
| TreasuryTradingParty   |                        | TreasuryTradePartyRole        |
| TreasuryTradingParty   | InvestmentFund         |                               |
| ReceivingAgent         |                        | SecuritiesSettlementPartyRole |
| Negotiation            |                        |                               |
| Negotiation            | TradingMethod          |                               |
|                        |                        |                               |

| Negotiation              | TradeExecution            |       |
|--------------------------|---------------------------|-------|
| Negotiation              | TradingSystem             |       |
| Negotiation              | NegotiationIdentification |       |
| Negotiation              | Quote                     |       |
| Negotiation              | IndicationOfInterest      |       |
| Negotiation              | SecuritiesOrder           |       |
| LiquidityManagementLimit |                           | Limit |
| LiquidityManagementLimit | VolatilityMargin          |       |
|                          |                           |       |

| LiquidityManagementLimit | CurrencyExchange      |  |
|--------------------------|-----------------------|--|
| LiquidityManagementLimit | RelatedCashServices   |  |
| LiquidityManagementLimit | LiquidityLimitType    |  |
| LiquidityManagementLimit | RequiredAmount        |  |
| Authentication           |                       |  |
| Authentication           | Cardholder            |  |
| Authentication           | AuthenticationMethod  |  |
| Authentication           | AuthenticationEntity  |  |
| Authentication           | AuthenticationValue   |  |
| Authentication           | PINFormat             |  |
| Authentication           | PIN                   |  |
| Authentication           | AuthenticationSupport |  |
|                          |                       |  |

| Authentication<br>CollectionIndicator<br>Authentication<br>Mandate<br>Authentication<br>AuthenticationResult<br>Authentication<br>Exemption<br>MerchantRole<br>CardPaymentPartyRole<br>MerchantRole<br>MerchantCategoryCode<br>MerchantRole<br>MerchantIdentification<br>CreditorAgentRole<br>PaymentPartyRole |                           |                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------|
|                                                                                                                                                                                                                                                                                                                |                           |                  |
|                                                                                                                                                                                                                                                                                                                |                           |                  |
|                                                                                                                                                                                                                                                                                                                |                           |                  |
|                                                                                                                                                                                                                                                                                                                |                           |                  |
|                                                                                                                                                                                                                                                                                                                |                           |                  |
|                                                                                                                                                                                                                                                                                                                |                           |                  |
|                                                                                                                                                                                                                                                                                                                |                           |                  |
|                                                                                                                                                                                                                                                                                                                |                           |                  |
|                                                                                                                                                                                                                                                                                                                | InvoiceFinancingPartyRole | InvoicePartyRole |
| InvoiceFinancingPartyRole<br>CashAccount                                                                                                                                                                                                                                                                       |                           |                  |

| InvoiceFinancingPartyRole | InvoiceFinancingTransaction |                           |
|---------------------------|-----------------------------|---------------------------|
| IntermediateAgentRole     |                             | InvoiceFinancingPartyRole |
| AcceptorConfiguration     |                             |                           |
| AcceptorConfiguration     | ApplicationIdentification   |                           |
| AcceptorConfiguration     | FinancialCapture            |                           |
| AcceptorConfiguration     | BatchTransferContent        |                           |
| AcceptorConfiguration     | ExchangePolicy              |                           |
| AcceptorConfiguration     | MaximumNumber               |                           |
| AcceptorConfiguration     | MaximumAmount               |                           |
| AcceptorConfiguration     | ReconciliationByAcquirer    |                           |
| AcceptorConfiguration     | TotalsPerCurrency           |                           |

| AcceptorConfiguration    | ProtectCardData          |  |
|--------------------------|--------------------------|--|
| AcceptorConfiguration    | RetailerParameters       |  |
| AcceptorConfiguration    | ApplicationParameters    |  |
| AcceptorConfiguration    | TerminalManagementSystem |  |
| AcceptorConfiguration    | ApplicationVersion       |  |
| TerminalManagementAction |                          |  |
| TerminalManagementAction | Type                     |  |
| TerminalManagementAction | Trigger                  |  |
| TerminalManagementAction | AdditionalProcess        |  |
| TerminalManagementAction | ActionResult             |  |
| TerminalManagementAction | ActionToProcess          |  |
| TerminalManagementAction | TerminalManagementSystem |  |
|                          |                          |  |

| NetworkAccess            |                          |
|--------------------------|--------------------------|
| NetworkAccess            | HostIPAddress            |
| NetworkAccess            | HostPortNumber           |
| NetworkAccess            | UserName                 |
| NetworkAccess            | AccessCode               |
| NetworkAccess            | ClientCertificate        |
| NetworkAccess            | TerminalManagementSystem |
| NetworkAccess            | NetworkAddress           |
| TerminalManagementSystem | System                   |
| TerminalManagementSystem | AcceptorConfiguration    |
| TerminalManagementSystem | NetworkAccess            |
| TerminalManagementSystem | CardPaymentAcquiring     |
| TerminalManagementSystem | ContactLevel             |
|                          |                          |

| TerminalManagementSystem<br>ContactDateTime<br>TerminalManagementSystem<br>TerminalManagerRole<br>TerminalManagementSystem<br>ControlledPointOfInteraction<br>TerminalManagementSystem<br>Action<br>CardPaymentStatus<br>Status<br>CardPaymentStatus<br>RejectionReason<br>CardPaymentStatus<br>FailureReason<br>CardPaymentStatus<br>CardPayment<br>AcquirerRole<br>CardPaymentPartyRole<br>AuthorisationEntity<br>CardPaymentPartyRole<br>Response<br>Response<br>ResponseReason<br>Response<br>RelatedCardPaymentValidation<br>Response<br>ResponseToAuthorisation |  |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |

| CardPaymentValidation |                                     |  |
|-----------------------|-------------------------------------|--|
| CardPaymentValidation | TransactionSuccess                  |  |
| CardPaymentValidation | MerchantOverride                    |  |
| CardPaymentValidation | ValidityDate                        |  |
| CardPaymentValidation | CardPayment                         |  |
| CardPaymentValidation | Response                            |  |
| CardPaymentValidation | AuthorisationCode                   |  |
| CardPaymentValidation | OnLineReason                        |  |
| CardPaymentValidation | Balance                             |  |
| CardPaymentValidation | CardholderAddressVerificationResult |  |
| CardPaymentValidation | CSCResult                           |  |
|                       |                                     |  |

| CardPaymentValidation | DeclinedProductCode                    |  |
|-----------------------|----------------------------------------|--|
| CardPaymentValidation | ElectronicCommerceAuthenticationResult |  |
| CardPaymentValidation | FailureReason                          |  |
| CardPaymentValidation | Signature                              |  |
| FundsCashFlow         |                                        |  |
| FundsCashFlow         | ExceptionalCashFlowIndicator           |  |
| FundsCashFlow         | FlowDirection                          |  |
| FundsCashFlow         | FundSubscriptionAccountEntry           |  |
| FundsCashFlow         | FundRedemptionAccountEntry             |  |
| FundsCashFlow         | RelatedOrder                           |  |
| FundsCashFlow         | NetIndicator                           |  |

| FundsCashFlow         | NetAssetValueCalculation         |        |
|-----------------------|----------------------------------|--------|
| FundsCashFlow         | CashFlowQuantity                 |        |
| SecuritiesOrderStatus |                                  | Status |
| SecuritiesOrderStatus | ConfirmationRejectedStatusReason |        |
| SecuritiesOrderStatus | ConfirmationStatus               |        |
| SecuritiesOrderStatus | CancellationStatus               |        |
| SecuritiesOrderStatus | PartiallySettledStatusReason     |        |
| SecuritiesOrderStatus | SuspendedStatusReason            |        |
| SecuritiesOrderStatus | ListOrderStatus                  |        |
| SecuritiesOrderStatus | SecuritiesOrder                  |        |
| SecuritiesOrderStatus | InvestmentFundOrder              |        |
| SecuritiesOrderStatus | CumulativeQuantity               |        |
| SecuritiesOrderStatus | RemainingQuantity                |        |

| SecuritiesOrderStatus | ConditionallyAcceptedStatus |                     |
|-----------------------|-----------------------------|---------------------|
| SecuritiesOrderStatus | OrderStatus                 |                     |
| RedemptionOrder       |                             | InvestmentFundOrder |
| RedemptionOrder       | HoldingsRedemptionRate      |                     |
| SwitchOrder           |                             | InvestmentFundOrder |
| SwitchOrder           | AdditionalCashIn            |                     |
| SwitchOrder           | ResultingCashOut            |                     |
| SwitchOrder           | TotalRedemptionAmount       |                     |
| SwitchOrder           | TotalSubscriptionAmount     |                     |
|                       |                             |                     |

| SwitchOrder<br>RedemptionLeg<br>SwitchOrder<br>SubscriptionLeg<br>RedemptionExecution<br>InvestmentFundOrderExecution<br>RedemptionExecution<br>RedeemedNetAmount<br>RedemptionExecution<br>PartialRedemptionWithholdingAmount<br>RedemptionExecution<br>SettlementDate<br>SubscriptionOrder<br>InvestmentFundOrder<br>SwitchExecution<br>InvestmentFundOrderExecution<br>SwitchExecution<br>RedemptionLeg<br>SwitchExecution<br>SubscriptionLeg<br>SwitchRedemptionLeg<br>RedemptionOrder<br>SwitchRedemptionLeg<br>RedemptionRelatedSwitchOrder |  |  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |

| SwitchRedemptionLeg            | PercentageOfTotalSubscriptionAmount |                       |
|--------------------------------|-------------------------------------|-----------------------|
| SwitchSubscriptionLeg          |                                     | SubscriptionOrder     |
| SwitchSubscriptionLeg          | SubscriptionRelatedSwitchOrder      |                       |
| SwitchSubscriptionLeg          | PercentageOfTotalRedemptionAmount   |                       |
| SwitchExecutionRedemptionLeg   |                                     | RedemptionExecution   |
| SwitchExecutionRedemptionLeg   | RelatedSwitchExecution              |                       |
| SwitchExecutionRedemptionLeg   | PercentageOfTotalSubscriptionAmount |                       |
| SwitchExecutionSubscriptionLeg |                                     | SubscriptionExecution |
| SwitchExecutionSubscriptionLeg | RelatedSwitchExecution              |                       |
|                                |                                     |                       |

| SwitchExecutionSubscriptionLeg | PercentageOfTotalRedemptionAmount |              |
|--------------------------------|-----------------------------------|--------------|
| NonFinancialInstitution        |                                   | Organisation |
| DebitAuthorisation             |                                   |              |
| DebitAuthorisation             | ValueDateToDebit                  |              |
| DebitAuthorisation             | DebitAuthorisationDecision        |              |
| DebitAuthorisation             | AmountToDebit                     |              |
| DebitAuthorisation             | Reason                            |              |
| DebitAuthorisation             | AuthorisedReturn                  |              |
|                                |                                   |              |

| DebitAuthorisation                 | RelatedInvestigationCaseResolution |                           |
|------------------------------------|------------------------------------|---------------------------|
| FirstAgentRole                     |                                    | InvoiceFinancingPartyRole |
| InvestigationResolution            |                                    |                           |
| InvestigationResolution            | InvestigationCase                  |                           |
| InvestigationResolution            | InvestigationCaseReference         |                           |
| PaymentInvestigationCaseResolution |                                    | InvestigationResolution   |
| PaymentInvestigationCaseResolution | InvestigationStatus                |                           |
| PaymentInvestigationCaseResolution | DebitAuthorisationConfirmation     |                           |
| PaymentInvestigationCaseResolution | CoverCorrection                    |                           |
| PaymentInvestigationCaseResolution | EntryCorrection                    |                           |

| PaymentInvestigationCaseResolution | PaymentCorrection          |  |
|------------------------------------|----------------------------|--|
| PaymentInvestigationCaseResolution | PaymentExecutionCorrection |  |
| PaymentInvestigationCaseResolution | InvestigationCaseRejection |  |
| PaymentInvestigationCaseResolution | DuplicateCase              |  |
| PaymentInvestigationCaseRejection  |                            |  |
| PaymentInvestigationCaseRejection  | RejectedModification       |  |
| PaymentInvestigationCaseRejection  | RejectedCancellation       |  |
| PaymentInvestigationCaseRejection  | RejectedCancellationReason |  |

| PaymentInvestigationCaseRejection | AssignmentCancellationConfirmation |                         |
|-----------------------------------|------------------------------------|-------------------------|
| PaymentInvestigationCaseRejection | RejectionReason                    |                         |
| PaymentInvestigationCaseRejection | RelatedInvestigationCaseResolution |                         |
| PaymentInvestigationCaseRejection | InvestigationRejection             |                         |
| Reassignment                      |                                    | InvestigationResolution |
| Reassignment                      | Justification                      |                         |
| Reassignment                      | ReassignedCase                     |                         |
| InvestigationCaseStatus           |                                    | Status                  |
| InvestigationCaseStatus           | CaseStatus                         |                         |
| InvestigationCaseStatus           | InvestigationCase                  |                         |
|                                   |                                    |                         |

| MeetingNotice            |                                   |                          |
|--------------------------|-----------------------------------|--------------------------|
| MeetingNotice            | RelatedServicing                  |                          |
| MeetingNotice            | BeneficialOwnerExclusiveIndicator |                          |
| MeetingNotice            | ParticipationMethod               |                          |
| CorporateActionPartyRole |                                   | Role                     |
| CorporateActionPartyRole | CorporateActionEvent              |                          |
| CorporateActionPartyRole | Account                           |                          |
| MeetingPartyRole         |                                   | CorporateActionPartyRole |
| MeetingPartyRole         | Meeting                           |                          |
|                          |                                   |                          |

| MeetingInitiatorRole |                           | MeetingPartyRole | Specifies a party, other than the<br>issuer, that requested that the<br>meeting take place. It may be a<br>court of justice or an association<br>of security holders.                                                                                                                                                                                                   |
|----------------------|---------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AssignedProxyRole    |                           | MeetingPartyRole | Party appointed by the rights<br>holder to attend a meeting and<br>vote in its name. The proxy can<br>be the chairman of the meeting<br>or another party selected by the<br>issuer. The proxy can also be a<br>third party selected by the rights<br>holder. The proxy can be<br>assigned by a specific instruction<br>or pre-assigned by the issuer of<br>the meeting. |
| AssignedProxyRole    | ProxyPerson               |                  | Specifies the person who is the<br>Person<br>assigned proxy for a meeting.                                                                                                                                                                                                                                                                                              |
| AssignedProxyRole    | PreAssignedProxyRole      |                  | Identifies a proxy that has been<br>assigned by the issuer of the<br>Person<br>meeting.                                                                                                                                                                                                                                                                                 |
| ProxyAppointment     |                           |                  | Specifies that a proxy has been<br>appointed to represent a party<br>authorised to vote at a general<br>meeting.                                                                                                                                                                                                                                                        |
| ProxyAppointment     | ProxyType                 |                  | Specifies the type of proxy.<br>ProxyTypeCode                                                                                                                                                                                                                                                                                                                           |
| ProxyAppointment     | RelatedMeetingInstruction |                  | Instruction in which the<br>parameters for proxy<br>InstructionForMeeting<br>appointment are included.                                                                                                                                                                                                                                                                  |
| ProxyAppointment     | Identification            |                  | Uniquely identifies a proxy card.<br>Max35Text                                                                                                                                                                                                                                                                                                                          |
| ProxyAppointment     | Vote                      |                  | Voting instructions for the proxy.<br>VoteInstructionRequest                                                                                                                                                                                                                                                                                                            |

| ProxyAppointment   | AdditionalParticipationCost           |         |
|--------------------|---------------------------------------|---------|
| ResolutionProposal |                                       |         |
| ResolutionProposal | ResolutionProposalThreshold           |         |
| ResolutionProposal | ResolutionProposalThresholdPercentage |         |
| ResolutionProposal | Meeting                               |         |
| IssuerMeeting      |                                       | Meeting |
| IssuerMeeting      | IssuerMeetingIdentification           |         |
| IssuerMeeting      | NomineePowerOfAttorneyIndicator       |         |

| IssuerMeeting             | NomineeVotingIndicator          |
|---------------------------|---------------------------------|
| IssuerMeeting             | NomineeBeneficialOwnerIndicator |
| IssuerMeeting             | ProxyVotingIndicator            |
| IssuerMeeting             | ProxyBeneficialOwnerIndicator   |
| IssuerMeeting             | ProxyPowerOfAttorneyIndicator   |
| IssuerMeeting             | ValidCreditorIndicator          |
| IssuerMeeting             | CapitalStock                    |
| ProxyAppointmentCondition |                                 |
| ProxyAppointmentCondition | NotificationAddress             |
|                           |                                 |

| ProxyAppointmentCondition | Meeting                            |
|---------------------------|------------------------------------|
| ProxyAppointmentCondition | RegistrationMethod                 |
| ProxyAppointmentCondition | AllowedProxyType                   |
| MeetingParticipation      |                                    |
| MeetingParticipation      | TotalNumberOfSecuritiesOutstanding |
| MeetingParticipation      | TotalNumberOfVotingRights          |
| MeetingParticipation      | CalculationDate                    |
| MeetingParticipation      | TotalNumberOfSecurities            |
| MeetingParticipation      | Meeting                            |
| Quorum                    |                                    |
| Quorum                    | Quantity                           |
| Quorum                    | Percentage                         |

| Quorum             | QuorumRequired             |  |
|--------------------|----------------------------|--|
| Quorum             | Meeting                    |  |
| MeetingEntitlement |                            |  |
| MeetingEntitlement | EntitlementFixingDate      |  |
| MeetingEntitlement | EntitlementRatio           |  |
| MeetingEntitlement | EligiblePosition           |  |
| MeetingEntitlement | RelatedServicing           |  |
| MeetingEntitlement | EntitlementCalculationDate |  |
| Resolution         |                            |  |
| Resolution         | IssuerLabel                |  |

| Resolution | Description                  |  |
|------------|------------------------------|--|
| Resolution | Title                        |  |
| Resolution | Type                         |  |
| Resolution | ForInformationOnly           |  |
| Resolution | SubmittedBySecurityHolder    |  |
| Resolution | ManagementRecommendation     |  |
| Resolution | NotifyingPartyRecommendation |  |
| Resolution | CastVotes                    |  |
| Resolution | Meeting                      |  |
| Resolution | VoteOptions                  |  |
| Resolution | VoteType                     |  |
|            |                              |  |

| Resolution      | VotingRightsThresholdForApproval |        |
|-----------------|----------------------------------|--------|
| Resolution      | ThresholdBasis                   |        |
| MeetingStatus   |                                  | Status |
| MeetingStatus   | MeetingResolutionStatus          |        |
| MeetingStatus   | InstructionCancellationStatus    |        |
| MeetingStatus   | Reason                           |        |
| MeetingStatus   | NotificationStatus               |        |
| MeetingStatus   | Meeting                          |        |
| VotingCondition |                                  |        |
| VotingCondition | SecuritiesQuantityRequiredToVote |        |
| VotingCondition | PartialVoteAllowed               |        |
|                 |                                  |        |

| VotingCondition | SplitVoteAllowed          |  |
|-----------------|---------------------------|--|
| VotingCondition | VoteLocation              |  |
| VotingCondition | BeneficialOwnerDisclosure |  |
| VotingCondition | IncentivePremium          |  |
| VotingCondition | VoteInstructionType       |  |
| VotingCondition | StandingVotingInstruction |  |
| VotingCondition | VotingPremiumAmount       |  |
| VotingCondition | VotingPremiumRate         |  |
| VotingCondition | Meeting                   |  |
|                 |                           |  |

| VotingCondition                | PreviousInstructionInvalidity |
|--------------------------------|-------------------------------|
| IncentivePremium               |                               |
| IncentivePremium               | PerSecurity                   |
| IncentivePremium               | PerVote                       |
| IncentivePremium               | PerAttendee                   |
| IncentivePremium               | Description                   |
| IncentivePremium               | PremiumAmount                 |
| IncentivePremium               | PaymentDate                   |
| IncentivePremium               | Meeting                       |
| IncentivePremium               | CorporateActionDistribution   |
| SecuritiesRegistrationDeadline | Deadline                      |
| SecuritiesRegistrationDeadline | RegistrationDate              |

| RegistrationBeneficiary     |                    | MeetingPartyRole         |
|-----------------------------|--------------------|--------------------------|
| PowerOfAttorneyRequirements |                    |                          |
| PowerOfAttorneyRequirements | LegalRequirement   |                          |
| PowerOfAttorneyRequirements | OtherDocumentation |                          |
| PowerOfAttorneyRequirements | PowerOfAttorney    |                          |
| PowerOfAttorneyRequirements | Meeting            |                          |
| CorporateActionAgent        |                    | CorporateActionPartyRole |
| CorporateActionAgent        | AgentRole          |                          |
| MeetingDeadline             |                    | Deadline                 |

| MeetingParticipationRegistrationDeadline |                                    | MeetingDeadline |
|------------------------------------------|------------------------------------|-----------------|
| AdditionalRight                          |                                    |                 |
| AdditionalRight                          | Meeting                            |                 |
| AdditionalRight                          | Type                               |                 |
| AdditionalRight                          | AdditionalRightThreshold           |                 |
| AdditionalRight                          | AdditionalRightThresholdPercentage |                 |
| MeetingStatusReason                      |                                    | StatusReason    |
|                                          |                                    |                 |

| MeetingStatusReason    | MeetingCancellationReason  |                  |
|------------------------|----------------------------|------------------|
| MeetingStatusReason    | MeetingStatus              |                  |
| MeetingStatusReason    | InstructionRejectionReason |                  |
| MeetingAttendeeRole    |                            | MeetingPartyRole |
| MeetingAttendeeRole    | Person                     |                  |
| VoteInstructionRequest |                            |                  |
| VoteInstructionRequest | MeetingInstruction         |                  |
| VoteInstructionRequest | VotePerResolution          |                  |
| VoteInstructionRequest | Discretionary              |                  |
| VoteInstructionRequest | GlobalVoteInstruction      |                  |
|                        |                            |                  |

| VoteInstructionRequest | VoteForMeetingResolution  |  |
|------------------------|---------------------------|--|
| VoteInstructionRequest | VoteExecutionConfirmation |  |
| VoteInstructionRequest | RelatedProxyAppointment   |  |
| InstructionForMeeting  |                           |  |
| InstructionForMeeting  | VoteInstruction           |  |
| InstructionForMeeting  | RequestedExecutionDate    |  |
| InstructionForMeeting  | RelatedServicing          |  |
| InstructionForMeeting  | MeetingAttendance         |  |
| InstructionForMeeting  | ProxyAppointment          |  |
| InstructionForMeeting  | MeetingIdentification     |  |
| InstructionForMeeting  | SecuritiesRegistration    |  |
|                        |                           |  |

| InstructionForMeeting | BlockingSecurities        |  |
|-----------------------|---------------------------|--|
| InstructionForMeeting | ParticipationRegistration |  |
| InstructionForMeeting | SafekeepingAccount        |  |
| Vote                  |                           |  |
| Vote                  | VoteRequest               |  |
| Vote                  | For                       |  |
| Vote                  | Against                   |  |
| Vote                  | Abstain                   |  |
| Vote                  | Withhold                  |  |
| Vote                  | WithManagement            |  |
| Vote                  | AgainstManagement         |  |
| Vote                  | Resolution                |  |
| Vote                  | NoAction                  |  |

| Vote           | Result              |  |
|----------------|---------------------|--|
| Vote           | TwoYears            |  |
| Vote           | OneYear             |  |
| Vote           | Withdrawn           |  |
| Vote           | ThreeYears          |  |
| Vote           | Blank               |  |
| Vote           | VoteReceiptDateTime |  |
| AttendanceCard |                     |  |

| AttendanceCard    | AttendanceCardLabelling  |  |
|-------------------|--------------------------|--|
| AttendanceCard    | MeetingAttendance        |  |
| AttendanceCard    | DeliveryMethod           |  |
| AttendanceCard    | DeliveryPlace            |  |
| MeetingAttendance |                          |  |
| MeetingAttendance | AttendanceCard           |  |
| MeetingAttendance | PercentageOfVotingRights |  |
| MeetingAttendance | RelatedMeeting           |  |
| VoteResult        |                          |  |
| VoteResult        | Vote                     |  |
| VoteResult        | Accepted                 |  |

| VoteResult                     | VoteDissemination  |  |
|--------------------------------|--------------------|--|
| VoteResult                     | TotalVotesCast     |  |
| VoteResult                     | ModalityOfCounting |  |
| CorporateActionOptionServicing |                    |  |
| CorporateActionOptionServicing | RelatedOption      |  |
| CorporateActionOptionServicing | RelatedServicing   |  |
| Distribution                   |                    |  |
| Distribution                   | ExercisePeriod     |  |
| Distribution                   | OfferPeriod        |  |
| Distribution                   | TradingPeriod      |  |
|                                |                    |  |

| Distribution<br>BlockingPeriod<br>Distribution<br>InterestPeriod<br>Distribution<br>DistributionTax<br>Distribution<br>OfferPrice<br>Distribution<br>IncentivePremium<br>Distribution<br>EffectiveDate<br>Distribution<br>EventConditions<br>Distribution<br>ExDate<br>Distribution<br>GrossRate |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                  |  |  |
|                                                                                                                                                                                                                                                                                                  |  |  |

| Distribution     | MeetingDate           |              |
|------------------|-----------------------|--------------|
| Distribution     | NetRate               |              |
| Distribution     | NewFaceValue          |              |
| Distribution     | NewParValue           |              |
| Distribution     | PaymentDate           |              |
| Distribution     | Dividend              |              |
| Distribution     | CorporateActionOption |              |
| Distribution     | CurrencyOption        |              |
| Distribution     | DecreaseAmount        |              |
| Distribution     | DecreaseRate          |              |
| Distribution     | OfferPriceFixingDate  |              |
| CashDistribution |                       | Distribution |

| CashDistribution | DistributionCurrencyExchangeInformation |  |
|------------------|-----------------------------------------|--|
| CashDistribution | SecuritiesAndCashDistribution           |  |
| CashDistribution | AmortisedRate                           |  |
| CashDistribution | Rate                                    |  |
| CashDistribution | CashIndemnityRate                       |  |
| CashDistribution | DividendReinvestmentIndicator           |  |
| CashDistribution | InterestAmount                          |  |
| CashDistribution | InterestRate                            |  |
| CashDistribution | LoyaltyPremiumIndicator                 |  |

| CashDistribution                        | PaymentType                   |
|-----------------------------------------|-------------------------------|
| CashDistribution                        | SelectionDate                 |
| CashDistribution                        | CashDistributionRate          |
| CashDistribution                        | CashDistributionAmount        |
| AgentCorporateActionStandingInstruction | StandingSettlementInstruction |
| AgentCorporateActionStandingInstruction | StandingInstructionType       |
| AgentCorporateActionStandingInstruction | GrossOrNetIndicator           |
| AgentCorporateActionStandingInstruction | RelatedDeliveryInstructions   |
| AgentCorporateActionStandingInstruction | Security                      |
|                                         |                               |

| CollateralStatus |                                        | Status |
|------------------|----------------------------------------|--------|
| CollateralStatus | ResponseStatus                         |        |
| CollateralStatus | CollateralManagementCancellationReason |        |
| CollateralStatus | SubstitutionStatus                     |        |
| CollateralStatus | InterestRejectionReason                |        |
| CollateralStatus | MarginCallResponse                     |        |
| CollateralStatus | Settlement                             |        |
| CollateralStatus | CancellationReason                     |        |
| CollateralStatus | Collateral                             |        |

| PaymentInitiation           |                    | PaymentExecution     |
|-----------------------------|--------------------|----------------------|
| NonDeliverableTrade         |                    | ForeignExchangeTrade |
| NonDeliverableTrade         | SettlementCurrency |                      |
| NonDeliverableTrade         | FixingConditions   |                      |
| NonDeliverableTrade         | OpeningLeg         |                      |
| NonDeliverableTrade         | ClosingLeg         |                      |
| TreasurySettlementPartyRole |                    | SettlementPartyRole  |

| TreasurySettlementPartyRole | TreasuryTrade            |               |
|-----------------------------|--------------------------|---------------|
| CurrencyOption              |                          | TreasuryTrade |
| CurrencyOption              | CallAmount               |               |
| CurrencyOption              | PutAmount                |               |
| CurrencyOption              | PremiumCalculation       |               |
| CurrencyOption              | OptionDefinition         |               |
| CurrencyOption              | PremiumSettlement        |               |
| CurrencyOption              | ExercisedOption          |               |
| CurrencyOption              | OptionSettlementCurrency |               |
| CurrencyOption              | StrikeRate               |               |

| PremiumCalculation        |                        |           |
|---------------------------|------------------------|-----------|
| PremiumCalculation        | Option                 |           |
| PremiumCalculation        | PercentageOfCallAmount |           |
| PremiumCalculation        | PercentageOfPutAmount  |           |
| PremiumCalculation        | PointsOfCallAmount     |           |
| PremiumCalculation        | PointsOfPutAmount      |           |
| InvoiceFinancingAgreement |                        | Agreement |

| InvoiceFinancingAgreement | Authorisation             |  |
|---------------------------|---------------------------|--|
| InvoiceFinancingAgreement | FinancingMethod           |  |
| InvoiceFinancingAgreement | RequestedAmount           |  |
| InvoiceFinancingAgreement | RequestedPercentage       |  |
| InvoiceFinancingAgreement | AppliedPercentage         |  |
| InvoiceFinancingAgreement | FinancedAmount            |  |
| InvoiceFinancingAgreement | Identification            |  |
| InvoiceFinancingAgreement | InvoiceFinancingPartyRole |  |
|                           |                           |  |

| InvoiceFinancingAgreement | InvoiceFinancingStatus |                           |
|---------------------------|------------------------|---------------------------|
| InvoiceFinancingAgreement | Invoice                |                           |
| InvoiceFinancingAgreement | ResultingCashEntry     |                           |
| InvoiceFinancingAgreement | Assignment             |                           |
| FinancingRequestorRole    |                        | InvoiceFinancingPartyRole |
| CommercialTrade           |                        | Trade                     |
| CommercialTrade           | PurchaseAccount        |                           |
| CommercialTrade           | PaymentObligation      |                           |
| CommercialTrade           | TotalAcceptedAmount    |                           |
| CommercialTrade           | PartyRole              |                           |
| CommercialTrade           | TradeSettlement        |                           |
|                           |                        |                           |

| CommercialTrade | ProductDeliveryObligation |  |
|-----------------|---------------------------|--|
| CommercialTrade | PurchaseOrder             |  |
| CommercialTrade | Documents                 |  |
| CommercialTrade | RelatedUndertaking        |  |
| CommercialTrade | TransactionStatus         |  |
| CommercialTrade | Agreement                 |  |
| LineItem        |                           |  |
| LineItem        | FinancialAdjustment       |  |
| LineItem        | LogisticsCharge           |  |
| LineItem        | GrossAmount               |  |
| LineItem        | Identification            |  |

| LineItem | InvoicedProduct                     |  |
|----------|-------------------------------------|--|
| LineItem | NetWeight                           |  |
| LineItem | BilledQuantity                      |  |
| LineItem | ChargeFreeQuantity                  |  |
| LineItem | MeasureQuantityStartRelatedLineItem |  |
| LineItem | MeasureQuantityEndRelatedLineItem   |  |
| LineItem | MeasureDateTimeStart                |  |
| LineItem | MeasureDateTimeEnd                  |  |
| LineItem | Invoice                             |  |
| LineItem | NetAmount                           |  |
| LineItem | Packaging                           |  |
| LineItem | DeliveryDateTime                    |  |

| LineItem               | Charges                  |        |
|------------------------|--------------------------|--------|
| LineItem               | NetPriceCharge           |        |
| LineItem               | GrossPriceQuantity       |        |
| LineItem               | NetPriceQuantity         |        |
| LineItem               | GrossWeight              |        |
| InvoiceFinancingStatus |                          | Status |
| InvoiceFinancingStatus | ValidationStatusReason   |        |
| InvoiceFinancingStatus | ValidationStatus         |        |
| InvoiceFinancingStatus | CancellationStatus       |        |
| InvoiceFinancingStatus | CancellationStatusReason |        |

| InvoiceFinancingStatus | FinancingTransactionStatus  |  |
|------------------------|-----------------------------|--|
| InvoiceFinancingStatus | CancellationRequestReason   |  |
| InvoiceFinancingStatus | InvoiceFinancingTransaction |  |
| InvoiceFinancingStatus | FinancingStatusReason       |  |
| Transport              |                             |  |
| Transport              | Incoterms                   |  |
| Transport              | Identification              |  |
| Transport              | Packaging                   |  |
| Transport              | ArrivalDateTime             |  |
| Transport              | PartialShipment             |  |
| Transport              | TransShipment               |  |
|                        |                             |  |

| Transport | ProductDelivery                |  |
|-----------|--------------------------------|--|
| Transport | PlaceOfDeparture               |  |
| Transport | PlaceOfDestination             |  |
| Transport | TransportCharges               |  |
| Transport | FreightChargesPrepaidOrCollect |  |
| Transport | ShipmentDates                  |  |
| Transport | TransportedGoods               |  |
| Transport | PartyRole                      |  |
| Transport | TransitLocation                |  |
| Transport | TransportDocuments             |  |
|           |                                |  |

| Incoterms |           |         |
|-----------|-----------|---------|
| Incoterms | Transport |         |
| Incoterms | Code      |         |
| Incoterms | Location  |         |
| Goods     |           | Product |
| Goods     | Transport |         |

| Goods           | Analysis                |                      |
|-----------------|-------------------------|----------------------|
| Goods           | HealthCheck             |                      |
| Goods           | PhytosanitaryInspection |                      |
| Goods           | PartyRole               |                      |
| ProductDelivery |                         | ObligationFulfilment |
| ProductDelivery | DeliveryPeriod          |                      |
| ProductDelivery | Routing                 |                      |
| ProductDelivery | TradeSettlement         |                      |
| ProductDelivery | Obligation              |                      |
| ProductDelivery | TradeCertificate        |                      |
|                 |                         |                      |

| ProductDelivery<br>InsuranceCertificate<br>ProductDelivery<br>Product<br>CommercialTradePartyRole<br>TradePartyRole<br>CommercialTradePartyRole<br>CommercialTrade<br>ShipFrom<br>CommercialTradePartyRole<br>ShipTo<br>CommercialTradePartyRole<br>Packaging<br>Packaging<br>Quantity<br>Packaging<br>PerPackageUnitQuantity<br>Packaging<br>Transport<br>Packaging<br>PackagingName<br>Packaging<br>TotalConsignmentQuantity |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |  |  |

| Packaging                 | TotalVolume     |                    |
|---------------------------|-----------------|--------------------|
| Packaging                 | TotalWeight     |                    |
| Packaging                 | RelatedLineItem |                    |
| Packaging                 | PackageType     |                    |
| TransportPartyRole        |                 | Role               |
| TransportPartyRole        | Transport       |                    |
| Consignor                 |                 | TransportPartyRole |
| Consignee                 |                 | TransportPartyRole |
| CommercialTradeSettlement |                 | Settlement         |
| CommercialTradeSettlement | Payment         |                    |
| CommercialTradeSettlement | Invoice         |                    |
| CommercialTradeSettlement | LetterOfCredit  |                    |
|                           |                 |                    |

| CommercialTradeSettlement | ProductDelivery   |                  |
|---------------------------|-------------------|------------------|
| CommercialTradeSettlement | CommercialTrade   |                  |
| InvoicerRole              |                   | InvoicePartyRole |
| Allowance                 |                   | Adjustment       |
| Allowance                 | TotalAllowance    |                  |
| Allowance                 | NetPriceAllowance |                  |
| ProductCharacteristics    |                   |                  |
| ProductCharacteristics    | Product           |                  |
| ProductCharacteristics    | Characteristics   |                  |
| ProductCharacteristics    | Type              |                  |
| BaselineStatus            |                   | Status           |
| BaselineStatus            | Status            |                  |
| BaselineStatus            | CommercialTrade   |                  |
|                           |                   |                  |

| ShipmentDateRange |                      |           |
|-------------------|----------------------|-----------|
| ShipmentDateRange | LatestShipmentDate   |           |
| ShipmentDateRange | RelatedTransport     |           |
| ShipmentDateRange | EarliestShipmentDate |           |
| ShipmentDateRange | ShipmentDate         |           |
| TransportByAir    |                      | Transport |
| TransportByAir    | AirportName          |           |
| TransportByAir    | FlightNumber         |           |
| TransportBySea    |                      | Transport |
| TransportBySea    | VesselName           |           |
| TransportBySea    | VoyageNumber         |           |
| TransportBySea    | ChartererName        |           |
| TransportBySea    | MasterName           |           |
|                   |                      |           |

| TransportBySea   | OwnerName                 |
|------------------|---------------------------|
|                  |                           |
| TransportBySea   | IMONumber                 |
|                  |                           |
| TransportByRoad  | Transport                 |
| TransportByRail  | Transport                 |
| TransportByRail  | CarriageIdentification    |
| TradeCertificate | Document                  |
| TradeCertificate | CertificateType           |
| TradeCertificate | InspectionDate            |
| TradeCertificate | TradeCertificatePartyRole |
| TradeCertificate | ProductDelivery           |

| PurchaseOrder       |                          | Order              |
|---------------------|--------------------------|--------------------|
| PurchaseOrder       | TotalAmount              |                    |
| PurchaseOrder       | ResultingCommercialTrade |                    |
| PurchaseOrder       | Product                  |                    |
| PurchaseOrder       | Identification           |                    |
| InsurancePartyRole  |                          | Role               |
| InsurancePartyRole  | InsuranceCertificate     |                    |
| Assured             |                          | InsurancePartyRole |
| Assured             | AssuredType              |                    |
| CollateralAgreement |                          | Agreement          |
| CollateralAgreement | BaseCurrency             |                    |
|                     |                          |                    |

| CollateralAgreement | AssociatedMasterAgreement      |                     |
|---------------------|--------------------------------|---------------------|
| CollateralAgreement | StandingSettlementInstructions |                     |
| CollateralAgreement | MarginConvention               |                     |
| CollateralAgreement | ExposureTerm                   |                     |
| CollateralAgreement | CallFrequency                  |                     |
| CollateralAgreement | Collateral                     |                     |
| CollateralAgreement | RiskCoverage                   |                     |
| CollateralPartyRole |                                | Role                |
| CollateralPartyRole | Collateral                     |                     |
| ServicingPartyRole  |                                | CollateralPartyRole |

| MarginCall |                                         |  |
|------------|-----------------------------------------|--|
| MarginCall | MarginCallValuationDate                 |  |
| MarginCall | AgreedAmount                            |  |
| MarginCall | VariationMargin                         |  |
| MarginCall | SegregatedIndependentAmount             |  |
| MarginCall | DefaultFundContribution                 |  |
| MarginCall | ExpectedVariationMarginType             |  |
| MarginCall | ExpectedSegregatedIndependentAmountType |  |
| MarginCall | TotalMarkToMarket                       |  |
| MarginCall | MarkToMarketNetted                      |  |
|            |                                         |  |

| MarginCall | MarkToMarketGross                    |  |
|------------|--------------------------------------|--|
| MarginCall | MarkToMarketFails                    |  |
| MarginCall | FailsHaircut                         |  |
| MarginCall | InitialMargin                        |  |
| MarginCall | IncreaseCoverage                     |  |
| MarginCall | CollateralisedMarginAccountIndicator |  |
| MarginCall | CollateralMovement                   |  |
| MarginCall | RelatedManagementProcess             |  |
| MarginCall | Security                             |  |

| MarginCall         | MarginProduct              |  |
|--------------------|----------------------------|--|
| MarginCall         | MarginType                 |  |
| MarginCall         | TotalMarginAmount          |  |
| CollateralProposal |                            |  |
| CollateralProposal | ProposedCollateralMovement |  |
| CollateralProposal | ResponseType               |  |
| CollateralProposal | Type                       |  |
| CollateralProposal | RelatedManagementProcess   |  |
| CollateralMovement |                            |  |
| CollateralMovement | RelatedCollateralProposal  |  |
|                    |                            |  |

| CollateralMovement | VariationMargin              |           |
|--------------------|------------------------------|-----------|
| CollateralMovement | SegregatedIndependentAmount  |           |
| CollateralMovement | MarginCall                   |           |
| CollateralMovement | SecuritiesCollateralMovement |           |
| CollateralMovement | CashCollateralMovement       |           |
| CollateralMovement | FinancialTransaction         |           |
| MasterAgreement    |                              | Agreement |
| MasterAgreement    | CollateralAgreement          |           |
| MasterAgreement    | MasterAgreementType          |           |
|                    |                              |           |

| MasterAgreement      | GovernedTrades      |  |
|----------------------|---------------------|--|
| MasterAgreement      | GovernedContract    |  |
| MasterAgreement      | GoverningLaw        |  |
| CollateralManagement |                     |  |
| CollateralManagement | CollateralProposal  |  |
| CollateralManagement | CollateralValuation |  |
| CollateralManagement | FeesAndCommissions  |  |
| CollateralManagement | InterestManagement  |  |
| CollateralManagement | DisputeManagement   |  |
| CollateralManagement | MarginCall          |  |
|                      |                     |  |

| CollateralManagement | CollateralSubstitution |       |
|----------------------|------------------------|-------|
| CollateralManagement | RiskToCover            |       |
| CollateralManagement | Collateral             |       |
| CollateralManagement | AgreedTerms            |       |
| CollateralManagement | ClearingSystem         |       |
| Money                |                        | Asset |
| Money                | CashAmount             |       |
| Deposit              |                        | Money |
| Deposit              | DepositType            |       |
|                      |                        |       |

| Deposit<br>Interest<br>LetterOfCredit<br>Asset<br>LetterOfCredit<br>Amount<br>LetterOfCredit<br>Document<br>LetterOfCredit<br>CommercialTradeSettlement<br>Guarantee<br>Asset<br>Guarantee<br>CoveredAmount<br>Guarantee<br>EffectivePeriod<br>Guarantee<br>GuaranteeType |  |  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                           |  |  |
|                                                                                                                                                                                                                                                                           |  |  |
|                                                                                                                                                                                                                                                                           |  |  |
|                                                                                                                                                                                                                                                                           |  |  |
|                                                                                                                                                                                                                                                                           |  |  |
|                                                                                                                                                                                                                                                                           |  |  |
|                                                                                                                                                                                                                                                                           |  |  |
|                                                                                                                                                                                                                                                                           |  |  |
|                                                                                                                                                                                                                                                                           |  |  |

| Guarantee              | CoveredPercentage        |  |
|------------------------|--------------------------|--|
| Guarantee              | Document                 |  |
| Guarantee              | GuaranteedTrade          |  |
| Guarantee              | ExcessAmount             |  |
| Guarantee              | GuaranteePartyRole       |  |
| CollateralSubstitution |                          |  |
| CollateralSubstitution | Type                     |  |
| CollateralSubstitution | AcceptedAmount           |  |
| CollateralSubstitution | RejectedAmount           |  |
| CollateralSubstitution | RelatedManagementProcess |  |
| CollateralSubstitution | NewCollateral            |  |
|                        |                          |  |

| CollateralBalance   |                                                   |  |
|---------------------|---------------------------------------------------|--|
| CollateralBalance   | CollateralDescription                             |  |
| CollateralBalance   | HeldAmount                                        |  |
| CollateralBalance   | PriorAgreed                                       |  |
| CollateralBalance   | VariationMarginRelatedRiskCalculation             |  |
| CollateralBalance   | InTransit                                         |  |
| CollateralBalance   | SegregatedIndependentAmountRelatedRiskCalculation |  |
| CollateralBalance   | RelatedCollateralInterestManagement               |  |
| CollateralBalance   | CollateralInterestManagement                      |  |
| ExposureCalculation |                                                   |  |

| ExposureCalculation | TotalCollateralCurrentValue        |  |
|---------------------|------------------------------------|--|
| ExposureCalculation | TotalExposedAmount                 |  |
| ExposureCalculation | CurrentIndependentAmount           |  |
| ExposureCalculation | CurrentVariationMargin             |  |
| ExposureCalculation | CurrentSegregatedIndependentAmount |  |
| ExposureCalculation | VariationMarginAmountRequirement   |  |
| ExposureCalculation | SegregatedAmountRequirement        |  |

| ExposureCalculation | CollateralManagement        |  |
|---------------------|-----------------------------|--|
| ExposureCalculation | CounterpartyRisk            |  |
| ExposureCalculation | TransactionRisk             |  |
| ExposureCalculation | TotalCollateralAfterHaircut |  |
| DisputeManagement   |                             |  |
| DisputeManagement   | DisputedAmount              |  |
| DisputeManagement   | DisputeDate                 |  |
| DisputeManagement   | DisputeResolutionType       |  |
| DisputeManagement   | RelatedManagementProcess    |  |
|                     |                             |  |

| IndependentAmount     |                                  |              |
|-----------------------|----------------------------------|--------------|
| IndependentAmount     | RelatedRiskCalculation           |              |
| IndependentAmount     | IndependentAmountPerTrade        |              |
| IndependentAmount     | IndependentAmountValueAtRisk     |              |
| IndependentAmount     | IndependentAmountNetOpenPosition |              |
| IndependentAmountTerm |                                  | ExposureTerm |

| IndependentAmountTerm   | Convention                                  |              |
|-------------------------|---------------------------------------------|--------------|
| VariationMarginTerm     |                                             | ExposureTerm |
| VariationMarginTerm     | ThresholdAmount                             |              |
| VariationMarginTerm     | ThresholdType                               |              |
| MarginAmountRequirement |                                             |              |
| MarginAmountRequirement | VariationMarginAmountRequirementCalculation |              |
|                         |                                             |              |

| MarginAmountRequirement | DeliverMarginAmount                    |  |
|-------------------------|----------------------------------------|--|
| MarginAmountRequirement | ReturnMarginAmount                     |  |
| MarginAmountRequirement | SegregatedAmountRequirementCalculation |  |
| MarginAmountRequirement | IntraDayMarginCall                     |  |
| MarginAmountRequirement | PeakInitialMarginLiability             |  |
| MarginAmountRequirement | AggregatePeakLiability                 |  |
| MarginAmountRequirement | PeakVariationMarginLiability           |  |

| DefaultFundContribution |                            |  |
|-------------------------|----------------------------|--|
|                         |                            |  |
| DefaultFundContribution | RelatedMarginCall          |  |
| DefaultFundContribution | DefaultFund                |  |
| DefaultFundContribution | ExcessOrDeficitAmount      |  |
| DefaultFundContribution | ContributionAccount        |  |
| DefaultFundContribution | AmountDirection            |  |
| ExpectedCollateralType  |                            |  |
| ExpectedCollateralType  | VariationMarginRelatedCall |  |
| ExpectedCollateralType  | Delivery                   |  |
|                         |                            |  |

| ExpectedCollateralType | Return                                 |  |
|------------------------|----------------------------------------|--|
| ExpectedCollateralType | SegregatedIndependentAmountRelatedCall |  |
| PortfolioValuation     |                                        |  |
| PortfolioValuation     | TotalPortfolioValue                    |  |
| PortfolioValuation     | TotalBookValue                         |  |
| PortfolioValuation     | TotalReceipts                          |  |
| PortfolioValuation     | TotalDisbursements                     |  |
| PortfolioValuation     | IncomeReceived                         |  |
| PortfolioValuation     | ExpensesPaid                           |  |
| PortfolioValuation     | Portfolio                              |  |
| PortfolioValuation     | ValuationPeriod                        |  |
|                        |                                        |  |

| BuyIn          | ObligationFulfilment             |
|----------------|----------------------------------|
| BuyIn          | SecuritiesCompensation           |
| BuyIn          | BuyinDate                        |
| BuyIn          | BuyInPrice                       |
| BuyIn          | Fees                             |
| BuyIn          | CashCompensation                 |
| BuyIn          | RelatedSecuritiesClearingProcess |
| ThirdPartyRole | SystemPartyRole                  |

| NonClearingMemberRole |                              | ThirdPartyRole |
|-----------------------|------------------------------|----------------|
| DefaultFund           |                              |                |
| DefaultFund           | TotalAmount                  |                |
| DefaultFund           | Contribution                 |                |
| DefaultFund           | ClearingSystem               |                |
| SidePocket            |                              |                |
| SidePocket            | SidePocketInclusionIndicator |                |

| SidePocket                       | SidePocketIdentification |                    |
|----------------------------------|--------------------------|--------------------|
| SidePocket                       | InvestmentAccount        |                    |
| SidePocket                       | SidePocketQuantity       |                    |
| CollateralInterestAdministration |                          | InterestManagement |
| CollateralInterestAdministration | CollateralManagement     |                    |
| CollateralInterestAdministration | ClosingCollateralBalance |                    |
| CollateralInterestAdministration | OpeningCollateralBalance |                    |
| ClearingExceptionPartyRole       |                          | TradePartyRole     |
| ReportingPartyRole               |                          | Role               |

| ReportingPartyRole  | RegulatoryReport   |                   |
|---------------------|--------------------|-------------------|
| MatchingSystem      |                    | System            |
| Garnishment         |                    | PaymentObligation |
| Penalty             |                    | Adjustment        |
| Penalty             | PenaltyBasisAmount |                   |
| AccountEntry        |                    | CreditInstrument  |
| ShareholderRegister |                    |                   |
| ShareholderRegister | Identification     |                   |
| ShareholderRegister | Entry              |                   |
| WarrantAgent        |                    | AssetPartyRole    |
|                     |                    |                   |

| LegalRepresentative |               | Role                 |
|---------------------|---------------|----------------------|
| CapitalValue        |               |                      |
| CapitalValue        | Capital       |                      |
| Capital             |               |                      |
| Capital             | AssetIssuance |                      |
| Capital             | Date          |                      |
| Capital             | Type          |                      |
| Capital             | Amount        |                      |
| Capital             | Unit          |                      |
| SchemeOwner         |               | InformationPartyRole |
| Cashier             |               | CardPaymentPartyRole |

| Cashier                  | ShiftNumber                |                               |
|--------------------------|----------------------------|-------------------------------|
| Reconciliation           |                            |                               |
| Reconciliation           | System                     |                               |
| Reconciliation           | Document                   |                               |
| Reconciliation           | ReconciledTrades           |                               |
| Reconciliation           | Account                    |                               |
| SSIDatabaseProvider      |                            | SettlementPartyRole           |
| SSIDatabaseProvider      | StandingSettlementDatabase |                               |
| PortfolioManagerRole     |                            | AssetPartyRole                |
| LocalSettlementAgentRole |                            | SecuritiesSettlementPartyRole |
| ChequePartyRole          |                            | Role                          |

| ChequePartyRole | Cheque                   |                 |
|-----------------|--------------------------|-----------------|
| Payee           |                          | ChequePartyRole |
| Liquidity       |                          |                 |
| Liquidity       | Quantity                 |                 |
| Liquidity       | ListTrading              |                 |
| Liquidity       | IndicatorType            |                 |
| Liquidity       | Upper                    |                 |
| Liquidity       | Lower                    |                 |
| Liquidity       | Value                    |                 |
| Liquidity       | WeightedAverageLiquidity |                 |
|                 |                          |                 |

| SecuritiesOrderParameters |                                 | Parameters of the transfer of a<br>financial instrument.                                                                                                                                                                                                                                             |
|---------------------------|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SecuritiesOrderParameters | MinimumQuantity                 | Minimum quantity of financial<br>instrument to be bought or sold<br>if the entire order cannot be<br>executed.                                                                                                                                                                                       |
| SecuritiesOrderParameters | MatchIncrement                  | Allows orders to specify a<br>minimum quantity that applies to<br>every execution. (one execution<br>could be for multiple counter<br>orders). The order may still fill<br>against smaller orders, but the<br>cumulative quantity of the<br>execution must be in multiples of<br>the MatchIncrement. |
| SecuritiesOrderParameters | PegInstructions                 | Additional instructions if the<br>SecuritiesPegOrderInstruction<br>order is pegged.                                                                                                                                                                                                                  |
| SecuritiesOrderParameters | PreviousClosingPrice            | Previous closing price of security.<br>SecuritiesPricing                                                                                                                                                                                                                                             |
| SecuritiesOrderParameters | AutoRouting                     | Indicates whether an automatic<br>AutoRoutingCode<br>routing system is involved.                                                                                                                                                                                                                     |
| SecuritiesOrderParameters | CorporateActionOptionIndicator  | Indicates the possible options or<br>choices available to account<br>IncomePreferenceCode<br>owner (for investment funds).                                                                                                                                                                           |
| SecuritiesOrderParameters | ExecutionTimeLimit              | Indicates from/until when an<br>ExecutionTimeLimitCode<br>order must be executed.                                                                                                                                                                                                                    |
| SecuritiesOrderParameters | PreAllocationConditionIndicator | Indicates the conditions that<br>Max16Text<br>apply to a pre-allocation.                                                                                                                                                                                                                             |
| SecuritiesOrderParameters | PriorityIndicator               | Indicates the execution priority<br>PriorityCode<br>of the trade.                                                                                                                                                                                                                                    |
|                           |                                 |                                                                                                                                                                                                                                                                                                      |

| SecuritiesOrderParameters | RequestedDealCurrency    |  |
|---------------------------|--------------------------|--|
| SecuritiesOrderParameters | OrderHandlingInstruction |  |
| SecuritiesOrderParameters | StockLocateRequired      |  |
| SecuritiesOrderParameters | WorkingIndicator         |  |
| SecuritiesOrderParameters | BookPriorityIndicator    |  |
| SecuritiesOrderParameters | MaxPriceLevels           |  |

| SecuritiesOrderParameters | PreTradeAnonymity           |  |
|---------------------------|-----------------------------|--|
| SecuritiesOrderParameters | GoodTillBooking             |  |
| SecuritiesOrderParameters | ManualOrderIndicator        |  |
| SecuritiesOrderParameters | DirectedOrder               |  |
| SecuritiesOrderParameters | ReceivedDepartment          |  |
| SecuritiesOrderParameters | CustomerHandlingInstruction |  |
| SecuritiesOrderParameters | ProcessCode                 |  |
| SecuritiesOrderParameters | RelatedSecuritiesOrder      |  |
|                           |                             |  |

| Quote |                      |  |
|-------|----------------------|--|
| Quote | MaximumQuantity      |  |
| Quote | Quantity             |  |
| Quote | MinimumQuantity      |  |
| Quote | PartyRole            |  |
| Quote | RelatedNegotiation   |  |
| Quote | QuotedRate           |  |
| Quote | PreviousClosingPrice |  |
| Quote | RequestedPrice       |  |
| Quote | Price                |  |
|       |                      |  |

| Quote   | MarketPrice            |                      |
|---------|------------------------|----------------------|
| Quote   | MidSideQuoteVariable   |                      |
| Quote   | BidSideQuoteVariable   |                      |
| Quote   | OfferSideQuoteVariable |                      |
| Quote   | SecurityQuoteVariable  |                      |
| Quote   | QuoteSwap              |                      |
| Quote   | ValidUntilDateTime     |                      |
| Quote   | Currency               |                      |
| Quote   | Status                 |                      |
| Quote   | QuotedSecurity         |                      |
| PairOff |                        | ObligationFulfilment |
| PairOff | PairedOffQuantity      |                      |

| PairOff                       | RelatedSecuritiesSettlement         |              |
|-------------------------------|-------------------------------------|--------------|
| SecuritiesAndCashDistribution |                                     | Distribution |
| SecuritiesAndCashDistribution | IntermediateToUnderlyingDenominator |              |
| SecuritiesAndCashDistribution | MaximumHolding                      |              |
| SecuritiesAndCashDistribution | MaximumExercisableQuantity          |              |
| SecuritiesAndCashDistribution | MinimumExercisableQuantity          |              |
| SecuritiesAndCashDistribution | DistributedToUnderlyingDenominator  |              |
| SecuritiesAndCashDistribution | IntermediateToUnderlyingNumerator   |              |
| SecuritiesAndCashDistribution | MinimumHolding                      |              |
| SecuritiesAndCashDistribution | DistributedToUnderlyingNumerator    |              |

| SecuritiesAndCashDistribution | SecuritiesDistribution              |              |
|-------------------------------|-------------------------------------|--------------|
| SecuritiesAndCashDistribution | CashDistribution                    |              |
| SecuritiesDistribution        |                                     | Distribution |
| SecuritiesDistribution        | MaximumHolding                      |              |
| SecuritiesDistribution        | IntermediateToUnderlyingNumerator   |              |
| SecuritiesDistribution        | IntermediateToUnderlyingDenominator |              |
| SecuritiesDistribution        | DistributedToUnderlyingDenominator  |              |
| SecuritiesDistribution        | DistributedToUnderlyingNumerator    |              |
| SecuritiesDistribution        | MinimumHolding                      |              |

| SecuritiesDistribution | CashFractionsPrice             |  |
|------------------------|--------------------------------|--|
| SecuritiesDistribution | SubscriptionPrice              |  |
| SecuritiesDistribution | ReinvestmentPrice              |  |
| SecuritiesDistribution | IntermediateSecurityExpiryDate |  |
| SecuritiesDistribution | TradingAvailabilityDate        |  |
| SecuritiesDistribution | OfferExpiryDate                |  |
| SecuritiesDistribution | OversubscriptionRate           |  |
| SecuritiesDistribution | OversubscriptionAmount         |  |
| SecuritiesDistribution | ReinvestmentAmount             |  |
| SecuritiesDistribution | ReinvestmentRate               |  |
| SecuritiesDistribution | LoyalityPremiumIndicator       |  |

| SecuritiesDistribution | OversubscriptionIndicator                 |                     |
|------------------------|-------------------------------------------|---------------------|
| SecuritiesDistribution | RenounceableIndicator                     |                     |
| SecuritiesDistribution | DecimalPrecision                          |                     |
| SecuritiesDistribution | ReinvestmentType                          |                     |
| SecuritiesDistribution | RevocableIndicator                        |                     |
| SecuritiesDistribution | SecuritiesAndCashDistribution             |                     |
| SecuritiesDistribution | FractionTreatment                         |                     |
| SecuritiesDistribution | IntermediateSecurityDistributionIndicator |                     |
| Sponsor                |                                           | SecuritiesPartyRole |
| FundPromoter           |                                           | FundManagerRole     |
| ProxyAgent             |                                           | MeetingPartyRole    |

| PortfolioStrategy<br>PortfolioStrategy<br>Portfolio<br>PortfolioStrategy<br>InclusionIndicator<br>PortfolioStrategy<br>MinimumInvestmentAmount<br>PortfolioStrategy<br>MinimumInvestmentRate<br>PortfolioStrategy<br>MaximumInvestmentAmount<br>PortfolioStrategy<br>MaximumInvestmentRate<br>PortfolioStrategy<br>EffectivePeriod<br>PortfolioStrategy<br>DistributionPolicy<br>PortfolioStrategy<br>Description<br>PortfolioStrategy<br>Definition<br>JurisdictionStrategy<br>PortfolioStrategy |  |  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |

| JurisdictionStrategy           | Jurisdiction     |                         |
|--------------------------------|------------------|-------------------------|
| AttendanceConfirmationDeadline |                  | MeetingDeadline         |
| Auditor                        |                  | InvestmentFundPartyRole |
| BondCounsel                    |                  | SecuritiesPartyRole     |
| PortfolioBenchmark             |                  |                         |
| PortfolioBenchmark             | Index            |                         |
| PortfolioBenchmark             | Portfolio        |                         |
| PortfolioBenchmark             | BenchmarkWeight  |                         |
| PortfolioBenchmark             | MaximumDeviation |                         |
| PortfolioBenchmark             | MinimumDeviation |                         |
| PortfolioBenchmark             | EffectivePeriod  |                         |
|                                |                  |                         |

| PortfolioBenchmark              | Description              |                          |
|---------------------------------|--------------------------|--------------------------|
| PortfolioBenchmark              | Approver                 |                          |
| PortfolioBenchmark              | Administrator            |                          |
| CentralClearingCounterpartyRole |                          | SettlementPartyRole      |
| CentralClearingCounterpartyRole | System                   |                          |
| TerminalManagerRole             |                          | SystemPartyRole          |
| TerminalManagerRole             | TerminalManagementSystem |                          |
| MarketClaimCounterparty         |                          | CorporateActionPartyRole |
| CorporateActionOfferor          |                          | CorporateActionPartyRole |
|                                 |                          |                          |

| MeetingServicing           |                            | CorporateActionServicing |
|----------------------------|----------------------------|--------------------------|
| MeetingServicing           | MeetingSpecification       |                          |
| MeetingServicing           | MeetingNotice              |                          |
| MeetingServicing           | MeetingEntitlement         |                          |
| MeetingServicing           | MeetingInstruction         |                          |
| MeetingServicing           | MeetingResultDissemination |                          |
| MeetingResultDissemination |                            |                          |
| MeetingResultDissemination | RelatedServicing           |                          |

| MeetingResultDissemination      | VoteResult |                        |
|---------------------------------|------------|------------------------|
| CardIssuer                      |            | CardPaymentPartyRole   |
| CaseCreator                     |            | InvestigationPartyRole |
| CentralSecuritiesDepositoryRole |            | DepositoryRole         |
| ChargeAgent                     |            | ChargePartyRole        |
| ChargeBearer                    |            | ChargePartyRole        |
| ChargeRecipient                 |            | ChargePartyRole        |
| ClaimsAgent                     |            | InsurancePartyRole     |
|                                 |            |                        |

| ClearingPlace             |            | SettlementPartyRole      |
|---------------------------|------------|--------------------------|
| CollectionAgent           |            | SecuritiesPartyRole      |
| CommissionPartyRole       |            | Role                     |
| CommissionPartyRole       | Commission |                          |
| CommissionRecipient       |            | CommissionPartyRole      |
| ContraClearingFirm        |            | SettlementPartyRole      |
| ContraFirm                |            | SecuritiesTradePartyRole |
| CorrespondentClearingFirm |            | SettlementPartyRole      |
| CustodianRole             |            | SecuritiesPartyRole      |
|                           |            |                          |

| CustodianRole            | InvestmentFund |                               |
|--------------------------|----------------|-------------------------------|
| DataSetInitiator         |                | CardPaymentPartyRole          |
| DeliverersCustodian      |                | SecuritiesSettlementPartyRole |
| DeliverersIntermediary   |                | SecuritiesSettlementPartyRole |
| DeliveringAgent          |                | SecuritiesSettlementPartyRole |
| DeliveringDepositoryRole |                | DeliveringSettlementParty     |

| DeterminationAgent | SecuritiesPartyRole      |
|--------------------|--------------------------|
| DirectMember       | SystemMemberRole         |
| DocumentSignatory  | DocumentPartyRole        |
| Drawee             | ChequePartyRole          |
| Drawer             | ChequePartyRole          |
| EnteringFirm       | SecuritiesOrderPartyRole |
| ETCServiceProvider | SecuritiesTradePartyRole |

| ExecutingTrader<br>ExecutingBroker<br>SecuritiesTradeSystemRole<br>SecuritiesTradePartyRole<br>ExecutionDestination<br>SecuritiesTradePartyRole<br>ForwardingAgentRole<br>PaymentPartyRole<br>FundAccountantRole<br>InvestmentFundPartyRole<br>FundAdministratorRole<br>InvestmentFundPartyRole | ExecutingTrader | SecuritiesTradePartyRole |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|--------------------------|
|                                                                                                                                                                                                                                                                                                 |                 |                          |
|                                                                                                                                                                                                                                                                                                 |                 |                          |
|                                                                                                                                                                                                                                                                                                 |                 |                          |
|                                                                                                                                                                                                                                                                                                 |                 |                          |
|                                                                                                                                                                                                                                                                                                 |                 |                          |
|                                                                                                                                                                                                                                                                                                 |                 |                          |
| FundOrderDesk<br>InvestmentFundPartyRole                                                                                                                                                                                                                                                        |                 |                          |

| FundOrderDesk        | MainFundOrderDeskIndicator |                     |
|----------------------|----------------------------|---------------------|
| FundOrderDesk        | MainFundOrderDeskAccount   |                     |
| GiverRole            |                            | CollateralPartyRole |
| GiveUpClearingFirm   |                            | SettlementPartyRole |
| GoodsPartyRole       |                            | Role                |
| GoodsPartyRole       | Item                       |                     |
| GuarantorRole        |                            | GuaranteePartyRole  |
| GuarantorRole        | Position                   |                     |
| GuaranteeBeneficiary |                            | GuaranteePartyRole  |
| IndirectMember       |                            | ThirdPartyRole      |
|                      |                            |                     |

| InitiatingPartyRole           | PaymentPartyRole                   |
|-------------------------------|------------------------------------|
| InstructingReimbursementAgent | CashSettlementInstructionPartyRole |
| Insurer                       | InsurancePartyRole                 |
| InvestmentAdvisor             | AssetPartyRole                     |
| LeadUnderwriter               | SecuritiesPartyRole                |

| LegalAdvisor           |                  | SecuritiesPartyRole      |
|------------------------|------------------|--------------------------|
| LocalBroker            |                  | Broker                   |
| MandateIssuer          |                  | MandatePartyRole         |
| ObligorBank            |                  | CommercialTradePartyRole |
| OrderOriginationFirm   |                  | SecuritiesOrderPartyRole |
| OrderOriginationTrader |                  | SecuritiesOrderPartyRole |
| PayingAgentRole        |                  |                          |
| PayingAgentRole        | CommissionAmount |                          |
| PlacementAgent         |                  | InvestmentFundPartyRole  |

| PlaceOfRegistry              |                  | SecuritiesPartyRole           |
|------------------------------|------------------|-------------------------------|
| PlaceOfSettlement            |                  | SecuritiesSettlementPartyRole |
| PlaceOfSettlement            | SettlementMarket |                               |
| POIManufacturer              |                  | CardPaymentPartyRole          |
| PrimaryPlaceOfDeposit        |                  | SecuritiesPartyRole           |
| PrincipalCollectionAgent     |                  | SecuritiesPartyRole           |
| PrincipalPayingAgent         |                  | SecuritiesPartyRole           |
| ProxyAssignerRole            |                  | MeetingPartyRole              |
| QualifiedForeignIntermediary |                  | TradePartyRole                |
| QualifiedForeignIntermediary | Country          |                               |
| QuoteOriginator              |                  | InformationPartyRole          |

| QuoteOriginator       | QuoteOriginatorType  |                               |
|-----------------------|----------------------|-------------------------------|
| QuoteRequestor        |                      | InformationPartyRole          |
| QuoteRequestor        | RequestorEligibility |                               |
| QuotingInstitution    |                      | InformationPartyRole          |
| ReceiversCustodian    |                      | SecuritiesSettlementPartyRole |
| ReceiversIntermediary |                      | SecuritiesSettlementPartyRole |

| ReceivingDepositoryRole |       | ReceivingSettlementParty |
|-------------------------|-------|--------------------------|
| RecipientBank           |       | CommercialTradePartyRole |
| RemarketingAgent        |       | SecuritiesPartyRole      |
| RightsHolder            |       | MeetingPartyRole         |
| CounterpartyRisk        |       |                          |
| CounterpartyRisk        | Party |                          |
|                         |       |                          |

| CounterpartyRisk              | ExposedAmount       |                              |
|-------------------------------|---------------------|------------------------------|
| CounterpartyRisk              | ExposureCalculation |                              |
| CounterpartyRisk              | SecureMarketValue   |                              |
| CounterpartyRisk              | LiquidResourceValue |                              |
| SecurityCertificateIssuerRole |                     | SecurityCertificatePartyRole |
| SellerBank                    |                     | TradePartyRole               |
| SponsoringFirm                |                     | SecuritiesOrderPartyRole     |
| StockExchange                 |                     | TradePartyRole               |
| StockExchange                 | Market              |                              |
| SystemAdministratorRole       |                     | SystemPartyRole              |
| TakerRole                     |                     | CollateralPartyRole          |
|                               |                     |                              |

| TaxRecipient              |                  | TaxPartyRole                       |
|---------------------------|------------------|------------------------------------|
| ThirdReimbursementAgent   |                  | CashSettlementInstructionPartyRole |
| TradeCertificatePartyRole |                  | Role                               |
| TradeCertificatePartyRole | TradeCertificate |                                    |
| TradingBranch             |                  | TreasuryTradingParty               |

| TransferAgentRole            |            | InvestmentFundPartyRole     |
|------------------------------|------------|-----------------------------|
| TreasurySettlementSystem     |            | System                      |
| TreasurySettlementSystem     | SystemRole |                             |
| TreasurySettlementSystemRole |            | TreasurySettlementPartyRole |
| TreasurySettlementSystemRole | System     |                             |

| TripartyAgent                   | CollateralPartyRole      |
|---------------------------------|--------------------------|
| UnderwriterRole                 | SecuritiesPartyRole      |
| VotingPartyRole                 | MeetingPartyRole         |
| AcceptorRole                    | CardPaymentPartyRole     |
| AccountInformationRecipientRole | AccountPartyRole         |
| AccountingAgent                 | SecuritiesTradePartyRole |
| AuthorisedAccountModifier       | AccountPartyRole         |
| BillTo                          | CommercialTradePartyRole |
| BuyerBank                       | TradePartyRole           |
| QuoteStatus                     | Status                   |

| QuoteStatus               | Status                      |                      |
|---------------------------|-----------------------------|----------------------|
| QuoteStatus               | RejectionReason             |                      |
| QuoteStatus               | RelatedQuote                |                      |
| VoluntaryCorporateAction  |                             | CorporateActionEvent |
| PowerOfAttorney           |                             | Mandate              |
| PowerOfAttorney           | AuthorisedParty             |                      |
| PowerOfAttorney           | PowerOfAttorneyRequirements |                      |
| PowerOfAttorney           | AuthorisedAccount           |                      |
| VoteRegistrationDeadline  |                             | MeetingDeadline      |
| ProductDeliveryObligation |                             | Obligation           |
|                           |                             |                      |

| ProductDeliveryObligation  | ProductDeliveryOffset |                 |
|----------------------------|-----------------------|-----------------|
| ProductDeliveryObligation  | CommercialTrade       |                 |
| AdditionalRightDeadline    |                       | MeetingDeadline |
| VoteRevocabilityDeadline   |                       | MeetingDeadline |
| ProxyAppointmentDeadline   |                       | MeetingDeadline |
| ResolutionProposalDeadline |                       | MeetingDeadline |
| VoteDeadline               |                       | MeetingDeadline |
| VoteWithPremiumDeadline    |                       | MeetingDeadline |

| TransactionRisk |                     |         |
|-----------------|---------------------|---------|
| TransactionRisk | Obligation          |         |
| TransactionRisk | ExposedAmount       |         |
| TransactionRisk | ExposureCalculation |         |
| CashLoanDeposit |                     | Deposit |
| AccountLink     |                     |         |

| AccountLink<br>CashAccount<br>AccountLink<br>ValidityPeriod<br>AccountLink<br>SecuritiesAccount<br>AccountLink<br>MarketInfrastructure<br>AccountLink<br>CashSettlementIndicator<br>AccountLink<br>CollateralisationIndicator<br>AccountLink<br>DefaultIndicator<br>Netting<br>ObligationFulfilment |  |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                     |  |  |
|                                                                                                                                                                                                                                                                                                     |  |  |

| Netting            | AverageDealPrice                 |                      |
|--------------------|----------------------------------|----------------------|
|                    |                                  |                      |
| Netting            | RelatedSecuritiesClearingProcess |                      |
| Netting            | NetPositionAmount                |                      |
| Netting            | AmountDirection                  |                      |
| Netting            | NetQuantity                      |                      |
| Netting            | PositionAmount                   |                      |
| Rollover           |                                  | ObligationFulfilment |
| Rollover           | SecuritiesSettlement             |                      |
| SecuritiesClearing |                                  | Clearing             |
| SecuritiesClearing | SecuritiesSettlement             |                      |
| SecuritiesClearing | BuyIn                            |                      |
| SecuritiesClearing | Novation                         |                      |
| SecuritiesClearing | Netting                          |                      |

| Novation                 |                       | ObligationFulfilment    |
|--------------------------|-----------------------|-------------------------|
| Novation                 | SecuritiesClearing    |                         |
| Novation                 | NovationStatus        |                         |
| MandatoryCorporateAction |                       | CorporateActionEvent    |
| Carrier                  |                       | TransportPartyRole      |
| Manufacturer             |                       | GoodsPartyRole          |
| DuplicateCase            |                       | InvestigationResolution |
| DuplicateCase            | DuplicatedCase        |                         |
| DuplicateCase            | RelatedCaseResolution |                         |

| BulkPayment       |                           | Payment          |
|-------------------|---------------------------|------------------|
| BulkPayment       | Groups                    |                  |
| CashDelivery      |                           | CreditInstrument |
| CashDelivery      | CashAmount                |                  |
| CashDelivery      | RelatedBankingTransaction |                  |
| ComponentSecurity |                           |                  |
| ComponentSecurity | SeparationPeriod          |                  |
| ComponentSecurity | Security                  |                  |
| ComponentSecurity | SeparationChoice          |                  |
| ComponentSecurity | QuantityNumerator         |                  |
|                   |                           |                  |

| ComponentSecurity       | QuantityDenominator      | Number of held securities for the<br>BaseOneRate<br>exercise.                                                              |  |
|-------------------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------|--|
| ComponentSecurity       | SeparationDate           | Date/time at which the related<br>security can (optional) or must<br>ISODateTime<br>(mandatory) be separated.              |  |
| FinancialInstrumentSwap |                          | Characteristics and conditions by<br>which a borrower can exchange<br>one type of financial instrument<br>for another.     |  |
| FinancialInstrumentSwap | Maturity                 | Range of time during which a<br>DateTimePeriod<br>swap is in effect.                                                       |  |
| FinancialInstrumentSwap | SpotSell                 | Details of the spot leg of the sell<br>SecuritiesSwapLeg<br>side of a swap.                                                |  |
| FinancialInstrumentSwap | SpotBuy                  | Details of the spot leg of the buy<br>SecuritiesSwapLeg<br>side of a swap.                                                 |  |
| FinancialInstrumentSwap | ForwardBuyBack           | Details of the forward leg of a<br>swap that has been sold and is<br>SecuritiesSwapLeg<br>being returned, ie, bought back. |  |
| FinancialInstrumentSwap | ForwardSellBack          | Details of the forward leg of a<br>swap that has been bought and<br>SecuritiesSwapLeg<br>is being returned, ie, sold back. |  |
| FinancialInstrumentSwap | RelatedQuote             | Quote related to a swap.<br>Quote                                                                                          |  |
| FinancialInstrumentSwap | ForwardSellBackFrequency | Frequency at which the sold<br>financial instrument is being<br>FrequencyCode<br>returned.                                 |  |
| FinancialInstrumentSwap | ForwardBuyBackFrequency  | Frequency at which the bought<br>financial instrument is being<br>FrequencyCode<br>returned.                               |  |
|                         |                          |                                                                                                                            |  |

| FinancialInstrumentSwap       | InterestComputation |  |
|-------------------------------|---------------------|--|
| BuyOrSellIndicationOfInterest |                     |  |
| BuyOrSellIndicationOfInterest | NegotiationDetails  |  |
| BuyOrSellIndicationOfInterest | Organisations       |  |
| BuyOrSellIndicationOfInterest | RelativeSize        |  |
| BuyOrSellIndicationOfInterest | Price               |  |
| BuyOrSellIndicationOfInterest | QualityIndication   |  |
| BuyOrSellIndicationOfInterest | NaturalIndicator    |  |
| BuyOrSellIndicationOfInterest | Qualifier           |  |
| BuyOrSellIndicationOfInterest | NumberOfLegs        |  |
|                               |                     |  |

| BuyOrSellIndicationOfInterest | SpreadToBenchmark    |                   |
|-------------------------------|----------------------|-------------------|
| BuyOrSellIndicationOfInterest | SwapSpread           |                   |
| BuyOrSellIndicationOfInterest | TwoLegTransaction    |                   |
| BuyOrSellIndicationOfInterest | RoutingType          |                   |
| BuyOrSellIndicationOfInterest | OrganisationListName |                   |
|                               |                      |                   |
| OrganisationStrategy          |                      | PortfolioStrategy |
| OrganisationStrategy          | Organisation         |                   |
| SecuritiesPegOrderInstruction |                      |                   |
| SecuritiesPegOrderInstruction | Offset               |                   |
| SecuritiesPegOrderInstruction | PriceType            |                   |
| SecuritiesPegOrderInstruction | MoveType             |                   |
| SecuritiesPegOrderInstruction | OffsetType           |                   |

| SecuritiesPegOrderInstruction | LimitType            | Specifies nature of resulting<br>Max35Text<br>pegged price.                                                                                                                                                        |
|-------------------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SecuritiesPegOrderInstruction | Scope                | The scope of "related to" price of<br>the peg (for example, local,<br>PriceProtectionScopeCode<br>global etc).                                                                                                     |
| SecuritiesPegOrderInstruction | OffsetSign           | Indicates whether the offset<br>should be added to or subtracted<br>PlusOrMinusIndicator<br>from the peg for a pegged order.                                                                                       |
| SecuritiesPegOrderInstruction | Order                | Order which is pegged.<br>SecuritiesOrderParameters                                                                                                                                                                |
| SecuritiesPegOrderInstruction | RoundDirection       | If the calculated peg price is not<br>a valid tick price, specifies how to<br>RoundingParameters<br>round the price.                                                                                               |
| SecuritiesRegulatoryDetails   |                      | Information related to order and<br>required for regulatory purposes.                                                                                                                                              |
| SecuritiesRegulatoryDetails   | OrderRestrictions    | Classification and restrictions<br>linked to an order (for regulatory<br>OrderClassificationCode<br>purpose).                                                                                                      |
| SecuritiesRegulatoryDetails   | BrokerSolicitedTrade | Indicates whether the trading<br>party has suggested to his client<br>to buy/sell a financial instrument<br>YesNoIndicator<br>or whether the investor acts on<br>its own without advice from its<br>trading party. |
| SecuritiesRegulatoryDetails   | RelatedOrder         | Order for which legal parameters<br>SecuritiesOrder<br>are provided.                                                                                                                                               |
| AnalyticsCalculation          |                      | Characteristics related to the<br>analytics.                                                                                                                                                                       |
| AnalyticsCalculation          | SecuritiesPricing    | Pricing for which an analytics<br>SecuritiesPricing<br>calculation is specified.                                                                                                                                   |

| AnalyticsCalculation | Value                    |
|----------------------|--------------------------|
| AnalyticsCalculation | CalculationType          |
| AnalyticsCalculation | ValueDate                |
| AnalyticsCalculation | ValuePeriod              |
| AnalyticsCalculation | EstimatedInterestRate    |
| AnalyticsCalculation | VariableRateValueDate    |
| DurationCalculation  |                          |
| DurationCalculation  | RelatedSecuritiesPricing |
| DurationCalculation  | VariableInterest         |
| DurationCalculation  | Years                    |
| DurationCalculation  | CalculationType          |
|                      |                          |

| DurationCalculation | ValueDate         |          |
|---------------------|-------------------|----------|
| DurationCalculation | ValuePeriod       |          |
| LifeCalculation     |                   |          |
| LifeCalculation     | SecuritiesPricing |          |
| LifeCalculation     | VariableInterest  |          |
| LifeCalculation     | Years             |          |
| LifeCalculation     | CalculationType   |          |
| LifeCalculation     | ValueDate         |          |
| LifeCalculation     | ValuePeriod       |          |
| Entitlement         |                   | Security |

| Entitlement | StrikePrice           |  |
|-------------|-----------------------|--|
| Entitlement | CoveredIndicator      |  |
| Entitlement | OptionStyle           |  |
| Entitlement | OptionType            |  |
| Entitlement | CappedValue           |  |
| Entitlement | CappedIndicator       |  |
| Discretion  |                       |  |
| Discretion  | RelatedOrderExecution |  |
| Discretion  | Offset                |  |
|             |                       |  |

| Discretion           | OffsetSign       |             |
|----------------------|------------------|-------------|
| Discretion           | RelatedPriceType |             |
| Discretion           | MoveType         |             |
| Discretion           | LimitType        |             |
| Discretion           | RoundDirection   |             |
| Discretion           | Scope            |             |
| Discretion           | OffsetType       |             |
| DisclosedListTrading |                  | ListTrading |

| DisclosedListTrading    | DisclosedListTradingAccount |  |
|-------------------------|-----------------------------|--|
| DisclosedListTrading    | BuyAmount                   |  |
| DisclosedListTrading    | SellAmount                  |  |
| DisclosedListTrading    | RequestedSettlementDateCode |  |
| SecuritiesQuoteVariable |                             |  |
| SecuritiesQuoteVariable | Qualifier                   |  |
| SecuritiesQuoteVariable | Type                        |  |
| SecuritiesQuoteVariable | QuoteTradingSession         |  |
| SecuritiesQuoteVariable | LegSwapType                 |  |

| SecuritiesQuoteVariable  | PriceType       |  |
|--------------------------|-----------------|--|
| SecuritiesQuoteVariable  | MidSide         |  |
| SecuritiesQuoteVariable  | BidSide         |  |
| SecuritiesQuoteVariable  | OfferSide       |  |
| SecuritiesQuoteVariable  | RelatedQuote    |  |
| SecuritiesQuoteVariable  | SecuritiesOrder |  |
| SecuritiesQuoteVariable  | Commission      |  |
| ExchangeForPhysicalTrade |                 |  |
| ExchangeForPhysicalTrade | OutsideIndex    |  |
|                          |                 |  |

| ExchangeForPhysicalTrade | FairValue           |                 | Difference between the value of a<br>future and the value of the<br>underlying equities after allowing<br>CurrencyAndAmount<br>for the discounted cash flows<br>associated with the underlying<br>stocks. |  |
|--------------------------|---------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| ExchangeForPhysicalTrade | ValueForFutures     |                 | Value of a futures position<br>involved in an Exchange For<br>CurrencyAndAmount<br>Physical trade.                                                                                                        |  |
| ExchangeForPhysicalTrade | OutMainCountryIndex |                 | Accepted value of stocks<br>composing an index located<br>CurrencyAndAmount<br>outside its country of origin.                                                                                             |  |
| ExchangeForPhysicalTrade | SecuritiesOrder     |                 | Order for which parameters for<br>exchange for physical trading are<br>SecuritiesOrder<br>specified.                                                                                                      |  |
| OrderBook                |                     |                 | Record of orders to buy and sell<br>a financial instrument.                                                                                                                                               |  |
| OrderBook                | Order               |                 | Instruction to a broker or dealer<br>SecuritiesOrder<br>to buy or sell a specific security.                                                                                                               |  |
| OrderBook                | PriceTimePriority   |                 | Priority given to an order based<br>on its price and/or time<br>Max16Text<br>specification.                                                                                                               |  |
| CrossTrade               |                     | SecuritiesOrder | Transaction where either the<br>buy-broker and the sell-broker<br>are the same, or the buy-broker<br>and the sell-broker belong to the<br>same firm.                                                      |  |
| CrossTrade               | BuySideOrder        |                 | Buyside order details.<br>SecuritiesOrder                                                                                                                                                                 |  |
| CrossTrade               | SellSideOrder       |                 | Sell side order details.<br>SecuritiesOrder                                                                                                                                                               |  |

| CrossTrade        | ExecutionType  |  |
|-------------------|----------------|--|
| CrossTrade        | CrossType      |  |
| CrossTrade        | Prioritisation |  |
| SecuritiesSwapLeg |                |  |
| SecuritiesSwapLeg | Amount         |  |
| SecuritiesSwapLeg | Benchmark      |  |
| SecuritiesSwapLeg | CurvePoint     |  |
| SecuritiesSwapLeg | BenchmarkYield |  |
|                   |                |  |

| SecuritiesSwapLeg       | BenchmarkOffset     |             |
|-------------------------|---------------------|-------------|
| SecuritiesSwapLeg       | SpotSellSwap        |             |
| SecuritiesSwapLeg       | SpotBuySwap         |             |
| SecuritiesSwapLeg       | ForwardBuyBackSwap  |             |
| SecuritiesSwapLeg       | ForwardSellBackSwap |             |
| NonDisclosedListTrading |                     | ListTrading |
| NonDisclosedListTrading | BidByCurrency       |             |
| NonDisclosedListTrading | BidBySector         |             |
| NonDisclosedListTrading | BidByIndex          |             |
|                         |                     |             |

| NonDisclosedListTrading<br>NumberOfBidders |
|--------------------------------------------|
| NonDisclosedListTrading<br>SideValue       |
| Curve                                      |
| Curve<br>Currency                          |
| Curve<br>Name                              |
| Curve<br>Point                             |
| Curve<br>Spread                            |
| AnalyticsValue                             |
| AnalyticsValue<br>Amount                   |
| AnalyticsValue<br>Rate                     |
| AnalyticsValue<br>NumberOfYears            |
| AnalyticsValue<br>AnalyticsCalculation     |

| PaymentSchedule             |                 |                   |
|-----------------------------|-----------------|-------------------|
| PaymentSchedule             | Date            |                   |
| PaymentSchedule             | Amount          |                   |
| PaymentSchedule             | Rate            |                   |
| PortfolioStrategyDefinition |                 |                   |
| PortfolioStrategyDefinition | Strategy        |                   |
| PortfolioStrategyDefinition | Name            |                   |
| PortfolioStrategyDefinition | Description     |                   |
| PortfolioStrategyDefinition | EffectivePeriod |                   |
| SectorStrategy              |                 | PortfolioStrategy |
| SectorStrategy              | Sector          |                   |
| CurrencyStrategy            |                 | PortfolioStrategy |
| CurrencyStrategy            | Currency        |                   |
| AssetClassStrategy          |                 | PortfolioStrategy |
| AssetClassStrategy          | AssetClass      |                   |
|                             |                 |                   |

| PersonProfile | RiskLevel                       |        |
|---------------|---------------------------------|--------|
| PersonProfile | Person                          |        |
| PersonProfile | PoliticalExposureType           |        |
| PersonProfile | CustomerConductClassification   |        |
| PersonProfile | FamilyMedicalInsuranceIndicator |        |
| PersonProfile | ProfileCertification            |        |
| PersonProfile | SourceOfWealth                  |        |
| PersonProfile | SalaryRange                     |        |
| PersonProfile | PoliticallyExposedStatus        |        |
| InvoiceStatus |                                 | Status |
|               |                                 |        |

| InvoiceStatus        | Invoice                         |                   |
|----------------------|---------------------------------|-------------------|
| Reinvestment         |                                 |                   |
| Reinvestment         | RelatedinvestmentAccountService |                   |
| Reinvestment         | InvestmentFundClass             |                   |
| Reinvestment         | Percentage                      |                   |
| DeliveryNote         |                                 | Document          |
| AmountAndPeriod      |                                 |                   |
| AmountAndPeriod      | Period                          |                   |
| AmountAndPeriod      | Amount                          |                   |
| NotificationReceiver |                                 | DocumentPartyRole |
| Market               |                                 |                   |
| Market               | Trade                           |                   |

| Market         | Jurisdiction            |                   |
|----------------|-------------------------|-------------------|
| Market         | Country                 |                   |
| Market         | GeographicalEnvironment |                   |
| Market         | Identification          |                   |
| Assessment     |                         | Document          |
| Assessment     | AssessmentType          |                   |
| Assessment     | System                  |                   |
| Assessment     | ExpiryDate              |                   |
| Assessment     | DeliveryDate            |                   |
| Evidence       |                         |                   |
| Evidence       | RelatedDocument         |                   |
| NotifyingParty |                         | DocumentPartyRole |

| GuaranteePartyRole |                      | Role |
|--------------------|----------------------|------|
| GuaranteePartyRole | Guarantee            |      |
| Order              |                      |      |
| Order              | Trade                |      |
| Order              | MasterIdentification |      |
| BankingTransaction |                      |      |
| BankingTransaction | PaymentObligation    |      |
| BankingTransaction | FinancialTransaction |      |
| BankingTransaction | CashDelivery         |      |
| BankingTransaction | CashDeposit          |      |
|                    |                      |      |

| SecuritiesTransaction |                             | SecuritiesTrade     |
|-----------------------|-----------------------------|---------------------|
| SecuritiesTransaction | ReplacedAmount              |                     |
| RepurchaseAgreement   |                             | SecuritiesFinancing |
| RepurchaseAgreement   | PaymentObligation           |                     |
| Assignment            |                             |                     |
| Assignment            | PaymentObligation           |                     |
| Assignment            | FinancingAgreement          |                     |
| FinancialTransaction  |                             |                     |
| FinancialTransaction  | CorporateActionDistribution |                     |
|                       |                             |                     |

| FinancialTransaction  | InterestManagement |                            |
|-----------------------|--------------------|----------------------------|
| FinancialTransaction  | Trade              |                            |
| FinancialTransaction  | CollateralMovement |                            |
| FinancialTransaction  | BankingTransaction |                            |
| FinancialTransaction  | RegulatoryReport   |                            |
| OrganisationHierarchy |                    |                            |
| OrganisationHierarchy | Organisation       |                            |
| FinancialDocument     |                    | Document                   |
| IndividualInvestor    |                    | InvestmentAccountPartyRole |
|                       |                    |                            |

| LocalDepositoryRole     |                      | DepositoryRole           |
|-------------------------|----------------------|--------------------------|
| SystematicInternaliser  |                      | SecuritiesTradePartyRole |
| DepositoryRole          |                      | SecuritiesPartyRole      |
| FinancialProduct        |                      | Product                  |
| CorporateActionDeadline |                      | Deadline                 |
| CorporateActionDeadline | RevocabilityPeriod   |                          |
| CorporateActionDeadline | ProtectDate          |                          |
| CorporateActionDeadline | TradingSuspendedDate |                          |
|                         |                      |                          |

| CorporateActionDeadline | CoverExpirationDate            |  |
|-------------------------|--------------------------------|--|
| CorporateActionDeadline | ElectionToCounterpartyDeadline |  |
| CorporateActionDeadline | ExpiryDate                     |  |
| CorporateActionDeadline | EarlyThirdPartyDeadline        |  |
| CorporateActionDeadline | DepositoryCoverExpirationDate  |  |
| CorporateActionDeadline | ResponseDeadline               |  |
| CorporateActionDeadline | ConsentExpirationDate          |  |
|                         |                                |  |

| CorporateActionDeadline | RegistrationDeadline        |  |
|-------------------------|-----------------------------|--|
| CorporateActionDeadline | StockLendingDeadline        |  |
| CorporateActionDeadline | ConsentRecordDate           |  |
| CorporateActionDeadline | EarlyResponseDeadline       |  |
| CorporateActionDeadline | GuaranteedParticipationDate |  |

| PaymentTerms |                            |  |
|--------------|----------------------------|--|
| PaymentTerms | Amount                     |  |
| PaymentTerms | Percentage                 |  |
| PaymentTerms | PaymentPeriod              |  |
| PaymentTerms | RelatedPaymentObligation   |  |
| PaymentTerms | PaymentTime                |  |
| PaymentTerms | RelatedPaymentScheduleType |  |
| PaymentTerms | RelatedLoan                |  |
| Tranche      |                            |  |
| Tranche      | Asset                      |  |
| Tranche      | DetachmentPoint            |  |
|              |                            |  |

| Tranche             | AttachmentPoint        |                            |
|---------------------|------------------------|----------------------------|
| AllocationPartyRole |                        | TradePartyRole             |
| CorporateInvestor   |                        | InvestmentAccountPartyRole |
| Investor            |                        | InvestmentAccountPartyRole |
| Investor            | NewIssuePermission     |                            |
| Investor            | DeMinimusApplicable    |                            |
| Investor            | Restricted             |                            |
| Investor            | RestrictedPersonReason |                            |
| PercentageAndPeriod |                        |                            |
| PercentageAndPeriod | Period                 |                            |
| PercentageAndPeriod | Percentage             |                            |

| InterestManagement    |                      |                 |
|-----------------------|----------------------|-----------------|
| InterestManagement    | InterestCalculation  |                 |
| InterestManagement    | FinancialTransaction |                 |
| InterestManagement    | Interest             |                 |
| InterestManagement    | PaymentObligation    |                 |
| SecuritiesOptionTrade |                      | SecuritiesTrade |
| SecuritiesOptionTrade | Option               |                 |
| Position              |                      |                 |
|                       |                      |                 |
| Position              | NetQuantity          |                 |
| Position              | NetPositionAmount    |                 |
| Position              | System               |                 |

| Position                       | Price                     |                     |
|--------------------------------|---------------------------|---------------------|
| Position                       | SecuritiesSettlement      |                     |
| Position                       | InitialPositionAmount     |                     |
| Household                      |                           |                     |
| Household                      | Member                    |                     |
| ManagedAccountProduct          |                           | FinancialProduct    |
| ManagedAccountProduct          | Account                   |                     |
| ManagedAccountProduct          | InvestmentAccountContract |                     |
| SystemReferenceDataResponsible |                           | SystemPartyRole     |
| FinancialService               |                           | Service             |
| Pledgee                        |                           | SecuritiesPartyRole |
| Pledgee                        | PledgeeType               |                     |
| Pledgee                        | SecuritiesBalance         |                     |
|                                |                           |                     |

| CustodyService |                        | FinancialService |
|----------------|------------------------|------------------|
| FATCAStatus    |                        |                  |
| FATCAStatus    | FATCAStatus            |                  |
| FATCAStatus    | FATCASourceStatus      |                  |
| FATCAStatus    | InvestmentAccountParty |                  |
| FATCAStatus    | FATCAReportingDate     |                  |
| ATMTotal       |                        |                  |
| ATMTotal       | ATMBalance             |                  |
| ATMTotal       | Currency               |                  |
|                |                        |                  |

| ATMTotal           | ATMCurrentNumber   |          |
|--------------------|--------------------|----------|
| ATMTotal           | ATMBalanceNumber   |          |
| ATMTotal           | ATMCurrent         |          |
| ATMTotal           | RelatedCardPayment |          |
| RegisteredContract |                    | Contract |
| RegisteredContract | Certificate        |          |
| RegisteredContract | ContractBalance    |          |
| RegisteredContract | ReportingParty     |          |
| RegisteredContract | Identification     |          |
| RegisteredContract | DeliveryDate       |          |
| RegisteredContract | RegistrationAgent  |          |
|                    |                    |          |

| RegisteredContract | ReceivingParty      | Party which receives support<br>information about the registered<br>RegulatoryReportingRole<br>contract.          |  |
|--------------------|---------------------|-------------------------------------------------------------------------------------------------------------------|--|
| RegisteredContract | Priority            | Priority requested for the<br>PriorityCode<br>registered contract.                                                |  |
| RegisteredContract | RegistrationDate    | Provides the date for the<br>registration of the registered<br>ISODate<br>contract.                               |  |
| RegisteredContract | ClosureReason       | Reason of closure of the contract.<br>StatusReason                                                                |  |
| RegisteredContract | ClosureDate         | Date of closure of the contract.<br>ISODate                                                                       |  |
| RegisteredContract | PaymentScheduleType | Type of the payment schedule<br>PaymentTerms<br>provided in the contract.                                         |  |
| RegisteredContract | SubmissionDate      | Provides the date for the<br>submission of the registered<br>ISODate<br>contract.                                 |  |
| RegisteredContract | SendingParty        | Party which sends support<br>information about the registered<br>RegulatoryReportingRole<br>contract.             |  |
| RegisteredContract | DeliveryMethod      | Provides the communication<br>method for the delivery of the<br>CommunicationMethodCode<br>registered contract.   |  |
| RegisteredContract | SubmissionMethod    | Provides the communication<br>method for the submission of the<br>CommunicationMethodCode<br>registered contract. |  |
| RegisteredContract | RelatedPayment      | Provides the payment related of<br>Payment<br>the registered contract.                                            |  |
| RegisteredContract | Attachment          | Documents provided as<br>attachments to the registered<br>Document<br>contract.                                   |  |
|                    |                     |                                                                                                                   |  |

| Loan                    |                           | Debt |
|-------------------------|---------------------------|------|
| Loan                    | PrincipalAmount           |      |
| Loan                    | InterestPaymentsSchedule  |      |
| Loan                    | IntraCompanyLoanIndicator |      |
| RegulatoryReportingRole |                           | Role |
| RegulatoryReportingRole |                           |      |
|                         | RelatedReportingParty     |      |
| RegulatoryReportingRole | RelatedRegistrationAgent  |      |
| RegulatoryReportingRole | RelatedReceivingParty     |      |
| RegulatoryReportingRole | RelatedSendingParty       |      |

| CreditDefaultSwap |                 | Swaps      |
|-------------------|-----------------|------------|
| CreditDefaultSwap | RollDate        |            |
| CreditDefaultSwap | RollMonth       |            |
| CreditDefaultSwap | Series          |            |
| Swaps             |                 | Derivative |
| Swaps             | SovereignIssuer |            |
| Swaps             | Obligation      |            |
|                   |                 |            |

| Commodity |                             | Asset |
|-----------|-----------------------------|-------|
| Commodity | BaseProduct                 |       |
| Commodity | DetailedSubProduct          |       |
| Commodity | SubProduct                  |       |
| CRSStatus |                             |       |
| CRSStatus | CRSStatus                   |       |
| CRSStatus | ExceptionalReportingCountry |       |
| CRSStatus | CRSSourceStatus             |       |

| CRSStatus        | CRSReportingDate       |                    |
|------------------|------------------------|--------------------|
| CRSStatus        | InvestmentAccountParty |                    |
| AccountSwitching |                        | CashAccountService |
| AccountSwitching | SwitchReceivedDateTime |                    |
| AccountSwitching | SwitchDate             |                    |
| AccountSwitching | SwitchStatus           |                    |
| AccountSwitching | UniqueReferenceNumber  |                    |
|                  |                        |                    |

| AccountSwitching              | SwitchType                |  |
|-------------------------------|---------------------------|--|
| AccountSwitching              | BalanceTransferWindow     |  |
| CappedLimit                   |                           |  |
| CappedLimit                   | IncomeCurrentPeriod       |  |
| CappedLimit                   | StartDate                 |  |
| CappedLimit                   | IncomeLimitCurrentPeriod  |  |
| CappedLimit                   | RelatedDrawdown           |  |
| CappedLimit                   | IncomeLimitNextPeriod     |  |
| CorporateActionProtectProcess |                           |  |
| CorporateActionProtectProcess | ProtectDate               |  |
| CorporateActionProtectProcess | TransactionIdentification |  |
|                               |                           |  |

| CorporateActionProtectProcess | ProtectSafekeepingAccount      |  |
|-------------------------------|--------------------------------|--|
| CorporateActionProtectProcess | ProtectTransactionStatus       |  |
| CorporateActionProtectProcess | UncoveredProtectQuantity       |  |
| CorporateActionProtectProcess | RelatedCorporateActionElection |  |
| CorporateActionProtectProcess | TransactionType                |  |
| PaymentTracker                |                                |  |
| PaymentTracker                | Agent                          |  |
| PaymentTracker                | ChargesAmount                  |  |
| PaymentTracker                | ChargeBearer                   |  |
| PaymentTracker                | ExchangeRateData               |  |
|                               |                                |  |

| TaxEfficientProduct |                                 |  |
|---------------------|---------------------------------|--|
| TaxEfficientProduct | EstimatedValue                  |  |
| TaxEfficientProduct | PreviousYears                   |  |
| TaxEfficientProduct | CurrentInvestmentAmount         |  |
| TaxEfficientProduct | Amount                          |  |
| TaxEfficientProduct | UnusedTaxDeduction              |  |
| TaxEfficientProduct | TaxCalculationBase              |  |
| TaxEfficientProduct | LowestInvestedAmountCurrentYear |  |
| TaxEfficientProduct | InvestorTaxReference            |  |
| TaxEfficientProduct | RelatedInvestmentPlan           |  |
| TaxEfficientProduct | TaxEfficientProductType         |  |
| TaxEfficientProduct | AmountType                      |  |
| TaxEfficientProduct | InvestmentsToFollowValue        |  |
|                     |                                 |  |

| TaxEfficientProduct | InvestorTaxReferenceType       | Identification of the type of<br>investor as assigned by a tax<br>authority.                                                                                 | PersonIdentificationTypeCode |
|---------------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| TaxEfficientProduct | CurrentYearSubscription        | Amounts already subscribed for<br>the current year.                                                                                                          | SubscriptionExecution        |
| Drawdown            |                                | Details of a drawdown tranche.                                                                                                                               |                              |
| Drawdown            | BeneficiaryType                | Information about the recipient<br>of the drawdown, when not the<br>original pension holder.                                                                 | BeneficiaryTypeCode          |
| Drawdown            | CrystallisedUnitsNumber        | Number of units crystallised.<br>DecimalNumber                                                                                                               |                              |
| Drawdown            | CrystallisationAmount          | Amount that was originally<br>designated for crystallisation.                                                                                                | CurrencyAndAmount            |
| Drawdown            | DrawdownStatus                 | Drawdown status of the pension.                                                                                                                              | DrawdownStatusCode           |
| Drawdown            | EventType                      | Type of crystallisation event.                                                                                                                               | DrawdownEventTypeCode        |
| Drawdown            | TrancheType                    | Type of drawdown tranche.                                                                                                                                    | DrawdownTypeCode             |
| Drawdown            | PercentageOfTotalTransferValue | Percentage of the total transfer<br>PercentageRate<br>value covered by the drawdown.                                                                         |                              |
| Drawdown            | ApplicableRules                | Specifies the rules that are<br>applicable to the drawdown. For<br>example, in the UK market, the<br>pre-A-day rule that was<br>introduced on 6 April 2006.) | ApplicableRulesCode          |
| Drawdown            | CappedLimit                    | Limits of the capped drawdown.<br>CappedLimit                                                                                                                |                              |
| Drawdown            | Beneficiary                    | Information about the recipient<br>of the drawdown, when not the<br>original pension holder.                                                                 |                              |
|                     |                                |                                                                                                                                                              |                              |

| Drawdown | TriggeredDate                 |
|----------|-------------------------------|
| Drawdown | EventDate                     |
| Drawdown | DrawdownAmount                |
| Drawdown | Pension                       |
| Drawdown | LifetimeAllowance             |
| Drawdown | DrawdownTrancheIdentification |
| Drawdown | NumberOfDrawdownTranches      |
| Pension  |                               |
| Pension  | ValueOfPensionPolicy          |
| Pension  | RelatedInvestmentPlan         |
| Pension  | EstimatedValue                |
| Pension  | TransferScope                 |
| Pension  | Drawdown                      |
| Pension  | PensionOrderType              |

| Pension                | RetirementAge                     |  |
|------------------------|-----------------------------------|--|
| Pension                | Identification                    |  |
| Pension                | Type                              |  |
| Pension                | TaxFreeCashAmount                 |  |
| Pension                | LumpSumType                       |  |
| Pension                | TaxReference                      |  |
| Pension                | ClientLifetimeAllowanceProtection |  |
| CollateralReinvestment |                                   |  |
| CollateralReinvestment | CashReinvestmentRate              |  |
| CollateralReinvestment | ReinvestedCashType                |  |
| CollateralReinvestment | FundingSourceType                 |  |

| CollateralReinvestment  | RelatedCollateral                 |         |
|-------------------------|-----------------------------------|---------|
| AdditionalLEIAttributes |                                   |         |
| AdditionalLEIAttributes | RelationshipType                  |         |
| AdditionalLEIAttributes | RelationshipStatus                |         |
| AdditionalLEIAttributes | RelatedOrganisationIdentification |         |
| AdditionalLEIAttributes | ManagingLOU                       |         |
| CreditTransferMandate   |                                   | Mandate |
| CreditTransferMandate   | Reason                            |         |
| CreditTransferMandate   | FirstPaymentDate                  |         |
| CreditTransferMandate   | DateOfVerification                |         |

| CreditTransferMandate | FinalPaymentDate                          |  |
|-----------------------|-------------------------------------------|--|
| CreditTransferMandate | Signature                                 |  |
| ActivationService     |                                           |  |
| ActivationService     | DedicatedActivation                       |  |
| ActivationService     | EndDate                                   |  |
| ActivationService     | StartDate                                 |  |
| ActivationService     | OriginalActivation                        |  |
| ActivationService     | RelatedActivation                         |  |
| ActivationService     | RelatedElectronicInvoiceProcessingService |  |
| EnrolmentVisibility   |                                           |  |

| EnrolmentVisibility | EndDate                  |  |
|---------------------|--------------------------|--|
| EnrolmentVisibility | RelatedEnrolmentService  |  |
| EnrolmentVisibility | LimitedVisibility        |  |
| EnrolmentVisibility | StartDate                |  |
| EnrolmentService    |                          |  |
| EnrolmentService    | ServiceActivationLink    |  |
| EnrolmentService    | ServiceActivationAllowed |  |
| EnrolmentService    | EndDate                  |  |
| EnrolmentService    | UltimateCreditor         |  |
| EnrolmentService    | Visibility               |  |
|                     |                          |  |

| EnrolmentService                   | ServiceDescriptionLink                    |                |
|------------------------------------|-------------------------------------------|----------------|
| EnrolmentService                   | StartDate                                 |                |
| EnrolmentService                   | Creditor                                  |                |
| EnrolmentService                   | OriginalEnrolment                         |                |
| EnrolmentService                   | RelatedElectronicInvoiceProcessingService |                |
| EnrolmentService                   | RelatedEnrolment                          |                |
| ElectronicInvoiceProcessingService |                                           | AccountService |
| ElectronicInvoiceProcessingService | RelatedInvoice                            |                |
| ElectronicInvoiceProcessingService | ElectronicInvoiceSolutionProvider         |                |
| ElectronicInvoiceProcessingService | CreditorEnrolment                         |                |
| ElectronicInvoiceProcessingService | ElectronicInvoiceDirectoryProvider        |                |
| ElectronicInvoiceProcessingService | DebtorActivation                          |                |
|                                    |                                           |                |

| ElectronicInvoiceProcessingService | ProcessingStatus                          |      |
|------------------------------------|-------------------------------------------|------|
| ElectronicInvoiceServiceProvider   |                                           | Role |
| ElectronicInvoiceServiceProvider   | RelatedElectronicInvoiceSolutionService   |      |
| ElectronicInvoiceServiceProvider   | ServiceStatus                             |      |
| ElectronicInvoiceServiceProvider   | RelatedElectronicInvoiceDirectoryService  |      |
| ElectronicInvoiceServiceStatus     |                                           |      |
| ElectronicInvoiceServiceStatus     | ServiceStatus                             |      |
| ElectronicInvoiceServiceStatus     | ActivationStatusReason                    |      |
| ElectronicInvoiceServiceStatus     | EnrolmentStatusReason                     |      |
| ElectronicInvoiceServiceStatus     | StatusReasonOriginator                    |      |
| ElectronicInvoiceServiceStatus     | RelatedElectronicinvoiceProcessingService |      |

| CountrySubdivisionIdentification |          | Identification code and name to<br>identify a name of a unit<br>resulting from the division of a<br>country, dependency, or other<br>area of special geopolitical<br>interest contained in ISO 3166-1,<br>on the basis of country names<br>obtained from the United Nations<br>(ISO 3166-2: Country<br>subdivision code). |
|----------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CountrySubdivisionIdentification | Code     | Code to identify a name of a unit<br>resulting from the division of a<br>country, dependency, or other<br>area of special geopolitical<br>interest contained in ISO 3166-1,<br>CountrySubDivisionCode<br>on the basis of country names<br>obtained from the United Nations<br>(ISO 3166-2: Country<br>subdivision code).  |
| CountrySubdivisionIdentification | Name     | Name to identify a code of a unit<br>resulting from the division of a<br>country, dependency, or other<br>area of special geopolitical<br>interest contained in ISO 3166-1,<br>Max35Text<br>on the basis of country names<br>obtained from the United Nations<br>(ISO 3166-2: Country<br>subdivision code).               |
| CountrySubDivision               |          | Sub division of a nation with its<br>own government.                                                                                                                                                                                                                                                                      |
| CountrySubDivision               | Country  | Nation with its own government.<br>Country                                                                                                                                                                                                                                                                                |
| CountrySubDivision               | Province | A territory governed as an<br>administrative or political unit of<br>a country.                                                                                                                                                                                                                                           |
|                                  |          |                                                                                                                                                                                                                                                                                                                           |

| CountrySubDivision     | Region                 |                   |
|------------------------|------------------------|-------------------|
| CountrySubDivision     | County                 |                   |
| CountrySubDivision     | DistrictSubDivision    |                   |
| CountrySubDivision     | State                  |                   |
| CountrySubDivision     | District               |                   |
| DigitalWallet          |                        | SecuritiesAccount |
| DigitalWallet          | DigitalAssetIdentifier |                   |
| PostTradeRiskReduction |                        |                   |
| PostTradeRiskReduction | Structurer             |                   |
|                        |                        |                   |

| PostTradeRiskReduction | Technique              |  |
|------------------------|------------------------|--|
| PostTradeRiskReduction | PTRRIdentifier         |  |
| PostTradeRiskReduction | RelatedDerivativeEvent |  |
| PostTradeRiskReduction | ServiceProvider        |  |
| DerivativeEvent        |                        |  |
| DerivativeEvent        | EventIdentifier        |  |
| DerivativeEvent        | RelatedDerivative      |  |
| DerivativeEvent        | TimeStamp              |  |
| DerivativeEvent        | PostTradeRiskReduction |  |
| DerivativeEvent        | Type                   |  |
| EnergyDelivery         |                        |  |
| EnergyDelivery         | PointOrZone            |  |
| EnergyDelivery         | Capacity               |  |
|                        |                        |  |

| EnergyDelivery           | Interval             |                          |
|--------------------------|----------------------|--------------------------|
| EnergyDelivery           | RelatedEnergy        |                          |
| Energy                   |                      | Commodity                |
| Energy                   | WeekDay              |                          |
| Energy                   | LoadType             |                          |
| Energy                   | Delivery             |                          |
| Energy                   | Duration             |                          |
| Energy                   | Price                |                          |
| Energy                   | QuantityUnit         |                          |
| Energy                   | InterConnectionPoint |                          |
| Energy                   | Date                 |                          |
| ExecutingPerson          |                      | SecuritiesOrderPartyRole |
| InvestmentDecisionPerson |                      | SecuritiesOrderPartyRole |

| NonExecutingBroker | SecuritiesOrderPartyRole |
|--------------------|--------------------------|
|                    |                          |

## **Traces**

| Message Component Name       | Message Element Name | Type Trace To         | Is<br>Technical | Trace To Business Component |
|------------------------------|----------------------|-----------------------|-----------------|-----------------------------|
| AccountIdentification4Choice | IBAN                 |                       | False           | AccountIdentification       |
| AccountIdentification4Choice | Other                | AccountIdentification | False           | AccountIdentification       |
| AccountSchemeName1Choice     |                      |                       | False           | Scheme                      |
| AccountSchemeName1Choice     | Code                 |                       | False           | Scheme                      |
| AccountSchemeName1Choice     | Proprietary          |                       | False           | Scheme                      |
| AddressType3Choice           |                      |                       | True            |                             |
| AddressType3Choice           | Code                 |                       | True            |                             |
| AddressType3Choice           | Proprietary          | GenericIdentification | True            |                             |
| AdviceType1                  |                      |                       | False           | PaymentProcessing           |
| AdviceType1                  | CreditAdvice         |                       | False           | PaymentProcessing           |
| AdviceType1                  | DebitAdvice          |                       | False           | PaymentProcessing           |
| AdviceType1Choice            |                      |                       | True            |                             |
| AdviceType1Choice            | Code                 |                       | True            |                             |

| AdviceType1Choice             | Proprietary                          |                                | True  |                    |
|-------------------------------|--------------------------------------|--------------------------------|-------|--------------------|
| AmendmentInformationDetails15 |                                      |                                | False | DirectDebitMandate |
| AmendmentInformationDetails15 | OriginalCreditorAgent                | Organisation                   | False | Organisation       |
| AmendmentInformationDetails15 | OriginalCreditorAgentAccount         | CashAccount                    | False | PaymentPartyRole   |
| AmendmentInformationDetails15 | OriginalCreditorSchemeIdentification | PartyIdentificationInformation | False | Party              |
| AmendmentInformationDetails15 | OriginalDebtor                       | PartyIdentificationInformation | False | Party              |
| AmendmentInformationDetails15 | OriginalDebtorAccount                | CashAccount                    | False | PaymentPartyRole   |
| AmendmentInformationDetails15 | OriginalDebtorAgent                  | Organisation                   | False | Organisation       |
| AmendmentInformationDetails15 | OriginalDebtorAgentAccount           | CashAccount                    | False | PaymentPartyRole   |
| AmendmentInformationDetails15 | OriginalFinalCollectionDate          |                                | False | DirectDebitMandate |
| AmendmentInformationDetails15 | OriginalFrequency                    |                                | False | Mandate            |
| AmendmentInformationDetails15 | OriginalMandateIdentification        |                                | False | Mandate            |
| AmendmentInformationDetails15 | OriginalReason                       |                                | False | Agreement          |
| AmendmentInformationDetails15 | OriginalTrackingDays                 |                                | False | Mandate            |

| AmountType4Choice                            |                                    |                            | False | Payment                    |
|----------------------------------------------|------------------------------------|----------------------------|-------|----------------------------|
| AmountType4Choice                            | EquivalentAmount                   | Payment                    | False | Payment                    |
| AmountType4Choice                            | InstructedAmount                   |                            | False | Payment                    |
| Authorisation1Choice                         |                                    |                            | True  |                            |
| Authorisation1Choice                         | Code                               |                            | True  |                            |
| Authorisation1Choice                         | Proprietary                        |                            | True  |                            |
| BranchAndFinancialInstitutionIdentification8 |                                    |                            | False | Organisation               |
| BranchAndFinancialInstitutionIdentification8 | BranchIdentification               | OrganisationIdentification | False | Organisation               |
| BranchAndFinancialInstitutionIdentification8 | FinancialInstitutionIdentification | OrganisationIdentification | False | Organisation               |
| BranchData5                                  |                                    |                            | False | OrganisationIdentification |
| BranchData5                                  | Identification                     |                            | False | GenericIdentification      |
| BranchData5                                  | LEI                                |                            | True  |                            |
| BranchData5                                  | Name                               |                            | False | PartyName                  |
| BranchData5                                  | PostalAddress                      | PostalAddress              | False |                            |
| CashAccount40                                |                                    |                            | False | CashAccount                |
| CashAccount40                                | Currency                           |                            | False | Account                    |
| CashAccount40                                | Identification                     | AccountIdentification      | False | Account                    |
| CashAccount40                                | Name                               |                            | False | AccountIdentification      |
| CashAccount40                                | Proxy                              | AccountIdentification      | False | Account                    |

| CashAccount40          | Type               | CashAccount                    | False | CashAccount       |
|------------------------|--------------------|--------------------------------|-------|-------------------|
| CashAccountType2Choice |                    |                                | False | CashAccount       |
| CashAccountType2Choice | Code               |                                | False | CashAccount       |
| CashAccountType2Choice | Proprietary        |                                | False | CashAccount       |
| CategoryPurpose1Choice |                    |                                | False | Payment           |
| CategoryPurpose1Choice | Code               |                                | False | PaymentProcessing |
| CategoryPurpose1Choice | Proprietary        |                                | False | PaymentProcessing |
| Charges16              |                    |                                | False | Charges           |
| Charges16              | Agent              | Organisation                   | False |                   |
| Charges16              | Amount             |                                | False | Adjustment        |
| Charges16              | Type               | Charges                        | False | Charges           |
| ChargeType3Choice      |                    |                                | False | Charges           |
| ChargeType3Choice      | Code               |                                | False | Charges           |
| ChargeType3Choice      | Proprietary        | GenericIdentification          | False | Charges           |
| Cheque19               |                    |                                | False | ChequeIssue       |
| Cheque19               | ChequeFrom         | PartyIdentificationInformation | False | Party             |
| Cheque19               | ChequeMaturityDate |                                | False | Cheque            |
| Cheque19               | ChequeNumber       |                                | False | CreditInstrument  |

| Cheque19                            | ChequeType           |                                | False | Cheque                   |
|-------------------------------------|----------------------|--------------------------------|-------|--------------------------|
| Cheque19                            | DeliverTo            | PartyIdentificationInformation | False | ChequeIssue              |
| Cheque19                            | DeliveryMethod       | ChequeIssue                    | False | ChequeIssue              |
| Cheque19                            | FormsCode            |                                | False | Cheque                   |
| Cheque19                            | InstructionPriority  |                                | False | Payment                  |
| Cheque19                            | MemoField            |                                | False | Cheque                   |
| Cheque19                            | PrintLocation        |                                | False | ChequeIssue              |
| Cheque19                            | RegionalClearingZone |                                | False | Cheque                   |
| Cheque19                            | Signature            |                                | False |                          |
| ChequeDeliveryMethod1Choice         |                      |                                | False | ChequeIssue              |
| ChequeDeliveryMethod1Choice         | Code                 |                                | False | ChequeIssue              |
| ChequeDeliveryMethod1Choice         | Proprietary          |                                | False | ChequeIssue              |
| ClearingSystemIdentification2Choice |                      |                                | False | CashClearingSystem       |
| ClearingSystemIdentification2Choice | Code                 |                                | False | CashClearingSystem       |
| ClearingSystemIdentification2Choice | Proprietary          |                                | False | CashClearingSystem       |
| ClearingSystemIdentification3Choice |                      |                                | False | CashClearingSystem       |
| ClearingSystemIdentification3Choice | Code                 |                                | False | CashClearingSystem       |
| ClearingSystemIdentification3Choice | Proprietary          |                                | False | CashClearingSystem       |
| ClearingSystemMemberIdentification2 |                      |                                | False | CashClearingSystemMember |

| ClearingSystemMemberIdentification2 | ClearingSystemIdentification | CashClearingSystem | False | CashClearingSystem             |
|-------------------------------------|------------------------------|--------------------|-------|--------------------------------|
| ClearingSystemMemberIdentification2 | MemberIdentification         |                    | False | GenericIdentification          |
| Contact13                           |                              |                    | False | PersonIdentification           |
| Contact13                           | Department                   |                    | False | PostalAddress                  |
| Contact13                           | EmailAddress                 |                    | False | ElectronicAddress              |
| Contact13                           | EmailPurpose                 |                    | True  |                                |
| Contact13                           | FaxNumber                    |                    | False | PhoneAddress                   |
| Contact13                           | JobTitle                     |                    | False | Person                         |
| Contact13                           | MobileNumber                 |                    | False | PhoneAddress                   |
| Contact13                           | Name                         |                    | False | PartyName                      |
| Contact13                           | NamePrefix                   |                    | False | PersonName                     |
| Contact13                           | Other                        | ContactPoint       | False | PartyIdentificationInformation |
| Contact13                           | PhoneNumber                  |                    | False | PhoneAddress                   |
| Contact13                           | PreferredMethod              |                    | False | Party                          |
| Contact13                           | Responsibility               |                    | False | Person                         |
| Contact13                           | URLAddress                   |                    | False | ElectronicAddress              |
|                                     |                              |                    |       |                                |

| CreditorReferenceInformation3 |                       |          | False | PaymentIdentification |
|-------------------------------|-----------------------|----------|-------|-----------------------|
| CreditorReferenceInformation3 | Reference             |          | False | PaymentIdentification |
| CreditorReferenceInformation3 | Type                  | Document | True  |                       |
| CreditorReferenceType2Choice  |                       |          | False | Document              |
| CreditorReferenceType2Choice  | Code                  |          | False | Document              |
| CreditorReferenceType2Choice  | Proprietary           |          | False | Document              |
| CreditorReferenceType3        |                       |          | False | Document              |
| CreditorReferenceType3        | CodeOrProprietary     | Document | False |                       |
| CreditorReferenceType3        | Issuer                |          | False |                       |
| CreditTransferMandateData1    |                       |          | False | CreditTransferMandate |
| CreditTransferMandateData1    | DateOfSignature       |          | False | Agreement             |
| CreditTransferMandateData1    | DateOfVerification    |          | False | CreditTransferMandate |
| CreditTransferMandateData1    | ElectronicSignature   |          | False | CreditTransferMandate |
| CreditTransferMandateData1    | FinalPaymentDate      |          | False | CreditTransferMandate |
| CreditTransferMandateData1    | FirstPaymentDate      |          | False | CreditTransferMandate |
| CreditTransferMandateData1    | Frequency             |          | False | Mandate               |
| CreditTransferMandateData1    | MandateIdentification |          | False | Mandate               |
| CreditTransferMandateData1    | Reason                |          | False | CreditTransferMandate |
| CreditTransferMandateData1    | Type                  | Mandate  | False | Mandate               |
| CreditTransferTransaction61   |                       |          | False | CreditTransfer        |
|                               |                       |          |       |                       |

| CreditTransferTransaction61 | Amount                      | Payment                        | False | Payment          |
|-----------------------------|-----------------------------|--------------------------------|-------|------------------|
| CreditTransferTransaction61 | ChargeBearer                |                                | False | Charges          |
| CreditTransferTransaction61 | ChequeInstruction           | ChequeIssue                    | False |                  |
| CreditTransferTransaction61 | Creditor                    | PartyIdentificationInformation | False | Party            |
| CreditTransferTransaction61 | CreditorAccount             | CashAccount                    | False | PaymentPartyRole |
| CreditTransferTransaction61 | CreditorAgent               | Organisation                   | False | Organisation     |
| CreditTransferTransaction61 | CreditorAgentAccount        | CashAccount                    | False | PaymentPartyRole |
| CreditTransferTransaction61 | ExchangeRateInformation     | CurrencyExchange               | False | Payment          |
| CreditTransferTransaction61 | InstructionForCreditorAgent | Payment                        | False | Payment          |
| CreditTransferTransaction61 | InstructionForDebtorAgent   | Payment                        | False | Payment          |
| CreditTransferTransaction61 | IntermediaryAgent1          | Organisation                   | False | Organisation     |
| CreditTransferTransaction61 | IntermediaryAgent1Account   | CashAccount                    | False | PaymentPartyRole |
| CreditTransferTransaction61 | IntermediaryAgent2          | Organisation                   | False | Organisation     |
| CreditTransferTransaction61 | IntermediaryAgent2Account   | CashAccount                    | False | PaymentPartyRole |
|                             |                             |                                |       |                  |

| CreditTransferTransaction61 | IntermediaryAgent3           | Organisation                   | False | Organisation         |
|-----------------------------|------------------------------|--------------------------------|-------|----------------------|
| CreditTransferTransaction61 | IntermediaryAgent3Account    | CashAccount                    | False | PaymentPartyRole     |
| CreditTransferTransaction61 | MandateRelatedInformation    | CreditTransferMandate          | False | MandatePartyRole     |
| CreditTransferTransaction61 | PaymentIdentification        | PaymentIdentification          | False | Payment              |
| CreditTransferTransaction61 | PaymentTypeInformation       | PaymentProcessing              | False | PaymentExecution     |
| CreditTransferTransaction61 | Purpose                      | PaymentObligation              | False | PaymentObligation    |
| CreditTransferTransaction61 | RegulatoryReporting          | RegulatoryReport               | False | FinancialTransaction |
| CreditTransferTransaction61 | RelatedRemittanceInformation | ContactPoint                   | False | PaymentObligation    |
| CreditTransferTransaction61 | RemittanceInformation        | Document                       | False | PaymentObligation    |
| CreditTransferTransaction61 | SupplementaryData            |                                | True  |                      |
| CreditTransferTransaction61 | Tax                          | Tax                            | False | Payment              |
| CreditTransferTransaction61 | UltimateCreditor             | PartyIdentificationInformation | False | Party                |
| CreditTransferTransaction61 | UltimateDebtor               | PartyIdentificationInformation | False | Party                |
| CurrencyExchange13          |                              |                                | False | CurrencyExchange     |
| CurrencyExchange13          | ExchangeRate                 |                                | False | CurrencyExchange     |
| CurrencyExchange13          | SourceCurrency               |                                | False | CurrencyExchange     |
|                             |                              |                                |       |                      |

| CurrencyExchange13     | TargetCurrency  | False | CurrencyExchange   |
|------------------------|-----------------|-------|--------------------|
| CurrencyExchange13     | UnitCurrency    | False | CurrencyExchange   |
| DateAndDateTime2Choice |                 | True  |                    |
| DateAndDateTime2Choice | Date            | True  |                    |
| DateAndDateTime2Choice | DateTime        | True  |                    |
| DateAndPlaceOfBirth1   |                 | False | Person             |
| DateAndPlaceOfBirth1   | BirthDate       | False | Person             |
| DateAndPlaceOfBirth1   | CityOfBirth     | False | PostalAddress      |
| DateAndPlaceOfBirth1   | CountryOfBirth  | False | Country            |
| DateAndPlaceOfBirth1   | ProvinceOfBirth | False | CountrySubDivision |
| DateAndType1           |                 | True  |                    |
| DateAndType1           | Date            | True  |                    |
| DateAndType1           | Type            | True  |                    |
| DatePeriod2            |                 | True  |                    |
| DatePeriod2            | FromDate        | False | DateTimePeriod     |
| DatePeriod2            | ToDate          | False | DateTimePeriod     |
| DateType2Choice        |                 | True  |                    |
| DateType2Choice        | Code            | True  |                    |
| DateType2Choice        | Proprietary     | True  |                    |
|                        |                 |       |                    |

| DirectDebitTransaction12            |                               |                                | False | DirectDebit       |
|-------------------------------------|-------------------------------|--------------------------------|-------|-------------------|
| DirectDebitTransaction12            | CreditorSchemeIdentification  | PartyIdentificationInformation | False | Party             |
| DirectDebitTransaction12            | MandateRelatedInformation     | DirectDebitMandate             | False | DirectDebit       |
| DirectDebitTransaction12            | PreNotificationDate           |                                | False | DirectDebit       |
| DirectDebitTransaction12            | PreNotificationIdentification |                                | False | DirectDebit       |
| DirectDebitTransactionInformation32 |                               |                                | False | DirectDebit       |
| DirectDebitTransactionInformation32 | ChargeBearer                  |                                | False | Charges           |
| DirectDebitTransactionInformation32 | Debtor                        | PartyIdentificationInformation | False | Party             |
| DirectDebitTransactionInformation32 | DebtorAccount                 | CashAccount                    | False | PaymentPartyRole  |
| DirectDebitTransactionInformation32 | DebtorAgent                   | Organisation                   | False | Organisation      |
| DirectDebitTransactionInformation32 | DebtorAgentAccount            | CashAccount                    | False | PaymentPartyRole  |
| DirectDebitTransactionInformation32 | DirectDebitTransaction        | DirectDebit                    | False |                   |
| DirectDebitTransactionInformation32 | InstructedAmount              |                                | False | Payment           |
| DirectDebitTransactionInformation32 | InstructionForCreditorAgent   |                                | False | Payment           |
| DirectDebitTransactionInformation32 | PaymentIdentification         | PaymentIdentification          | False | Payment           |
| DirectDebitTransactionInformation32 | PaymentTypeInformation        | PaymentProcessing              | False | Payment           |
| DirectDebitTransactionInformation32 | Purpose                       | PaymentObligation              | False | PaymentProcessing |

| DirectDebitTransactionInformation32 | RegulatoryReporting          | RegulatoryReport               | False | FinancialTransaction |
|-------------------------------------|------------------------------|--------------------------------|-------|----------------------|
| DirectDebitTransactionInformation32 | RelatedRemittanceInformation | ContactPoint                   | False | Document             |
| DirectDebitTransactionInformation32 | RemittanceInformation        | Document                       | False | PaymentObligation    |
| DirectDebitTransactionInformation32 | SupplementaryData            |                                | True  |                      |
| DirectDebitTransactionInformation32 | Tax                          | Tax                            | False | Payment              |
| DirectDebitTransactionInformation32 | UltimateCreditor             | PartyIdentificationInformation | False | Party                |
| DirectDebitTransactionInformation32 | UltimateDebtor               | PartyIdentificationInformation | False | Party                |
| DocumentAdjustment1                 |                              |                                | False | Adjustment           |
| DocumentAdjustment1                 | AdditionalInformation        |                                | True  |                      |
| DocumentAdjustment1                 | Amount                       |                                | False | Adjustment           |
| DocumentAdjustment1                 | CreditDebitIndicator         |                                | False | Adjustment           |
| DocumentAdjustment1                 | Reason                       |                                | False | Adjustment           |
| DocumentAmount1                     |                              |                                | False | Adjustment           |
| DocumentAmount1                     | Amount                       |                                | False | Adjustment           |
| DocumentAmount1                     | Type                         | Discount                       | False |                      |
| DocumentAmountType1Choice           |                              |                                | False | Discount             |
| DocumentAmountType1Choice           | Code                         |                                | False | Discount             |

| DocumentAmountType1Choice   | Proprietary       |          | True  |                       |
|-----------------------------|-------------------|----------|-------|-----------------------|
| DocumentLineIdentification1 |                   |          | False | Document              |
| DocumentLineIdentification1 | Number            |          | True  |                       |
| DocumentLineIdentification1 | RelatedDate       |          | False | Document              |
| DocumentLineIdentification1 | Type              | Document | False | Document              |
| DocumentLineInformation2    |                   |          | False | Document              |
| DocumentLineInformation2    | Amount            | Document | False | Document              |
| DocumentLineInformation2    | Description       |          | False |                       |
| DocumentLineInformation2    | Identification    | Document | False | GenericIdentification |
| DocumentLineType1           |                   |          | False | Document              |
| DocumentLineType1           | CodeOrProprietary | Document | False |                       |
| DocumentLineType1           | Issuer            |          | False | GenericIdentification |
| DocumentLineType1Choice     |                   |          | False | Document              |
| DocumentLineType1Choice     | Code              |          | False | Document              |
| DocumentLineType1Choice     | Proprietary       |          | False | Document              |
| DocumentType1               |                   |          | False | Document              |
| DocumentType1               | CodeOrProprietary | Document | False |                       |
| DocumentType1               | Issuer            |          | False |                       |
| DocumentType2Choice         |                   |          | False | Document              |
|                             |                   |          |       |                       |

| DocumentType2Choice                      | Code                               |                            | False | Document                   |
|------------------------------------------|------------------------------------|----------------------------|-------|----------------------------|
| DocumentType2Choice                      | Proprietary                        |                            | False | Document                   |
| EquivalentAmount2                        |                                    |                            | False | Payment                    |
| EquivalentAmount2                        | Amount                             |                            | False | Payment                    |
| EquivalentAmount2                        | CurrencyOfTransfer                 |                            | False | Payment                    |
| ExchangeRate1                            |                                    |                            | False | CurrencyExchange           |
| ExchangeRate1                            | ContractIdentification             |                            | False | TradeIdentification        |
| ExchangeRate1                            | ExchangeRate                       |                            | False | CurrencyExchange           |
| ExchangeRate1                            | RateType                           |                            | False | CurrencyExchange           |
| ExchangeRate1                            | UnitCurrency                       |                            | False | CurrencyExchange           |
| FinancialIdentificationSchemeName1Choice |                                    |                            | False | Scheme                     |
| FinancialIdentificationSchemeName1Choice | Code                               |                            | False | Scheme                     |
| FinancialIdentificationSchemeName1Choice | Proprietary                        |                            | False | Scheme                     |
| FinancialInstitutionIdentification23     |                                    |                            | False | OrganisationIdentification |
| FinancialInstitutionIdentification23     | BICFI                              |                            | False | OrganisationIdentification |
| FinancialInstitutionIdentification23     | ClearingSystemMemberIdentification | CashClearingSystemMember   | False | OrganisationIdentification |
| FinancialInstitutionIdentification23     | LEI                                |                            | True  |                            |
| FinancialInstitutionIdentification23     | Name                               |                            | False | PartyName                  |
| FinancialInstitutionIdentification23     | Other                              | OrganisationIdentification | False |                            |

| FinancialInstitutionIdentification23 | PostalAddress                   | PostalAddress                  | False |               |
|--------------------------------------|---------------------------------|--------------------------------|-------|---------------|
| Frequency36Choice                    |                                 |                                | True  |               |
| Frequency36Choice                    | Period                          |                                | True  |               |
| Frequency36Choice                    | PointInTime                     |                                | True  |               |
| Frequency36Choice                    | Type                            |                                | True  |               |
| FrequencyAndMoment1                  |                                 |                                | True  |               |
| FrequencyAndMoment1                  | PointInTime                     |                                | True  |               |
| FrequencyAndMoment1                  | Type                            |                                | True  |               |
| FrequencyPeriod1                     |                                 |                                | True  |               |
| FrequencyPeriod1                     | CountPerPeriod                  |                                | True  |               |
| FrequencyPeriod1                     | Type                            |                                | True  |               |
| Garnishment4                         |                                 |                                | False | Garnishment   |
| Garnishment4                         | Date                            |                                | False | Trade         |
| Garnishment4                         | EmployeeTerminationIndicator    |                                | False | PersonProfile |
| Garnishment4                         | FamilyMedicalInsuranceIndicator |                                | False | PersonProfile |
| Garnishment4                         | Garnishee                       | PartyIdentificationInformation | False |               |
| Garnishment4                         | GarnishmentAdministrator        | PartyIdentificationInformation | False | Party         |

| ReferenceNumber   |          | False | Tax                        |
|-------------------|----------|-------|----------------------------|
| RemittedAmount    |          | False | Document                   |
| Type              | Document | False | PaymentObligation          |
|                   |          | False | Document                   |
| CodeOrProprietary | Document | False |                            |
| Issuer            |          | False |                            |
|                   |          | False | Document                   |
| Code              |          | False | Document                   |
| Proprietary       |          | False | Document                   |
|                   |          | False | AccountIdentification      |
| Identification    |          | False | GenericIdentification      |
| Issuer            |          | False |                            |
| SchemeName        | Scheme   | False | GenericIdentification      |
|                   |          | False | OrganisationIdentification |
| Identification    |          | False | GenericIdentification      |
| Issuer            |          | False |                            |
| SchemeName        | Scheme   | False | GenericIdentification      |
|                   |          | False | GenericIdentification      |
| Identification    |          | False | GenericIdentification      |
|                   |          |       |                            |

| GenericIdentification3             | Issuer           |                            | False |                            |
|------------------------------------|------------------|----------------------------|-------|----------------------------|
| GenericIdentification30            |                  |                            | False | GenericIdentification      |
| GenericIdentification30            | Identification   |                            | False | GenericIdentification      |
| GenericIdentification30            | Issuer           |                            | False |                            |
| GenericIdentification30            | SchemeName       |                            | False | Scheme                     |
| GenericOrganisationIdentification3 |                  |                            | False | OrganisationIdentification |
| GenericOrganisationIdentification3 | Identification   |                            | False | GenericIdentification      |
| GenericOrganisationIdentification3 | Issuer           |                            | False |                            |
| GenericOrganisationIdentification3 | SchemeName       | OrganisationIdentification | False | GenericIdentification      |
| GenericPersonIdentification2       |                  |                            | False | PersonIdentification       |
| GenericPersonIdentification2       | Identification   |                            | False | GenericIdentification      |
| GenericPersonIdentification2       | Issuer           |                            | False |                            |
| GenericPersonIdentification2       | SchemeName       | PersonIdentification       | False | GenericIdentification      |
| GroupHeader114                     |                  |                            | False | Payment                    |
| GroupHeader114                     | Authorisation    |                            | True  |                            |
| GroupHeader114                     | ControlSum       |                            | True  |                            |
| GroupHeader114                     | CreationDateTime |                            | False | PaymentExecution           |
| GroupHeader114                     | ForwardingAgent  | Organisation               | False | Organisation               |

| GroupHeader114 | InitiatingParty       | PartyIdentificationInformation | False | Party                 |
|----------------|-----------------------|--------------------------------|-------|-----------------------|
| GroupHeader114 | InitiationSource      |                                | True  |                       |
| GroupHeader114 | MessageIdentification |                                | False | PaymentIdentification |
| GroupHeader114 | NumberOfTransactions  |                                | True  |                       |
| GroupHeader118 |                       |                                | False | Payment               |
| GroupHeader118 | Authorisation         |                                | True  |                       |
| GroupHeader118 | ControlSum            |                                | True  |                       |
| GroupHeader118 | CreationDateTime      |                                | False | PaymentExecution      |
| GroupHeader118 | ForwardingAgent       | Organisation                   | False | Organisation          |
| GroupHeader118 | InitiatingParty       | PartyIdentificationInformation | False | Party                 |
| GroupHeader118 | MessageIdentification |                                | False | PaymentIdentification |
| GroupHeader118 | NumberOfTransactions  |                                | True  |                       |
| GroupHeader124 |                       |                                | False | Payment               |
| GroupHeader124 | Authorisation         |                                | True  |                       |
| GroupHeader124 | ControlSum            |                                | True  |                       |
| GroupHeader124 | CreationDateTime      |                                | False | PaymentExecution      |

| GroupHeader124 | CreditorAgent         | Organisation                   | False | Organisation          |
|----------------|-----------------------|--------------------------------|-------|-----------------------|
| GroupHeader124 | DebtorAgent           | Organisation                   | False | Organisation          |
| GroupHeader124 | ForwardingAgent       | Organisation                   | False | Organisation          |
| GroupHeader124 | GroupReversal         |                                | True  |                       |
| GroupHeader124 | InitiatingParty       | PartyIdentificationInformation | False | Party                 |
| GroupHeader124 | MessageIdentification |                                | False | PaymentIdentification |
| GroupHeader124 | NumberOfTransactions  |                                | True  |                       |
| GroupHeader128 |                       |                                | False | Payment               |
| GroupHeader128 | CreationDateTime      |                                | False | PaymentExecution      |
| GroupHeader128 | CreditorAgent         | Organisation                   | False | Organisation          |
| GroupHeader128 | DebtorAgent           | Organisation                   | False | Organisation          |
| GroupHeader128 | ForwardingAgent       | Organisation                   | False | Organisation          |
| GroupHeader128 | InitiatingParty       | PartyIdentificationInformation | False | Party                 |
|                |                       |                                |       |                       |

| GroupHeader128               | MessageIdentification       |                       | False | PaymentIdentification |
|------------------------------|-----------------------------|-----------------------|-------|-----------------------|
| InstructionForCreditorAgent3 |                             |                       | False | Payment               |
| InstructionForCreditorAgent3 | Code                        |                       | False | Payment               |
| InstructionForCreditorAgent3 | InstructionInformation      |                       | True  |                       |
| InstructionForDebtorAgent1   |                             |                       | False | Payment               |
| InstructionForDebtorAgent1   | Code                        |                       | False | Payment               |
| InstructionForDebtorAgent1   | InstructionInformation      |                       | True  |                       |
| LocalInstrument2Choice       |                             |                       | False | PaymentProcessing     |
| LocalInstrument2Choice       | Code                        |                       | False | PaymentProcessing     |
| LocalInstrument2Choice       | Proprietary                 |                       | False | PaymentProcessing     |
| MandateClassification1Choice |                             |                       | False | Payment               |
| MandateClassification1Choice | Code                        |                       | False | PaymentProcessing     |
| MandateClassification1Choice | Proprietary                 |                       | False | PaymentProcessing     |
| MandateRelatedData3Choice    |                             |                       | True  |                       |
| MandateRelatedData3Choice    | CreditTransferMandate       | CreditTransferMandate | True  |                       |
| MandateRelatedData3Choice    | DirectDebitMandate          | DirectDebitMandate    | True  |                       |
| MandateRelatedInformation16  |                             |                       | False | DirectDebitMandate    |
| MandateRelatedInformation16  | AmendmentIndicator          |                       | False | Mandate               |
| MandateRelatedInformation16  | AmendmentInformationDetails | DirectDebitMandate    | False |                       |
|                              |                             |                       |       |                       |

| MandateRelatedInformation16 | DateOfSignature       |                   | False | Agreement                      | DateSigned            |
|-----------------------------|-----------------------|-------------------|-------|--------------------------------|-----------------------|
| MandateRelatedInformation16 | ElectronicSignature   |                   | False |                                |                       |
| MandateRelatedInformation16 | FinalCollectionDate   |                   | False | DirectDebitMandate             | FinalCollectionDate   |
| MandateRelatedInformation16 | FirstCollectionDate   |                   | False | DirectDebitMandate             | FirstCollectionDate   |
| MandateRelatedInformation16 | Frequency             |                   | False | Mandate                        | Frequency             |
| MandateRelatedInformation16 | MandateIdentification |                   | False | Mandate                        | MandateIdentification |
| MandateRelatedInformation16 | Reason                |                   | False | Agreement                      | Description           |
| MandateRelatedInformation16 | TrackingDays          |                   | False | Mandate                        | TrackingDays          |
| MandateSetupReason1Choice   |                       |                   | True  |                                |                       |
| MandateSetupReason1Choice   | Code                  |                   | True  |                                |                       |
| MandateSetupReason1Choice   | Proprietary           |                   | True  |                                |                       |
| MandateTypeInformation2     |                       |                   | False | Mandate                        |                       |
| MandateTypeInformation2     | CategoryPurpose       | Payment           | False | PaymentProcessing              | CategoryPurpose       |
| MandateTypeInformation2     | Classification        | Payment           | False | DirectDebitMandate             | Classification        |
| MandateTypeInformation2     | LocalInstrument       | PaymentProcessing | False | Mandate                        | MandatePaymentType    |
| MandateTypeInformation2     | ServiceLevel          | ServiceLevel      | False | PaymentProcessing              | ServiceLevel          |
| NameAndAddress18            |                       |                   | False | PartyIdentificationInformation |                       |
| NameAndAddress18            | Address               | PostalAddress     | False |                                |                       |

| NameAndAddress18                            | Name                              |                            | False | PartyName                      |
|---------------------------------------------|-----------------------------------|----------------------------|-------|--------------------------------|
| NumberOfTransactionsPerStatus5              |                                   |                            | True  |                                |
| NumberOfTransactionsPerStatus5              | DetailedControlSum                |                            | True  |                                |
| NumberOfTransactionsPerStatus5              | DetailedNumberOfTransactions      |                            | True  |                                |
| NumberOfTransactionsPerStatus5              | DetailedStatus                    |                            | True  |                                |
| OrganisationIdentification39                |                                   |                            | False | OrganisationIdentification     |
| OrganisationIdentification39                | AnyBIC                            |                            | False | OrganisationIdentification     |
| OrganisationIdentification39                | LEI                               |                            | True  |                                |
| OrganisationIdentification39                | Other                             | OrganisationIdentification | False | PartyIdentificationInformation |
| OrganisationIdentificationSchemeName1Choice |                                   |                            | False | OrganisationIdentification     |
| OrganisationIdentificationSchemeName1Choice | Code                              |                            | False | Scheme                         |
| OrganisationIdentificationSchemeName1Choice | Proprietary                       |                            | False | Scheme                         |
| OriginalGroupHeader20                       |                                   |                            | False | PaymentExecution               |
| OriginalGroupHeader20                       | OriginalCreationDateTime          |                            | False | PaymentExecution               |
| OriginalGroupHeader20                       | OriginalMessageIdentification     |                            | False | PaymentIdentification          |
| OriginalGroupHeader20                       | OriginalMessageNameIdentification |                            | True  |                                |
| OriginalGroupHeader20                       | ReversalReasonInformation         | StatusReason               | False | Payment                        |
| OriginalGroupHeader22                       |                                   |                            | False | PaymentExecution               |
| OriginalGroupHeader22                       | GroupStatus                       |                            | False | PaymentStatus                  |

| OriginalGroupHeader22        | NumberOfTransactionsPerStatus            |               | True  |                       |
|------------------------------|------------------------------------------|---------------|-------|-----------------------|
| OriginalGroupHeader22        | OriginalControlSum                       |               | True  |                       |
| OriginalGroupHeader22        | OriginalCreationDateTime                 |               | False | PaymentExecution      |
| OriginalGroupHeader22        | OriginalMessageIdentification            |               | False | PaymentIdentification |
| OriginalGroupHeader22        | OriginalMessageNameIdentification        |               | True  |                       |
| OriginalGroupHeader22        | OriginalNumberOfTransactions             |               | True  |                       |
| OriginalGroupHeader22        | StatusReasonInformation                  | PaymentStatus | False | Status                |
| OriginalPaymentInstruction50 |                                          |               | False | Payment               |
| OriginalPaymentInstruction50 | BatchBooking                             |               | True  |                       |
| OriginalPaymentInstruction50 | OriginalControlSum                       |               | True  |                       |
| OriginalPaymentInstruction50 | OriginalNumberOfTransactions             |               | True  |                       |
| OriginalPaymentInstruction50 | OriginalPaymentInformationIdentification |               | False | TradeIdentification   |
| OriginalPaymentInstruction50 | PaymentInformationReversal               |               | True  |                       |
| OriginalPaymentInstruction50 | ReversalPaymentInformationIdentification |               | False | PaymentIdentification |
| OriginalPaymentInstruction50 | ReversalReasonInformation                | StatusReason  | False | Status                |
| OriginalPaymentInstruction50 | TransactionInformation                   | Payment       | False |                       |
| OriginalPaymentInstruction51 |                                          |               | False | Payment               |
| OriginalPaymentInstruction51 | NumberOfTransactionsPerStatus            |               | True  |                       |
| OriginalPaymentInstruction51 | OriginalControlSum                       |               | True  |                       |
|                              |                                          |               |       |                       |

| OriginalPaymentInstruction51   | OriginalNumberOfTransactions             |                                | True  |                     |
|--------------------------------|------------------------------------------|--------------------------------|-------|---------------------|
| OriginalPaymentInstruction51   | OriginalPaymentInformationIdentification |                                | False | TradeIdentification |
| OriginalPaymentInstruction51   | PaymentInformationStatus                 |                                | False | PaymentStatus       |
| OriginalPaymentInstruction51   | StatusReasonInformation                  | PaymentStatus                  | False | Status              |
| OriginalPaymentInstruction51   | TransactionInformationAndStatus          | Payment                        | False |                     |
| OriginalTransactionReference42 |                                          |                                | False | Payment             |
| OriginalTransactionReference42 | Amount                                   | Payment                        | False | Payment             |
| OriginalTransactionReference42 | Creditor                                 | PartyIdentificationInformation | False | Party               |
| OriginalTransactionReference42 | CreditorAccount                          | CashAccount                    | False | PaymentPartyRole    |
| OriginalTransactionReference42 | CreditorAgent                            | Organisation                   | False | Party               |
| OriginalTransactionReference42 | CreditorAgentAccount                     | CashAccount                    | False | PaymentPartyRole    |
| OriginalTransactionReference42 | CreditorSchemeIdentification             | PartyIdentificationInformation | False | Party               |
| OriginalTransactionReference42 | Debtor                                   | PartyIdentificationInformation | False | Party               |
| OriginalTransactionReference42 | DebtorAccount                            | CashAccount                    | False | PaymentPartyRole    |
| OriginalTransactionReference42 | DebtorAgent                              | Organisation                   | False | Party               |
| OriginalTransactionReference42 | DebtorAgentAccount                       | CashAccount                    | False | PaymentPartyRole    |
|                                |                                          |                                |       |                     |

| OriginalTransactionReference42 | InterbankSettlementAmount |                                | False | CashSettlement                 |
|--------------------------------|---------------------------|--------------------------------|-------|--------------------------------|
| OriginalTransactionReference42 | InterbankSettlementDate   |                                | False | CashSettlement                 |
| OriginalTransactionReference42 | MandateRelatedInformation |                                | False |                                |
| OriginalTransactionReference42 | PaymentMethod             |                                | False | CreditInstrument               |
| OriginalTransactionReference42 | PaymentTypeInformation    | PaymentProcessing              | False | PaymentExecution               |
| OriginalTransactionReference42 | Purpose                   | PaymentObligation              | False | PaymentObligation              |
| OriginalTransactionReference42 | RemittanceInformation     | Document                       | False | PaymentObligation              |
| OriginalTransactionReference42 | RequestedCollectionDate   |                                | False | Obligation                     |
| OriginalTransactionReference42 | RequestedExecutionDate    |                                | False | Obligation                     |
| OriginalTransactionReference42 | SettlementInformation     | CashSettlement                 | False | PaymentInstruction             |
| OriginalTransactionReference42 | UltimateCreditor          | PartyIdentificationInformation | False | Party                          |
| OriginalTransactionReference42 | UltimateDebtor            | PartyIdentificationInformation | False | Party                          |
| OtherContact1                  |                           |                                | False | ContactPoint                   |
| OtherContact1                  | ChannelType               |                                | True  |                                |
| OtherContact1                  | Identification            |                                | False | ContactPoint                   |
| Party50Choice                  |                           |                                | False | PartyIdentificationInformation |
|                                |                           |                                |       |                                |

| Party50Choice            | Agent                      | Organisation                   | False |                                |
|--------------------------|----------------------------|--------------------------------|-------|--------------------------------|
| Party50Choice            | Party                      | PartyIdentificationInformation | False |                                |
| Party52Choice            |                            |                                | False | PartyIdentificationInformation |
| Party52Choice            | OrganisationIdentification | OrganisationIdentification     | False |                                |
| Party52Choice            | PrivateIdentification      | PersonIdentification           | False |                                |
| PartyIdentification272   |                            |                                | False | PartyIdentificationInformation |
| PartyIdentification272   | ContactDetails             | PersonIdentification           | False | Party                          |
| PartyIdentification272   | CountryOfResidence         |                                | False | Country                        |
| PartyIdentification272   | Identification             | PartyIdentificationInformation | False |                                |
| PartyIdentification272   | Name                       |                                | False | PartyName                      |
| PartyIdentification272   | PostalAddress              | PostalAddress                  | False |                                |
| PaymentIdentification6   |                            |                                | False | PaymentIdentification          |
| PaymentIdentification6   | EndToEndIdentification     |                                | False | PaymentIdentification          |
| PaymentIdentification6   | InstructionIdentification  |                                | False | PaymentIdentification          |
| PaymentIdentification6   | UETR                       |                                | False | PaymentIdentification          |
| PaymentInitiationSource1 |                            |                                | True  |                                |
| PaymentInitiationSource1 | Name                       |                                | True  |                                |
| PaymentInitiationSource1 | Provider                   |                                | True  |                                |
| PaymentInitiationSource1 | Version                    |                                | True  |                                |
|                          |                            |                                |       |                                |

| PaymentInstruction44 |                                      |                                | False | PaymentInstruction  |
|----------------------|--------------------------------------|--------------------------------|-------|---------------------|
| PaymentInstruction44 | BatchBooking                         |                                | True  |                     |
| PaymentInstruction44 | ChargeBearer                         |                                | False | Charges             |
| PaymentInstruction44 | ChargesAccount                       | CashAccount                    | False | Charges             |
| PaymentInstruction44 | ChargesAccountAgent                  | Organisation                   | False | Organisation        |
| PaymentInstruction44 | ControlSum                           |                                | True  |                     |
| PaymentInstruction44 | CreditTransferTransactionInformation | CreditTransfer                 | False |                     |
| PaymentInstruction44 | Debtor                               | PartyIdentificationInformation | False | Party               |
| PaymentInstruction44 | DebtorAccount                        | CashAccount                    | False | PaymentPartyRole    |
| PaymentInstruction44 | DebtorAgent                          | Organisation                   | False | Organisation        |
| PaymentInstruction44 | DebtorAgentAccount                   | CashAccount                    | False | PaymentPartyRole    |
| PaymentInstruction44 | InstructionForDebtorAgent            |                                | False | Payment             |
| PaymentInstruction44 | NumberOfTransactions                 |                                | True  |                     |
| PaymentInstruction44 | PaymentInformationIdentification     |                                | False | TradeIdentification |
| PaymentInstruction44 | PaymentMethod                        |                                | False | CreditInstrument    |
|                      |                                      |                                |       |                     |

| PaymentInstruction44 | PaymentTypeInformation | PaymentProcessing              | False | PaymentExecution   |
|----------------------|------------------------|--------------------------------|-------|--------------------|
| PaymentInstruction44 | PoolingAdjustmentDate  |                                | False | Payment            |
| PaymentInstruction44 | RequestedAdviceType    | PaymentProcessing              | True  |                    |
| PaymentInstruction44 | RequestedExecutionDate |                                | False | PaymentExecution   |
| PaymentInstruction44 | UltimateDebtor         | PartyIdentificationInformation | False | Party              |
| PaymentInstruction45 |                        |                                | False | PaymentInstruction |
| PaymentInstruction45 | BatchBooking           |                                | True  |                    |
| PaymentInstruction45 | ChargeBearer           |                                | False | Charges            |
| PaymentInstruction45 | ChargesAccount         | CashAccount                    | False | Charges            |
| PaymentInstruction45 | ChargesAccountAgent    | Organisation                   | False | Organisation       |
| PaymentInstruction45 | ControlSum             |                                | True  |                    |
| PaymentInstruction45 | Creditor               | PartyIdentificationInformation | False | Party              |
| PaymentInstruction45 | CreditorAccount        | CashAccount                    | False | PaymentPartyRole   |
| PaymentInstruction45 | CreditorAgent          | Organisation                   | False | Party              |
| PaymentInstruction45 | CreditorAgentAccount   | CashAccount                    | False | PaymentPartyRole   |

| PaymentInstruction45    | CreditorSchemeIdentification      | PartyIdentificationInformation | False | Party                 |
|-------------------------|-----------------------------------|--------------------------------|-------|-----------------------|
| PaymentInstruction45    | DirectDebitTransactionInformation | DirectDebit                    | False |                       |
| PaymentInstruction45    | NumberOfTransactions              |                                | True  |                       |
| PaymentInstruction45    | PaymentInformationIdentification  |                                | False | TradeIdentification   |
| PaymentInstruction45    | PaymentMethod                     |                                | False | CreditInstrument      |
| PaymentInstruction45    | PaymentTypeInformation            | PaymentProcessing              | False | PaymentExecution      |
| PaymentInstruction45    | RequestedAdviceType               | PaymentProcessing              | True  |                       |
| PaymentInstruction45    | RequestedCollectionDate           |                                | False | PaymentExecution      |
| PaymentInstruction45    | UltimateCreditor                  | PartyIdentificationInformation | False | Party                 |
| PaymentReversalReason10 |                                   |                                | False | StatusReason          |
| PaymentReversalReason10 | AdditionalInformation             |                                | False | StatusReason          |
| PaymentReversalReason10 | Originator                        | PartyIdentificationInformation | False | Party                 |
| PaymentReversalReason10 | Reason                            | PaymentStatus                  | False |                       |
| PaymentTransaction156   |                                   |                                | False | Payment               |
| PaymentTransaction156   | ChargeBearer                      |                                | False | Charges               |
| PaymentTransaction156   | OriginalEndToEndIdentification    |                                | False | PaymentIdentification |
| PaymentTransaction156   | OriginalInstructedAmount          |                                | False | Payment               |

| PaymentTransaction156 | OriginalInstructionIdentification |               | False | PaymentIdentification |
|-----------------------|-----------------------------------|---------------|-------|-----------------------|
| PaymentTransaction156 | OriginalTransactionReference      | Payment       | False |                       |
| PaymentTransaction156 | OriginalUETR                      |               | False | PaymentIdentification |
| PaymentTransaction156 | ReversalIdentification            |               | True  |                       |
| PaymentTransaction156 | ReversalReasonInformation         | StatusReason  | False | Status                |
| PaymentTransaction156 | ReversedInstructedAmount          |               | False | Payment               |
| PaymentTransaction156 | SupplementaryData                 |               | True  |                       |
| PaymentTransaction160 |                                   |               | False | Payment               |
| PaymentTransaction160 | AcceptanceDateTime                |               | False | PaymentExecution      |
| PaymentTransaction160 | AccountServicerReference          |               | False | Entry                 |
| PaymentTransaction160 | ChargesInformation                | Charges       | False |                       |
| PaymentTransaction160 | ClearingSystemReference           |               | False | PaymentIdentification |
| PaymentTransaction160 | OriginalEndToEndIdentification    |               | False | PaymentIdentification |
| PaymentTransaction160 | OriginalInstructionIdentification |               | False | PaymentIdentification |
| PaymentTransaction160 | OriginalTransactionReference      | Payment       | False |                       |
| PaymentTransaction160 | OriginalUETR                      |               | False | PaymentIdentification |
| PaymentTransaction160 | StatusIdentification              |               | True  |                       |
| PaymentTransaction160 | StatusReasonInformation           | PaymentStatus | False | Status                |
|                       |                                   |               |       |                       |

| PaymentTransaction160    | SupplementaryData   |                   | True  |                   |
|--------------------------|---------------------|-------------------|-------|-------------------|
| PaymentTransaction160    | TrackerData         | PaymentTracker    | False |                   |
| PaymentTransaction160    | TransactionStatus   |                   | False | Payment           |
| PaymentTypeInformation26 |                     |                   | False | PaymentProcessing |
| PaymentTypeInformation26 | CategoryPurpose     | Payment           | False | PaymentProcessing |
| PaymentTypeInformation26 | InstructionPriority |                   | False | PaymentProcessing |
| PaymentTypeInformation26 | LocalInstrument     | PaymentProcessing | False | PaymentProcessing |
| PaymentTypeInformation26 | ServiceLevel        | ServiceLevel      | False | PaymentProcessing |
| PaymentTypeInformation27 |                     |                   | False | PaymentProcessing |
| PaymentTypeInformation27 | CategoryPurpose     | Payment           | False | PaymentProcessing |
| PaymentTypeInformation27 | ClearingChannel     |                   | False | PaymentProcessing |
| PaymentTypeInformation27 | InstructionPriority |                   | False | PaymentProcessing |
| PaymentTypeInformation27 | LocalInstrument     | PaymentProcessing | False | PaymentProcessing |
| PaymentTypeInformation27 | SequenceType        |                   | False | PaymentProcessing |
| PaymentTypeInformation27 | ServiceLevel        | ServiceLevel      | False | PaymentProcessing |
| PaymentTypeInformation29 |                     |                   | False | PaymentProcessing |
| PaymentTypeInformation29 | CategoryPurpose     | Payment           | False | PaymentProcessing |
| PaymentTypeInformation29 | InstructionPriority |                   | False | PaymentProcessing |
| PaymentTypeInformation29 | LocalInstrument     | PaymentProcessing | False | PaymentProcessing |

| PaymentTypeInformation29              | SequenceType        |                      | False | PaymentProcessing              |
|---------------------------------------|---------------------|----------------------|-------|--------------------------------|
| PaymentTypeInformation29              | ServiceLevel        | ServiceLevel         | False | PaymentProcessing              |
| PersonIdentification18                |                     |                      | False | PersonIdentification           |
| PersonIdentification18                | DateAndPlaceOfBirth | Person               | False | PersonIdentification           |
| PersonIdentification18                | Other               | PersonIdentification | False | PartyIdentificationInformation |
| PersonIdentificationSchemeName1Choice |                     |                      | False | PersonIdentification           |
| PersonIdentificationSchemeName1Choice | Code                |                      | False | Scheme                         |
| PersonIdentificationSchemeName1Choice | Proprietary         |                      | False | Scheme                         |
| PostalAddress27                       |                     |                      | False | PostalAddress                  |
| PostalAddress27                       | AddressLine         |                      | True  |                                |
| PostalAddress27                       | AddressType         |                      | False | PostalAddress                  |
| PostalAddress27                       | BuildingName        |                      | False | PostalAddress                  |
| PostalAddress27                       | BuildingNumber      |                      | False | PostalAddress                  |
| PostalAddress27                       | CareOf              |                      | False | PostalAddress                  |
| PostalAddress27                       | Country             |                      | False | Country                        |
| PostalAddress27                       | CountrySubDivision  |                      | False | CountrySubDivision             |
| PostalAddress27                       | Department          |                      | False | PostalAddress                  |
| PostalAddress27                       | DistrictName        |                      | False | CountrySubDivision             |
| PostalAddress27                       | Floor               |                      | False | PostalAddress                  |
| PostalAddress27                       | PostBox             |                      | False | PostalAddress                  |

| PostalAddress27              | PostCode         |          | False | PostalAddress         |
|------------------------------|------------------|----------|-------|-----------------------|
| PostalAddress27              | Room             |          | False | PostalAddress         |
| PostalAddress27              | StreetName       |          | False | PostalAddress         |
| PostalAddress27              | SubDepartment    |          | False | PostalAddress         |
| PostalAddress27              | TownLocationName |          | False |                       |
| PostalAddress27              | TownName         |          | False | PostalAddress         |
| PostalAddress27              | UnitNumber       |          | False | PostalAddress         |
| ProxyAccountIdentification1  |                  |          | False | AccountIdentification |
| ProxyAccountIdentification1  | Identification   |          | False | GenericIdentification |
| ProxyAccountIdentification1  | Type             | Scheme   | False | GenericIdentification |
| ProxyAccountType1Choice      |                  |          | False | Scheme                |
| ProxyAccountType1Choice      | Code             |          | False | Scheme                |
| ProxyAccountType1Choice      | Proprietary      |          | False | Scheme                |
| Purpose2Choice               |                  |          | False | PaymentObligation     |
| Purpose2Choice               | Code             |          | False | PaymentObligation     |
| Purpose2Choice               | Proprietary      |          | False | PaymentObligation     |
| ReferredDocumentInformation8 |                  |          | False | Document              |
| ReferredDocumentInformation8 | LineDetails      | Document | False |                       |
| ReferredDocumentInformation8 | Number           |          | False | GenericIdentification |
| ReferredDocumentInformation8 | RelatedDate      |          | False | Document              |

| ReferredDocumentInformation8 | Type                          | Document                | False | Document                |
|------------------------------|-------------------------------|-------------------------|-------|-------------------------|
| RegulatoryAuthority2         |                               |                         | False | RegulatoryAuthorityRole |
| RegulatoryAuthority2         | Country                       |                         | False | Country                 |
| RegulatoryAuthority2         | Name                          |                         | False | PartyName               |
| RegulatoryReporting3         |                               |                         | False | RegulatoryReport        |
| RegulatoryReporting3         | Authority                     | RegulatoryAuthorityRole | False | RegulatoryReport        |
| RegulatoryReporting3         | DebitCreditReportingIndicator |                         | False | RegulatoryReport        |
| RegulatoryReporting3         | Details                       | RegulatoryReport        | False |                         |
| RemittanceAmount4            |                               |                         | False | Document                |
| RemittanceAmount4            | AdjustmentAmountAndReason     | Adjustment              | False | Payment                 |
| RemittanceAmount4            | RemittanceAmountAndType       | Adjustment              | False | Document                |
| RemittanceInformation22      |                               |                         | False | Document                |
| RemittanceInformation22      | Structured                    | Document                | False |                         |
| RemittanceInformation22      | Unstructured                  |                         | False |                         |
| RemittanceLocation8          |                               |                         | False | ContactPoint            |
| RemittanceLocation8          | RemittanceIdentification      |                         | True  |                         |
| RemittanceLocation8          | RemittanceLocationDetails     | ContactPoint            | False |                         |
| RemittanceLocationData2      |                               |                         | False | ContactPoint            |
| RemittanceLocationData2      | ElectronicAddress             |                         | False |                         |

| RemittanceLocationData2 | Method                               |                                | False | PaymentObligation                  |
|-------------------------|--------------------------------------|--------------------------------|-------|------------------------------------|
| RemittanceLocationData2 | PostalAddress                        | PartyIdentificationInformation | False |                                    |
| ReversalReason4Choice   |                                      |                                | False | PaymentStatus                      |
| ReversalReason4Choice   | Code                                 |                                | False | PaymentStatus                      |
| ReversalReason4Choice   | Proprietary                          |                                | False | PaymentStatus                      |
| ServiceLevel8Choice     |                                      |                                | False | ServiceLevel                       |
| ServiceLevel8Choice     | Code                                 |                                | False | ServiceLevel                       |
| ServiceLevel8Choice     | Proprietary                          |                                | False |                                    |
| SettlementInstruction15 |                                      |                                | False | CashSettlement                     |
| SettlementInstruction15 | ClearingSystem                       | CashClearingSystem             | False |                                    |
| SettlementInstruction15 | InstructedReimbursementAgent         | Organisation                   | False |                                    |
| SettlementInstruction15 | InstructedReimbursementAgentAccount  | CashAccount                    | False | CashSettlementInstructionPartyRole |
| SettlementInstruction15 | InstructingReimbursementAgent        | Organisation                   | False | Organisation                       |
| SettlementInstruction15 | InstructingReimbursementAgentAccount | CashAccount                    | False | CashSettlementInstructionPartyRole |
| SettlementInstruction15 | SettlementAccount                    | CashAccount                    | False | CashSettlement                     |

| SettlementInstruction15           | SettlementMethod                |                                | False | CashSettlement                     |
|-----------------------------------|---------------------------------|--------------------------------|-------|------------------------------------|
| SettlementInstruction15           | ThirdReimbursementAgent         | Organisation                   | False | Party                              |
| SettlementInstruction15           | ThirdReimbursementAgentAccount  | CashAccount                    | False | CashSettlementInstructionPartyRole |
| StatusReason6Choice               |                                 |                                | False | StatusReason                       |
| StatusReason6Choice               | Code                            |                                | False | StatusReason                       |
| StatusReason6Choice               | Proprietary                     |                                | False | StatusReason                       |
| StatusReasonInformation14         |                                 |                                | False | PaymentStatus                      |
| StatusReasonInformation14         | AdditionalInformation           |                                | False | Status                             |
| StatusReasonInformation14         | Originator                      | PartyIdentificationInformation | False | Party                              |
| StatusReasonInformation14         | Reason                          | StatusReason                   | False | Status                             |
| StructuredRegulatoryReporting3    |                                 |                                | False | RegulatoryReport                   |
| StructuredRegulatoryReporting3    | Amount                          |                                | False | RegulatoryReport                   |
| StructuredRegulatoryReporting3    | Code                            |                                | False | RegulatoryReport                   |
| StructuredRegulatoryReporting3    | Country                         |                                | False | Country                            |
| StructuredRegulatoryReporting3    | Date                            |                                | False | RegulatoryReport                   |
| StructuredRegulatoryReporting3    | Information                     |                                | False | RegulatoryReport                   |
| StructuredRegulatoryReporting3    | Type                            |                                | False | RegulatoryReport                   |
| StructuredRemittanceInformation18 |                                 |                                | False | Document                           |
| StructuredRemittanceInformation18 | AdditionalRemittanceInformation |                                | False |                                    |
|                                   |                                 |                                |       |                                    |

| StructuredRemittanceInformation18 | CreditorReferenceInformation | PaymentIdentification          | False | PaymentIdentification |
|-----------------------------------|------------------------------|--------------------------------|-------|-----------------------|
| StructuredRemittanceInformation18 | GarnishmentRemittance        | Garnishment                    | False |                       |
| StructuredRemittanceInformation18 | Invoicee                     | PartyIdentificationInformation | False |                       |
| StructuredRemittanceInformation18 | Invoicer                     | PartyIdentificationInformation | False | Party                 |
| StructuredRemittanceInformation18 | ReferredDocumentAmount       | Document                       | False | Document              |
| StructuredRemittanceInformation18 | ReferredDocumentInformation  | Document                       | False |                       |
| StructuredRemittanceInformation18 | TaxRemittance                | Tax                            | False | Payment               |
| SupplementaryData1                |                              |                                | True  |                       |
| SupplementaryData1                | Envelope                     |                                | True  |                       |
| SupplementaryData1                | PlaceAndName                 |                                | True  |                       |
| TaxAmount3                        |                              |                                | False | Tax                   |
| TaxAmount3                        | Details                      | Tax                            | True  |                       |
| TaxAmount3                        | Rate                         |                                | False | Tax                   |
| TaxAmount3                        | TaxableBaseAmount            |                                | False | Tax                   |
| TaxAmount3                        | TotalAmount                  |                                | False | Tax                   |
| TaxAuthorisation1                 |                              |                                | False | TaxPartyRole          |
| TaxAuthorisation1                 | Name                         |                                | False | PartyName             |

| TaxAuthorisation1 | Title                      |              | False | Person                         |
|-------------------|----------------------------|--------------|-------|--------------------------------|
| TaxData1          |                            |              | False | Tax                            |
| TaxData1          | AdministrationZone         |              | False | Tax                            |
| TaxData1          | Creditor                   | TaxPartyRole | False |                                |
| TaxData1          | Date                       |              | False | Tax                            |
| TaxData1          | Debtor                     | TaxPartyRole | False |                                |
| TaxData1          | Method                     |              | False | Tax                            |
| TaxData1          | Record                     | TaxRecord    | False | Tax                            |
| TaxData1          | ReferenceNumber            |              | False | Tax                            |
| TaxData1          | SequenceNumber             |              | True  |                                |
| TaxData1          | TotalTaxableBaseAmount     |              | False | Tax                            |
| TaxData1          | TotalTaxAmount             |              | False | Tax                            |
| TaxData1          | UltimateDebtor             | TaxPartyRole | False | Party                          |
| TaxParty1         |                            |              | False | TaxPartyRole                   |
| TaxParty1         | RegistrationIdentification |              | False | PartyIdentificationInformation |
| TaxParty1         | TaxIdentification          |              | False | PartyIdentificationInformation |
| TaxParty1         | TaxType                    |              | False |                                |
| TaxParty2         |                            |              | False | TaxPartyRole                   |

| TaxParty2         | Authorisation              | TaxPartyRole | False |                                |
|-------------------|----------------------------|--------------|-------|--------------------------------|
| TaxParty2         | RegistrationIdentification |              | False | PartyIdentificationInformation |
| TaxParty2         | TaxIdentification          |              | False | PartyIdentificationInformation |
| TaxParty2         | TaxType                    |              | False |                                |
| TaxPeriod3        |                            |              | False | TaxPeriod                      |
| TaxPeriod3        | FromToDate                 |              | False | TaxPeriod                      |
| TaxPeriod3        | Type                       |              | False | TaxPeriod                      |
| TaxPeriod3        | Year                       |              | False | TaxPeriod                      |
| TaxRecord3        |                            |              | False | TaxRecord                      |
| TaxRecord3        | AdditionalInformation      |              | True  |                                |
| TaxRecord3        | Category                   |              | False | TaxRecord                      |
| TaxRecord3        | CategoryDetails            |              | True  |                                |
| TaxRecord3        | CertificateIdentification  |              | False | Tax                            |
| TaxRecord3        | DebtorStatus               |              | False | TaxRecord                      |
| TaxRecord3        | FormsCode                  |              | False | TaxRecord                      |
| TaxRecord3        | Period                     | TaxPeriod    | False | TaxRecord                      |
| TaxRecord3        | TaxAmount                  | Tax          | False | TaxRecord                      |
| TaxRecord3        | Type                       |              | False | TaxRecord                      |
| TaxRecordDetails3 |                            |              | False | Tax                            |
|                   |                            |              |       |                                |

| TaxRecordDetails3 | Amount           |                  | False | Tax              |
|-------------------|------------------|------------------|-------|------------------|
| TaxRecordDetails3 | Period           | TaxPeriod        | True  |                  |
| TrackerData7      |                  |                  | False | PaymentTracker   |
| TrackerData7      | ConfirmedAmount  |                  | False | PaymentTracker   |
| TrackerData7      | ConfirmedDate    |                  | False | CurrencyExchange |
| TrackerData7      | TrackerRecord    | PaymentTracker   | False |                  |
| TrackerRecord5    |                  |                  | False | PaymentTracker   |
| TrackerRecord5    | Agent            | Organisation     | False | PaymentTracker   |
| TrackerRecord5    | ChargeBearer     |                  | False | PaymentTracker   |
| TrackerRecord5    | ChargesAmount    |                  | False | PaymentTracker   |
| TrackerRecord5    | ExchangeRateData | CurrencyExchange | False | PaymentTracker   |
|                   |                  |                  |       |                  |
|                   |                  |                  |       |                  |
|                   |                  |                  |       |                  |
|                   |                  |                  |       |                  |
|                   |                  |                  |       |                  |
|                   |                  |                  |       |                  |
|                   |                  |                  |       |                  |
|                   |                  |                  |       |                  |
|                   |                  |                  |       |                  |
|                   |                  |                  |       |                  |
|                   |                  |                  |       |                  |
|                   |                  |                  |       |                  |
|                   |                  |                  |       |                  |
|                   |                  |                  |       |                  |

## **PaymentsInitiation**