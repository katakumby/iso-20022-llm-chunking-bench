## Introduction
| Unnamed: 0 | Unnamed: 1 | Unnamed: 2 | Unnamed: 3 | Unnamed: 4 | Unnamed: 5 | Unnamed: 6 | Unnamed: 7 | Unnamed: 8 | Introduction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| This document describes the Business Model Components and Elements used by the Payments Initiation message definitions. | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| In the “Business Model” tab, the cells with text in green indicate the business concepts used by the Payments Initiation message set | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| The “Traces” tab shows to which business concepts the Payments Initiation message components and message elements trace. | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Notes: | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Specialisation | Some components inherit from a parent. In this illustration, the AccountContract is a specialisation (a child) of Contract and inherits from all its elements. | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | CashAccountContract inherits AccountContract and indirectly from Contract. | NaN | NaN | NaN | NaN | NaN | NaN | NaN |

## FullBusinessModel
| Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- |
| Asset | NaN | NaN | Tangible items of value to a business. | NaN | NaN |
| Asset | ExpiryDate | NaN | Date on which an order, a privilege, an entitlement or an offer terminates. For an interest bearing asset, it is the date/time at which it becomes due and has to be repaid. | ISODateTime | NaN |
| Asset | MaturityDate | NaN | Planned date, at the time of issuance, on which an interest bearing financial instrument becomes due and principal is repaid by the issuer to the investor. | ISODateTime | NaN |
| Asset | Derivative | NaN | Specifies the parameters of a derivative instrument based on a specific asset. | Derivative | UnderlyingAsset |
| Asset | AssetValue | NaN | Specifies the different values of an asset. | AssetHolding | Asset |
| Asset | AssetClassification | NaN | Classification of the asset. | AssetClassification | Asset |
| Asset | FinancialAssetCategory | NaN | Categorization of financial asset type. | FinancialAssetTypeCategoryCode | NaN |
| Asset | AssetPartyRole | NaN | Party which plays a role for a specific asset. | AssetPartyRole | Asset |
| Asset | Issuance | NaN | Details regarding the issuance of an asset. | Issuance | IssuedAsset |
| Asset | Portfolio | NaN | Asset which is part of a portfolio. | Portfolio | AssetDescription |
| Asset | InvestmentAmount | NaN | Invested amount of the portfolio asset. | CurrencyAndAmount | NaN |
| Asset | InvestmentRate | NaN | Invested percentage of the portfolio asset. | PercentageRate | NaN |
| Asset | EffectiveDate | NaN | Cut off date/time for the information of the specified portfolio asset. | ISODateTime | NaN |
| Asset | FinancialInstrumentSubStructure | NaN | Indicates the type of deal for structured finance. | InstrumentSubStructureTypeCode | NaN |
| Asset | InvestmentPlan | NaN | Investment plan that invests in a specific asset. | InvestmentPlan | Asset |
| Asset | Trade | NaN | Trade which which involves a specific asset. | Trade | Asset |
| Asset | Tranche | NaN | One of a number of related assets offered as part of the same transaction. | Tranche | Asset |
| Asset | LegAdditionalInformation | NaN | Provides details about the leg. | Leg | RelatedAsset |
| Asset | StandingSettlementInstruction | NaN | Standing settlement instruction for which an asset is specified. | StandingSettlementInstruction | Asset |
| Asset | GenericAssetIdentification | NaN | Identifies the asset. | NaN | NaN |
| Security | NaN | Asset | Financial instruments representing a sum of rights of the investor vis-a-vis the issuer. | NaN | NaN |
| Security | Identification | NaN | Way(s) of identifying the security. | SecuritiesIdentification | IdentifiedSecurity |
| Security | RegisteredDistributionCountry | NaN | Country in which the processing characteristic applies. | CountryCode | NaN |
| Security | DenominationCurrency | NaN | Currency in which a security is issued or redenominated. | CurrencyCode | NaN |
| Security | RegistrationForm | NaN | Specifies the form, ie, ownership, of the security. | FormOfSecurityCode | NaN |
| Security | DematerialisedIndicator | NaN | Indicates whether a security exists only as an electronic record, ie, there is no physical document representing the security. | YesNoIndicator | NaN |
| Security | EUSavingsDirective | NaN | Indicates whether the investment fund class is subject to the European Union Saving Directive. | EUSavingsDirectiveCode | NaN |
| Security | SecuritiesQuantity | NaN | Specifies the quantity associated with a security. | SecuritiesQuantity | SecurityIdentification |
| Security | Fees | NaN | Fees related to securities. | SecuritiesRelatedFees | Security |
| Security | Pricing | NaN | Information on the price of the security. | SecuritiesPricing | Security |
| Security | SecuritiesAccount | NaN | Account on which the security is held. | SecuritiesAccount | Security |
| Security | TradingMarket | NaN | Market(s) on which the security is traded. | TradingMarket | TradedSecurity |
| Security | PlaceOfListing | NaN | Market(s) on which the security is listed. | TradingMarket | ListedSecurity |
| Security | Registration | NaN | Information related to registration of securities. | BasicSecuritiesRegistration | Security |
| Security | Restriction | NaN | Regulatory restriction(s) linked to the security. | SecuritiesRestriction | Security |
| Security | CorporateEvent | NaN | Corporate event linked to the security | CorporateActionEvent | UnderlyingSecurity |
| Security | TemporaryFinancialInstrumentIndicator | NaN | Specifies that the security is a temporary security. | YesNoIndicator | NaN |
| Security | AvailableDate | NaN | Date on which securities become available for sale. | ISODateTime | NaN |
| Security | DeclarationDetails | NaN | Provides declaration details narrative relative to the financial instrument, eg, beneficial ownership. | Max350Text | NaN |
| Security | Spread | NaN | Spread that uses the security as benchmark reference. | Spread | BenchmarkSecurity |
| Security | Dividend | NaN | Dividend per financial instrument. | Dividend | Security |
| Security | Balance | NaN | Balance of the account which holds a specific security. | SecuritiesBalance | Security |
| Security | FungibleIndicator | NaN | Indicates whether a security is interchangeable, ie, the security is allowed to be replaced by another security, without loss of value. | YesNoIndicator | NaN |
| Security | Appearance | NaN | Specifies the deliverability of a security. | AppearanceCode | NaN |
| Security | NearTermPositionLimit | NaN | Position limit in the near-term contract for a given exchange-traded product. | Number | NaN |
| Security | ContractSettlementMonth | NaN | Specifies when the contract (i.e. MBS/TBA) will settle. | ISOYearMonth | NaN |
| Security | MinimumTradingPricingIncrement | NaN | Minimum price increase for a given exchange-traded Instrument | Number | NaN |
| Security | Rating | NaN | Rating(s) of the security. | Rating | Security |
| Security | CouponAttached | NaN | Coupon information of the security. | CouponAttached | Security |
| Security | Sector | NaN | Indicates the market sector the security is classified as pharmaceuticals, automobile, housing, etc. | Sector | Security |
| Security | WarrantAttachedOnDelivery | NaN | Indicates whether the warrants on a financial instrument (which has been traded cum warrants) will be attached on delivery. | YesNoIndicator | NaN |
| Security | StrippableIndicator | NaN | Indicates whether the interest is separable from the principal. | YesNoIndicator | NaN |
| Security | FirstDealingDate | NaN | Date on which new securities begin trading. | ISODateTime | NaN |
| Security | TaxDetails | NaN | Tax details of the security. | SecuritiesTax | Security |
| Security | SecuritiesTrade | NaN | Trade in which the security is involved. | SecuritiesTrade | Security |
| Security | RegistrationJurisdiction | NaN | Jurisdiction (country, county, state, province, city) in which the security is legally recorded for regulatory and/or tax purposes. | Jurisdiction | RegisteredSecurities |
| Security | PartyRole | NaN | Specifies roles played by a party that are linked to the handling of securities but not related to a specific process. | SecuritiesPartyRole | Security |
| Security | SecurityStatus | NaN | Specifies the status of the security within its lifecycle. | SecuritiesStatus | Security |
| Security | Modification | NaN | Modification process which applies to a specific security. | SecuritiesModification | NewSecurityReferenceData |
| Security | RedemptionSchedule | NaN | RedemptionSchedule(s) linked to the security. | RedemptionSchedule | Security |
| Security | SecuritiesSettlement | NaN | Settlement of a specific security. | SecuritiesSettlement | Security |
| Security | SecuritiesTransfer | NaN | Transfer process in which that security is transferred.. | SecuritiesTransfer | Security |
| Security | CorporateActionStandingInstructions | NaN | Standing instructions related to the security in the context of corporate action. | AgentCorporateActionStandingInstruction | Security |
| Security | Quote | NaN | Quote of a security. | Quote | QuotedSecurity |
| Security | SecuritiesOrder | NaN | Order for which a specific security is indicated. | SecuritiesOrder | OrderedSecurity |
| Security | RelatedVariableInterest | NaN | Variable interest parameters specified for interest related to a financial instrument. | VariableInterest | BenchmarkReference |
| Security | Conversion | NaN | Information on the conversion exchange of an entitlement or of preferred equities or of convertible bonds, into another form of securities, usually common equities. | SecuritiesConversion | SecurityIdentification |
| Security | ComponentSecurity | NaN | The security is part of the component security. | ComponentSecurity | Security |
| Security | RecompositionIndicator | NaN | Indicates whether the interest and the principal can be recomposed. This is the reverse operation of stripping. | YesNoIndicator | NaN |
| Security | Series | NaN | Identifier that links multiple security classes. | Max35Text | NaN |
| Security | PercentageOfDebtClaim | NaN | Percentage of the underlying assets of a fund that represents a debt and is in the scope of the EU Savings directive. | PercentageRate | NaN |
| Security | CoverRate | NaN | Amount of dividends the issuer intends to pay out the following year based on their normalised earnings. | PercentageRate | NaN |
| Security | MaturityRedemption | NaN | Return of an investor's principal in a security at maturity. | MaturityRedemptionTypeCode | NaN |
| Security | RelatedMarginCall | NaN | Margin call for which the associated securities are specified. | MarginCall | Security |
| Security | CloseLink | NaN | Situation in which two entities are linked because one of these entities owns some of the capital of the other one, or has a control relationship with it. | Party | CloseLinkSecurity |
| Security | PotentialEuroSystemEligibility | NaN | Indicates that the security is intended to be held in a manner that could allow the Eurosystem eligibility. | YesNoIndicator | NaN |
| Security | MinimumQuantity | NaN | Indicates the minimum tradable quantity of a security. | SecuritiesQuantity | MinimumQuantityDebt |
| Security | RestrictedIndicator | NaN | Identifies if the securities is restricted or not (as per Rule 144 of the Securities and Exchange Commission,that sets the conditions under which restricted, unregistered and control securities can be sold). | YesNoIndicator | NaN |
| InvestmentFundClass | NaN | Security | Security that is a sub-set of an investment fund, and is governed by the same investment fund policy, for example, a dividend option or valuation currency. | NaN | NaN |
| InvestmentFundClass | ClassType | NaN | Features of units offered by a fund. For example, a unit may have a specific load structure, eg, front end or back end, an income policy, eg, pay out or accumulate, or a trailer policy, eg, with or without. Fund classes are typically denoted by a single character, eg, 'Class A', 'Class 2'. | Max35Text | NaN |
| InvestmentFundClass | DistributionPolicy | NaN | Income policy relating to a class type, ie, if income is paid out or retained in the fund. | DistributionPolicyCode | NaN |
| InvestmentFundClass | DividendPolicy | NaN | Dividend policy of the fund, eg, cash, units. | DividendPolicyCode | NaN |
| InvestmentFundClass | DualFundIndicator | NaN | Indicates whether the fund has two prices. | YesNoIndicator | NaN |
| InvestmentFundClass | RequestedNAVCurrency | NaN | Currency to be used for pricing the fund. This currency must be among the set of currencies in which the price may be expressed, as stated in the prospectus. | CurrencyCode | NaN |
| InvestmentFundClass | TradingCurrency | NaN | Currency of the investment fund class. | CurrencyCode | NaN |
| InvestmentFundClass | InvestmentFund | NaN | Investment fund which is related to the investment fund class. | InvestmentFund | InvestmentFundClass |
| InvestmentFundClass | PhysicalBearerSecurities | NaN | Indicates whether or not it is possible to hold bearer units/shares in this class in certified form | YesNoIndicator | NaN |
| InvestmentFundClass | DematerialisedBearerSecurities | NaN | Indicate whether or not it is possible to hold bearer units/shares in paperless form | YesNoIndicator | NaN |
| InvestmentFundClass | PhysicalRegisteredSecurities | NaN | Indicate whether or not it is possible to hold registered units/shares in this class in paperless form | YesNoIndicator | NaN |
| InvestmentFundClass | DematerialisedRegisteredSecurities | NaN | Indicate whether or not it is possible to hold registered units/shares in this class in paperless form | YesNoIndicator | NaN |
| InvestmentFundClass | ProcessingCharacteristics | NaN | Processing characteristics linked to the investment fund class, ie, not to the market. | InvestmentFundClassProcessingCharacteristics | FundClass |
| InvestmentFundClass | ProductGroup | NaN | Company specific description of a group of funds. | Max140Text | NaN |
| InvestmentFundClass | InvestmentAccount | NaN | Account which holds investment fund classes. | InvestmentAccount | InvestmentFundClass |
| InvestmentFundClass | NetAssetValueCalculation | NaN | Calculation of the value of the fund. | NetAssetValueCalculation | RelatedFund |
| InvestmentFundClass | InvestmentFundTransaction | NaN | Transaction which is related to the fund class. | InvestmentFundTransaction | InvestmentFundClass |
| InvestmentFundClass | SeriesIssueIdentificationDate | NaN | Date that identifies the issue of a fund series. Typically applicable to a redemption or order confirmation, but may be specified in the subscription, if known. | ISODate | NaN |
| InvestmentFundClass | SeriesName | NaN | Identifies the name of a fund series. Typically applicable to a redemption or order confirmation, but may be specified in the subscription, if known. | Max35Text | NaN |
| InvestmentFundClass | NewIssueIndicator | NaN | Indicates that the financial instrument and/or series included in the message is a new issue. | YesNoIndicator | NaN |
| InvestmentFundClass | Equalisation | NaN | Part of an investor's subscription amount that is held by the fund in order to pay incentive / performance fees at the end of the fiscal year. | Equalisation | RelatedInvestmentFundTransaction |
| InvestmentFundClass | TopUpAmount | NaN | Additional amount of money (top-up amount) required to meet the minimum subscription amount. | CurrencyAndAmount | NaN |
| InvestmentFundClass | HoldBackAmount | NaN | Value of the redemption amount subject to hold back. | CurrencyAndAmount | NaN |
| InvestmentFundClass | HoldBackReleaseDate | NaN | Date on which the hold back amount is to be released. | ISODate | NaN |
| InvestmentFundClass | LotDescription | NaN | Description of the lot. | Max350Text | NaN |
| InvestmentFundClass | FundClassification | NaN | Method of classifying a fund. | GenericIdentification | IdentificationForInvestmentFundClass |
| InvestmentFundClass | UnderlyingAssetType | NaN | Specifies the type of assets in which the fund invests. | FinancialInstrumentProductTypeCode | NaN |
| InvestmentFundClass | InvestorType | NaN | Type of investor that can invest in the fund class. | InvestorTypeCode | NaN |
| InvestmentFundClass | Reinvestment | NaN | Reinvestment information which involves this investment fund class. | Reinvestment | InvestmentFundClass |
| InvestmentFundClass | OutstandingUnits | NaN | Investment fund class currently held by shareholders. | DecimalNumber | NaN |
| InvestmentFundClass | FundEndDate | NaN | Date on which the fund is closed to investment. | ISODate | NaN |
| SecuritiesIdentification | NaN | NaN | Unique and unambiguous identifier of a security, assigned under a formal or proprietary identification scheme. | NaN | NaN |
| SecuritiesIdentification | IdentifiedSecurity | NaN | Security for which an identification is provided. | Security | Identification |
| SecuritiesIdentification | SecurityIdentification | NaN | Identification of a security by an ISIN. | ISINOct2015Identifier | NaN |
| SecuritiesIdentification | RIC | NaN | Reuters Identification Code (RIC). A numbering system used within the Reuters system to identify instruments worldwide. The RIC contains an X-character market specific code (can be the CUSIP or EPIC codes) followed by a full stop, then the two-digit ISO country code, eg, IBM in UK is IBM.UK. | RICIdentifier | NaN |
| SecuritiesIdentification | TickerSymbol | NaN | Letters that identify a stock traded on a stock exchange. The Ticker Symbol is a short and convenient way of identifying a stock, eg, RTR.L for Reuters quoted in London. | TickerIdentifier | NaN |
| SecuritiesIdentification | Bloomberg | NaN | Identifier of a security assigned by the Bloomberg organisation. | Bloomberg2Identifier | NaN |
| SecuritiesIdentification | CTA | NaN | Identifier of a security assigned by the Consolidated Tape Association. | ConsolidatedTapeAssociationIdentifier | NaN |
| SecuritiesIdentification | Common | NaN | Identifier of securities issued in Luxembourg. The common code is a 9-digit code that replaces the CEDEL (Clearstream) and Euroclear codes. | EuroclearClearstreamIdentifier | NaN |
| SecuritiesIdentification | Name | NaN | Name of the financial instrument in free format text. | LocalName | RelatedSecurity |
| SecuritiesIdentification | SEDOL | NaN | Stock Exchange Daily Official List (SEDOL) number. A code used by the London Stock Exchange to identify foreign stocks, especially those that aren't actively traded in the US and don't have a CUSIP number. | SEDOLIdentifier | NaN |
| SecuritiesIdentification | CUSIP | NaN | Committee on Uniform Securities and Identification Procedures (CUSIP). The standards body that created and maintains the securities classification system in the US. The CUSIP is composed of a 9-character number that uniquely identifies a particular security. Non-US securities have a similar number called the CINS number. | CUSIPIdentifier | NaN |
| SecuritiesIdentification | QUICK | NaN | Identifier of a security assigned by the Japanese QUICK identification scheme for financial instruments. | QUICKIdentifier | NaN |
| SecuritiesIdentification | Wertpapier | NaN | Wertpapier Kenn-nummer. A number issued in Germany by the Wertpapier Mitteilungen. The Wertpapier Kenn-nummer, sometimes called WPK, contains 6-digits, but no check digit. There are different ranges of numbers representing different classes of securities. | WertpapierIdentifier | NaN |
| SecuritiesIdentification | Dutch | NaN | Identifier for Dutch securities. | DutchIdentifier | NaN |
| SecuritiesIdentification | Valoren | NaN | Identifier for Swiss securities assigned by Telekurs Financial, the Swiss numbering agency. | ValorenIdentifier | NaN |
| SecuritiesIdentification | Sicovam | NaN | Identifier for French securities assigned by the Societe Interprofessionnelle Pour La Compensation des Valeurs Mobilieres in France. The Sicovam is composed of 5-digits. | SicovamIdentifier | NaN |
| SecuritiesIdentification | Belgian | NaN | Identifier for Belgian securities. | BelgianIdentifier | NaN |
| SecuritiesIdentification | IdentificationSuffix | NaN | Identifies the suffix of the security identification. | Max35Text | NaN |
| SecuritiesIdentification | GenericIdentification | NaN | Proprietary identification of a security assigned by an institution or organisation. | GenericIdentification | RelatedSecuritiesIdentification |
| SecuritiesIdentification | ValidityPeriod | NaN | Specifies the period during which an identification is valid. | DateTimePeriod | RelatedSecuritiesIdentification |
| SecuritiesIdentification | ApplicableTradingMarket | NaN | Market(s) on which the trading identification is used. | TradingMarket | ListedSecurityTradingIdentification |
| SecuritiesIdentification | PrimeIdentification | NaN | Specifies the main identification of a security. | SecuritiesIdentification | RelatedOtherIdentification |
| SecuritiesIdentification | RelatedOtherIdentification | NaN | Alternate security identification(s) related to the security trading identification. | SecuritiesIdentification | PrimeIdentification |
| SecuritiesIdentification | TradingIdentification | NaN | Security identifier specific to a trading market or markets, for example, Ticker. | Max70Text | NaN |
| Role | NaN | NaN | Role of a party in an activity. | NaN | NaN |
| Role | Player | NaN | Entity which plays a role in the context of the business domain in which the role is defined. | RolePlayer | Role |
| Role | ContactPersonRole | NaN | Contact person in the context of a role played by an organisation. | ContactPersonRole | Role |
| Role | PartyRole | NaN | Specifies the role of the party in the transaction. | PartyRoleCode | NaN |
| Role | CounterpartyRisk | NaN | Specifies the risk which is related to the role played by a party. | CounterpartyRisk | Party |
| Role | Entry | NaN | Entry for which a role is specified. | Entry | Role |
| InformationPartyRole | NaN | Role | Role played by a party as source of information. | NaN | NaN |
| InformationPartyRole | GenericIdentification | NaN | Specifies the identification for which a party plays the issuer role. | GenericIdentification | PartyRole |
| InformationPartyRole | HaircutValuation | NaN | Specifies the haircut valuation for which a party provides the information. | HaircutValuation | PartyRole |
| InformationPartyRole | Price | NaN | Specifies the security price for which a party plays a role. | SecuritiesPricing | InformationPartyRole |
| InformationPartyRole | Scheme | NaN | Scheme for which the party is the source. | Scheme | InformationPartyRole |
| InformationPartyRole | Quote | NaN | Quoting process in which an information party plays a role. | Quote | PartyRole |
| InformationPartyRole | TreasuryTrade | NaN | Trade for which a quote is provided. | TreasuryTrade | InformationPartyRole |
| IdentificationIssuerRole | NaN | InformationPartyRole | Entity that assigns the identification. | NaN | NaN |
| IdentificationIssuerRole | Country | NaN | Country of the proprietary identification scheme. | CountryCode | NaN |
| IdentificationIssuerRole | EntityName | NaN | Entity that issues the proprietary identification. | Max35Text | NaN |
| IdentificationIssuerRole | OwnerCode | NaN | Code representing the organisation that owns and is responsible of an enumerated code list, for example ISO. | Max35Text | NaN |
| GenericIdentification | NaN | NaN | Information related to a non-standardised identification, such as a proprietary party identification or account identification. | NaN | NaN |
| GenericIdentification | Identification | NaN | Name or number assigned by an entity to enable recognition of that entity, for example account identifier, identification assigned by a provider to identify its customers. | Max35Text | NaN |
| GenericIdentification | IdentificationForContactPoint | NaN | Contact point which uses a generic identification as identification. | ContactPoint | Identification |
| GenericIdentification | IdentificationForAccount | NaN | Account Identification which uses a generic identification as proprietary identification. | AccountIdentification | ProprietaryIdentification |
| GenericIdentification | RelatedPartyIdentification | NaN | Party identified with a scheme. | PartyIdentificationInformation | OtherIdentification |
| GenericIdentification | IssueDate | NaN | Date at which the identification was issued. | ISODate | NaN |
| GenericIdentification | ExpiryDate | NaN | Date at which the identification expires. | ISODate | NaN |
| GenericIdentification | Scheme | NaN | Information regarding an enumerated code list and its owner. | Scheme | Identification |
| GenericIdentification | IdentificationForSecuritiesCertificate | NaN | Securities certificate which uses a generic identification as certificate number. | SecuritiesCertificate | Number |
| GenericIdentification | IdentificationForLot | NaN | Lot breakdown which uses a generic identification as lot number. | LotBreakdown | LotNumber |
| GenericIdentification | PartyRole | NaN | Entity that assigns the identification. | InformationPartyRole | GenericIdentification |
| GenericIdentification | IdentificationForCashProceedsIncome | NaN | Cash proceeds definition which uses a generic identification as type of income. | CashProceedsDefinition | IncomeType |
| GenericIdentification | RelatedStatusReason | NaN | Specifies the status reason for which a data source scheme is specified. | StatusReason | DataSourceScheme |
| GenericIdentification | IdentificationForBankTransaction | NaN | Bank transaction which uses a generic identification as proprietary identification. | BankTransaction | ProprietaryIdentification |
| GenericIdentification | IdentificationForAccountCostReferencePattern | NaN | Account identification for which a cost reference pattern is provided. | AccountIdentification | CostReferencePattern |
| GenericIdentification | Account | NaN | Account for which a type is specified | Account | Type |
| GenericIdentification | RelatedSystemIdentification | NaN | System identification which uses a generic identification. | SystemIdentification | Identification |
| GenericIdentification | IdentificationForInterestName | NaN | Interest which uses a generic identification as name. | Interest | InterestName |
| GenericIdentification | RelatedCashAccountService | NaN | Cash account service identified in a generic way. | CashAccountService | Identification |
| GenericIdentification | IdentificationForInvestmentFundClass | NaN | Investment fund class which uses a generic identification as fund classification. | InvestmentFundClass | FundClassification |
| GenericIdentification | IdentifiedLocation | NaN | Location for which an identification is provided. | Location | Identification |
| GenericIdentification | RelatedSecuritiesIdentification | NaN | Securities identification for which generic identification elements and scheme are provided. | SecuritiesIdentification | GenericIdentification |
| GenericIdentification | IdentifiedDocument | NaN | Document for which an identification is provided. | Document | DocumentIdentification |
| GenericIdentification | RelatedPurchaseOrder | NaN | Purchase order for which an identification is provided. | PurchaseOrder | Identification |
| GenericIdentification | RelatedCertificate | NaN | Related certificate against which all transactions in the scope of the regulatory requirements are registered. | RegisteredContract | Certificate |
| LocalName | NaN | NaN | Name of the security. | NaN | NaN |
| LocalName | FullName | NaN | Name of the security. | Max350Text | NaN |
| LocalName | RelatedSecurity | NaN | Identification which contains a name. | SecuritiesIdentification | Name |
| LocalName | ShortName | NaN | Short name of the security | Max35Text | NaN |
| LocalName | Language | NaN | Language in which the security name is expressed. | LanguageCode | NaN |
| UmbrellaFund | NaN | NaN | In securities, a collective investment scheme that has a contractual or a corporate form. When it has a contractual form, a fund is constituted under either the law of contract or under the trust law and thus it is not a legal entity. In its corporate form, a fund is a legal entity and is structured as a company. It has several distinct sub-funds which in effect are traded as individual investment funds. | NaN | NaN |
| UmbrellaFund | Name | NaN | Name of the fund. | Max350Text | NaN |
| UmbrellaFund | SubFund | NaN | Compartment of an umbrellla fund. | InvestmentFund | UmbrellaFund |
| InvestmentFund | NaN | FinancialProduct | Distinct pool of financial instruments managed by a single investment policy. May or not be part of an umbrella fund. The pool is issued in at least one investment fund class. | NaN | NaN |
| InvestmentFund | DomicileCountry | NaN | Country in which the investment fund is domiciled. | Country | DomiciledFunds |
| InvestmentFund | OrderDesk | NaN | Entity appointed by the fund, to which orders should be submitted. | ContactPoint | RelatedInvestmentFund |
| InvestmentFund | InvestmentFundClass | NaN | Sub-set of an investment fund. | InvestmentFundClass | InvestmentFund |
| InvestmentFund | FundType | NaN | Legal form of the fund, eg, UCITS, SICAV, OEIC, Unit Trust, and FCP. | Max35Text | NaN |
| InvestmentFund | TreasuryTradingParty | NaN | Party which executes a treasury trade on behalf of an investment fund. | TreasuryTradingParty | InvestmentFund |
| InvestmentFund | Identification | NaN | Identification of the investment fund. | AnyBICDec2014Identifier | NaN |
| InvestmentFund | Custodian | NaN | Party which settles the trades for the account of the fund. | CustodianRole | InvestmentFund |
| InvestmentFund | PartyRole | NaN | Specifies each role linked to an investment fund and played by a party in that context. | InvestmentFundPartyRole | InvestmentFund |
| InvestmentFund | Family | NaN | Family to which the investment fund belongs. | InvestmentFundFamily | InvestmentFund |
| InvestmentFund | Structure | NaN | Structure of the subfund, eg, single fund, multi-class. | FundStructureCode | NaN |
| InvestmentFund | LegalForm | NaN | Legal form of a fund, eg, corporation or trust. | FundLegalFormCode | NaN |
| InvestmentFund | SubFundIndicator | NaN | Indicates whether the investment fund is a subfund, when it is a compartment of an umbrella fund. In this case, subfund is a synonym of investment fund and therefore has the same attributes as investment fund. | YesNoIndicator | NaN |
| InvestmentFund | EndOfFiscalYear | NaN | Date at which the books are closed and profit and loss is determined. | ISODate | NaN |
| InvestmentFund | AccountingYearEndDate | NaN | Last day of the accounting year for the fund. | ISODate | NaN |
| InvestmentFund | FirstAccountingYearEndDate | NaN | Last day of the first accounting year for the fund. | ISODate | NaN |
| InvestmentFund | UmbrellaFund | NaN | Umbrella fund for which compartments are specified. | UmbrellaFund | SubFund |
| InvestmentFund | AuthorisedCountry | NaN | Country in which it is authorised to commercialise the fund. | CountryCode | NaN |
| Country | NaN | NaN | Nation with its own government. | NaN | NaN |
| Country | DomiciledFunds | NaN | Investment funds which are domiciled in a specific country. | InvestmentFund | DomicileCountry |
| Country | Code | NaN | Identifies a nation with its own government (ISO 3166). | CountryCode | NaN |
| Country | Citizen | NaN | Specifies a person which is a citizen of a country. | Person | Nationality |
| Country | Tax | NaN | Tax parameters applicable in a country. | Tax | Country |
| Country | CountryForSafekeepingPlace | NaN | Specifies the safekeeping places located in a specific country. | SafekeepingPlace | Country |
| Country | CountryForBeneficialOwner | NaN | Specifies the beneficial owner which has certified that it is not domiciled in the country. | BeneficialOwner | NonDomicileCountry |
| Country | ProducedProducts | NaN | Specifies the product for which an origin is specified. | Product | Origin |
| Country | NationalRegulatoryAuthority | NaN | Regulatory authority of the country. | RegulatoryAuthorityRole | Country |
| Country | RelatedCardPayment | NaN | Card payment which took place in the specified country. | CardPaymentAcquiring | Country |
| Country | Name | NaN | Name by which a country is known. It is normally the name attached to the ISO country code. | Max35Text | NaN |
| Country | PostalAddressSpecification | NaN | Specifies the representation of a postal address per country. | PostalAddress | Country |
| Country | CountryRelatedInvestmentFundProcessing | NaN | Specifies the other parameters of the investment fund class which apply in that country. | InvestmentFundClassProcessingCharacteristics | Country |
| Country | Market | NaN | Market for which a country is specified. | Market | Country |
| Country | RelatedPaymentCard | NaN | Payment card for which a country code is attached. | PaymentCard | CardCountryCode |
| Country | SubDivision | NaN | Unit resulting from the division of a country, dependency, or other area of special geopolitical interest contained in ISO 3166-1, on the basis of country names obtained from the United Nations (ISO 3166-2: Country subdivision code). | CountrySubDivision | Country |
| Dividend | NaN | NaN | Distribution of earnings to shareholders, paid for in cash, stock, scrip issue or, rarely, in kind, for example, in company products or property. The dividend amount is decided by the board of directors. | NaN | NaN |
| Dividend | DividendFrequency | NaN | Frequency with which the income is allocated to investors. | EventFrequencyCode | NaN |
| Dividend | AnnualTotalDividendRate | NaN | Provides the annual total dividend rate. | PercentageRate | NaN |
| Dividend | FinalDividend | NaN | Dividend is final. | RateAndAmount | FinalDividendParameters |
| Dividend | FullyFrankedRateAndAmount | NaN | Rate of a fully franked dividend paid by a company, or amount resulting from a fully franked dividend paid by a company; amount includes tax credit for companies that have made sufficient tax payments during the fiscal period. | RateAndAmount | FullyFrankedRateAndAmountDividendParameters |
| Dividend | GrossDividend | NaN | Cash dividend amount per equity before deductions or allowances have been made. | RateAndAmount | GrossDividendParameters |
| Dividend | RateType | NaN | Specifies the type of dividend rate. | DividendRateTypeCode | NaN |
| Dividend | NetDividend | NaN | Cash dividend amount per equity after deductions or allowances have been made. | RateAndAmount | NetDividendParameters |
| Dividend | ProvisionalDividend | NaN | Dividend is provisional. | RateAndAmount | ProvisionalDividendParameters |
| Dividend | DividendRankingDate | NaN | Date on which a security will be entitled to a dividend. | ISODateTime | NaN |
| Dividend | ManufacturedDividendAmount | NaN | Amount of money that the borrower pays to the lender as a compensation. It does not entitle the lender to reclaim any tax credit and is sometimes treated differently by the local tax authorities of the lender. | CurrencyAndAmount | NaN |
| Dividend | UnfrankedAmount | NaN | Amount resulting from an unfranked dividend paid by a company; the amount does not include tax credit and is subject to withholding tax. | CurrencyAndAmount | NaN |
| Dividend | NotionalDividendPayableAmount | NaN | Amount of cash that would have been payable if the dividend had been taken in the form of cash rather than shares. | CurrencyAndAmount | NaN |
| Dividend | Rate | NaN | Planned dividend rate, for example, for preferred shares. | PercentageRate | NaN |
| Dividend | ExDividendDate | NaN | Date/time as from which trading (including exchange and OTC trading) occurs on the underlying security without the benefit. | ISODateTime | NaN |
| Dividend | Security | NaN | Security for which a dividend is specified. | Security | Dividend |
| Dividend | Type | NaN | Nature of the dividend. | DividendTypeCode | NaN |
| Dividend | CashProceeds | NaN | Defines the proceeds which resulted in dividends. | CashProceedsDefinition | Dividend |
| Dividend | Obligation | NaN | Specifies the payment terms of the dividend. | PaymentObligation | Dividend |
| Dividend | Tax | NaN | Tax on dividend. | Tax | Dividend |
| Dividend | RelatedDistribution | NaN | Distribution for which a dividend is specified. | Distribution | Dividend |
| Dividend | DividendFrequenceType | NaN | Specifies the cycle of dividends. | CorporateActionFrequencyTypeCode | NaN |
| Dividend | DividendRatio | NaN | Percentage of earnings paid to shareholders in dividends. | PercentageRate | NaN |
| Dividend | PaymentDate | NaN | Date upon which the dividend is paid. | ISODate | NaN |
| Dividend | PaymentFrequency | NaN | Specifies the cycle of dividend payments. | FrequencyCode | NaN |
| Dividend | ReinvestmentDate | NaN | Date upon which the dividend is reinvested. | ISODate | NaN |
| Dividend | Value | NaN | Value of the dividend expressed as an amount. | CurrencyAndAmount | NaN |
| Dividend | DeemedAmount | NaN | Amount of proceeds which is not actually paid to the security holder but on which withholding tax is applicable. | RateAndAmount | DeemedAmountDividendParameters |
| Dividend | DeemedRate | NaN | Rate applied for the calculation of deemed proceeds which are not paid to security holders but on which withholding tax is applicable. | PercentageRate | NaN |
| Dividend | ConduitForeignIncomeAmount | NaN | Amount relating to a conduit foreign income. | RateAndAmount | ConduitForeignIncomeAmountDividendParameters |
| InvestmentFundClassProcessingCharacteristics | NaN | NaN | Processing characteristics linked to the instrument, ie, not to the market. | NaN | NaN |
| InvestmentFundClassProcessingCharacteristics | ReinvestmentFrequency | NaN | Frequency with which the reinvestment takes place, This is the same or less than the dividend frequency, | EventFrequencyCode | NaN |
| InvestmentFundClassProcessingCharacteristics | FrontEndLoadIndicator | NaN | Front end charge on subscription orders for this class can be applied. | YesNoIndicator | NaN |
| InvestmentFundClassProcessingCharacteristics | BackEndLoadIndicator | NaN | Exit charge (eg. CDSC) on redemption orders for this class can be applied. | YesNoIndicator | NaN |
| InvestmentFundClassProcessingCharacteristics | SwitchingFeeIndicator | NaN | If a separate fee for switching between sub-funds of the same umbrella can be applied. | YesNoIndicator | NaN |
| InvestmentFundClassProcessingCharacteristics | LimitedSubscriptionPeriod | NaN | Specific period, eg, for some guaranteed funds, during which the units/shares may be subscribed to. | Max350Text | NaN |
| InvestmentFundClassProcessingCharacteristics | LimitedRedemptionPeriod | NaN | Specific period, eg, for some guaranteed funds, during which the units/shares may be redeemed. | Max350Text | NaN |
| InvestmentFundClassProcessingCharacteristics | Decimalisation | NaN | Number of decimal places to which quantities of units/shares are rounded. | Number | NaN |
| InvestmentFundClassProcessingCharacteristics | HoldingTransferableIndicator | NaN | Indicates whether registered investors are able to transfer some or all of their holdings to third parties. | YesNoIndicator | NaN |
| InvestmentFundClassProcessingCharacteristics | ApplicationForm | NaN | Physical application form is required. | YesNoIndicator | NaN |
| InvestmentFundClassProcessingCharacteristics | SignatureRequired | NaN | Specifies which type of signature is required when completing an initial subscription, when completing a subsequent subscription, and when completing redemption. | SignatureTypeCode | NaN |
| InvestmentFundClassProcessingCharacteristics | AmountIndicator | NaN | Indicates whether subscriptions/redemption in amount are allowed. | YesNoIndicator | NaN |
| InvestmentFundClassProcessingCharacteristics | UnitsIndicator | NaN | Indicates whether subsciptions/redemption may be placed as a number of units. | YesNoIndicator | NaN |
| InvestmentFundClassProcessingCharacteristics | OrderCutOffDateTime | NaN | Last date/time at which an order to subscribe or an order to redeem can be given. | ISODateTime | NaN |
| InvestmentFundClassProcessingCharacteristics | SettlementCycle | NaN | An agreed number of days after the Trade date (T) used to define standard timeframes e.g T+3 settlement period Where T = the date the price is applied to a transaction. | TimeFrame | SubscriptionSettlementRelatedFundProcessing |
| InvestmentFundClassProcessingCharacteristics | FundClass | NaN | Investment fund class for which processing characteristics are specified. | InvestmentFundClass | ProcessingCharacteristics |
| InvestmentFundClassProcessingCharacteristics | HoldingTransferable | NaN | Indicates whether registered investors are able to transfer some or all of their holdings to third parties. | HoldingTransferableCode | NaN |
| InvestmentFundClassProcessingCharacteristics | DealingFrequency | NaN | Frequency at which the subscriptions and redemptions are done. | FrequencyCode | NaN |
| InvestmentFundClassProcessingCharacteristics | LimitedPeriod | NaN | Specific period, eg, for some guaranteed funds, during which the units/shares may be redeemed. | Max350Text | NaN |
| InvestmentFundClassProcessingCharacteristics | SettlementAccount | NaN | Account used for settlement of fund transactions. | Account | RelatedFundProcessingCharacteristics |
| InvestmentFundClassProcessingCharacteristics | Country | NaN | Country in which the processing characteristic applies. | Country | CountryRelatedInvestmentFundProcessing |
| InvestmentFundClassProcessingCharacteristics | LocalMarketAnnex | NaN | Context, or geographic environment, in which trading parties may meet in order to negotiate and execute trades among themselves. | ContactPoint | InvestmentFundClassProcessing |
| InvestmentFundClassProcessingCharacteristics | EffectiveDate | NaN | Date/time as from which the processing characteristics are valid. | ISODateTime | NaN |
| InvestmentFundClassProcessingCharacteristics | SubsequentSubscriptionApplicationForm | NaN | Physical application form for subsequent investments by the same investor. | YesNoIndicator | NaN |
| InvestmentFundClassProcessingCharacteristics | RedemptionForm | NaN | Physical written instruction/renunciation form for redemption of units/shares by the investor. | YesNoIndicator | NaN |
| InvestmentFundClassProcessingCharacteristics | DealingCurrency | NaN | Currency in which a subscription or redemption is accepted. | CurrencyCode | NaN |
| InvestmentFundClassProcessingCharacteristics | DealingCutOffTimeFrame | NaN | Specifies the number of days for cut off before or after an activity. | TimeFrame | RelatedProcessingCharacteristics |
| InvestmentFundClassProcessingCharacteristics | MinimumHoldingAmount | NaN | Minimum value of units that must be maintained to avoid automatic redemption. | ActiveCurrencyAndAmount | NaN |
| InvestmentFundClassProcessingCharacteristics | MaximumRedemptionUnits | NaN | Maximum number of shares/units that may be redeemed on a single dealing day. | DecimalNumber | NaN |
| InvestmentFundClassProcessingCharacteristics | MinimumHoldingUnits | NaN | Minimum number of units that must be maintained to avoid automatic redemption. | DecimalNumber | NaN |
| InvestmentFundClassProcessingCharacteristics | MinimumRemainingHoldingAmount | NaN | Minimum value of units/shares that must be retained to avoid automatic redemption. | CurrencyAndAmount | NaN |
| InvestmentFundClassProcessingCharacteristics | MaximumRedemptionPercentage | NaN | Maximum quantity of securities, expressed as a percentage that can be sold. | PercentageRate | NaN |
| InvestmentFundClassProcessingCharacteristics | MaximumRedemptionAmount | NaN | Maximum quantity of securities, expressed as an amount that can be sold. | CurrencyAndAmount | NaN |
| InvestmentFundClassProcessingCharacteristics | MinimumInitialSubscriptionUnits | NaN | Minimum initial number of units/shares that must be purchased. | DecimalNumber | NaN |
| InvestmentFundClassProcessingCharacteristics | MinimumSubscriptionAmount | NaN | Minimum quantity of securities, expressed as an amount that must be purchased. | CurrencyAndAmount | NaN |
| InvestmentFundClassProcessingCharacteristics | MinimumInitialSubscriptionAmount | NaN | Minimum initial quantity of securities, expressed as an amount that must be purchased at subscription. | CurrencyAndAmount | NaN |
| InvestmentFundClassProcessingCharacteristics | MinimumSubscriptionUnits | NaN | Minimum number of units/shares that must be purchase by existing investors. | DecimalNumber | NaN |
| InvestmentFundClassProcessingCharacteristics | MinimumHoldingPeriod | NaN | Description of a period, that may be a number of days, weeks or descriptive period during which the units/shares must be held following their issue before redemption will be permitted. | Max70Text | NaN |
| InvestmentFundClassProcessingCharacteristics | MinimumRedemptionPercentage | NaN | Minimum percentage of holding that may be redeemed. | DecimalNumber | NaN |
| NetAssetValueCalculation | NaN | NaN | Calculation of the net asset value for an investment fund/fund class. | NaN | NaN |
| NetAssetValueCalculation | ValuationFrequency | NaN | Frequency of the valuation. | EventFrequencyCode | NaN |
| NetAssetValueCalculation | ValuationDateTime | NaN | Date and time of the price valuation for the investment fund/fund class. | ISODateTime | NaN |
| NetAssetValueCalculation | NetAssetValue | NaN | Value of all the holdings, less the fund's liabilities, attributable to a specific investment fund class. | CurrencyAndAmount | NaN |
| NetAssetValueCalculation | RelatedFund | NaN | Specifies the fund for which the NAV is calculated (per fund unit). | InvestmentFundClass | NetAssetValueCalculation |
| NetAssetValueCalculation | ValuationType | NaN | Specifies how the valuation is done, based on the schedule stated in the prospectus. | ValuationTimingCode | NaN |
| NetAssetValueCalculation | SuspendedIndicator | NaN | Indicates whether the valuation of the investment fund class is suspended. | YesNoIndicator | NaN |
| NetAssetValueCalculation | ForExecutionIndicator | NaN | Indicates whether the price information can be used for the execution of a transaction. | YesNoIndicator | NaN |
| NetAssetValueCalculation | TaxLiability | NaN | Information related to taxes that are due. | Tax | TaxLiabilityValueCalculation |
| NetAssetValueCalculation | TaxRefund | NaN | Information related to taxes that are paid back. | Tax | TaxRefundValueCalculation |
| NetAssetValueCalculation | OfficialValuationIndicator | NaN | Indicates whether the valuation is an official valuation. | YesNoIndicator | NaN |
| NetAssetValueCalculation | EstimatedPriceIndicator | NaN | Indicates whether the price is an estimated price. | YesNoIndicator | NaN |
| NetAssetValueCalculation | ValuationStatistics | NaN | Information related to the price variations of an investment fund class. | ValuationStatistics | NetAssetValueCalculation |
| NetAssetValueCalculation | InvestmentFundPerformanceFactors | NaN | Factors that give indications about the performance of a fund. | PerformanceFactors | NetAssetValueCalculation |
| NetAssetValueCalculation | Price | NaN | Price derived from the net asset value. | SecuritiesPricing | NetAssetValueCalculation |
| NetAssetValueCalculation | SecuritiesQuantity | NaN | Quantity on which the NAV is calculated. | SecuritiesQuantity | NetAssetValueCalculation |
| NetAssetValueCalculation | Interest | NaN | Interest that has accumulated between the most recent payment of interest and the sale of the financial instrument. | Interest | RelatedNetAssetValueCalculation |
| NetAssetValueCalculation | FundsCashFlow | NaN | Net cash flow for a valuation date, which is incorporated in the NAV. | FundsCashFlow | NetAssetValueCalculation |
| NetAssetValueCalculation | DeclarationChannel | NaN | Means of the net asset value publication, for example, a newspaper. | Max35Text | NaN |
| NetAssetValueCalculation | DeclarationDate | NaN | Date/time of the net asset value publication. | ISODateTime | NaN |
| NetAssetValueCalculation | FirstValuationDate | NaN | Date on which the investment fund class was first priced. | ISODate | NaN |
| NetAssetValueCalculation | HistoricPricingIndicator | NaN | Indicates whether the price is historic or forward. | YesNoIndicator | NaN |
| SecuritiesPricing | NaN | NaN | Characteristics related to the price of the security. | NaN | NaN |
| SecuritiesPricing | PriceMethod | NaN | Type of pricing calculation method. | PriceMethodCode | NaN |
| SecuritiesPricing | PriceType | NaN | Type and information about a price. | TypeOfPriceCode | NaN |
| SecuritiesPricing | CumDividendIndicator | NaN | Indicates whether the dividend is included, ie, cum-dividend, in the executed price. When the dividend is not included, the price will be ex-dividend. | YesNoIndicator | NaN |
| SecuritiesPricing | CalculationBasis | NaN | Ratio applied on the non-adjusted price. | PercentageRate | NaN |
| SecuritiesPricing | PriceChangeRelatedStatistics | NaN | Valuation statistics for which a change of price is specified. | ValuationStatistics | PriceChange |
| SecuritiesPricing | Rate | NaN | Price expressed as a rate, ie, percentage. | PercentageRate | NaN |
| SecuritiesPricing | HighestPriceValueRelatedStatistics | NaN | Valuation statistics for which a highest price value is specified. | ValuationStatistics | HighestPriceValue |
| SecuritiesPricing | LowestPriceValueRelatedStatistics | NaN | Valuation statistics for which a lowest price value is specified. | ValuationStatistics | LowestPriceValue |
| SecuritiesPricing | Security | NaN | Identifies the security for which a price is given. | Security | Pricing |
| SecuritiesPricing | SecuritiesTradeExecution | NaN | Trade execution for which a deal price is specified. | SecuritiesTradeExecution | DealPrice |
| SecuritiesPricing | Yielded | NaN | Indicates whether the price is expressed as a yield (yield is the annual rate of return expressed as a percentage). | YesNoIndicator | NaN |
| SecuritiesPricing | TypeOfRate | NaN | Type of value in which the price (as a rate) is expressed. | PriceValueTypeCode | NaN |
| SecuritiesPricing | Derivative | NaN | Derivative for which an exercise price is specified. | Derivative | ExercisePrice |
| SecuritiesPricing | RelatedWarrant | NaN | Warrant for which a subscription price is provided. | Warrant | SubscriptionPrice |
| SecuritiesPricing | RelatedSecuritiesConversion | NaN | Securities conversion process for which a conversion price is specified. | SecuritiesConversion | ConversionPrice |
| SecuritiesPricing | LotBreakdown | NaN | Lot for which a price is specified. | LotBreakdown | LotPrice |
| SecuritiesPricing | TypeOfAmount | NaN | Type of value in which the price (as a rate) is expressed. | AmountPriceTypeCode | NaN |
| SecuritiesPricing | ExercisePriceRelatedEvent | NaN | Corporate action event for which an exercise price is provided. | CorporateActionPrice | CorporateActionExercisePrice |
| SecuritiesPricing | GenericCashPriceReceivedPerProductRelatedEvent | NaN | Corporate action event for which a generic cash price received per product is provided. | CorporateActionPrice | GenericCashPriceReceivedPerProduct |
| SecuritiesPricing | AmountPricePerFinancialInstrumentQuantity | NaN | Price expressed as an amount per a quantity of financial instruments. | AmountAndQuantity | SecuritiesPricing |
| SecuritiesPricing | AmountPricePerAmount | NaN | Price expressed as an amount per another amount. | AmountRatio | SecuritiesPricing |
| SecuritiesPricing | GenericCashPricePaidPerProductRelatedEvent | NaN | Corporate action event for which a generic cash price paid per product is provided. | CorporateActionPrice | GenericCashPricePaidPerProduct |
| SecuritiesPricing | PriceCalculationPeriod | NaN | Period during which the price of a security is determined (For outturn securities). | DateTimePeriod | PriceCalculationRelatedPricing |
| SecuritiesPricing | CashInLieuOfSharePriceRelatedEvent | NaN | Corporate action event for which a cash in lieu of share price is provided. | CorporateActionPrice | CashInLieuOfSharePrice |
| SecuritiesPricing | OverSubscriptionDepositPriceRelatedEvent | NaN | Corporate action event for which an over subscription deposit price is provided. | CorporateActionPrice | OverSubscriptionDepositPrice |
| SecuritiesPricing | CashValueForTaxRelatedEvent | NaN | Corporate action event for which a cash value has been provided. | CorporateActionPrice | CashValueForTax |
| SecuritiesPricing | MaximumPriceBiddingConditions | NaN | Bidding conditions for which a maximum price is specified. | BiddingConditions | MaximumPrice |
| SecuritiesPricing | MinimumPriceBiddingConditions | NaN | Bidding conditions for which a minimum price is specified. | BiddingConditions | MinimumPrice |
| SecuritiesPricing | QuotationDate | NaN | Date on which the price is obtained. | ISODateTime | NaN |
| SecuritiesPricing | YieldCalculation | NaN | Rate of return on an investment, based on the price. | YieldCalculation | RedemptionPrice |
| SecuritiesPricing | RelatedSecuritiesFinancing | NaN | Securities financing process for which an end price is specified. | SecuritiesFinancing | EndPrice |
| SecuritiesPricing | FundOrderRelatedToExecutedPrice | NaN | Fund order for which an executed price is specified. | InvestmentFundOrderExecution | ExecutedTradePrice |
| SecuritiesPricing | FundOrderRelatedToInformativePrice | NaN | Fund order for which an informative price is specified. | InvestmentFundOrderExecution | InformativePrice |
| SecuritiesPricing | TaxVoucher | NaN | Tax voucher for which the cost per share is specified. | TaxVoucher | ScripDividendReinvestmentPricePerShare |
| SecuritiesPricing | SecuritiesTrade | NaN | Trade for which the trade price is calculated. | SecuritiesTrade | TradePrice |
| SecuritiesPricing | NetAssetValueCalculation | NaN | Value calculation for which a securities pricing is specified. | NetAssetValueCalculation | Price |
| SecuritiesPricing | RelatedBuyIn | NaN | BuyIn process for which a price is specified. | BuyIn | BuyInPrice |
| SecuritiesPricing | Index | NaN | Specifies the index information when used for calculating the price. | Index | SecuritiesPricing |
| SecuritiesPricing | InformationPartyRole | NaN | Party which provided the pricing. | InformationPartyRole | Price |
| SecuritiesPricing | PriceFactPeriod | NaN | Period during which the price fact type is valid. | DateTimePeriod | PriceFactRelatedPricing |
| SecuritiesPricing | AnalyticsCalculation | NaN | Calculated analytics based on the price. | AnalyticsCalculation | SecuritiesPricing |
| SecuritiesPricing | DurationCalculation | NaN | Calculated duration based on the price. | DurationCalculation | RelatedSecuritiesPricing |
| SecuritiesPricing | LifeCalculation | NaN | Calculated life based on the price. | LifeCalculation | SecuritiesPricing |
| SecuritiesPricing | Date | NaN | Date/time of the price. For CIV, this is the NAV date. | ISODateTime | NaN |
| SecuritiesPricing | Spread | NaN | Spread which uses the price as benchmark. | Spread | BenchmarkPrice |
| SecuritiesPricing | Order | NaN | Securities order for which a price is specified. | SecuritiesOrder | OrderPrice |
| SecuritiesPricing | StopPriceOrder | NaN | Order for which a stop price is specified. | SecuritiesOrder | StopPrice |
| SecuritiesPricing | Allocation | NaN | Allocation process for which a price is specified. | Allocation | AllocatedPrice |
| SecuritiesPricing | RelatedOrder | NaN | Order for which a previous closing price is specified. | SecuritiesOrderParameters | PreviousClosingPrice |
| SecuritiesPricing | Issuance | NaN | Issuance for which a discount is specified. | Issuance | OriginalIssueDiscount |
| SecuritiesPricing | Entitlement | NaN | Entitlement for which a strike price is specified. | Entitlement | StrikePrice |
| SecuritiesPricing | CashFractionsPriceRelatedSecuritiesDistribution | NaN | Securities distribution for which a cash fractions price is provided. | SecuritiesDistribution | CashFractionsPrice |
| SecuritiesPricing | SuscriptionPriceRelatedSecuritiesDistribution | NaN | Securities distribution for which a subscription price is provided. | SecuritiesDistribution | SubscriptionPrice |
| SecuritiesPricing | ReinvestmentPriceRelatedSecuritiesDistribution | NaN | Securities distribution for which a reinvestment price is provided. | SecuritiesDistribution | ReinvestmentPrice |
| SecuritiesPricing | RelatedFuture | NaN | Contract for which a tick is specified. | Derivative | Tick |
| SecuritiesPricing | Distribution | NaN | Distribution for which an offer price is specified. | Distribution | OfferPrice |
| SecuritiesPricing | PriceChangeRedemptionSchedule | NaN | Redemption schedule for which a change in price is provided. | RedemptionSchedule | PriceChange |
| SecuritiesPricing | RelatedRedemptionSchedule | NaN | Redemption schedule for which a price is specified. | RedemptionSchedule | Price |
| SecuritiesPricing | PreviousClosingPriceRelatedQuote | NaN | Quote which contains a previous closing price. | Quote | PreviousClosingPrice |
| SecuritiesPricing | RequestedPriceRelatedQuote | NaN | Quote which contains a requested price. | Quote | RequestedPrice |
| SecuritiesPricing | PriceRelatedQuote | NaN | Quote which contains a price. | Quote | Price |
| SecuritiesPricing | MarketPriceRelatedQuote | NaN | Quote which contains a market price. | Quote | MarketPrice |
| SecuritiesPricing | Price | NaN | Value of the price. | Price | SecuritiesPricing |
| SecuritiesPricing | RelatedCorporateActionPrice | NaN | Corporate action price for which pricing information is provided. | CorporateActionPrice | PricingCalculation |
| SecuritiesPricing | RelatedPosition | NaN | Position for which a price is provided. | Position | Price |
| SecuritiesPricing | MinimumCashToInstructRelatedEvent | NaN | Corporate action event for which a minimum cash is instructed. | CorporateActionPrice | MinimumCashToInstruct |
| SecuritiesPricing | MaximumCashToInstructRelatedEvent | NaN | Corporate action event for which a maximum cash is instructed. | CorporateActionPrice | MaximumCashToInstruct |
| SecuritiesPricing | MinimumMultipleCashToInstructRelatedEvent | NaN | Corporate action event for which a minimum multiple cash is instructed. | CorporateActionPrice | MinimumMultipleCashToInstruct |
| RolePlayer | NaN | NaN | Type of entity that plays a specific role in a specific context. | NaN | NaN |
| RolePlayer | Role | NaN | Role of the entity in the activity. | Role | Player |
| RolePlayer | ValidityPeriod | NaN | Specifies the period during which a role player is valid | DateTimePeriod | RelatedRolePlayer |
| Party | NaN | RolePlayer | Entity involved in an activity. | NaN | NaN |
| Party | ContactPoint | NaN | Number, physical or virtual address, used for communication. | ContactPoint | RelatedParty |
| Party | Identification | NaN | Specific identification assigned to a party. | PartyIdentificationInformation | IdentifiedParty |
| Party | MoneyLaunderingCheck | NaN | Status of an identity check to prevent money laundering. This includes the counter-terrorism check. | MoneyLaunderingCheckCode | NaN |
| Party | TaxationConditions | NaN | Taxation parameters which apply to an individual person or to an organisation. | Tax | TaxableParty |
| Party | Domicile | NaN | Location in which a person is permanently domiciled (the place of a person's permanent home). | Location | DomiciledParty |
| Party | Residence | NaN | Location from which the affairs of a company are directed or location in which a person resides (the place of a person's home). | Location | Party |
| Party | PowerOfAttorney | NaN | Power of attorney which is held by the party. | PowerOfAttorney | AuthorisedParty |
| Party | Location | NaN | Location of the taxable party. | Location | TaxableParty |
| Party | CloseLinkSecurity | NaN | Security for which a close link with a party is identified. | Security | CloseLink |
| Party | CreditQuality | NaN | Credit quality for the clearing member. | CreditQualityCode | NaN |
| Party | ShareholdingType | NaN | Specifies the type of shareholding. | ShareholdingTypeCode | NaN |
| Party | RelatedCareOf | NaN | <p><span style="color:#ff8040;"></span>Identifies a Postal address of the addressee that is accepting the correspondence for an intended recipient.</p> | PostalAddress | CareOf |
| Organisation | NaN | Party | Organised structure that is set up for a particular purpose. For example, a business, government body, department, charity, or financial institution. | NaN | NaN |
| Organisation | Purpose | NaN | Purpose of the organisation, eg, charity. | Max35Text | NaN |
| Organisation | RegistrationDate | NaN | Date and time at which a given organisation was officially registered. | ISODateTime | NaN |
| Organisation | OrganisationIdentification | NaN | Specific identification assigned to an organisation. It is derived from the association between Party and PartyIdentification. | OrganisationIdentification | Organisation |
| Organisation | ParentOrganisation | NaN | Organisation which is divided in branches. | Organisation | Branch |
| Organisation | Branch | NaN | Specifies an organisation which is not a head office. | Organisation | ParentOrganisation |
| Organisation | SecuritiesModification | NaN | Specifies the process which originates the changes to an organisation. | SecuritiesModification | NewOrganisationInformation |
| Organisation | PlaceOfOperation | NaN | Place (including country) in which the organisation has its business activity. | Location | OperatingOrganisation |
| Organisation | PlaceOfRegistration | NaN | Place (including country) in which the organisation is registered. | Location | RegisteredOrganisation |
| Organisation | Description | NaN | Description of an organisation. | Max350Text | NaN |
| Organisation | LegalStructure | NaN | Legal standing of the organisation. | LegalStructureCode | NaN |
| Organisation | Sector | NaN | Sector of business of the organisation, for example, pharmaceutical. | Sector | Organisation |
| Organisation | RelatedIndicationOfInterest | NaN | Indication of interest process for which a list of organisations is specified. | BuyOrSellIndicationOfInterest | Organisations |
| Organisation | Strategy | NaN | Strategy related to an organisation. | OrganisationStrategy | Organisation |
| Organisation | OrganisationHierarchy | NaN | Description of the structure of a company. | OrganisationHierarchy | Organisation |
| Organisation | RepresentativeOfficer | NaN | Officer who has some rights to represent a given organisation. In account management, it is the person to be contacted by the account servicer. | RepresentativeOfficer | Organisation |
| Organisation | EstablishmentDate | NaN | Date when the organisation was established. | ISODate | NaN |
| Organisation | EntityExpirationDate | NaN | The date the Legal Entity ceased operation or was merged. This element SHALL be present if EntityExpirationReason is present, and omitted otherwise. | ISODateTime | NaN |
| Organisation | EntityExpirationReason | NaN | Reason that a Legal Entity ceased to operate. This element SHALL be present if EntityExpirationDate is present, and omitted otherwise. | CorporateActionEventTypeV6Code | NaN |
| Organisation | EntityStatus | NaN | Status of Legal Entity. | Max35Text | NaN |
| Organisation | MerchantCategory | NaN | Classification of a business by the types of goods or services it provides. | MerchantCategoryCodeIdentifier | NaN |
| Organisation | Logo | NaN | Commercial logo of the organisation. | Max10KBinary | NaN |
| Organisation | RelatedUltimateCreditrorEnrolmentService | NaN | Enrolment service for the ultimate party to which an amount of money is due. | EnrolmentService | UltimateCreditor |
| Organisation | RelatedCreditrorEnrolmentService | NaN | Enrolment service for the party to which an amount of money is due. | EnrolmentService | Creditor |
| Organisation | RelatedPostTradeRiskReduction | NaN | Post trade risk reduction for which the organisation is the structurer. | PostTradeRiskReduction | Structurer |
| PartyName | NaN | NaN | Name by which a party is known and which is usually used to identify that party. | NaN | NaN |
| PartyName | Name | NaN | Name by which a party is known and which is usually used to identify that party. This name is derived from the concatenation of the elements that compose the name of a person or from the legal name of an organisation. | Max140Text | NaN |
| PartyName | PartyIdentification | NaN | Party identification which contains a name. | PartyIdentificationInformation | PartyName |
| ContactPoint | NaN | NaN | Number, physical or virtual address, used for communication. | NaN | NaN |
| ContactPoint | Identification | NaN | Identification of a contact point. | GenericIdentification | IdentificationForContactPoint |
| ContactPoint | RelatedInvestmentFund | NaN | Investment fund class for which an order desk is specified. | InvestmentFund | OrderDesk |
| ContactPoint | BICAddress | NaN | BIC address which identifies the contact point. | AnyBICDec2014Identifier | NaN |
| ContactPoint | RelatedParty | NaN | Party for which a contact point is specified. | Party | ContactPoint |
| ContactPoint | RelatedCorporateActionEvent | NaN | Corporate action event for which the documentation location is specified. | CorporateActionEvent | DocumentationLocation |
| ContactPoint | RelatedReportingService | NaN | Reporting service for which a contact point is specified. | ReportingService | ReportingChannel |
| ContactPoint | StoredDocument | NaN | Document which is stored at a specific place. | Document | PlaceOfStorage |
| ContactPoint | RemittanceRelatedPayment | NaN | Payment for which a remittance location is specified. | PaymentObligation | RemittanceLocation |
| ContactPoint | RelatedProxyAppointment | NaN | Proxy appointment process for which a notification address is specified. | ProxyAppointmentCondition | NotificationAddress |
| ContactPoint | ContactPointForMeeting | NaN | Meeting which takes place at a specific place. | Meeting | MeetingLocation |
| ContactPoint | ContactPointForVote | NaN | Vote parameters which apply to a vote location. | VotingCondition | VoteLocation |
| ContactPoint | MainContact | NaN | Contact address used for normal operations. | ContactPoint | ReturnAddress |
| ContactPoint | ReturnAddress | NaN | Physical/logical address, segregated from the main address that is used for normal operations. The return address is used to route messages that require specific attention/exception handling, eg, returns or rejects. | ContactPoint | MainContact |
| ContactPoint | RelatedPayment | NaN | Payment for which a notification method is specified. | PaymentProcessing | ContactPoint |
| ContactPoint | TemporaryIndicator | NaN | Indicates whether the address is a temporary address. | YesNoIndicator | NaN |
| ContactPoint | DeliveredAttendanceCard | NaN | Attendance card which is delivered at a specific location. | AttendanceCard | DeliveryPlace |
| ContactPoint | InvestmentFundClassProcessing | NaN | Processing characteristics of an investment fund class for which a local market annex is specified. | InvestmentFundClassProcessingCharacteristics | LocalMarketAnnex |
| PostalAddress | NaN | ContactPoint | Information that locates and identifies a specific address. | NaN | NaN |
| PostalAddress | AddressType | NaN | Specifies the type of address. | AddressTypeCode | NaN |
| PostalAddress | StreetName | NaN | Name of a street or thoroughfare. | Max35Text | NaN |
| PostalAddress | StreetBuildingIdentification | NaN | Number that identifies the position of a building on a street. | Max35Text | NaN |
| PostalAddress | PostCodeIdentification | NaN | Identifier consisting of a group of letters and/or numbers that is added to a postal address to assist the sorting of mail. | Max16Text | NaN |
| PostalAddress | TownName | NaN | Name of a built-up area, with defined boundaries, and a local government. | Max35Text | NaN |
| PostalAddress | BuildingName | NaN | Name of the building or house. | Max35Text | NaN |
| PostalAddress | Floor | NaN | Floor or storey within a building. | Max16Text | NaN |
| PostalAddress | PostOfficeBox | NaN | Numbered box in a post office, assigned to a person or organisation, where letters are kept until called for. | Max16Text | NaN |
| PostalAddress | Department | NaN | Identification of a division of a large organisation or building. | Max70Text | NaN |
| PostalAddress | SubDepartment | NaN | Identification of a sub-division of a large organisation or building. | Max70Text | NaN |
| PostalAddress | Location | NaN | Specifies a place. | Location | Address |
| PostalAddress | ChequeIssue | NaN | Cheque issue information for which a delivery address is specified. | ChequeIssue | DeliverTo |
| PostalAddress | Country | NaN | Country of the address. | Country | PostalAddressSpecification |
| PostalAddress | ValidityPeriod | NaN | Specifies the period during which a postal address is valid. | DateTimePeriod | RelatedPostalAddress |
| PostalAddress | SuiteIdentification | NaN | Identification of a suite or apartment. | Max35Text | NaN |
| PostalAddress | BuildingIdentification | NaN | Identification of a building, within a group of buildings, that have the same street number identifier. | Max35Text | NaN |
| PostalAddress | MailDeliverySubLocation | NaN | Specific place to deliver mail within a pre-defined postal address. | Max35Text | NaN |
| PostalAddress | Block | NaN | Area of land bounded by streets. | Max35Text | NaN |
| PostalAddress | Lot | NaN | Identification of an allotment of land. | Max35Text | NaN |
| PostalAddress | MailingInstructions | NaN | Specifies the characteristics of an address. | MailingInstructions | RelatedPostalAddress |
| PostalAddress | PhysicalDelivery | NaN | Physical delivery information related to an address. | PhysicalDelivery | Address |
| PostalAddress | UnitNumber | NaN | <p>Identifies a flat or dwelling within the building.</p> | Max16Text | NaN |
| PostalAddress | CareOf | NaN | <p>Identifies an addressee that is accepting the correspondence for the intended recipient. Using care of ensures the correspondence reaches the right recipient rather than getting returned to the sender.</p> | Party | RelatedCareOf |
| PhoneAddress | NaN | ContactPoint | Collection of information that identifies a phone address. | NaN | NaN |
| PhoneAddress | PhoneNumber | NaN | Collection of information that identifies a phone number, as defined by telecom services. It is recommended to use only numbers and limited punctuation +,-.(.). | Max35Text | NaN |
| PhoneAddress | FaxNumber | NaN | Collection of information that identifies a FAX number, as defined by telecom services. It is recommended to use only numbers and limited punctuation +,-.(.). | Max35Text | NaN |
| PhoneAddress | MobileNumber | NaN | Collection of information that identifies a mobile phone number, as defined by telecom services. It is recommended to use only numbers and limited punctuation +,-.(.). | Max35Text | NaN |
| ElectronicAddress | NaN | ContactPoint | Address which is accessed by electronic means. | NaN | NaN |
| ElectronicAddress | EmailAddress | NaN | Address for electronic mail (e-mail). | Max256Text | NaN |
| ElectronicAddress | URLAddress | NaN | Address for the Universal Resource Locator (URL), eg, used over the www (HTTP) service. | Max256Text | NaN |
| ElectronicAddress | TelexAddress | NaN | Address for a telex machine. | Max35Text | NaN |
| ElectronicAddress | RelatedPresentation | NaN | Presentation process for which an electronic presentation address is specified. | Presentation | ElectronicPresentationAddress |
| ElectronicAddress | TeletextAddress | NaN | Address for a teletext. | Max35Text | NaN |
| ElectronicAddress | ISDNAddress | NaN | Address for an Integrated Services Digital Network. | Max35Text | NaN |
| PartyIdentificationInformation | NaN | NaN | Unique and unambiguous way to identify a party | NaN | NaN |
| PartyIdentificationInformation | OtherIdentification | NaN | Identifier issued to a party for which no specific identifier has been defined. | GenericIdentification | RelatedPartyIdentification |
| PartyIdentificationInformation | IdentifiedParty | NaN | Party for which an identification is provided. | Party | Identification |
| PartyIdentificationInformation | TaxIdentificationNumber | NaN | Number assigned by a tax authority to an entity. | Max35Text | NaN |
| PartyIdentificationInformation | NationalRegistrationNumber | NaN | Number assigned by a national registration authority to an entity. In Singapore this is known as the NRIC. | Max35Text | NaN |
| PartyIdentificationInformation | TypeOfIdentification | NaN | Specifies the type of alternate identification which can be used to identify a party. | TypeOfIdentificationCode | NaN |
| PartyIdentificationInformation | Declaration | NaN | Provides declaration details relative to the party. | Max350Text | NaN |
| PartyIdentificationInformation | PartyType | NaN | Specifies the type of party in different business contexts. | PartyTypeCode | NaN |
| PartyIdentificationInformation | PartyName | NaN | Name by which a party is known and which is usually used to identify that party. | PartyName | PartyIdentification |
| PartyIdentificationInformation | ValidityPeriod | NaN | Specifies the period during which an identification is valid | DateTimePeriod | RelatedIdentification |
| PartyIdentificationInformation | IdentifiedMarket | NaN | Market for which an identification is provided. | Market | Identification |
| PartyIdentificationInformation | RelatedApprovedBenchmark | NaN | Benchmark that is supervised by the endorsing party. | PortfolioBenchmark | Approver |
| PartyIdentificationInformation | RelatedAdministratedBenchmark | NaN | Benchmark that is administrated by the administrator party. | PortfolioBenchmark | Administrator |
| PartyIdentificationInformation | RegistrationAuthorityIdentification | NaN | An identifier for the Legal Entity in a business registry in the jurisdiction of legal registration, or in the appropriate registration authority. | Max8Text | NaN |
| OrganisationIdentification | NaN | PartyIdentificationInformation | Unique and unambiguous way to identify an organisation. | NaN | NaN |
| OrganisationIdentification | BICFI | NaN | Code allocated to a financial institution by the ISO 9362 Registration Authority as described in ISO 9362 "Banking - Banking telecommunication messages - Business identifier code (BIC)". | BICFIDec2014Identifier | NaN |
| OrganisationIdentification | AnyBIC | NaN | Code allocated to a financial or non-financial institution by the ISO 9362 Registration Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business identifier code (BIC)". | AnyBICDec2014Identifier | NaN |
| OrganisationIdentification | OrganisationName | NaN | Name by which an organisation is known and which is usually used to identify that organisation. It is derived from the association between PartyIdentificationInformation and PartyName. | OrganisationName | Organisation |
| OrganisationIdentification | Organisation | NaN | Organisation which is identified | Organisation | OrganisationIdentification |
| OrganisationIdentification | ClearingSystemMemberIdentificationType | NaN | Unique and unambiguous identifier of a clearing system member, assigned by the system or system administrator. | CashClearingSystemMember | OrganisationIdentification |
| OrganisationIdentification | BICNonFI | NaN | Code allocated to a non-financial institution by the ISO 9362 Registration Authority as described in ISO 9362 "Banking - Banking telecommunication messages - Business identifier code (BIC)". | BICNonFIDec2014Identifier | NaN |
| OrganisationIdentification | EANGLN | NaN | Global Location Number. A non-significant reference number used to identify legal entities, functional entities, or physical entities according to the European Association for Numbering (EAN) numbering scheme rules. The number is used to retrieve detailed information that is linked to it. | EANGLNIdentifier | NaN |
| OrganisationIdentification | CHIPSUniversalIdentifier | NaN | (United States) Clearing House Interbank Payments System (CHIPS) Universal Identification (UID). Identifies entities that own accounts at CHIPS participating financial institutions, through which CHIPS payments are effected. The CHIPS UID is assigned by the New York Clearing House. | CHIPSUniversalIdentifier | NaN |
| OrganisationIdentification | DUNS | NaN | Data Universal Numbering System. A unique identification number provided by Dun & Bradstreet to identify an organization. | DunsIdentifier | NaN |
| OrganisationIdentification | BankPartyIdentification | NaN | Unique and unambiguous assignment made by a specific bank to identify a relationship as defined between the bank and its client. | Max35Text | NaN |
| OrganisationIdentification | MIC | NaN | Market Identifier Code. Identification of a financial market, as stipulated in the norm ISO 10383 "Codes for exchanges and market identifications". | MICIdentifier | NaN |
| OrganisationIdentification | LEI | NaN | Legal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial Services - Legal Entity Identifier (LEI)". | LEIIdentifier | NaN |
| OrganisationIdentification | ELF | NaN | Entity Legal Forms is a code allocated to a party as described in ISO 20275 "Financial services â€” Entity legal forms (ELF)". | ELFIdentifier | NaN |
| OrganisationIdentification | AdditionalLEIAttributes | NaN | Additional LEI attributes belonging to the organisation. | AdditionalLEIAttributes | RelatedOrganisationIdentification |
| PersonName | NaN | PartyName | Name by which a person is known and that is usually used to identify that person. | NaN | NaN |
| PersonName | BirthName | NaN | Name received at birth, eg, maiden name. | Max35Text | NaN |
| PersonName | NamePrefix | NaN | Specifies the terms used to formally address a person. | NamePrefixCode | NaN |
| PersonName | GivenName | NaN | First name of a person. | Max35Text | NaN |
| PersonName | MiddleName | NaN | Second name of a person. | Max35Text | NaN |
| PersonName | NameSuffix | NaN | Additional information about a person that follows a person's name, eg, qualification such as Doctor of Philosophy (PhD). | Max35Text | NaN |
| PersonName | Identification | NaN | Person identification which contains a name. | PersonIdentification | PersonName |
| TimeFrame | NaN | NaN | TimeFrame or period concept that allows definition of a period as number of days before or after a defined activity. | NaN | NaN |
| TimeFrame | TradeMinus | NaN | An agreed number of days before the Trade date (T) used to define standard timeframes e.g. T-1 Dealing cut off or T-2 prepayment condition Where = T is the date that the price is applied to a transaction, | Number | NaN |
| TimeFrame | RenunciationMinus | NaN | An agreed number of days before the Renunciation of Title documents are received used to define standard timeframes in redemption. | Number | NaN |
| TimeFrame | SubscriptionSettlementRelatedFundProcessing | NaN | Fund processing characteristics related to a subscription cycle. | InvestmentFundClassProcessingCharacteristics | SettlementCycle |
| TimeFrame | TradePlus | NaN | An agreed number of days after the Trade date (T) used to define standard timeframes e.g T+3 settlement period. Where = T is the date that the price is applied to a transaction. | Number | NaN |
| TimeFrame | RenunciationPlus | NaN | An agreed number of days after the renunciation of title documents are received used to define standard timeframes in Redemption e.g R+3 Redemption settlement cycle. | Number | NaN |
| TimeFrame | Prepayment | NaN | Indicates whether pre-payment is necessary. | YesNoIndicator | NaN |
| TimeFrame | OtherTimeFrameDescription | NaN | Specifies a description of any other TimeFrame that may be used for the DealingCutOffTimeFrame | Max350Text | NaN |
| TimeFrame | RelatedProcessingCharacteristics | NaN | Processing characteristics for which a cut off time frame is specified. | InvestmentFundClassProcessingCharacteristics | DealingCutOffTimeFrame |
| Account | NaN | NaN | Record of transactions in specific types of assets, maintained by a servicing party on behalf of one or more owning parties. Business relationship between an account servicer and one or more account owners. | NaN | NaN |
| Account | BaseCurrency | NaN | Base currency of the account. | CurrencyCode | NaN |
| Account | Identification | NaN | Unique and unambiguous identification for the account between the account owner and the account servicer. | AccountIdentification | Account |
| Account | ParentAccount | NaN | Account for which one or more sub-accounts are specified. | Account | SubAccount |
| Account | SubAccount | NaN | Subdivision of an account used to segregate specific holdings. | Account | ParentAccount |
| Account | RelatedFundProcessingCharacteristics | NaN | Fund processing characteristics for which a settlement account is specified. | InvestmentFundClassProcessingCharacteristics | SettlementAccount |
| Account | Status | NaN | Specifies the current state of an account, eg, enabled or deleted. | AccountStatus | Account |
| Account | Language | NaN | Language for all communication concerning the account. | LanguageCode | NaN |
| Account | PartyRole | NaN | Specifies each role linked to an account and played by a party in that context. | AccountPartyRole | Account |
| Account | TradePartyRole | NaN | Party for which an account is specified in the context of a trade. | TradePartyRole | Account |
| Account | ReportingCurrency | NaN | Currency used to calculate and report the balance and related entries of an account. | CurrencyCode | NaN |
| Account | AccountRestriction | NaN | Restriction on capability or operations allowed. | AccountRestriction | Account |
| Account | SettlementPartyRole | NaN | Specifies the role of the party which uses the account for settlement. | SettlementPartyRole | SettlementAccount |
| Account | Purpose | NaN | Specifies the purpose of the account. | Max140Text | NaN |
| Account | ClosingDate | NaN | Date on which the account and related services cease effectively to be operational for the account owner. | ISODateTime | NaN |
| Account | LiveDate | NaN | Date of the first movement on the account. | ISODateTime | NaN |
| Account | ReportedPeriod | NaN | Specifies the period for which the movements in the account are reported. | DateTimePeriod | Account |
| Account | InvestmentFundPartyRole | NaN | Party role for which an account is specified. | InvestmentFundPartyRole | Account |
| Account | RelatedCollateralProcess | NaN | Collateral data for which a collateral account is specified. | Collateral | CollateralAccount |
| Account | Type | NaN | Specifies the type of account. | GenericIdentification | Account |
| Account | RelatedProceedsDelivery | NaN | Proceeds delivery instruction which contain account identification. | CorporateActionProceedsDeliveryInstruction | SettlementAccount |
| Account | RelatedCorporateActionPartyRole | NaN | Party for which an account is specified in the context of a corporate action. | CorporateActionPartyRole | Account |
| Account | DefaultFundAccountOwner | NaN | Clearing member which holds a default fund account at an ICSD or at the central bank. | ClearingMemberRole | DefaultFundAccount |
| Account | System | NaN | System where the account is held. | System | Account |
| Account | Balance | NaN | Overall position representing the net debits and credits in an account at a specific point in time. | Balance | Account |
| Account | Entry | NaN | Record of the movements into or out of an account. | Entry | Account |
| Account | AccountContract | NaN | Agreement which provides information on the account and on the services linked to it. | AccountContract | Account |
| Account | OpeningDate | NaN | Date on which the account and related basic services are effectively operational for the account owner. | ISODateTime | NaN |
| Account | CurrencyExchange | NaN | Rate used to calculate the difference between amounts based on the base currency and the reporting currency. | CurrencyExchange | ReportedAccount |
| Account | DefaultFundContribution | NaN | Default fund contribution parameters associated with a contribution account. | DefaultFundContribution | ContributionAccount |
| Account | SystemMember | NaN | Member of a system which is the owner of an account with the system. | SystemMemberRole | Account |
| Account | CollateralAccountType | NaN | Specifies the collateral account type. | CollateralAccountTypeCode | NaN |
| Account | AccountService | NaN | Services linked to the account and specified in the account contract. | AccountService | Account |
| Account | Reconciliation | NaN | Process which compares and matches trade information with entries in an account. | Reconciliation | Account |
| Account | ManagedAccountProduct | NaN | Product which provides guidance to investors to manage their portfolios. | ManagedAccountProduct | Account |
| CashAccount | NaN | Account | Account to or from which a cash entry is made. | NaN | NaN |
| CashAccount | CashAccountType | NaN | Specifies the nature, or use, of the cash account. | CashAccountTypeCode | NaN |
| CashAccount | RelatedInvestmentAccount | NaN | Investment account for which a cash branch is specified. | InvestmentAccount | CashAccount |
| CashAccount | CashEntry | NaN | Record of the cash movements into or out of a cash account. It is derived from the association between Account and Entry. | CashEntry | CashAccount |
| CashAccount | CashBalance | NaN | Overall position representing the net debits and credits in an account at a specific point in time. It is derived from the association between Account and Balance. | CashBalance | CashAccount |
| CashAccount | PaymentPartyRole | NaN | Specifies each role linked to a payment and using a specific cash account in the payment context. | PaymentPartyRole | CashAccount |
| CashAccount | RelatedCreditStandingOrder | NaN | Instruction given by an account holder to an account servicer to make regular transfers on given dates to the same beneficiary. | StandingOrder | CreditAccount |
| CashAccount | RelatedDebitStandingOrder | NaN | Instruction given by an account holder to an account servicer to make regular transfers on given dates to the same beneficiary. | StandingOrder | DebitAccount |
| CashAccount | CashAccountContract | NaN | Contract which manages the account. It is derived from the relation between AccountContract and Account. | CashAccountContract | CashAccount |
| CashAccount | RelatedCorporateActionElection | NaN | Election process which uses specific cash accounts. | CorporateActionElection | CashAccount |
| CashAccount | Charges | NaN | Specifies the charges which are debited from the account. | Charges | ChargesDebitAccount |
| CashAccount | Tax | NaN | Tax charged on a cash account. | Tax | TaxAccount |
| CashAccount | RelatedSettlementInstruction | NaN | Settlement process which uses specific cash accounts. | CashSettlement | SettlementAccount |
| CashAccount | CashSettlementPartyRole | NaN | Specifies each role linked to a payment settlement and using a specific cash account in the payment context. | CashSettlementInstructionPartyRole | CashAccount |
| CashAccount | UltimateObligor | NaN | Party for which different types of cash accounts are specified. | UndertakingUltimateObligor | CashAccount |
| CashAccount | RelatedPaymentCard | NaN | Payment card for which an account is specified. | PaymentCard | RelatedAccount |
| CashAccount | SecuritiesPartyRole | NaN | Specifies the role which uses a cash account. | SecuritiesPartyRole | CashAccount |
| CashAccount | RelatedInvoiceFinancingPartyRole | NaN | Specifies each role using a specific account in the context of invoice financing. | InvoiceFinancingPartyRole | CashAccount |
| CashAccount | RelatedCommercialTrade | NaN | Commercial trade for which a purchase account is specified. | CommercialTrade | PurchaseAccount |
| CashAccount | Level | NaN | Defines the level of an account within the account hierarchy. | AccountLevelCode | NaN |
| CashAccount | SettlementCurrency | NaN | Specifies the currency used for settlement, if different from the account currency. | CurrencyCode | NaN |
| CashAccount | ReportedMovements | NaN | Provides statistical information on the number of movements and their value for a particular account. | AccountReportedMovement | ReportedCashAccount |
| CashAccount | ClosedAccountContract | NaN | Contract which specifies the cash account to/from which the balance of a closed account must be transferred. | CashAccountContract | TransferCashAccount |
| CashAccount | AccountLink | NaN | Defines the link between a cash account and a securities account. | AccountLink | CashAccount |
| CashAccount | CashStandingOrder | NaN | Standing order which applies on a specific account. | CashStandingOrder | CashAccount |
| CashAccount | Cheque | NaN | Cheques drawn on a cash account. | Cheque | CashAccount |
| CashAccount | CashAccountService | NaN | Services linked to the cash account and specified in the cash account contract. It is derived from the association between Account and AccountService. | CashAccountService | CashAccount |
| CashAccount | Payment | NaN | Payment for which an account is specified. | Payment | Account |
| CashAccount | Commission | NaN | Amount of money due to a party as compensation for a service. | Commission | Account |
| AccountIdentification | NaN | NaN | Unique identifier of an account, as assigned by the account servicer. | NaN | NaN |
| AccountIdentification | Account | NaN | Account for which an identification is provided. | Account | Identification |
| AccountIdentification | IBAN | NaN | International Bank Account Number (IBAN) - identifier used internationally by financial institutions to uniquely identify the account of a customer. Further specifications of the format and content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services - International Bank Account Number (IBAN)" version 1997-10-01, or later revisions. | IBAN2007Identifier | NaN |
| AccountIdentification | BBAN | NaN | Basic Bank Account Number (BBAN) - identifier used nationally by financial institutions, ie, in individual countries, generally as part of a National Account Numbering Scheme(s), to uniquely identify the account of a customer. | BBANIdentifier | NaN |
| AccountIdentification | UPIC | NaN | Universal Payment Identification Code (UPIC) - identifier used by the New York Clearing House to mask confidential data, such as bank accounts and bank routing numbers. UPIC numbers remain with business customers, regardless of banking relationship changes. | UPICIdentifier | NaN |
| AccountIdentification | ProprietaryIdentification | NaN | Unique identifier for an account. It is assigned by the account servicer using a proprietary identification scheme. | GenericIdentification | IdentificationForAccount |
| AccountIdentification | Name | NaN | Name of the account. It provides an additional means of identification, and is designated by the account servicer in agreement with the account owner. | Max70Text | NaN |
| AccountIdentification | CostReferencePattern | NaN | Template describing the mask of the structure for the format of the accounting account identifier; for example "AABBBBCC" where AA represents the country, BBBB the service classification, CC the sales area. | GenericIdentification | IdentificationForAccountCostReferencePattern |
| AccountIdentification | Number | NaN | String of characters (mainly numbers) used to identify an account. | Max140Text | NaN |
| FinancialInstitution | NaN | Organisation | Organisation established primarily to provide financial services. | NaN | NaN |
| FinancialInstitution | RelatedPaymentTracker | NaN | Tracker identified by this agent. | PaymentTracker | Agent |
| Location | NaN | NaN | Specifies a place. | NaN | NaN |
| Location | NativePerson | NaN | Person for which a birth place is specified. | Person | PlaceOfBirth |
| Location | System | NaN | System for which a location is specified. | System | Location |
| Location | DomiciledParty | NaN | Party which is domiciled in a specific location. | Party | Domicile |
| Location | OperatingOrganisation | NaN | Organisation which has its operations in a specific location. | Organisation | PlaceOfOperation |
| Location | Address | NaN | Information that locates and identifies a specific address. | PostalAddress | Location |
| Location | IssuedDocument | NaN | Document which was issued at a specific location. | Document | PlaceOfIssue |
| Location | Incoterms | NaN | Incoterms associated with a location. | Incoterms | Location |
| Location | DepartureTransportParameters | NaN | Transport parameters linked to a place of departure. | Transport | PlaceOfDeparture |
| Location | DestinationTransportParameters | NaN | Transport parameters linked to a place of destination. | Transport | PlaceOfDestination |
| Location | InsuranceCertificate | NaN | Insurance for which the claims are payable at a specific location. | InsuranceCertificate | ClaimsPayableAt |
| Location | Party | NaN | Party which resides in a specific location. | Party | Residence |
| Location | RelatedExpiry | NaN | Expiry information which contains an expiry location. | Expiry | ExpiryPlace |
| Location | RelatedJurisdiction | NaN | Jurisdiction of the location. | Jurisdiction | Identification |
| Location | Identification | NaN | Identifies the location, for instance, the name of an airport, a county, a state, a province or a city by a code or a text. eg LHR for London Heathrow airport. | GenericIdentification | IdentifiedLocation |
| Location | TaxableParty | NaN | Party which is taxable at a specific location | Party | Location |
| Location | RegisteredOrganisation | NaN | Organisation which is registered at that location. | Organisation | PlaceOfRegistration |
| Location | RelatedTransport | NaN | Transport process for which a transit location is specified. | Transport | TransitLocation |
| Location | TimeZone | NaN | Offset of the time before or after 00:00 hour UTC. | UTCOffset | Location |
| UTCOffset | NaN | NaN | Offset of the time before or after 00:00 hour UTC. | NaN | NaN |
| UTCOffset | Sign | NaN | Indicates whether the offset is before or after 00:00 hour UTC. | PlusOrMinusIndicator | NaN |
| UTCOffset | NumberOfHours | NaN | Offset of the reporting time, in hours, before or after 00:00 hour UTC. | ISOTime | NaN |
| UTCOffset | Location | NaN | Location to which the time zone applies. | Location | TimeZone |
| RedemptionSchedule | NaN | NaN | Describes the reason and terms for early partial or total redemption, amortisation or extension of an issue. | NaN | NaN |
| RedemptionSchedule | BusinessDayConvention | NaN | Convention used for adjusting a date when it is not a business day. | BusinessDayConventionCode | NaN |
| RedemptionSchedule | EffectivePeriod | NaN | Period during which the issuer or holder may give notice. | DateTimePeriod | RedemptionSchedule |
| RedemptionSchedule | PriceChange | NaN | Redemption or amortisation price change. | SecuritiesPricing | PriceChangeRedemptionSchedule |
| RedemptionSchedule | Price | NaN | Redemption or amortisation price. | SecuritiesPricing | RelatedRedemptionSchedule |
| RedemptionSchedule | PartyType | NaN | Party type entitled to ask for the redemption. | PartyTypeCode | NaN |
| RedemptionSchedule | AmountFulfilType | NaN | Specifies if the full amount or only part of it is redeemed. | AmountFullfilTypeCode | NaN |
| RedemptionSchedule | MinimumNoticeDays | NaN | Minimum number of notice in days that must be given by either the issuer or the holder before redemption can take place. | Number | NaN |
| RedemptionSchedule | MaximumNoticeDays | NaN | Maximum number of notice in days that must be given by either the issuer or the holder before redemption can take place. | Number | NaN |
| RedemptionSchedule | FinancialCenter | NaN | Financial place taken into account to adjust the date and time, as defined within the business day convention. | FinancialCenterCode | NaN |
| RedemptionSchedule | NoticePeriodType | NaN | Specifies the type of notice period. | NoticePeriodTypeCode | NaN |
| RedemptionSchedule | PriceChangeFrequency | NaN | Redemption or amortisation price change frequency. | FrequencyCode | NaN |
| RedemptionSchedule | PriceFrequency | NaN | Specifies the frequency of the redemption. | FrequencyCode | NaN |
| RedemptionSchedule | Security | NaN | Security for which a redemption schedule is specified. | Security | RedemptionSchedule |
| TradingMarket | NaN | Market | Context or geographic environment in which trading parties may meet in order to negotiate and execute trades among themselves. It also identifies the primary market where an asset is issued. | NaN | NaN |
| TradingMarket | TradedSecurity | NaN | Security which is traded on a specific market. | Security | TradingMarket |
| TradingMarket | Type | NaN | Nature of a market in which transactions take place. | MarketTypeCode | NaN |
| TradingMarket | ListedSecurity | NaN | Security whch is listed on a specific market. | Security | PlaceOfListing |
| TradingMarket | SourceOfPrice | NaN | Party which provides a price on a market. | SourceOfPrice | MarketIdentification |
| TradingMarket | TradeLotSize | NaN | Specifies the number of securities that have to be traded in one lot . | LotBreakdown | TradeLotMarket |
| TradingMarket | MinimumTradedNominalQuantity | NaN | Minimum number of securities that can be traded. | SecuritiesQuantity | MinimumTradedQuantityMarket |
| TradingMarket | ListingDate | NaN | Date/time at which the security is listed at the specific exchange. | ISODateTime | NaN |
| TradingMarket | RelatedOrder | NaN | Order for which a place of trade is requested. | SecuritiesOrder | PlaceOfTrade |
| TradingMarket | TradingCurrency | NaN | Currency of the trading. | CurrencyCode | NaN |
| TradingMarket | MaximumTradedNominalQuantity | NaN | Miaximum number of securities that can be traded. | SecuritiesQuantity | MaximumTradedQuantityMarket |
| TradingMarket | StockExchange | NaN | Stock exchange which operates on a specific market. | StockExchange | Market |
| TradingMarket | QuoteLot | NaN | Lot size associated with the price. Most exchanges require that pricing be quoted in round lot size. However, some exchanges have pricing quoted in many different lot sizes, for example, Latin America, some Asian markets, Turkey. | LotBreakdown | QuoteLotMarket |
| TradingMarket | RoundLot | NaN | Minimum quantity of securities that can be purchased without incurring a larger fee. For example, if the round lot size is 100 and the trade is for 125 shares, then 100 will be processed without a fee and the remaining 25 will incur a service fee for being an odd lot size. | LotBreakdown | RoundLotMarket |
| TradingMarket | TradingSession | NaN | Trading session associated with a market. | TradingSession | Market |
| TradingMarket | ListedSecurityTradingIdentification | NaN | Trading identification used on this trading market. | SecuritiesIdentification | ApplicableTradingMarket |
| TradingMarket | DefaultCurrency | NaN | Default currency for the securities trading on this market. | CurrencyCode | NaN |
| TradingMarket | FirstTradingDate | NaN | First date/time at which the security is eligible for trading. | ISODateTime | NaN |
| TradingMarket | LastTradingDate | NaN | Last date/time at which the security is eligible for trading. | ISODateTime | NaN |
| TradingMarket | Issuance | NaN | Issuance for which the place has been defined. | Issuance | IssuePlace |
| TradingMarket | RelatedPlaceOfSettlement | NaN | Place of settlement for which a settlement market is specified. | PlaceOfSettlement | SettlementMarket |
| Trade | NaN | NaN | Result of an order between at least two parties. A trade relates to the delivery of goods and services, cash or securities. | NaN | NaN |
| Trade | TradeDateTime | NaN | Specifies the date/time on which the trade was executed. | ISODateTime | NaN |
| Trade | TradeCommission | NaN | Commission parameters associated with a trade. | Commission | Trade |
| Trade | ValueDate | NaN | Date on which the trade is settled, ie, the amounts are due. | ISODate | NaN |
| Trade | EndDate | NaN | End date of the trade, such as a treasury trade or a derivative trade. | ISODateTime | NaN |
| Trade | TradeRelatedIdentifications | NaN | Specifies the different identifications associated with a trade. | TradeIdentification | Trade |
| Trade | AllocationIndicator | NaN | Specifies the type of allocation for a trade. | Max35Text | NaN |
| Trade | CollateralisationType | NaN | Specifies the type of collateralisation. | Max35Text | NaN |
| Trade | BlockIndicator | NaN | Indicates whether the trade is a block or single trade. | YesNoIndicator | NaN |
| Trade | SettlementNetting | NaN | Indicates to the clearing member whether the trade is eligible for settlement netting or not. | NettingEligibleCode | NaN |
| Trade | TradePartyRole | NaN | Role played by a party in relation with a trade. | TradePartyRole | Trade |
| Trade | Obligation | NaN | Specifies the trade which originates the obligation to deliver a product, cash or securities.. | Obligation | Trade |
| Trade | RelatedNegotiation | NaN | Negotiation process which is the source of the treasury trade. | Negotiation | TradeExecution |
| Trade | GoverningDocument | NaN | Legal agreement applicable to a trade. | MasterAgreement | GovernedTrades |
| Trade | StartDate | NaN | Start date of the trade, such as a treasury trade or a derivative trade. | ISODateTime | NaN |
| Trade | System | NaN | System involved in the processing of a trade such as clearing, settlement or matching system. | System | Trade |
| Trade | Asset | NaN | Asset which is the object of a trade. | Asset | Trade |
| Trade | Market | NaN | Market where a trade is negotiated and executed. | Market | Trade |
| Trade | Guarantee | NaN | Guarantee which covers a trade. | Guarantee | GuaranteedTrade |
| Trade | Settlement | NaN | Transfer of proceeds. | Settlement | Trade |
| Trade | Order | NaN | Specifies the order related to a trade. | Order | Trade |
| Trade | Leg | NaN | Separate transactions which combined together form a trade. | Leg | Trade |
| Trade | FinancialTransaction | NaN | Financial transaction to which the trade belongs. | FinancialTransaction | Trade |
| Trade | Reconciliation | NaN | Process which compares and matches trade information with entries in an account. | Reconciliation | ReconciledTrades |
| Scheme | NaN | NaN | Information regarding an enumerated code list and its owner. | NaN | NaN |
| Scheme | NameShort | NaN | Short textual description of the scheme. | Max35Text | NaN |
| Scheme | Code | NaN | Code that represents the enumerated list, for example, ISO 6166 for ISIN. | Max35Text | NaN |
| Scheme | Identification | NaN | Identification information for which a scheme is specified. | GenericIdentification | Scheme |
| Scheme | Rating | NaN | Rating for which an identification by scheme is specified. | Rating | RatingScheme |
| Scheme | CreditorRole | NaN | Creditor for which an identification by scheme is specified. | CreditorRole | SchemeIdentification |
| Scheme | InformationPartyRole | NaN | Role played by a party as source of a scheme code. | InformationPartyRole | Scheme |
| Scheme | Version | NaN | Version number of the scheme. | Max35Text | NaN |
| Scheme | AssessmentValidityPeriod | NaN | Period during which the version of the scheme applies (see ISO-8601). | DateTimePeriod | AssessmentValidityScheme |
| Scheme | NameLong | NaN | Long textual description of the scheme. | Max70Text | NaN |
| Scheme | Description | NaN | Textual description of the scheme. | Max350Text | NaN |
| Scheme | DomainValueCode | NaN | Code for a specific instance of an entry within the enumerated list, for example, ISIN. | Max35Text | NaN |
| Scheme | DomainValueName | NaN | Textual description of the DomainValueCode, for example, International Securities Identification Number. | Max70Text | NaN |
| Scheme | Sector | NaN | Specifies the sector to which the scheme applies. | Sector | Scheme |
| Scheme | AssetClassification | NaN | Asset for which a classification by scheme is specified. | AssetClassification | AssetClassScheme |
| DateTimePeriod | NaN | NaN | Time span defined by a start date and time, and an end date and time. | NaN | NaN |
| DateTimePeriod | FromDateTime | NaN | Date and time at which the range starts. | ISODateTime | NaN |
| DateTimePeriod | ToDateTime | NaN | Date and time at which the range ends. | ISODateTime | NaN |
| DateTimePeriod | RelatedStandingOrder | NaN | Standing order for which a validity period is specified. | StandingOrder | ValidityPeriod |
| DateTimePeriod | PaymentInstruction | NaN | Payment instruction for which a processing validity time is specified. | PaymentInstruction | ProcessingValidityTime |
| DateTimePeriod | NumberOfDays | NaN | Period specified as a number of days. | Number | NaN |
| DateTimePeriod | ValuationStatistics | NaN | Valuation statistics for which a reference period is specified. | ValuationStatistics | Period |
| DateTimePeriod | PerformanceFactors | NaN | Performance factors for which an accumulation period is specified. | PerformanceFactors | AccumulationPeriod |
| DateTimePeriod | Status | NaN | Status for which a validity time is specified. | Status | ValidityTime |
| DateTimePeriod | PriceCalculationRelatedPricing | NaN | Securities pricing for which a price calculation period is specified. | SecuritiesPricing | PriceCalculationPeriod |
| DateTimePeriod | CorporateActionOption | NaN | Corporate action option for which an action period is defined. | CorporateActionOption | ActionPeriod |
| DateTimePeriod | ParallelTradingProceedsDefinition | NaN | Securities proceeds for which a parallel trading period is specified. | SecuritiesProceedsDefinition | ParallelTradingPeriod |
| DateTimePeriod | PrivilegeSuspensionCorporateAction | NaN | Corporate event for which a privilege suspension period has been defined. | SuspensionPeriod | PrivilegeSuspensionPeriod |
| DateTimePeriod | WithdrawalSuspensionRelatedEvent | NaN | Corporate event for which a suspension period for withdrawals is specified. | SuspensionPeriod | DepositorySuspensionPeriodForWithdrawal |
| DateTimePeriod | RelatedInterestCalculation | NaN | Interest calculation process for which an interest period is specified. | InterestCalculation | InterestPeriod |
| DateTimePeriod | BiddingConditions | NaN | Bidding conditions for which a compulsory purchase period is specified. | BiddingConditions | CompulsoryPurchasePeriod |
| DateTimePeriod | ClassAction | NaN | Class action for which a claim period is specified. | ClassAction | ClaimPeriod |
| DateTimePeriod | BookEntryTransferSuspensionRelatedEvent | NaN | Corporate event for which a suspension period for book entry transfers is specified. | SuspensionPeriod | DepositorySuspensionPeriodForBookEntryTransfer |
| DateTimePeriod | DepositAtAgentSuspensionRelatedEvent | NaN | Corporate event for which a suspension period for deposits at agent is specified. | SuspensionPeriod | DepositorySuspensionPeriodForDepositAtAgent |
| DateTimePeriod | DepositSuspensionRelatedEvent | NaN | Corporate event for which a suspension period for deposits is specified. | SuspensionPeriod | DepositorySuspensionPeriodForDeposit |
| DateTimePeriod | PledgeSuspensionRelatedEvent | NaN | Corporate event for which a suspension period for pledges is specified. | SuspensionPeriod | DepositorySuspensionPeriodForPledge |
| DateTimePeriod | SegregationPeriodRelatedEvent | NaN | Corporate event for which a suspension period for segregation is specified. | SuspensionPeriod | DepositorySuspensionPeriodForSegregation |
| DateTimePeriod | WithdrawalAtAgentSuspensionRelatedEvent | NaN | Corporate event for which a suspension period for withdrawals at agent is specified. | SuspensionPeriod | DepositorySuspensionPeriodForWithdrawalAtAgent |
| DateTimePeriod | WithdrawalInNomineeNameSuspensionRelatedEvent | NaN | Corporate event for which a suspension period for withdrawals in nominee name is specified. | SuspensionPeriod | DepositorySuspensionPeriodForWithdrawalInNomineeName |
| DateTimePeriod | WithdrawalInStreetNameSuspensionRelatedEvent | NaN | Corporate event for which a suspension period for withdrawals in street name is specified. | SuspensionPeriod | DepositorySuspensionPeriodForWithdrawalInStreetName |
| DateTimePeriod | BookClosureCorporateAction | NaN | Corporate action for which a book closure period has been specified. | CorporateActionEvent | BookClosurePeriod |
| DateTimePeriod | CoDepositoriesSuspensionRelatedEvent | NaN | Corporate event for which a suspension period for co-depositories is specified. | SuspensionPeriod | CoDepositoriesSuspensionPeriod |
| DateTimePeriod | ExtendiblePeriodDebt | NaN | Debt for which an extendible period is specified. | Debt | ExtendiblePeriod |
| DateTimePeriod | SecuritiesConversion | NaN | Securities conversion process for which a conversion period is specified. | SecuritiesConversion | ConversionPeriod |
| DateTimePeriod | YieldCalculation | NaN | Yield calculation for which a value period is specified. | YieldCalculation | ValuePeriod |
| DateTimePeriod | CustomDateDebt | NaN | Debt for which a custom date is specified. | Debt | CustomDate |
| DateTimePeriod | TaxPeriod | NaN | Tax period for which a from/to date is specified. | TaxPeriod | FromToDate |
| DateTimePeriod | Account | NaN | Account for which a reported period is specified. | Account | ReportedPeriod |
| DateTimePeriod | RelatedAgreement | NaN | Agreement for which a validity period is specified. | Agreement | ValidityPeriod |
| DateTimePeriod | AssentedLinePeriodProceedsDefinition | NaN | Securities proceeds for which an assented line period is specified. | SecuritiesProceedsDefinition | AssentedLinePeriod |
| DateTimePeriod | SellThruIssuerProceedsDefinition | NaN | Securities proceeds for which a sell thru issuer period is specified. | SecuritiesProceedsDefinition | SellThruIssuerPeriod |
| DateTimePeriod | RelatedProductDelivery | NaN | Trade delivery process for which a delivery period is specified. | ProductDelivery | DeliveryPeriod |
| DateTimePeriod | RelatedInvoice | NaN | Invoice for which a period is specified. | Invoice | PeriodCovered |
| DateTimePeriod | TradeCertificate | NaN | Trade certificate for which an inspection date is specified. | TradeCertificate | InspectionDate |
| DateTimePeriod | RelatedPortfolioValuation | NaN | Portfolio valuation process for which a valuation period is specified. | PortfolioValuation | ValuationPeriod |
| DateTimePeriod | System | NaN | System for which a validity period is specified. | System | VersionValidityPeriod |
| DateTimePeriod | AccountRestriction | NaN | Account restriction for which a validity period is specified. | AccountRestriction | ValidityPeriod |
| DateTimePeriod | BankOperation | NaN | Bank operation for which an applicable period is specified. | BankOperation | ApplicablePeriod |
| DateTimePeriod | RelatedCorporateAction | NaN | Corporate action event for which a trading period is specified. | CorporateActionEvent | TradingPeriod |
| DateTimePeriod | RelatedLimit | NaN | Limit for which a validity period is specified. | Limit | ValidityPeriod |
| DateTimePeriod | RelatedIdentification | NaN | Party identification for which a validity period is specified. | PartyIdentificationInformation | ValidityPeriod |
| DateTimePeriod | AssessmentValidityScheme | NaN | Scheme for which a validity period is specified. | Scheme | AssessmentValidityPeriod |
| DateTimePeriod | ExercisePeriodDistribution | NaN | Cash and securities distribution information for which an exercise period is specified. | Distribution | ExercisePeriod |
| DateTimePeriod | OfferPeriodDistribution | NaN | Cash and securities distribution information for which an offer period is specified. | Distribution | OfferPeriod |
| DateTimePeriod | TradingPeriodDistribution | NaN | Cash and securities distribution information for which a trading period is specified. | Distribution | TradingPeriod |
| DateTimePeriod | BlockingPeriodDistribution | NaN | Cash and securities distribution information for which a blocking period is specified. | Distribution | BlockingPeriod |
| DateTimePeriod | Guarantee | NaN | Guarantee for which an effective period is specified. | Guarantee | EffectivePeriod |
| DateTimePeriod | PriceFactRelatedPricing | NaN | Securities pricing for which a price fact period is specified. | SecuritiesPricing | PriceFactPeriod |
| DateTimePeriod | CashDistribution | NaN | Cash distribution for which an interest period is specified. | Distribution | InterestPeriod |
| DateTimePeriod | ComponentSecurity | NaN | Security component for which a separation period is specified. | ComponentSecurity | SeparationPeriod |
| DateTimePeriod | TradingSession | NaN | Trading session for which a time bracket is specified. | TradingSession | TimeBracket |
| DateTimePeriod | FinancialInstrumentSwap | NaN | Swap for which a maturity period is specified. | FinancialInstrumentSwap | Maturity |
| DateTimePeriod | RelatedPostalAddress | NaN | Postal address for which a validity period is specified. | PostalAddress | ValidityPeriod |
| DateTimePeriod | RedemptionSchedule | NaN | Redemption schedule for which a notice period is provided. | RedemptionSchedule | EffectivePeriod |
| DateTimePeriod | RelatedAccountLink | NaN | Link between two accounts for which a validity period is specified. | AccountLink | ValidityPeriod |
| DateTimePeriod | RelatedAdjustment | NaN | Adjustment for which a validity period is provided. | Adjustment | EffectivePeriod |
| DateTimePeriod | RelatedSecuritiesIdentification | NaN | Securities identification for which a validity period is specified. | SecuritiesIdentification | ValidityPeriod |
| DateTimePeriod | RelatedStandingSettlementInstruction | NaN | SSI for which a validity period is specified. | StandingSettlementInstruction | ValidityPeriod |
| DateTimePeriod | RelatedSecuritiesRegistration | NaN | Securities registration process for which a split period is specified. | BasicSecuritiesRegistration | SplitPeriod |
| DateTimePeriod | Amount | NaN | Relationship with an amount. | AmountAndPeriod | Period |
| DateTimePeriod | RelatedInvestmentPlan | NaN | InvestmentPlan for which an investment period is specified. | InvestmentPlan | InvestmentPeriod |
| DateTimePeriod | Issuance | NaN | Issuance for which subscription information is provided. | Issuance | SubscriptionPeriod |
| DateTimePeriod | RelatedPaymentTerms | NaN | Payment terms for which a period is specified. | PaymentTerms | PaymentPeriod |
| DateTimePeriod | Percentage | NaN | Relationship with a percentage. | PercentageAndPeriod | Period |
| DateTimePeriod | RelatedRolePlayer | NaN | Role player for which a validity period is specified. | RolePlayer | ValidityPeriod |
| DateTimePeriod | RelatedSystemAvailability | NaN | System availability for which the closure period is provided. | SystemAvailability | ClosurePeriod |
| SecuritiesAccount | NaN | Account | Account to or from which a securities entry is made. | NaN | NaN |
| SecuritiesAccount | SecuritiesAccountType | NaN | Specifies the type of securities account. | SecuritiesAccountPurposeTypeCode | NaN |
| SecuritiesAccount | RelatedInvestmentAccount | NaN | Investment account which contains a securities account to make securities movements. | InvestmentAccount | SecuritiesAccount |
| SecuritiesAccount | RelatedTransfer | NaN | Specifies the process which moves securities out of an account to another one. | SecuritiesTransfer | Account |
| SecuritiesAccount | SecuritiesPartyRole | NaN | Specifies the role which uses a securities account. | SecuritiesPartyRole | SecuritiesAccount |
| SecuritiesAccount | Security | NaN | Security which is held on the securities account. | Security | SecuritiesAccount |
| SecuritiesAccount | RelatedRegistrar | NaN | Specifies where the financial instruments are registered. | RegistrarRole | RegistrarAccount |
| SecuritiesAccount | SafekeepingPlace | NaN | Location where the financial instruments are safekept. | SafekeepingPlace | RelatedSecuritiesAccount |
| SecuritiesAccount | SecuritiesBalance | NaN | Value of financial assets held by a person or an organisation. It is derived from the association between Account and Balance. | SecuritiesBalance | SecuritiesAccount |
| SecuritiesAccount | CorporateActionServicing | NaN | Actions taken in relation with the securities account in the context of the corporate action. | CorporateActionServicing | SecuritiesAccount |
| SecuritiesAccount | RelatedAllocation | NaN | Allocation process for which an account is specified. | Allocation | AllocationAccount |
| SecuritiesAccount | SecuritiesEntry | NaN | Record of the movements into or out of an account. | SecuritiesEntry | SecuritiesAccount |
| SecuritiesAccount | ClearingAccountOwner | NaN | Clearing member which holds a clearing account at a CCP. | ClearingMemberRole | ClearingAccount |
| SecuritiesAccount | MarginAccountOwner | NaN | Clearing member which holds a margin account at a CCP. | ClearingMemberRole | MarginAccount |
| SecuritiesAccount | DeliveryAccountOwner | NaN | Clearing member which holds a delivery account at a CCP. | ClearingMemberRole | DeliveryAccount |
| SecuritiesAccount | RelatedPowerOfAttorney | NaN | Power of attorney related to the securities account. | PowerOfAttorney | AuthorisedAccount |
| SecuritiesAccount | RelatedMeetingInstruction | NaN | Meeting instruction which specifies an account. | InstructionForMeeting | SafekeepingAccount |
| SecuritiesAccount | ClearingAccountType | NaN | Specifies the clearing account type. | ClearingAccountTypeCode | NaN |
| SecuritiesAccount | RelatedOrder | NaN | Order process for which an ordering account is specified. | SecuritiesOrder | OrderingAccount |
| SecuritiesAccount | DisclosedListTrading | NaN | Disclosed list trading process for which a trading account is specified. | DisclosedListTrading | DisclosedListTradingAccount |
| SecuritiesAccount | AccountLink | NaN | Defines the link between a cash account and a securities account. | AccountLink | SecuritiesAccount |
| AccountPartyRole | NaN | Role | Role played by a party in the context of account operations. | NaN | NaN |
| AccountPartyRole | Account | NaN | Identifies the account for which a party plays a role. | Account | PartyRole |
| AccountOwnerRole | NaN | AccountPartyRole | Party that legally owns the account. | NaN | NaN |
| Product | NaN | NaN | Item that is offered for sale. Products can be services or goods. | NaN | NaN |
| Product | CardPayment | NaN | Card payment for which a product was specified. | CardPayment | Product |
| Product | UnitPrice | NaN | Price per unit of product. | Price | UnitPriceProduct |
| Product | ProductCategory | NaN | Category of the product. | ProductCategory | Product |
| Product | LineItem | NaN | Specifies the line item in which the product is specified. | LineItem | InvoicedProduct |
| Product | ProductIdentification | NaN | Identification of the product. | ProductIdentification | Product |
| Product | Name | NaN | Name of a product. | Max35Text | NaN |
| Product | Description | NaN | Information about the goods and/or services of a trade transaction. | Max140Text | NaN |
| Product | Origin | NaN | Country from which the product originates. | Country | ProducedProducts |
| Product | Characteristics | NaN | Characteristics of the product. | ProductCharacteristics | Product |
| Product | NetPrice | NaN | Net price of the goods and/or service. | Price | NetPriceProduct |
| Product | Quantity | NaN | Specifies the quantity of the product. | ProductQuantity | Product |
| Product | GrossPrice | NaN | Gross price of the goods and/or service. | Price | GrossPriceProduct |
| Product | Quality | NaN | Quality of the product. | Max70Text | NaN |
| Product | Delivery | NaN | Delivery process of a product | ProductDelivery | Product |
| Product | PurchaseOrder | NaN | Specifies the purchase order in which a specific product is ordered. | PurchaseOrder | Product |
| Product | Tax | NaN | Amount of money due to the government or tax authority, according to various pre-defined parameters linked to the value of the goods and services in a trade transaction. | Tax | Product |
| Service | NaN | Product | Service is the intangible equivalent of a good. | NaN | NaN |
| Service | Amount | NaN | Amount charged for the service. | CurrencyAndAmount | NaN |
| Service | Type | NaN | Type used to classify and organise different services. | Max35Text | NaN |
| Service | TaxDesignation | NaN | Identifies the taxable status of the service. | ServiceTaxDesignationCode | NaN |
| Service | Rate | NaN | Rate applied on a basis amount to calculate the service charge. | PercentageRate | NaN |
| AccountService | NaN | FinancialService | Services linked to an account which are available to the account owner or to the holder of a mandate. | NaN | NaN |
| AccountService | AccountContract | NaN | Account contract which specifies the services linked to an account. | AccountContract | AccountService |
| AccountService | Reservation | NaN | Reservation information included in the services related to an account. | Reservation | AccountService |
| AccountService | Account | NaN | Account for which services are specified. | Account | AccountService |
| AccountService | AccountAdministrationCharge | NaN | Charge applied for the administration of an account. | Charges | Services |
| ReportingService | NaN | AccountService | Specifies the reporting parameters that are included in the account contract which specifies the services linked to the account.. | NaN | NaN |
| ReportingService | StatementFrequency | NaN | Specifies the frequency at which a statement must be created by the account servicer. | FrequencyCode | NaN |
| ReportingService | FloorNotificationAmount | NaN | Specifies the balance amount of an account under which a notification should be sent from the account servicer to the account owner. | CurrencyAndAmount | NaN |
| ReportingService | CeilingNotificationAmount | NaN | Specifies the balance amount of an account above which a notification should be sent from the account servicer to the account owner. | CurrencyAndAmount | NaN |
| ReportingService | ReportingChannel | NaN | Specifies the channel through which the statement must be made available to the account owner or to the information recipient. | ContactPoint | RelatedReportingService |
| ReportingService | RelatedInvestmentAccountService | NaN | Investment account services which include reporting services. | InvestmentAccountService | ReportingService |
| InvestmentAccount | NaN | Account | Account between an investor(s) and a fund manager or a fund. The account can contain holdings in any investment fund or investment fund class managed (or distributed) by the fund manager, within the same fund family. | NaN | NaN |
| InvestmentAccount | InvestmentAccountType | NaN | Purpose of the account/source fund type. This is typically linked to an investment product, eg, wrapper, PEP, ISA. | FundCashAccountCode | NaN |
| InvestmentAccount | OwnershipType | NaN | Ownership status of the account, eg, joint owners. | AccountOwnershipTypeCode | NaN |
| InvestmentAccount | Designation | NaN | Supplementary registration information applying to a specific block of units for dealing and reporting purposes. The supplementary registration information may be used when all the units are registered, for example, to a funds supermarket, but holdings for each investor have to be reconciled individually. | Max70Text | NaN |
| InvestmentAccount | ReferenceCurrency | NaN | Currency chosen for reporting purposes by the account owner in agreement with the account servicer. | CurrencyCode | NaN |
| InvestmentAccount | InvestmentFundClass | NaN | Investment fund classes held in an investment account. | InvestmentFundClass | InvestmentAccount |
| InvestmentAccount | CashAccount | NaN | Part of the investment account to or from which cash entries are made. | CashAccount | RelatedInvestmentAccount |
| InvestmentAccount | SecuritiesAccount | NaN | Part of the investment account to or from which securities entries are made. | SecuritiesAccount | RelatedInvestmentAccount |
| InvestmentAccount | InvestmentFundTax | NaN | Taxes specific to the account. | InvestmentFundTax | InvestmentAccount |
| InvestmentAccount | InvestmentFundTransaction | NaN | Investment fund transaction which uses the investment account. | InvestmentFundTransaction | InvestmentAccount |
| InvestmentAccount | SidePocket | NaN | Separate account containing illiquid assets of a hedge fund portfolio. | SidePocket | InvestmentAccount |
| InvestmentAccount | InvestmentAccountPartyRole | NaN | Specifies each role linked to an investment account and played by a party in that context. | InvestmentAccountPartyRole | InvestmentAccount |
| InvestmentAccount | DebitPortfolioTransfer | NaN | Transfer process for which a debit investment account is specified. | PortfolioTransfer | AccountFrom |
| InvestmentAccount | CreditPortfolioTransfer | NaN | Transfer process for which a beneficiary investment account is specified. | PortfolioTransfer | AccountTo |
| InvestmentAccount | AccountForInvestmentFundProcessing | NaN | Order desk for which an account is specified. | FundOrderDesk | MainFundOrderDeskAccount |
| InvestmentAccount | InvestmentAccountContract | NaN | Contract defining the related account | InvestmentAccountContract | InvestmentAccount |
| InvestmentAccount | AccountUsageType | NaN | Specifies whether the account is used for investment or for settlement purpose. | AccountUsageTypeCode | NaN |
| InvestmentAccount | Category | NaN | Specifies the investment account category. | InvestmentAccountCategoryCode | NaN |
| InvestmentAccount | Portfolio | NaN | Portfolio held on an account. | Portfolio | Account |
| InvestmentAccount | RelatedPortfolioTransfer | NaN | Transfer of a portfolio held on a nominee account. | PortfolioTransfer | NomineeAccount |
| InvestmentAccount | UsufructPercentage | NaN | Percentage of usufruct that a person has on an asset. | PercentageRate | NaN |
| InvestmentAccount | OwnershipPercentage | NaN | Percentage of ownership that a person has on an asset. | PercentageRate | NaN |
| Tax | NaN | NaN | Amount of money due to the government or tax authority, according to various pre-defined parameters such as thresholds or income. | NaN | NaN |
| Tax | ExemptionReason | NaN | Reason for a tax exemption. | TaxExemptReasonCode | NaN |
| Tax | Country | NaN | Place of taxation of an individual person or an organisation, where the tax is due. | Country | Tax |
| Tax | TaxLiabilityValueCalculation | NaN | Net asset value calculation for which tax liability information is provided. | NetAssetValueCalculation | TaxLiability |
| Tax | Type | NaN | Type of tax applied. | TaxTypeCode | NaN |
| Tax | Amount | NaN | Amount of money resulting from the calculation of the tax. | CurrencyAndAmount | NaN |
| Tax | Rate | NaN | Rate used for calculation of the tax. | PercentageRate | NaN |
| Tax | TaxableParty | NaN | Party which is taxable at a specific location | Party | TaxationConditions |
| Tax | TaxRefundValueCalculation | NaN | Net asset value calculation for which tax refund information is provided. | NetAssetValueCalculation | TaxRefund |
| Tax | Basis | NaN | Basis used to determine the capital gain or loss, eg, the purchase price. | TaxationBasisCode | NaN |
| Tax | SecuritiesTransfer | NaN | Transfer process for which a tax is specified. | SecuritiesTransfer | TransferTax |
| Tax | TaxRateType | NaN | Specifies the type of tax rate. | RateTypeCode | NaN |
| Tax | TaxAccount | NaN | Account to be used for taxes. | CashAccount | Tax |
| Tax | TaxationConditions | NaN | Specifies other taxation conditions. | Max350Text | NaN |
| Tax | Adjustment | NaN | Specifies the adjustments subject to a tax. | Adjustment | Tax |
| Tax | Interest | NaN | Interest for which a tax is specified. | Interest | InterestTax |
| Tax | Identification | NaN | Reference used to identify the nature of tax levied, such as Value Added Tax (VAT). | Max35Text | NaN |
| Tax | RelatedPaymentSettlement | NaN | Payment to which the tax applies. | Payment | TaxOnPayment |
| Tax | TaxableBaseAmount | NaN | Amount of money on which the tax is based. | CurrencyAndAmount | NaN |
| Tax | TaxDate | NaN | Date by which tax is due. | ISODate | NaN |
| Tax | CertificateIdentification | NaN | Document issued by taxing authority identifying the tax payer. | Max35Text | NaN |
| Tax | AdministrationZone | NaN | Territorial part of a country to which the tax payment is related. | Max140Text | NaN |
| Tax | Method | NaN | Method used to indicate the underlying business or how the tax is paid. | Max35Text | NaN |
| Tax | Record | NaN | Record of tax details. | TaxRecord | Tax |
| Tax | Product | NaN | Product on which a tax is applied. | Product | Tax |
| Tax | CurrencyExchange | NaN | Currency exchange applicable to a tax | CurrencyExchange | Tax |
| Tax | Currency | NaN | Currency in which the tax must be settled. | CurrencyCode | NaN |
| Tax | PartyRole | NaN | Specifies each role linked to a tax and played by a party in that context. | TaxPartyRole | Tax |
| Tax | TaxDeduction | NaN | Amount of tax that have been previously deducted. | CurrencyAndAmount | NaN |
| Tax | RelatedCorporateActionDistribution | NaN | Distribution process for which a tax is specified. | Distribution | DistributionTax |
| Tax | CalculationDate | NaN | Date on which the tax is calculated. | ISODate | NaN |
| Tax | Dividend | NaN | Dividend for which a tax is specified. | Dividend | Tax |
| Tax | WithholdingTaxType | NaN | Type of withholding tax rate. | WithholdingTaxRateTypeCode | NaN |
| Tax | CorporateActionEvent | NaN | Event for which a transaction tax is specified. | CorporateActionEvent | TransactionTax |
| Tax | TaxIdentificationType | NaN | Type of tax identification number or identifier. | TaxIdentificationNumberTypeCode | NaN |
| Tax | TaxRateMarker | NaN | Specifies the rate of tax levied. | TaxRateMarkerCode | NaN |
| InvestmentAccountService | NaN | AccountService | Services linked to an account which are available to the account owner or to the holder of a mandate. The exercise of these services may be submitted to a limit. | NaN | NaN |
| InvestmentAccountService | IncomePreference | NaN | Dividend option chosen by the account owner based on the options offered in the prospectus. | IncomePreferenceCode | NaN |
| InvestmentAccountService | TaxWithholdingMethod | NaN | Method by which the tax (withholding tax) is to be processed i.e. either withheld at source or tax information reported to tax authorities or tax information is reported due to the provision of a tax certificate. | TaxWithholdingMethodCode | NaN |
| InvestmentAccountService | RoundingMethod | NaN | Rounding method used to determine the quantity of investment fund units. | RoundingParameters | InvestmentAccountService |
| InvestmentAccountService | BeneficiaryCertificationIndicator | NaN | Indicates whether the beneficial ownership certification has been sent, certifying that the beneficial owner is eligible to own a specific investment fund or investment fund class. | YesNoIndicator | NaN |
| InvestmentAccountService | BeneficiaryCertificationCompletion | NaN | Beneficial owner or its designated agent certifies that it complies with any holding or investment restrictions or requirements of the fund. | BeneficiaryCertificationCompletionCode | NaN |
| InvestmentAccountService | SystematicInvestmentPlan | NaN | Investment plan associated with an investment account. | InvestmentPlan | RelatedService |
| InvestmentAccountService | InvestmentAccountContract | NaN | Contract which specifies the services related to an account. | InvestmentAccountContract | Services |
| InvestmentAccountService | ReportingService | NaN | Reporting services parameters for an investment account. | ReportingService | RelatedInvestmentAccountService |
| InvestmentAccountService | Reinvestment | NaN | Reinvestment information included in the investment account contract. | Reinvestment | RelatedinvestmentAccountService |
| Status | NaN | NaN | The status of an instruction, advice or request. | NaN | NaN |
| Status | StatusReason | NaN | Specifies the reasons for the status. | StatusReason | Status |
| Status | StatusDateTime | NaN | Date and time at which the status was assigned. | ISODateTime | NaN |
| Status | ValidityTime | NaN | Period of time during which the status is valid. | DateTimePeriod | Status |
| Status | StatusDescription | NaN | Specifies the state or the condition. | Max350Text | NaN |
| Status | InstructionProcessingStatus | NaN | Status of the processing of an instruction. | StatusCode | NaN |
| Status | PartyRole | NaN | Role played by a party in the context of assigning a status. | InvestigationPartyRole | Status |
| Status | SettlementStatus | NaN | Status of settlement of a transaction. | SecuritiesSettlementStatusCode | NaN |
| Status | CancellationProcessingStatus | NaN | Specifies the status of a cancellation request. | CancellationProcessingStatusCode | NaN |
| Status | TransactionProcessingStatus | NaN | Status of processing of a transaction at account servicer level. | InstructionProcessingStatusCode | NaN |
| Status | ModificationProcessingStatus | NaN | Provides the status of a modification request. | ModificationProcessingStatusCode | NaN |
| AccountStatus | NaN | Status | Specifies the status of an account or the status of the processing of the actions linked to the management of an account. | NaN | NaN |
| AccountStatus | Account | NaN | Identifies the account for which a status is provided. | Account | Status |
| AccountStatus | Status | NaN | Specifies the status of an account. | AccountStatusCode | NaN |
| AccountStatus | Blocked | NaN | Indicates whether the account is blocked. | YesNoIndicator | NaN |
| AccountStatus | ManagementStatus | NaN | Specifies the status of the processing of a request linked to the management of an account. | AccountManagementStatusCode | NaN |
| AccountStatus | EntryStatus | NaN | Status of an entry on the books of the account servicer. | EntryStatusCode | NaN |
| AccountStatus | BalanceStatus | NaN | Current status of a cash balance. | BalanceStatusCode | NaN |
| AccountStatus | BlockedReason | NaN | Specifies the different reasons for which the account is blocked. | ReasonBlockedCode | NaN |
| Agreement | NaN | NaN | Contractual details related to an agreement between parties. | NaN | NaN |
| Agreement | DateSigned | NaN | Date on which the agreement was signed by all parties. | ISODate | NaN |
| Agreement | Description | NaN | Full name of an agreement, annexes and amendments in place between the principals. | Max350Text | NaN |
| Agreement | Version | NaN | Version number of a contract or of a legal agreement. | Max35Text | NaN |
| Agreement | ValidityPeriod | NaN | Period during which the agreement is valid | DateTimePeriod | RelatedAgreement |
| Agreement | Document | NaN | Document which materialises the agreement. | Document | Agreement |
| Agreement | Trade | NaN | Specifies the type of trade that is the subject of an agreement. The agreement contains the clauses that will govern each trade between the signing parties. | CommercialTrade | Agreement |
| Agreement | Jurisdiction | NaN | Jurisdiction where an agreement applies. | Jurisdiction | RelatedAgreement |
| Contract | NaN | Agreement | Document that contains the information of the contract agreed between both parties. | NaN | NaN |
| Contract | MasterAgreement | NaN | Agreement that governs a contract agreed between parties. | MasterAgreement | GovernedContract |
| AccountContract | NaN | Contract | Agreement between an account servicer and an account owner about the services linked to an account. | NaN | NaN |
| AccountContract | TargetClosingDate | NaN | Date on which the account and related services are expected to cease to be operational for the account owner. | ISODateTime | NaN |
| AccountContract | UrgencyFlag | NaN | Indicator that the change to the contract needs to be treated urgently. | TrueFalseIndicator | NaN |
| AccountContract | RemovalIndicator | NaN | Indicates removal of the account. After removal, an account will not appear anymore in reports. | YesNoIndicator | NaN |
| AccountContract | TargetGoLiveDate | NaN | Date on which the account and related services are expected to cease/to be operational for the account owner. | ISODateTime | NaN |
| AccountContract | AccountService | NaN | Operations on a bank account that are allowed as part of the services offered to the owners of a bank account, | AccountService | AccountContract |
| AccountContract | Account | NaN | Specifies the account which is managed by a contract. | Account | AccountContract |
| AccountContract | Interest | NaN | Interest that applies to the account. | Interest | RelatedAccountContract |
| AccountContract | RequestDate | NaN | Date of the request. | ISODateTime | NaN |
| AccountContract | AccountAuthorisation | NaN | Specifies the services which are assigned to another party. | Mandate | AccountContract |
| AccountContract | TransactionChannel | NaN | Specifies the means by which the account owner submits the open account form. | TransactionChannelCode | NaN |
| InvestmentAccountContract | NaN | AccountContract | Contract defining the related investment account. | NaN | NaN |
| InvestmentAccountContract | LetterIntentReference | NaN | Reference of a letter of intent program, in which sales commissions are reduced based on the aggregate of a customer's actual purchase and anticipated purchases, over a specific period of time, and as agreed by the customer. A letter of intent program is mainly used in the US market. | Max35Text | NaN |
| InvestmentAccountContract | AccumulationRightReference | NaN | Reference of an accumulation rights program, in which sales commissions are based on a customer's present purchases of shares and the aggregate quantity previously purchased by the customer. An accumulation rights program is mainly used in the US market. | Max35Text | NaN |
| InvestmentAccountContract | InvestmentAccount | NaN | Specifies the account for which the service is offered. | InvestmentAccount | InvestmentAccountContract |
| InvestmentAccountContract | Services | NaN | Services linked to an account which are available to the account owner or to the holder of a mandate. The exercise of these services may be submitted to a limit. | InvestmentAccountService | InvestmentAccountContract |
| InvestmentAccountContract | ModeledAccount | NaN | Product which provides guidance to investors to manage their portfolios. | ManagedAccountProduct | InvestmentAccountContract |
| SignatureCondition | NaN | NaN | Specifies the signature requirements for managing an account. | NaN | NaN |
| SignatureCondition | RequiredSignatureNumber | NaN | Number of account owners or related parties required to authorise transactions on the account. | Number | NaN |
| SignatureCondition | SignatoryRightIndicator | NaN | Indicates whether the signature of the account owner is required to authorise transactions on the account. | YesNoIndicator | NaN |
| SignatureCondition | Mandate | NaN | Mandate for which signature conditions are provided. | Mandate | SignatureConditions |
| SignatureCondition | SignatureOrderIndicator | NaN | Indicator whether a certain order of signatures has to be respected or not. | TrueFalseIndicator | NaN |
| SignatureCondition | SignatureOrder | NaN | Indicates the order in which the mandate holders are allowed to sign. | Max15PlusSignedNumericText | NaN |
| SignatureCondition | Signature | NaN | Manual or digital signature added as security provision by each party involved in the business covered by the document. | Signature | Conditions |
| InvestmentFundFamily | NaN | NaN | Group of investment funds under the same fund management company. | NaN | NaN |
| InvestmentFundFamily | FundFamilyName | NaN | Name of the investment fund family. | Max350Text | NaN |
| InvestmentFundFamily | InvestmentFund | NaN | Pool of financial instruments managed by a professional asset manager and belonging to one or several investment fund families that are part of the same investment fund network. | InvestmentFund | Family |
| RoundingParameters | NaN | NaN | Parameters applied to a fractional number. | NaN | NaN |
| RoundingParameters | InvestmentAccountService | NaN | Investment account services for which rounding parameters are specified. | InvestmentAccountService | RoundingMethod |
| RoundingParameters | RoundingModulus | NaN | Float value specifying the value to which rounding is required, eg, 10 means round to a multiple of 10 units/shares, 0.5 means round to a multiple of 0.5 units/shares. | DecimalNumber | NaN |
| RoundingParameters | RoundingDirection | NaN | Rounding direction applied to fractional numbers, eg, round up. | RoundingDirectionCode | NaN |
| RoundingParameters | RelatedPegOrderInstruction | NaN | Peg order for which a rounding direction is provided. | SecuritiesPegOrderInstruction | RoundDirection |
| InvestmentAccountPartyRole | NaN | AccountPartyRole | Specifies roles played by a party that are related to an investment account. | NaN | NaN |
| InvestmentAccountPartyRole | OwnershipBeneficiaryRate | NaN | Percentage of ownership or of beneficial ownership of the shares/units in the account. All subsequent subscriptions and or redemptions will be allocated using the same percentage. | PercentageRate | NaN |
| InvestmentAccountPartyRole | InvestmentAccount | NaN | Specifies the account for which the party plays a role. It is derived from the association between AccountPartyRole and Account. | InvestmentAccount | InvestmentAccountPartyRole |
| InvestmentAccountPartyRole | FATCAFormType | NaN | Type of Foreign Account Tax Compliance Act (FATCA) form submitted by the investor. | FATCAFormTypeCode | NaN |
| InvestmentAccountPartyRole | FATCAStatus | NaN | Foreign Account Tax Compliance Act (FATCA) status of the investor. | FATCAStatus | InvestmentAccountParty |
| InvestmentAccountPartyRole | CRSStatus | NaN | Common Reporting Standard (CRS) status of the investor. | CRSStatus | InvestmentAccountParty |
| PrimaryOwner | NaN | InvestmentAccountPartyRole | Single owner of the investment account or, when the ownership is split among several owners, the primary owner is the one giving its address and account details for the registration. | NaN | NaN |
| OrganisationName | NaN | PartyName | Name by which an organisation is known and which is usually used to identify that organisation. | NaN | NaN |
| OrganisationName | Organisation | NaN | Organisation identification which contains a name. | OrganisationIdentification | OrganisationName |
| OrganisationName | LegalName | NaN | Official name under which an organisation is registered. | Max35Text | NaN |
| OrganisationName | TradingName | NaN | Name used by a business for commercial purposes, although its registered legal name, used for contracts and other formal situations, may be another. | Max350Text | NaN |
| OrganisationName | ShortName | NaN | Specifies the short name of the organisation. | Max35Text | NaN |
| MailingInstructions | NaN | NaN | Characteristics of an address. | NaN | NaN |
| MailingInstructions | MailingIndicator | NaN | Indicates whether mail should be sent to an address. | YesNoIndicator | NaN |
| MailingInstructions | RegistrationAddressIndicator | NaN | Indicates whether the address is the official address of the party. | YesNoIndicator | NaN |
| MailingInstructions | RelatedPostalAddress | NaN | Postal address for which mailing instructions are specified. | PostalAddress | MailingInstructions |
| Person | NaN | Party | Human entity, as distinguished from a corporate entity (which is sometimes referred to as an 'artificial person'). | NaN | NaN |
| Person | Gender | NaN | Specifies the gender of the person. | GenderCode | NaN |
| Person | Language | NaN | Language in which a person communicates. | LanguageCode | NaN |
| Person | BirthDate | NaN | Date on which a person is born. | ISODateTime | NaN |
| Person | PlaceOfBirth | NaN | Place (for instance Country and City) where a person was born. | Location | NativePerson |
| Person | Profession | NaN | Name of the occupation or job of a person. | Max35Text | NaN |
| Person | ResidentialStatus | NaN | Residential status of an individual, for example, non-permanent resident. | ResidentialStatusCode | NaN |
| Person | Nationality | NaN | Specifies the country where a person was born or is legally accepted as belonging to the country. | Country | Citizen |
| Person | MinorIndicator | NaN | Indicates whether the person is a legal minor. It may depend on the nationality, the domicile country or the transaction in which the person is involved. | YesNoIndicator | NaN |
| Person | BusinessFunctionTitle | NaN | Title of the function in an organisation. | Max35Text | NaN |
| Person | PersonIdentification | NaN | Specific identification assigned to a person. It is derived from the association between Party and PartyIdentification. | PersonIdentification | Person |
| Person | EmployingParty | NaN | Party which is the employer of a person. | EmployingPartyRole | Employee |
| Person | MeetingAttendee | NaN | Specifies the meeting attendee which is an individual person. | MeetingAttendeeRole | Person |
| Person | RelatedRole | NaN | Role performed by the person for the proxy voting process. | AssignedProxyRole | ProxyPerson |
| Person | PreAssignedProxyPerson | NaN | Specifies the person who is the pre-assigned proxy for a meeting. | AssignedProxyRole | PreAssignedProxyRole |
| Person | PersonProfile | NaN | Information to support the Know Your Customer processes. | PersonProfile | Person |
| Person | ContactPersonRole | NaN | Contact role played by a person. | ContactPersonRole | Person |
| Person | Household | NaN | Specifies the members of a household in relation with the ownership of an account. | Household | Member |
| Person | CivilStatus | NaN | Specifies the civil status of a person. | CivilStatusCode | NaN |
| Person | DeathDate | NaN | Date on which a person is dead. | ISODateTime | NaN |
| Person | CitizenshipEndDate | NaN | Date of the end of citizenship. | ISODate | NaN |
| Person | CitizenshipStartDate | NaN | Date of the commencement of citizenship. | ISODate | NaN |
| PersonIdentification | NaN | PartyIdentificationInformation | Unique and unambiguous way to identify a person. | NaN | NaN |
| PersonIdentification | SocialSecurityNumber | NaN | Number assigned by a social security agency. | Max35Text | NaN |
| PersonIdentification | Person | NaN | Person for which an identification is provided. | Person | PersonIdentification |
| PersonIdentification | PersonName | NaN | Name by which a person is known and which is usually used to identify that person. It is derived from PartyName (association between PartyIdentificationInformation and PartyName). | PersonName | Identification |
| PersonIdentification | DriversLicenseNumber | NaN | Number assigned by a license authority to a driver's license. | Max35Text | NaN |
| PersonIdentification | AlienRegistrationNumber | NaN | Number assigned by a government agency to identify foreign nationals. | Max35Text | NaN |
| PersonIdentification | PassportNumber | NaN | Number assigned by a passport authority to a passport. | Max35Text | NaN |
| PersonIdentification | IdentityCardNumber | NaN | Number assigned by a national authority to an identity card. | Max35Text | NaN |
| PersonIdentification | EmployerIdentificationNumber | NaN | Number assigned to an employer by a registration authority. | Max35Text | NaN |
| EmployingPartyRole | NaN | Role | Organisation represented by a person, or for which a person works. | NaN | NaN |
| EmployingPartyRole | Employee | NaN | Identifies the employee of a party. | Person | EmployingParty |
| Document | NaN | NaN | General information that unambiguously identifies a document, such as identification number and issue date time. | NaN | NaN |
| Document | IssueDate | NaN | Issue date of the document. | ISODateTime | NaN |
| Document | CopyDuplicate | NaN | Specifies if this document is a copy, a duplicate, or a duplicate of a copy. | CopyDuplicateCode | NaN |
| Document | PlaceOfStorage | NaN | Specifies where the document is stored. | ContactPoint | StoredDocument |
| Document | PaymentObligation | NaN | Document which is referred to in a payment obligation. | PaymentObligation | AssociatedDocument |
| Document | Type | NaN | Specifies the type of the document, for example commercial invoice. | DocumentTypeCode | NaN |
| Document | Amount | NaN | Amount of money and currency of a document. The amount can be either the original amount due and payable for instance the ordered amount, or the amount actually remitted for the referred document. | ActiveCurrencyAndAmount | NaN |
| Document | Agreement | NaN | Agreement which is materialised by a document | Agreement | Document |
| Document | PlaceOfIssue | NaN | Place where the document was issued. | Location | IssuedDocument |
| Document | DocumentVersion | NaN | Unambiguous identification of the version of a document. | Number | NaN |
| Document | Status | NaN | Status of the document (eg delivered, paid, etc.) | Max140Text | NaN |
| Document | Reconciliation | NaN | Reconciliation process for which a document is specified. | Reconciliation | Document |
| Document | LetterOfCredit | NaN | Written undertaking by a bank to honour a demand for payment. | LetterOfCredit | Document |
| Document | PartyRole | NaN | Role played by a party in the context of a document or in the context of the business linked to the document. | DocumentPartyRole | Document |
| Document | DataSetType | NaN | Specifies the type of data set in which the document is included. | DataSetTypeCode | NaN |
| Document | Transport | NaN | Transport process for which related documents are specified. | Transport | TransportDocuments |
| Document | SignedIndicator | NaN | Indication whether the document must be signed or not. | YesNoIndicator | NaN |
| Document | RemittedAmount | NaN | Amount of money remitted for the referred document. | CurrencyAndAmount | NaN |
| Document | Guarantee | NaN | Guarantee that is described in a document. | Guarantee | Document |
| Document | Language | NaN | Language used for textual information in the document. | LanguageCode | NaN |
| Document | Purpose | NaN | Specifies the function of the document. | Max35Text | NaN |
| Document | DocumentIdentification | NaN | Identification of a document for instance unique identification of the purchase order, assigned by the buyer. | GenericIdentification | IdentifiedDocument |
| Document | Evidence | NaN | Proof of evidence which uses a document. | Evidence | RelatedDocument |
| Document | CommercialTrade | NaN | Trade for which a certificare is issued. | CommercialTrade | Documents |
| Document | Presentation | NaN | Presentation of documents and statements. | Presentation | PresentedDocument |
| Document | RelatedContract | NaN | Related document which materialises the agreement. | RegisteredContract | Attachment |
| PrivateCertificate | NaN | Document | Specifies the parameters associated with the production of a certificate to identify the profile of a customer. | NaN | NaN |
| PrivateCertificate | CertificateType | NaN | Identifies the type of certificate. | CertificateTypeCode | NaN |
| PrivateCertificate | CertificationIndicator | NaN | Indicates whether the certificate type has been obtained and verified. | YesNoIndicator | NaN |
| PrivateCertificate | CheckingDate | NaN | Date at which the certification check has been performed. | ISODate | NaN |
| PrivateCertificate | CheckingFrequency | NaN | Specifies how frequently the check is performed. | EventFrequencyCode | NaN |
| PrivateCertificate | NextRevisionDate | NaN | Specifies the date at which the next certification check will be performed. | ISODate | NaN |
| PrivateCertificate | Person | NaN | Profile of a person for which a private certificate is described. | PersonProfile | ProfileCertification |
| DocumentPartyRole | NaN | Role | Role played by a party in the context of a document. | NaN | NaN |
| DocumentPartyRole | Document | NaN | Identifies the document for which a party plays a role. | Document | PartyRole |
| ValidatingPartyRole | NaN | DocumentPartyRole | Identification of the person who validated the signature. | NaN | NaN |
| CheckingPartyRole | NaN | DocumentPartyRole | Identification of the person who checked the document and/or the signature. | NaN | NaN |
| ResponsiblePartyRole | NaN | DocumentPartyRole | Identification of the party who is responsible for the certificate. | NaN | NaN |
| SecuritiesTax | NaN | Tax | Amount of money due to the government or tax authority, according to various pre-defined parameters such as thresholds or income. | NaN | NaN |
| SecuritiesTax | TaxableIncomePerShare | NaN | Amount included in the NAV that corresponds to gains directly or indirectly derived from interest payment in the scope of the European Directive on taxation of savings income in the form of interest payments. | ActiveCurrencyAndAmount | NaN |
| SecuritiesTax | TaxableIncomePerShareCalculated | NaN | Specifies whether the fund calculates a taxable interest per share (TIS). | TaxableIncomePerShareCalculatedCode | NaN |
| SecuritiesTax | EUCapitalGain | NaN | Specifies whether capital gain is in the scope of the European directive on taxation of savings income in the form of interest payments (Council Directive 2003/48/EC 3 June), or an income realised upon sale, a refund or redemption of shares and units, etc. | EUCapitalGainCode | NaN |
| SecuritiesTax | EUDividendStatus | NaN | Specifies whether dividend is in the scope of the European directive on taxation of savings income in the form of interest payments (Council Directive 2003/48/EC 3 June), or an income realised upon sale, a refund or redemption of shares and units, etc. | EUDividendStatusCode | NaN |
| SecuritiesTax | TaxableIncomePerDividend | NaN | Amount included in the dividend that corresponds to gains directly or indirectly derived from interest payment in the scope of the European Directive on taxation of savings income in the form of interest payments. | CurrencyAndAmount | NaN |
| SecuritiesTax | StampDutyType | NaN | Indicates how the stamp duty should be applied. | StampDutyTypeCode | NaN |
| SecuritiesTax | StampDutyTaxBasis | NaN | Specifies the stamp duty type or exemption reason applicable to the settlement transaction. | Max4AlphaNumericText | NaN |
| SecuritiesTax | TaxVoucher | NaN | Tax voucher which is related to a securities tax. | TaxVoucher | RelatedSecurityTax |
| SecuritiesTax | TaxableIncomePerDividendShare | NaN | Amount included in the dividend/NAV that is identified as gains directly or indirectly derived from interest payments within the scope of the EU Savings directive | ActiveCurrencyAndAmount | NaN |
| SecuritiesTax | RelatedTax | NaN | Percentage of the gross dividend rate on which tax must be paid . | RateAndAmount | SecuritiesTax |
| SecuritiesTax | TaxLotNumber | NaN | Identification, for tax purposes, of a lot of identical securities that are bought at a certain date and at a certain price. | Max15NumericText | NaN |
| SecuritiesTax | Security | NaN | Security on which the tax applies. | Security | TaxDetails |
| SecuritiesTax | TaxRuleExemptIndicator | NaN | Indicates whether the tax rule applies within the jurisdiction as a condition of this security. | YesNoIndicator | NaN |
| SecuritiesTax | EffectivePeriod | NaN | Period during which the tax rule applies within the jurisdiction. | NaN | NaN |
| SecuritiesTax | FrankedRate | NaN | Percentage of dividend for which tax is already paid. | PercentageRate | NaN |
| SecuritiesTax | TEFRARule | NaN | Indicates the TEFRA rule under which the security is issued. | TEFRARulesCode | NaN |
| SecuritiesTax | Jurisdiction | NaN | Jurisdiction in which the tax rule applies. | Jurisdiction | RelatedSecuritiesTax |
| InvestmentFundTax | NaN | SecuritiesTax | Tax related to an investment fund order. | NaN | NaN |
| InvestmentFundTax | FiscalExemption | NaN | Indicates whether an owner of an investment account may benefit from a fiscal exemption or amnesty for instance for declaring overseas investments. | YesNoIndicator | NaN |
| InvestmentFundTax | InvestmentAccount | NaN | Investment account for which taxes are specified. | InvestmentAccount | InvestmentFundTax |
| InvestmentFundTax | PercentageOfDebtClaim | NaN | Percentage of the underlying assets of the funds that represents a debt and is in the scope of the European directive on taxation of savings income in the form of interest payments (Council Directive 2003/48/EC 3 June). | PercentageRate | NaN |
| InvestmentFundTax | PercentageGrandfatheredDebt | NaN | Percentage of grandfathered debt claim. | PercentageRate | NaN |
| InvestmentFundTax | ExemptionIndicator | NaN | Indicates whether a tax exemption applies. | YesNoIndicator | NaN |
| InvestmentFundTax | Transaction | NaN | Transaction for which the tax is specified. | InvestmentFundTransaction | TransactionTax |
| TrusteeRole | NaN | InvestmentAccountPartyRole | Legal owner of the property. However, the beneficiary has the equitable or beneficial ownership. The trustee must ensure all terms and conditions of the security are adhered to. | NaN | NaN |
| CustodianForMinor | NaN | InvestmentAccountPartyRole | Entity that holds shares/units on behalf of a legal minor. Although the account is registered under the name of the minor, the custodian retains control of the account. | NaN | NaN |
| Nominee | NaN | InvestmentAccountPartyRole | Entity (the registered owner) named by the beneficial owner to act on its behalf, often to facilitate dealing, or to conceal the identity of the beneficiary. Securities and other assets are recorded in the nominee's name. | NaN | NaN |
| JointOwner | NaN | InvestmentAccountPartyRole | Co-owner of an investment account when the ownership is assigned to more than one party. | NaN | NaN |
| SecondaryOwner | NaN | InvestmentAccountPartyRole | Entity that is not the primary owner when the ownership of the investment account is split among several owners. | NaN | NaN |
| MandatePartyRole | NaN | Role | Role played by a party in the context of a mandate. | NaN | NaN |
| MandatePartyRole | Mandate | NaN | Identifies the mandate in which a party plays a role. | Mandate | MandatePartyRole |
| MandateHolder | NaN | MandatePartyRole | Entity that was given by another entity the authority to act on its behalf. | NaN | NaN |
| LegalGuardianRole | NaN | InvestmentAccountPartyRole | Entity that has been appointed by a legal authority to act on behalf of a person judged to be incapacitated. | NaN | NaN |
| SuccessorOnDeath | NaN | InvestmentAccountPartyRole | Deceased's estate, or successor, to whom the respective percentage of ownership will be transferred upon the death of one of the owners. | NaN | NaN |
| AdministratorRole | NaN | InvestmentAccountPartyRole | Entity that has been appointed by a legal authority to act on behalf of a person or organisation that has gone bankrupt. | NaN | NaN |
| IntermediaryRole | NaN | AccountPartyRole | Party that provides services relating to financial products to investors, for example, advice on products and placement of orders. | NaN | NaN |
| Adjustment | NaN | NaN | Modification on the value of goods and / or services. For example: rebate, discount. | NaN | NaN |
| Adjustment | Amount | NaN | Amount of money that results from the application of an adjustment (charges. fees, discount or allowance) to the amount due. | CurrencyAndAmount | NaN |
| Adjustment | ChargeRate | NaN | Rate used to calculate the amount of the adjustment, allowance, charge or fee. | PercentageRate | NaN |
| Adjustment | CalculationMethod | NaN | Method used to calculate an adjustment (financial adjustment, charge or allowance). | TaxationBasisCode | NaN |
| Adjustment | Payment | NaN | Specifies the payment resulting from charges due by one party to another or the payment to which adjustements (for instance charges) are applied. | Payment | Adjustments |
| Adjustment | Direction | NaN | Specifies whether the adjustment must be subtracted or added to the total amount. | AdjustmentDirectionCode | NaN |
| Adjustment | Reason | NaN | Reason for the amount adjustment. | Max4AlphaNumericText | NaN |
| Adjustment | RelatedLineItem | NaN | Specifies the line item on which a financial adjustment took place. | LineItem | FinancialAdjustment |
| Adjustment | AllowanceChargeIndicator | NaN | Indication of whether or not this allowance charge is a charge (Indicator is Yes) that should be added or an allowance that should be subtracted (Indicator is No). | YesNoIndicator | NaN |
| Adjustment | Price | NaN | Specifies the price which is adjusted. | Price | PriceAdjustment |
| Adjustment | ChargeIndicator | NaN | Indication of whether or not this allowance charge is a charge. | YesNoIndicator | NaN |
| Adjustment | Type | NaN | Specifies the type of adjustment applied to the amount of goods/services by means of a code. | AdjustmentTypeCode | NaN |
| Adjustment | CollateralManagement | NaN | Process which groups the activities related to collateral. | CollateralManagement | FeesAndCommissions |
| Adjustment | AdjustedBalance | NaN | Balance for which adjustments are specified. | Balance | Adjustment |
| Adjustment | ChargesPartyRole | NaN | Role played by a party in the context of charges due. | ChargePartyRole | Adjustment |
| Adjustment | EffectivePeriod | NaN | Period during which the adjustment is applicable. | DateTimePeriod | RelatedAdjustment |
| Adjustment | CurrencyExchange | NaN | Currency exchange for which adjustments such as fees or commissions are applied. | CurrencyExchange | Adjustment |
| Adjustment | SecuritiesOrder | NaN | Order for which adjustments are specified. | SecuritiesOrder | Adjustments |
| Adjustment | Tax | NaN | Information on the calculation method resulting in the tax amount included in the charge transfer. The tax is expressed as a fixed amount, or as a percentage of the charge amount, upon which the tax is applied. | Tax | Adjustment |
| Commission | NaN | Adjustment | Amount of money due to a party as compensation for a service. | NaN | NaN |
| Commission | CommissionWaiving | NaN | Voluntary non-enforcement of the right to all or part of a commission. | CommissionWaiver | Commission |
| Commission | Trade | NaN | Trade for which commission parameters are specified. | Trade | TradeCommission |
| Commission | CommissionType | NaN | Service for which the commission is asked or paid. | CommissionTypeV2Code | NaN |
| Commission | Basis | NaN | Basis upon which a commission is charged, eg, flat fee. | TaxationBasisCode | NaN |
| Commission | CommercialAgreementReference | NaN | Reference to the agreement established between the fund and another party. This element, amongst others, defines the conditions of the commissions. | Max35Text | NaN |
| Commission | CalculationDate | NaN | Date/time at which the commission is calculated. | ISODateTime | NaN |
| Commission | Rate | NaN | Commission expressed as a percentage. | PercentageRate | NaN |
| Commission | CommissionAmount | NaN | Commission expressed as an amount of money. | CurrencyAndAmount | NaN |
| Commission | Broker | NaN | Broker to which a commission is paid. | Broker | Commission |
| Commission | CommissionPartyRole | NaN | Role played by a party in the context of commissions. | CommissionPartyRole | Commission |
| Commission | Account | NaN | Account used for the commission fees. | CashAccount | Commission |
| Commission | RelatedQuote | NaN | Quote which includes a commission. | SecuritiesQuoteVariable | Commission |
| Commission | SplitRate | NaN | Percentage of the total commission received by an intermediary. | PercentageRate | NaN |
| Commission | Currency | NaN | Currency in which the commission has to be settled. | CurrencyCode | NaN |
| Commission | CorporateActionFeesAndCharges | NaN | Corporate action fees to which commission fees are added. | CorporateActionFeesAndCharges | Commission |
| CommissionWaiver | NaN | NaN | Non-enforcement of the right to all or part of a commission by the party entitled to the commission. | NaN | NaN |
| CommissionWaiver | Commission | NaN | Commission to which the waiver applies. | Commission | CommissionWaiving |
| CommissionWaiver | InstructionBasis | NaN | Form of the rebate, eg, cash. | WaivingInstructionCode | NaN |
| CommissionWaiver | WaivedRate | NaN | Proportion of the commission that is waived, ie, if the commission is 5% and half is waived, 2.5% should be stated in this field. | PercentageRate | NaN |
| CommissionWaiver | NonWaivedRate | NaN | New commission rate applied, after waiving. | PercentageRate | NaN |
| InvestmentPlan | NaN | NaN | Plan that allows investors to schedule periodical investments or divestments, according to pre-defined criteria. | NaN | NaN |
| InvestmentPlan | Frequency | NaN | Frequency of the investment or divestment, eg, daily, weekly, or monthly. | FrequencyCode | NaN |
| InvestmentPlan | Amount | NaN | Currency and amount of the periodical payments. When the standing order is related to a fund investment plan, this is the cash part of the invested amount. | CurrencyAndAmount | NaN |
| InvestmentPlan | Asset | NaN | Security that an investment plan invests in, or from which the investment plan divests. | Asset | InvestmentPlan |
| InvestmentPlan | Instalment | NaN | Specifies information on the successive payments in an investment plan. | Instalment | InvestmentPlan |
| InvestmentPlan | RelatedService | NaN | Service which provides a systematic investment plan. | InvestmentAccountService | SystematicInvestmentPlan |
| InvestmentPlan | Insurance | NaN | Insurance contract which covers the investment plan. | InsuranceCertificate | RelatedInvestmentPlan |
| InvestmentPlan | StandingOrder | NaN | Order generated automatically, according to the terms of the investment plan. | InvestmentFundOrder | InvestmentPlan |
| InvestmentPlan | MultiCurrency | NaN | Specifies whether the investment plan is multi currency or not. | YesNoIndicator | NaN |
| InvestmentPlan | Currency | NaN | Currency of the investment plan. | CurrencyCode | NaN |
| InvestmentPlan | Portfolio | NaN | Portfolio for which the investment plan invests or divests. | Portfolio | InvestmentPlan |
| InvestmentPlan | InvestmentPeriod | NaN | Period during which an investment plan has to be executed. | DateTimePeriod | RelatedInvestmentPlan |
| InvestmentPlan | PlanStatus | NaN | Status of the savings or withdrawal investment plan. | PlanStatusCode | NaN |
| InvestmentPlan | Pension | NaN | Attributes of a pension. | Pension | RelatedInvestmentPlan |
| InvestmentPlan | TaxEfficientProduct | NaN | Characteristics of a tax efficient product. | TaxEfficientProduct | RelatedInvestmentPlan |
| InvestmentFundOrder | NaN | SecuritiesOrder | An investor's instruction to either subscribe or redeem an amount of money or its equivalent, for example other assets, into or out of an investment fund. | NaN | NaN |
| InvestmentFundOrder | GrossAmountIndicator | NaN | Indicates whether an ordered amount is a gross amount (including all charges, commissions, tax). If it is not a gross amount, the ordered amount is a net amount (amount to be invested or redeemed from the fund to which other elements will be added). | YesNoIndicator | NaN |
| InvestmentFundOrder | RelatedTransaction | NaN | Transaction which is the source of the order. | InvestmentFundTransaction | InvestmentFundOrder |
| InvestmentFundOrder | OrderType | NaN | Specifies the category of the investment fund order. | FundOrderTypeCode | NaN |
| InvestmentFundOrder | GrossAmount | NaN | Amount of money used to derive the quantity of investment fund units sold or subscribed, before deduction of charges, commissions, and taxes, expressed in the currency requested by the investor. [Quantity \* Price] + (Charges + Commissions +Taxes)] | CurrencyAndAmount | NaN |
| InvestmentFundOrder | UnitsNumber | NaN | Quantity of investment fund units to be subscribed or redeemed. | SecuritiesQuantity | Order |
| InvestmentFundOrder | InvestmentFundOrderExecution | NaN | Execution of an investment fund order. | InvestmentFundOrderExecution | Order |
| InvestmentFundOrder | NetAmount | NaN | Amount of money used to determine the quantity of investment fund units to be subscribed or to be sold. | CurrencyAndAmount | NaN |
| InvestmentFundOrder | OrderDateTime | NaN | Date and time at which the order was placed by the investor. | ISODateTime | NaN |
| InvestmentFundOrder | ExpiryDateTime | NaN | Date on which the order expires. | ISODateTime | NaN |
| InvestmentFundOrder | CancellationRight | NaN | Cancellation right of an investor with respect to an investment fund order. | CancellationRightCode | NaN |
| InvestmentFundOrder | RequestedSettlementCurrency | NaN | Currency requested for settlement of cash proceeds. | CurrencyCode | NaN |
| InvestmentFundOrder | RequestedExecutionDateTime | NaN | Date and time at which the investor requests the order to be executed. | ISODateTime | NaN |
| InvestmentFundOrder | FinancialAdvice | NaN | Specifies if advice has been received from an independent financial advisor. | FinancialAdviceCode | NaN |
| InvestmentFundOrder | NegotiatedTrade | NaN | Specifies whether the trade is negotiated. | NegotiatedTradeCode | NaN |
| InvestmentFundOrder | HoldingsRate | NaN | Percentage of the financial quantity to be invested or redeemed. | PercentageRate | NaN |
| InvestmentFundOrder | OrderWaiverReason | NaN | Reason why an order has to be handled differently, probably in a manual fashion, because for example, the investment manager has agreed a waiver to the extended terms. | OrderWaiverReasonCode | NaN |
| InvestmentFundOrder | InitialOrderIndicator | NaN | Indicates whether the subscription order is an initial order. | YesNoIndicator | NaN |
| InvestmentFundOrder | OrderBookingDate | NaN | Date and time an investment fund order is registered on the books of either the fund or its designated agent, eg, transfer agent. | ISODateTime | NaN |
| InvestmentFundOrder | InvestmentPlan | NaN | Investment plan which triggers the standing orders. | InvestmentPlan | StandingOrder |
| InvestmentFundOrder | OrderStatus | NaN | Status of an investment fund order. | SecuritiesOrderStatus | InvestmentFundOrder |
| InvestmentFundOrder | TotalAmount | NaN | Total amount subscribed in the current tax year. | CurrencyAndAmount | NaN |
| Obligation | NaN | NaN | Specifies the assets (quantity of securities, goods, services, and cash amounts) that have to be delivered. | NaN | NaN |
| Obligation | RequestedSettlementDate | NaN | Date and time at which a trade must be executed. For a direct debit, it is the date and time at which the creditor requests that the amount of money is to be collected from the debtor. For a credit transfer, it is the date and time at which the debtor requests the clearing agent to process the payment. For a securities trade, it is the date and time at which the securities are to be delivered or received. | ISODateTime | NaN |
| Obligation | RequestedSettlementAmount | NaN | Total amount of money to be paid or received. | CurrencyAndAmount | NaN |
| Obligation | Priority | NaN | Specifies whether the transaction is to be executed with a high priority. | Max4AlphaNumericText | NaN |
| Obligation | Trade | NaN | Specifies the trade which originates the obligation to deliver a product, cash or securities.. | Trade | Obligation |
| Obligation | TransactionRisk | NaN | Transaction risk calculated per obligation type. | TransactionRisk | Obligation |
| Obligation | ParentObligation | NaN | Obligation which is divided into several sub-obligations. | Obligation | SubObligation |
| Obligation | SubObligation | NaN | Specifies an obligation resulting from another existing obligation, for instance each leg of a financing agreement is a sub-obligation of the global financing obligation. | Obligation | ParentObligation |
| Obligation | Offset | NaN | Specifies the method used to settle a specific obligation. | ObligationFulfilment | ObligationOffset |
| Obligation | OriginalObligationProcess | NaN | Obligation fulfilment process which did not extinguish the obligation but replaced it by a new one, for instance in case of netting. | ObligationFulfilment | ResultingObligation |
| Obligation | ExposureType | NaN | Type of exposure related to this obligation. | ExposureTypeV2Code | NaN |
| PaymentObligation | NaN | Obligation | Obligation for the debtor to pay the creditor an amount of cash. | NaN | NaN |
| PaymentObligation | PaymentOffset | NaN | Fulfilment of a payment obligation through a payment and its execution. It is derived from the association between Obligation and Obligation fulfillment. | Payment | PaymentObligation |
| PaymentObligation | Purpose | NaN | Underlying reason for the payment obligation | PaymentPurposeCode | NaN |
| PaymentObligation | RemittanceDeliveryMethod | NaN | Specifies the method to be used by the first agent (debtor agent in the case of a credit transfer, creditor agent in the case of a direct debit) to deliver the remittance advice information, which may be sent separately from the payment instruction. | RemittanceLocationMethodCode | NaN |
| PaymentObligation | AssociatedDocument | NaN | Specifies the referred document/transaction, eg, invoice or credit note. | Document | PaymentObligation |
| PaymentObligation | Amount | NaN | Amount payable to the creditor. | CurrencyAndAmount | NaN |
| PaymentObligation | RemittanceLocation | NaN | Address to which the first agent is to send the remittance information. | ContactPoint | RemittanceRelatedPayment |
| PaymentObligation | Interest | NaN | Process which calculates the interest to be paid. It may also specify the interest charged on instalment. | InterestManagement | PaymentObligation |
| PaymentObligation | CommercialTrade | NaN | Commercial trade which creates the payment obligation. | CommercialTrade | PaymentObligation |
| PaymentObligation | Percentage | NaN | Maximum amount that a financial institution guarantees to pay for a specific commercial trade, expressed as a percentage of the purchase order net amount. | PercentageRate | NaN |
| PaymentObligation | MaximumAmount | NaN | Maximum amount that a financial institution guarantees to pay for a specific commercial trade. | CurrencyAndAmount | NaN |
| PaymentObligation | ExpiryDate | NaN | Date at which the obligation will expire. For instance, it is the transaction authorisation deadline to complete a payment by card. | ISODateTime | NaN |
| PaymentObligation | ApplicableLaw | NaN | Country of which the law governs the payment obligation. | CountryCode | NaN |
| PaymentObligation | PaymentSourceBuyIn | NaN | Buy-in process which created the payment obligation. | BuyIn | CashCompensation |
| PaymentObligation | RelatedCorporateAction | NaN | Corporate action processes which are the source of the payment obligation. | CorporateActionProceedsDeliveryInstruction | CashProceedsMovement |
| PaymentObligation | RelatedCollateralMovement | NaN | Collateral movement which is the source of the obligation. | CollateralMovement | CashCollateralMovement |
| PaymentObligation | PaymentSourceUndertakingDemand | NaN | Undertaking demand which is the source of a payment obligation. | Demand | Payment |
| PaymentObligation | PartyRole | NaN | Specifies each role linked to a payment obligation and played by a party at that step in a payment flow. | PaymentObligationPartyRole | PaymentObligation |
| PaymentObligation | ExecutedSecuritiesTrade | NaN | Securities trade which created a payment flow. | SecuritiesTradeExecution | PaymentObligation |
| PaymentObligation | RelatedAccountClosingTerms | NaN | Contract which authorises the transfer of funds resulting in a payment obligation. | CashAccountContract | BalanceTransfer |
| PaymentObligation | PaymentSourcePortfolioTransfer | NaN | The PaymentObligation that specifies the payment resulting from charges due by one party to another. | PortfolioTransfer | PaymentObligation |
| PaymentObligation | PaymentSourceCurrencyOption | NaN | The PaymentObligation that specifies the amount of the premium paid by the buyer of the option and its settlement place. | CurrencyOption | PremiumSettlement |
| PaymentObligation | ExchangeRateInformation | NaN | Foreign exchange trade which is the source of the payment. | ForeignExchangeTrade | ResultingSettlement |
| PaymentObligation | Dividend | NaN | Dividend for which payment terms are specified. | Dividend | Obligation |
| PaymentObligation | RepurchaseAgreement | NaN | Repurchase agreement which covers the delivery of cash by the buyer. | RepurchaseAgreement | PaymentObligation |
| PaymentObligation | RelatedAssignment | NaN | Assignment which contains one or more payment obligations. | Assignment | PaymentObligation |
| PaymentObligation | BankingTransaction | NaN | Transaction executed by the client of a financial institution from/to the account serviced by the financial institution, such as mortgage payment. | BankingTransaction | PaymentObligation |
| PaymentObligation | PaymentTerms | NaN | Specifies the payment terms of the obligation. | PaymentTerms | RelatedPaymentObligation |
| PaymentObligation | PaymentDueDate | NaN | Due date for the payment. | ISODate | NaN |
| Instalment | NaN | PaymentObligation | Specifies the details of each successive payment in settlement of a debt or in an investment plan. | NaN | NaN |
| Instalment | InitialNumberOfInstalment | NaN | Number of pre-paid instalment periods at the time an investment plan is created. | Number | NaN |
| Instalment | TotalNumberOfInstalment | NaN | Total number of times the amount must be invested at the predefined frequency as of the start date of the investment plan. | Number | NaN |
| Instalment | PeriodUnit | NaN | Period unit between consecutive payments (for example day, month, year). | FrequencyCode | NaN |
| Instalment | NumberOfUnits | NaN | Number of period units between consecutive payments. | Number | NaN |
| Instalment | SequenceIdentification | NaN | Specifies the progressive number of a single instalment. | Max70Text | NaN |
| Instalment | InvestmentPlan | NaN | Investment plan for which instalment information is provided. | InvestmentPlan | Instalment |
| Instalment | InstalmentPlanType | NaN | Type of instalment plan. | InstalmentPlanCode | NaN |
| Instalment | FirstPaymentAmount | NaN | Amount of the first payment. | CurrencyAndAmount | NaN |
| Instalment | FirstPaymentDate | NaN | Date of the first payment. | ISODateTime | NaN |
| ObligationFulfilment | NaN | NaN | Processes by which an obligation is extinguished fully or partially. | NaN | NaN |
| ObligationFulfilment | Date | NaN | Date and time on which assets become available. | ISODate | NaN |
| ObligationFulfilment | ObligationOffset | NaN | Specifies the obligation which has been offset for instance a payment obligation or a securities delivery. | Obligation | Offset |
| ObligationFulfilment | ResultingObligation | NaN | Specifies the obligation which result from a settlement process, for instance the remaining obligation when the obligations are netted. | Obligation | OriginalObligationProcess |
| Payment | NaN | ObligationFulfilment | Payment information and processes required to transfer cash end to end from the debtor to the creditor. | NaN | NaN |
| Payment | PaymentObligation | NaN | Specifies the obligation which created the payment. | PaymentObligation | PaymentOffset |
| Payment | CurrencyOfTransfer | NaN | Specifies the currency of the amount to be transferred which may be different from the currency of the debtor's account. | CurrencyCode | NaN |
| Payment | CreditMethod | NaN | Specifies the transfer method to be used for the credit. | CreditInstrument | RelatedPayment |
| Payment | Type | NaN | Type, or nature, of the payment, eg, express payment. | PaymentTypeCode | NaN |
| Payment | InstructedAmount | NaN | Amount of money to be moved between the debtor and creditor, before deduction of charges, expressed in the currency as ordered by the initiating party. | CurrencyAndAmount | NaN |
| Payment | Priority | NaN | Urgency or order of importance that the originator would like the recipient of the payment to apply to its processing. | PriorityCode | NaN |
| Payment | ValueDate | NaN | Date on which a payment must be executed | ISODate | NaN |
| Payment | PaymentStatus | NaN | Specifies the status of a payment at a specified time. | PaymentStatus | Payment |
| Payment | PartyRole | NaN | Specifies each role linked to a payment and played by a party at that step in a payment flow. | PaymentPartyRole | Payment |
| Payment | TaxOnPayment | NaN | Payment levy tax. | Tax | RelatedPaymentSettlement |
| Payment | PaymentExecution | NaN | Describes the processes necessary to execute a payment. | PaymentExecution | Payment |
| Payment | PoolingAdjustmentDate | NaN | Date used for the correction of the value date of a cash pool movement that has been posted with a different value date. | ISODate | NaN |
| Payment | EquivalentAmount | NaN | Amount of money to be transferred between debtor and creditor, before deduction of charges, expressed in the currency of the debtor's account, and to be transferred in a different currency. | ImpliedCurrencyAndAmount | NaN |
| Payment | CurrencyExchange | NaN | Information on the exchange rate and amounts used in the payment | CurrencyExchange | RelatedPayment |
| Payment | InstructionForCreditorAgent | NaN | Further information related to the processing of the payment instruction that may need to be acted upon by the creditor agent. Usage: The instruction can relate to a level of service, can be an instruction to be executed by the creditor's agent, or can be information required by the creditor's agent to process the instruction. | InstructionCode | NaN |
| Payment | InstructionForDebtorAgent | NaN | Further information related to the processing of the payment instruction that may need to be acted upon by the debtor's agent. Usage: The instruction can relate to a level of service, can be an instruction to be executed by the debtor's agent, or can be information required by the debtor's agent to process the instruction. | InstructionCode | NaN |
| Payment | PaymentRelatedIdentifications | NaN | Identifications provided to identify a payment at different processing levels. | PaymentIdentification | Payment |
| Payment | RelatedInvestigationCase | NaN | Investigation case assigned to the payment. | PaymentInvestigationCase | UnderlyingPayment |
| Payment | SettlementTimeRequest | NaN | Information on the requested settlement time of the instruction. | SettlementTimeRequest | Payment |
| Payment | Amount | NaN | Amount of the payment. | CurrencyAndAmount | NaN |
| Payment | TradeSettlement | NaN | Specifies the settlement operation which originates the payment. | CommercialTradeSettlement | Payment |
| Payment | StandardSettlementInstructions | NaN | Identifies the standard settlement instructions. | Max140Text | NaN |
| Payment | RelatedDebitAuthorisation | NaN | Payment which is the result of the debit authorisation | DebitAuthorisation | AuthorisedReturn |
| Payment | RelatedInvestigationCaseResolution | NaN | Case resolution related to a specific payment. | PaymentInvestigationCaseResolution | PaymentCorrection |
| Payment | OriginalPayment | NaN | Original payment which is returned. | Payment | ReturnPayment |
| Payment | ReturnPayment | NaN | Payment which offsets an original payment. | Payment | OriginalPayment |
| Payment | RelatedSecuritiesSettlement | NaN | Securities settlement process which is the source of the payment. | SecuritiesSettlement | Payment |
| Payment | InvoiceReconciliation | NaN | Reconciliation of the amounts of an invoice with the amounts included in one or more payments. | Invoice | Payment |
| Payment | PaymentInstrument | NaN | Payment type at the origin of the cash entry eg, a cheque. | PaymentInstrumentCode | NaN |
| Payment | Account | NaN | Account debited for the payment. | CashAccount | Payment |
| Payment | Adjustments | NaN | Specifies the charges or the allowance related to a payment. | Adjustment | Payment |
| Payment | ContractRegistration | NaN | Provides the payment of the registered contract. | RegisteredContract | RelatedPayment |
| IndividualPayment | NaN | Payment | Payment which consists of one single transaction. This payment may be grouped with other similar payments to form a bulk payment. | NaN | NaN |
| IndividualPayment | BulkPayment | NaN | Payment hich groups a series of individual payments. | BulkPayment | Groups |
| ChequePayment | NaN | IndividualPayment | Payment made by drawing a cheque in order to settle a debt. | NaN | NaN |
| ChequePayment | Cheque | NaN | Specifies the characteristics of the cheque which was drawn to settle a debt. | Cheque | RelatedPayment |
| CardPayment | NaN | IndividualPayment | Payment through an electronic money product. | NaN | NaN |
| CardPayment | PaymentCard | NaN | Specifies the card which is used in a payment by card. | PaymentCard | Payment |
| CardPayment | Product | NaN | Product purchased with the transaction. | Product | CardPayment |
| CardPayment | DetailedAmount | NaN | Detailed amount value. | ImpliedCurrencyAndAmount | NaN |
| CardPayment | AmountQualifier | NaN | Identification of the type of amount. | TypeOfAmountCode | NaN |
| CardPayment | CardPaymentAcquiring | NaN | Parameters of the process of acquiring a card payment. | CardPaymentAcquiring | RelatedCardPayment |
| CardPayment | PaymentCardPartyRole | NaN | Specifies each role played by a party in the process of a payment by card. | CardPaymentPartyRole | CardPayment |
| CardPayment | CardPaymentStatus | NaN | Status of the payment by card. | CardPaymentStatus | CardPayment |
| CardPayment | DetailedAmountLabel | NaN | Short description of the amount. | Max35Text | NaN |
| CardPayment | Reconciliation | NaN | Total of a certain type of transaction. | ReconciliationTransaction | CardPaymentTotal |
| CardPayment | TransactionCategory | NaN | Specifies the category to which the card transaction belongs. | ExternalCardTransactionCategoryCode | NaN |
| CardPayment | CashBackAmount | NaN | Amount added to the total price of the transaction and received in cash by the customer. | CurrencyAndAmount | NaN |
| CardPayment | Gratuity | NaN | Amount tendered for a service performed. | CurrencyAndAmount | NaN |
| CardPayment | DebitCreditDirection | NaN | Specifies the direction of a payment. | DebitCreditCode | NaN |
| CardPayment | ATMTotal | NaN | Current totals of the ATM. | ATMTotal | RelatedCardPayment |
| PaymentCard | NaN | NaN | Electronic money product that provides the cardholder with a portable and specialised computer device that typically contains a microprocessor. | NaN | NaN |
| PaymentCard | Payment | NaN | Payment for which a payment card is used. | CardPayment | PaymentCard |
| PaymentCard | Type | NaN | Type of card, eg, credit card. | CardTypeCode | NaN |
| PaymentCard | Number | NaN | Number embossed on a card that links the card to the account owner and account servicer (sometimes called personal account number or PAN). | Max35Text | NaN |
| PaymentCard | StartDate | NaN | Year and month the card is available for use. | ISOYearMonth | NaN |
| PaymentCard | ExpiryDate | NaN | Year and month the card expires. | ISOYearMonth | NaN |
| PaymentCard | SecurityCode | NaN | Security code written on the card, sometimes called card security code (CSC). | Max35Text | NaN |
| PaymentCard | SequenceNumber | NaN | Identifies a card inside a set of cards with the same number (or PAN). | Max35Text | NaN |
| PaymentCard | ServiceCode | NaN | Services attached to the card. | Exact3NumericText | NaN |
| PaymentCard | TrackValue | NaN | Card track content or equivalent. | Max140Text | NaN |
| PaymentCard | SecurityCodeManagement | NaN | Card Security Code management associated with the transaction. | CSCManagementCode | NaN |
| PaymentCard | CardBrand | NaN | Brand name of the card. | Max35Text | NaN |
| PaymentCard | RelatedAccount | NaN | Account linked to the card. | CashAccount | RelatedPaymentCard |
| PaymentCard | ProfileNumber | NaN | Defines a category of cards related the acceptance processing rules defined by the acquirer. | Max5NumericText | NaN |
| PaymentCard | RelatedAccountType | NaN | Type of cardholder account used for the transaction. | CardAccountTypeCode | NaN |
| PaymentCard | CreditAvailableAmount | NaN | Monetary value of the credit available for this financial card. | CurrencyAndAmount | NaN |
| PaymentCard | Limit | NaN | Limit specified on a payment card. | Limit | RelatedPaymentCard |
| PaymentCard | CardCurrencyCode | NaN | Currency code of the card issuer. | CurrencyCode | NaN |
| PaymentCard | Interest | NaN | Interest applied on amounts due for credit card payments. | Interest | RelatedPaymentCard |
| PaymentCard | CardCountryCode | NaN | Country code attached to the card by the card issuer. | Country | RelatedPaymentCard |
| PaymentCard | CardProgramme | NaN | The card programme associated by a retailer to a cardholder among a series of payment programmes offered by the retailer. | Max35Text | NaN |
| CardPaymentPartyRole | NaN | Role | Role played by a party in the context of a payment by card. | NaN | NaN |
| CardPaymentPartyRole | CardPayment | NaN | Identifies the payment by card for which a party plays a role. | CardPayment | PaymentCardPartyRole |
| CardPaymentPartyRole | PartyType | NaN | Specifies the type of party which plays a role in the context od a card payment process. | PartyTypeCode | NaN |
| CardholderRole | NaN | CardPaymentPartyRole | Party entitled by a card issuer to use a card. | NaN | NaN |
| CardholderRole | Authentication | NaN | Data related to the authentication of the cardholder. | Authentication | Cardholder |
| DirectDebit | NaN | IndividualPayment | Payment, initiated by the creditor, to debit a debtor's account in favour of the creditor. A direct debit can be pre-authorised or not. In most countries, authorisation is in the form of a mandate between the debtor and creditor. | NaN | NaN |
| DirectDebit | RegistrationIdentification | NaN | Reference assigned to a creditor by its financial institution, or relevant authority, authorising the creditor to take part in a direct debit scheme. | Max35Text | NaN |
| DirectDebit | DirectDebitMandate | NaN | Set of elements providing information specific to the direct debit mandate. | DirectDebitMandate | RelatedDirectDebit |
| DirectDebit | PreNotificationIdentification | NaN | Unique and unambiguous identification of the pre-notification which is sent separately from the direct debit instruction.Usage: the direct debit pre-notification is used to reconcile separately sent collection information with the direct debit transaction information. | Max35Text | NaN |
| DirectDebit | PreNotificationDate | NaN | Date on which the creditor notifies the debtor about the amount and date on which the direct debit instruction will be presented to the debtor's agent. | ISODate | NaN |
| CashClearingSystemMember | NaN | NaN | Unique and unambiguous identifier for a clearing system member, as assigned by the clearing system. In some clearing systems, the accounts of the clearing system members are also assigned an identifier. The identifier can be used when transmitting, reconciling and confirming payment orders or security transfer instructions prior to settlement, and may include the netting of instructions and the establishment of final positions for settlement. | NaN | NaN |
| CashClearingSystemMember | OrganisationIdentification | NaN | Identification parameters which include clearing system member identification. | OrganisationIdentification | ClearingSystemMemberIdentificationType |
| CashClearingSystemMember | CHIPSUniversalIdentification | NaN | (United States) Clearing House Interbank Payments System (CHIPS) Universal Identification (UID) - identifies entities that own accounts at CHIPS participating financial institutions, through which CHIPS payments are effected. The CHIPS UID is assigned by the New York Clearing House. | CHIPSUniversalIdentifier | NaN |
| CashClearingSystemMember | NewZealandNCC | NaN | New Zealand Bank/Branch Code - identifies New Zealand institutions on the New Zealand national clearing system. The code is assigned by the New Zealand Bankers' Association (NZBA). | NewZealandNCCIdentifier | NaN |
| CashClearingSystemMember | IrishNSC | NaN | Irish National Sorting Code - identifies Irish financial institutions on the Irish national clearing system. The code is assigned by the Irish Payments Services Organisation (IPSO). | IrishNSCIdentifier | NaN |
| CashClearingSystemMember | UKSortCode | NaN | United Kingdom (UK) Sort Code - identifies British financial institutions on the British national clearing systems. The sort code is assigned by the Association for Payments and Clearing Services (APACS). | UKDomesticSortCodeIdentifier | NaN |
| CashClearingSystemMember | CHIPSParticipantIdentification | NaN | (United States) Clearing House Interbank Payment System (CHIPS) Participant Identifier (ID) - identifies financial institutions participating on CHIPS. The CHIPS Participant ID is assigned by the New York Clearing House. | CHIPSParticipantIdentifier | NaN |
| CashClearingSystemMember | SwissBC | NaN | Swiss Bank Code - identifies Swiss institutions on the Swiss national clearing system. | SwissBCIdentifier | NaN |
| CashClearingSystemMember | FedwireRoutingNumber | NaN | Fed wire Routing Number - identifies financial institutions, in the US, on the Fed wire system. The routing number is assigned by the American Bankers Association (ABA). | FedwireRoutingNumberIdentifier | NaN |
| CashClearingSystemMember | PortugueseNCC | NaN | Portuguese National Clearing Code - identifies Portuguese financial institutions on the Portuguese national clearing system. | PortugueseNCCIdentifier | NaN |
| CashClearingSystemMember | RussianCentralBankIdentificationCode | NaN | Russian Central Bank Identification Code - identifies Russian financial institutions on the Russian national clearing system. | RussianCentralBankIdentificationCodeIdentifier | NaN |
| CashClearingSystemMember | ItalianDomesticIdentificationCode | NaN | Italian Domestic Identification Code - identifies Italian financial institutions on the Italian national clearing system. The code is assigned by the Associazione Bancaria Italiana (ABI). | ItalianDomesticIdentifier | NaN |
| CashClearingSystemMember | AustrianBankleitzahl | NaN | Austrian Bankleitzahl - identifies Austrian financial institutions on the Austrian national clearing system. | AustrianBankleitzahlIdentifier | NaN |
| CashClearingSystemMember | CanadianPaymentsAssociationRoutingNumber | NaN | Canadian Payments Association Routing Number - identifies Canadian financial institutions on the Canadian national clearing system. | CanadianPaymentsARNIdentifier | NaN |
| CashClearingSystemMember | SwissSIC | NaN | Swiss Interbank Clearing (SIC) Code - identifies Swiss financial institutions domestically, on the Swiss national clearing system. | SwissSICIdentifier | NaN |
| CashClearingSystemMember | GermanBankleitzahl | NaN | German Bankleitzahl - identifies German financial institutions on the German national clearing systems. | GermanBankleitzahlIdentifier | NaN |
| CashClearingSystemMember | SpanishDomesticInterbankingCode | NaN | Spanish Domestic Interbanking Code - identifies Spanish financial institutions on the Spanish national clearing system. The code is assigned by the Centro de Cooperacion Interbancaria (CCI). | SpanishDomesticInterbankingIdentifier | NaN |
| CashClearingSystemMember | SouthAfricanNCC | NaN | South African National Clearing Code (NCC) - identifies South African financial institutions on the South African national clearing system. The code is assigned by the South African Bankers Services Company Ltd. (BankServ). | SouthAfricanNCCIdentifier | NaN |
| CashClearingSystemMember | HongKongBankCode | NaN | Hong Kong Bank Code - identifies Hong Kong financial institutions on the Hong Kong local clearing system. | HongKongBankIdentifier | NaN |
| CashClearingSystemMember | ClearingMember | NaN | Clearing system member for which a clearing system member identification is specified. | ClearingMemberRole | ClearingSystemMemberIdentification |
| CashClearingSystemMember | IndianFinancialSystemCode | NaN | Indian Financial System Code - identifies Indian financial institutions on the Indian local clearing system. | IndianFinancialSystemCodeIdentifier | NaN |
| CashClearingSystemMember | HellenicBankIdentificationCode | NaN | Hellenic Bank Identification Code - identifies Hellenic financial institutions on the Hellenic national clearing system. | HellenicBankIdentificationCodeIdentifier | NaN |
| CashClearingSystemMember | PolishNationalClearingCode | NaN | Polish National Clearing Code - identifies Polish financial institutions on the Polish national clearing system. | PolishNationalClearingCodeIdentifier | NaN |
| CashClearingSystemMember | AustralianBSBCode | NaN | Australian Bank State Branch (BSB) Code - identifies Australian financial institutions on the Australian national clearing system. The code is assigned by the Australian Payments Clearing Association (APCA). | AustralianBSBIdentification | ClearingSystemMemberIdentificationType |
| AustralianBSBIdentification | NaN | NaN | Australian Bank State Branch (BSB) Code - identifies Australian financial institutions on the Australian national clearing system. The code is assigned by the Australian Payments Clearing Association (APCA). | NaN | NaN |
| AustralianBSBIdentification | ExtensiveBranchNetworkIdentification | NaN | Extensive branch network list of the Australian Bank State Branch (BSB) Code. The codes are used for identifying Australian financial institutions, as assigned by the Australian Payments Clearing Association (APCA). | ExtensiveBranchNetworkIdentifier | NaN |
| AustralianBSBIdentification | SmallNetworkIdentification | NaN | Small network list of the Australian Bank State Branch (BSB) Code. The codes are used for identifying Australian financial institutions , as assigned by the Australian Payments Clearing Association (APCA). | SmallNetworkIdentifier | NaN |
| AustralianBSBIdentification | ClearingSystemMemberIdentificationType | NaN | Clearing system member identification for which an Australian BSB identification is provided. | CashClearingSystemMember | AustralianBSBCode |
| AustralianBSBIdentification | ClearingSystemMember | NaN | Clearing system for which an Australian code is provided. | NaN | NaN |
| Entry | NaN | NaN | Posting to an account that results in an increase or decrease to a balance. | NaN | NaN |
| Entry | CreditDebitIndicator | NaN | Indicates whether an entry is a credit or a debit. | DebitCreditCode | NaN |
| Entry | EntryDate | NaN | Date and time at which an entry is posted to an account on the account servicer's books. | ISODateTime | NaN |
| Entry | Identification | NaN | Unique and unambiguous identifier for an entry, as assigned by the account servicer. | Max35Text | NaN |
| Entry | AccountOwnerTransactionIdentification | NaN | Unambiguous identification of the transaction as known by the account owner (or the instructing party managing the account). | Max35Text | NaN |
| Entry | AccountServicerTransactionIdentification | NaN | Unambiguous identification of the transaction as known by the account servicer. | Max35Text | NaN |
| Entry | ReversalIndicator | NaN | Indicates whether or not the entry is the result of a reversal. | TrueFalseIndicator | NaN |
| Entry | ValueDate | NaN | Date and time assets become available to the account owner (in a credit entry), or cease to be available to the account owner (in a debit entry). | ISODateTime | NaN |
| Entry | BankTransactionCode | NaN | Type of underlying transaction resulting in the entry. | BankTransaction | RelatedEntry |
| Entry | CommissionWaiverIndicator | NaN | Indicates whether the transaction is exempt from commission or not. | YesNoIndicator | NaN |
| Entry | Role | NaN | Specifies the role played by a party or a system in the context of an entry in an account. | Role | Entry |
| Entry | Account | NaN | Posting of an item to an account, that results in an increase or a decrease to the balance of the account. | Account | Entry |
| Entry | Balance | NaN | Amount that is the result of the sum of the entries from or to an account. | Balance | BalanceEntry |
| Entry | EntryType | NaN | Specifies the type of an entry in a report. | EntryCode | NaN |
| CashEntry | NaN | Entry | Posting of an item to a cash account, in the context of a cash transaction, that results in an increase or decrease to the balance of the account. | NaN | NaN |
| CashEntry | CashAccount | NaN | Cash account on which the amount of the entry is debited or credited. It is derived from the association between Entry and Account. | CashAccount | CashEntry |
| CashEntry | Amount | NaN | Amount of money in the cash entry. | CurrencyAndAmount | NaN |
| CashEntry | RelatedBookEntry | NaN | Account entry for which one or more cash entries are specified. | BookEntry | CashEntry |
| CashEntry | CashBalance | NaN | Cash amount that is the result of the sum of the cash entries from or to a cash account. | CashBalance | CashBalanceEntry |
| CashEntry | CurrencyExchange | NaN | Entry details related to currency exchange information. | CurrencyExchange | CurrencyExchangeForCashEntry |
| CashEntry | Charges | NaN | Provides information on the charges included in the entry amount. | Charges | CashEntry |
| CashEntry | Availability | NaN | Availability information on the entry. Elements used to indicate when the booked amount of money will become available, that is can be accessed and start generating interest. | CashAvailability | CashEntry |
| CashEntry | Interest | NaN | Interest amount included in the entry amount. | Interest | CashEntry |
| CashEntry | DebitRelatedBookEntry | NaN | Book entry which is the source of the cash entry. | BookEntry | DebitEntry |
| CashEntry | CreditRelatedBookEntry | NaN | Book entry which is the source of the cash entry. | BookEntry | CreditEntry |
| CashEntry | RelatedInvoiceFinancingTransaction | NaN | Specifies the invoice financing transaction which originates the entry. | InvoiceFinancingAgreement | ResultingCashEntry |
| CashEntry | RelatedInvestigationCase | NaN | Case which is investigating a cash entry. | PaymentInvestigationCase | UnderlyingCashEntry |
| CashEntry | RelatedInvestigationCaseResolution | NaN | Payment investigation case resolution which created a correction resulting in a cash entry. | PaymentInvestigationCaseResolution | EntryCorrection |
| CashEntry | ChargesIncluded | NaN | Indicates whether charges have already been included in the entry amount. | ChargeIncludedIndicator | NaN |
| CreditInstrument | NaN | NaN | Specifies the instrument to be used for the credit of a payment. | NaN | NaN |
| CreditInstrument | RelatedPayment | NaN | Payment which uses the credit instrument. | Payment | CreditMethod |
| CreditInstrument | Method | NaN | Transfer method to be used for the transfer. | PaymentMethodCode | NaN |
| CreditInstrument | CreditInstrumentIdentification | NaN | Identifies the credit instrument. | Max35Text | NaN |
| CreditInstrument | NetAmount | NaN | Amount less fees and charges, that will be exchanged on settlement date of the trade. | CurrencyAndAmount | NaN |
| CreditInstrument | Deadline | NaN | Time by which the amount must be paid in. | ISODateTime | NaN |
| ChequeIssue | NaN | CreditInstrument | Action to issue a cheque in order to settle an amount due to a creditor. | NaN | NaN |
| ChequeIssue | Cheque | NaN | Specifies the characteristics of the cheque used to pay an amount to a creditor. | Cheque | ChequeDelivery |
| ChequeIssue | DeliveryMethod | NaN | Specifies the delivery method of the cheque by the debtor's agent. | ChequeDeliveryCode | NaN |
| ChequeIssue | DeliverTo | NaN | Identifies the party to whom the debtor's agent should send the cheque. | PostalAddress | ChequeIssue |
| ChequeIssue | PrintLocation | NaN | Specifies the print location of the cheque. | Max35Text | NaN |
| TradeIdentification | NaN | NaN | Specifies the different identifications associated with a trade. | NaN | NaN |
| TradeIdentification | CounterpartyReference | NaN | Unambiguous identification of the trade allocated by the counterparty. | Max35Text | NaN |
| TradeIdentification | Identification | NaN | Reference assigned to the trade by the investor or the trading party. This reference will be used throughout the trade life cycle to access/update the trade details. | Max35Text | NaN |
| TradeIdentification | CommonIdentification | NaN | Unique reference agreed upon by the two trade counterparties to identify the trade. | Max35Text | NaN |
| TradeIdentification | MatchingReference | NaN | Reference assigned by a matching system when the trade is matched. | Max35Text | NaN |
| TradeIdentification | Trade | NaN | Specifies the trade for which identifications are provided. | Trade | TradeRelatedIdentifications |
| TradeIdentification | UniqueTradeIdentifier | NaN | This field specifies the unique transaction identifier (UTI) to be created at the time a transaction is first executed, shared with all registered entities and counterparties involved in the transaction, and used to track that particular transaction over its life. This identifier can also be known as the Unique Swap Identifier (USI). | Max35Text | NaN |
| TradeIdentification | ClearingBrokerIdentification | NaN | Reference number assigned by the clearing broker. | ClearingBrokerIdentification | RelatedTradeIdentification |
| TradeIdentification | RelatedPostTradeRiskReduction | NaN | Post trade risk reduction for which the trade has been created. | PostTradeRiskReduction | PTRRIdentifier |
| TradeIdentification | RelatedEventIdentifier | NaN | Derivative event linked to the trade. | DerivativeEvent | EventIdentifier |
| SecuritiesTradeIdentification | NaN | TradeIdentification | Specifies the different identifications associated with a securities transaction. | NaN | NaN |
| SecuritiesTradeIdentification | IdentifiedTrade | NaN | Trade for which one or more identifications are provided. | SecuritiesTrade | SecuritiesTradeRelatedIdentifications |
| SecuritiesTradeIdentification | MarketInfrastructureTransactionIdentification | NaN | Identification of a transaction assigned by a market infrastructure other than a central securities depository, for example, Target2-Securities. | Max35Text | NaN |
| SecuritiesTradeIdentification | ProcessorTransactionIdentification | NaN | Identification of the transaction assigned by the processor of the instruction other than the account owner the account servicer and the market infrastructure. | Max35Text | NaN |
| SecuritiesTradeIdentification | PoolIdentification | NaN | Collective reference identifying a set of messages. | Max35Text | NaN |
| SecuritiesTradeIdentification | CollateralTransactionIdentification | NaN | Unambiguous identification of a collateral transaction. | Max35Text | NaN |
| SecuritiesTradeIdentification | ClientTripartyCollateralTransactionIdentification | NaN | Unique reference identifying the triparty collateral management transaction from the client's point of view. | Max35Text | NaN |
| SecuritiesTradeIdentification | TripartyAgentCollateralTransactionIdentification | NaN | Unique reference identifying the triparty collateral management transaction from the triparty agent's point of view. | Max35Text | NaN |
| SecuritiesTradeIdentification | BasketIdentification | NaN | Identification of a basket trade. | Max35Text | NaN |
| SecuritiesTradeIdentification | ProgramIdentification | NaN | Program reference which identifies a program trade. | Max35Text | NaN |
| SecuritiesTradeIdentification | BlockIdentification | NaN | Reference of the linked message at the trade/block level which identifies a centrally matched transaction. | Max35Text | NaN |
| SecuritiesTradeIdentification | AllocationIdentification | NaN | Identification at the allocation level. | Max35Text | NaN |
| SecuritiesTradeIdentification | ComplianceIdentification | NaN | Identification which represents this transaction for compliance purposes. | Max35Text | NaN |
| SecuritiesTradeIdentification | CSDTransactionIdentification | NaN | Identification given by the central securities depository to the transaction. | Max35Text | NaN |
| SecuritiesTradeIdentification | CentralCounterpartyTransactionIdentification | NaN | Identification of the transaction assigned by the central counterparty. | Max35Text | NaN |
| SecuritiesTradeIdentification | CancellationRequestIdentification | NaN | Unambiguous identification of the cancellation request as known by the instructing party. | Max35Text | NaN |
| SecuritiesTradeIdentification | CounterpartyMarketInfrastructureTransactionIdentification | NaN | Identification of a counterparty transaction assigned by a market infrastructure other than a central securities depository, for example, Target2-Securities. | Max35Text | NaN |
| InvestmentFundPartyRole | NaN | Role | Specifies roles played by a party that are linked to the handling of investment funds but not related to a specific process. | NaN | NaN |
| InvestmentFundPartyRole | Account | NaN | Unambiguous identification of the account used in the context of the investment fund party role such as intermediary's account, beneficiary's account... | Account | InvestmentFundPartyRole |
| InvestmentFundPartyRole | InvestmentFund | NaN | Specifies the fund for which the party plays a role. | InvestmentFund | PartyRole |
| Grantor | NaN | InvestmentFundPartyRole | Grantor role in the hedge funds industry. | NaN | NaN |
| Settlor | NaN | InvestmentFundPartyRole | Entity that creates a trust or contributes assets to the trust. | NaN | NaN |
| TradePartyRole | NaN | Role | Trading party in a commercial, securities, treasury trade. This role may also represent parties which play different intermediary roles in a trade. | NaN | NaN |
| TradePartyRole | Account | NaN | Unambiguous identification of the account used in the context of the party role. | Account | TradePartyRole |
| TradePartyRole | TradingPartyCapacity | NaN | Specifies the role of a trading party in a transaction. | TradingCapacityCode | NaN |
| TradePartyRole | BuyerOrSeller | NaN | Specifies the party which is the buyer or the seller. | OptionPartyCode | NaN |
| TradePartyRole | Trade | NaN | Trade in which a party plays a role. | Trade | TradePartyRole |
| InvestorRole | NaN | TradePartyRole | Party that makes investment decisions. Identifies the beneficiary or its broker. | NaN | NaN |
| InvestorRole | IndividualInvestor | NaN | Specifies whether the investor is a primary or the secondary individual investor. | RankCode | NaN |
| InvestorRole | CorporateInvestor | NaN | Specifies whether the investor is a primary or a secondary corporate investor. | RankCode | NaN |
| InvestorRole | Capacity | NaN | Specifies whether the investor is the primary, or the secondary account owner or another account owner. | EligibilityCode | NaN |
| InvestorRole | InvestorProtectionAssociationMembership | NaN | Indicates whether the confirmation party is a member of the investor protection association required, eg, as per regulation. | YesNoIndicator | NaN |
| InvestorRole | Type | NaN | Specifies whether the investor is a corporate or an individual | InvestorTypeCode | NaN |
| AccountServicerRole | NaN | AccountPartyRole | Party that manages the account on behalf of the account owner, that is manages the registration and booking of entries on the account, calculates balances on the account and provides information about the account. | NaN | NaN |
| AccountServicerRole | RelatedPTRR | NaN | Post trade risk reduction that is serviced. | PostTradeRiskReduction | ServiceProvider |
| SecuritiesQuantity | NaN | NaN | Quantity of a security. | NaN | NaN |
| SecuritiesQuantity | Unit | NaN | Quantity of a security. | DecimalNumber | NaN |
| SecuritiesQuantity | SecuritiesTransfer | NaN | Transfer of a specific quantity of securities. | SecuritiesTransfer | TransferredQuantity |
| SecuritiesQuantity | SecurityIdentification | NaN | Identifies the security. | Security | SecuritiesQuantity |
| SecuritiesQuantity | Order | NaN | Order for which a number of units is specified. | InvestmentFundOrder | UnitsNumber |
| SecuritiesQuantity | Group1Or2Units | NaN | Tax group to which the purchased units belong. | UKTaxGroupUnitCode | NaN |
| SecuritiesQuantity | RelatedOrderExecution | NaN | Order execution process for which a number of units is specified. | InvestmentFundOrderExecution | UnitsNumber |
| SecuritiesQuantity | SecuritiesSettlement | NaN | Settlement of a specific amount of securities. | SecuritiesSettlement | SettlementQuantity |
| SecuritiesQuantity | MinimumQuantityDebt | NaN | Security for which a minimum quantity is specified. | Security | MinimumQuantity |
| SecuritiesQuantity | LotBreakdown | NaN | Number of securities purchased or sold in one transaction. In terms of options, a lot represents the number of contracts contained in one derivative security. | LotBreakdown | SecuritiesQuantity |
| SecuritiesQuantity | MinimumExercisableQuantitySecuritiesConversion | NaN | Securities conversion process for which a minimum exercisable quantity is specified. | SecuritiesConversion | MinimumExercisableQuantity |
| SecuritiesQuantity | MinimumExercisableMultipleQuantitySecuritiesConversion | NaN | Securities conversion process for which a minimum exercisable multiple quantity is specified. | SecuritiesConversion | MinimumExercisableMultipleQuantity |
| SecuritiesQuantity | AggregateQuantityBalance | NaN | Securities balance which contains the aggregate quantity. | SecuritiesBalance | AggregateQuantity |
| SecuritiesQuantity | SecuritiesProceedsDefinition | NaN | Securities proceeds for which an amount of securities is posted. | SecuritiesProceedsDefinition | SecuritiesQuantity |
| SecuritiesQuantity | ConditionalQuantitySecuritiesProceeds | NaN | Securities proceeds for which a conditional quantity has been defined. | SecuritiesProceedsDefinition | ConditionalQuantity |
| SecuritiesQuantity | OverAndAboveQuantitySecuritiesProceeds | NaN | Securities proceeds for which an over and above normal endured quantity has been provided. | SecuritiesProceedsDefinition | OverAndAboveNormalEnsuredEntitlementQuantity |
| SecuritiesQuantity | Entry | NaN | Entry in a securities account of a specific quantity of securities. | SecuritiesEntry | FinancialInstrumentQuantity |
| SecuritiesQuantity | Code | NaN | Quantity expressed as a code. | QuantityCode | NaN |
| SecuritiesQuantity | ExpectedQuantitySecuritiesProceeds | NaN | Securities proceeds for which a quantity of securities to receive has been specified. | SecuritiesProceedsDefinition | QuantityToReceive |
| SecuritiesQuantity | StatusRelatedSecuritiesProceeds | NaN | Securities proceeds related to securities with a specific status. | SecuritiesProceedsDefinition | StatusQuantity |
| SecuritiesQuantity | CorporateActionDistribution | NaN | Corporate action distribution process for which a quantity of securities has been posted. | CorporateActionDistribution | PostingQuantity |
| SecuritiesQuantity | RelatedEventForFractionalQuantity | NaN | Event for which the resulting fractional quantity will be paid with cash in lieu. | CorporateActionEvent | FractionalQuantity |
| SecuritiesQuantity | MaximumExercisableQuantitySecuritiesConversion | NaN | Securities conversion process for which a maximum exercisable quantity is specified. | SecuritiesConversion | MaximumExercisableQuantity |
| SecuritiesQuantity | BoardLotSecuritiesProceeds | NaN | Securities proceeds related to a board lot. | SecuritiesProceedsDefinition | BoardLotSecuritiesQuantity |
| SecuritiesQuantity | NewDenominationSecuritiesProceeds | NaN | Securities proceeds related to a quantity of redenominated securities. | SecuritiesProceedsDefinition | NewDenominationSecuritiesQuantity |
| SecuritiesQuantity | BackEndOddLotBiddingConditions | NaN | BiddingConditions for which a back end odd lot is provided. | BiddingConditions | BackEndOddLotQuantity |
| SecuritiesQuantity | SecuritiesEntitlement | NaN | Specifies the entitlement parameters relative to the securities entitlement. | CorporateActionSecuritiesEntitlement | EntitledSecuritiesQuantity |
| SecuritiesQuantity | CorporateActionEvent | NaN | Corporate action for which a quantity of securities is specified. | CorporateActionEvent | SecuritiesQuantity |
| SecuritiesQuantity | BiddingConditions | NaN | Bidding conditions related to the base denomination quantity. | BiddingConditions | BaseDenomination |
| SecuritiesQuantity | Lottery | NaN | Lottery for which an incremental denomination is specified. | Lottery | IncrementalDenomination |
| SecuritiesQuantity | RelatedSubBalance | NaN | Sub balance which contains a quantity of securities. | SecuritiesBalance | SubBalanceQuantity |
| SecuritiesQuantity | AvailableQuantityBalance | NaN | Securities balance which contains the securities quantity. | SecuritiesBalance | AvailableQuantity |
| SecuritiesQuantity | Trade | NaN | Trade for which a quantity is specified. | SecuritiesTrade | TradeQuantity |
| SecuritiesQuantity | RatioDenominatorSecuritiesConversion | NaN | Securities conversion process for which a conversion ratio denominator quantity is specified. | SecuritiesConversion | ConversionRatioDenominator |
| SecuritiesQuantity | RatioNumeratorSecuritiesConversion | NaN | Securities conversion process for which a conversion ratio denominator quantity is specified. | SecuritiesConversion | ConversionRatioNumerator |
| SecuritiesQuantity | MinimumTradedQuantityMarket | NaN | Market for which a minimum traded quantity is specified. | TradingMarket | MinimumTradedNominalQuantity |
| SecuritiesQuantity | MinimumDenominationDebt | NaN | Debt for which a minimum denomination is specified. | Debt | MinimumDenomination |
| SecuritiesQuantity | MinimumIncrementDebt | NaN | Debt for which a minimum increment is specified. | Debt | MinimumIncrement |
| SecuritiesQuantity | RelatedOrder | NaN | Order for which a specific quantity is requested. | SecuritiesOrder | OrderedQuantity |
| SecuritiesQuantity | Allocation | NaN | Allocation process for which a quantity is specified. | Allocation | AllocatedQuantity |
| SecuritiesQuantity | Amount | NaN | Quantity expressed as an amount, eg, in the investment fund business, a quantity of a financial instrument may be expressed as an amount of money. | CurrencyAndAmount | NaN |
| SecuritiesQuantity | DenominatorRatio | NaN | Ratio for which a denominator is specified. | UnderlyingRatio | UnderlyingQuantityDenominator |
| SecuritiesQuantity | NumeratorRatio | NaN | Ratio for which a numerator is specified. | UnderlyingRatio | UnderlyingQuantityNumerator |
| SecuritiesQuantity | SecuritiesTradeExecution | NaN | Trade for which settlement takes place. | SecuritiesTradeExecution | ExecutedTradeQuantity |
| SecuritiesQuantity | RelatedCorporateActionEvent | NaN | Corporate action for which the offeror/issuer has specified a quantity of securities to purchase or redeem under the terms of the event. | CorporateActionEvent | SecuritiesQuantitySought |
| SecuritiesQuantity | CorporateActionElection | NaN | Election process which selected a quantity of securities. | CorporateActionElection | Quantity |
| SecuritiesQuantity | TaxVoucher | NaN | Tax voucher for which the calculation of holdings at record date took place. | TaxVoucher | RecordDateHolding |
| SecuritiesQuantity | RelatedBuyIn | NaN | Buy-in process for which a compensation amount of securities is specified. | BuyIn | SecuritiesCompensation |
| SecuritiesQuantity | PreviousDayOrder | NaN | Securities order which uses information on a day order quantity. | SecuritiesOrder | DayOrderQuantity |
| SecuritiesQuantity | Liquidity | NaN | Liquidity information related to a quantity of a financial instrument. | Liquidity | Quantity |
| SecuritiesQuantity | Rate | NaN | Quantity expressed as a percentage rate, eg, in the investment fund business, a quantity of a financial instrument may be expressed as percentage of the investor's total holding. | PercentageRate | NaN |
| SecuritiesQuantity | MinimumQuantityOrderParameters | NaN | Securities order for which a minimum quantity to execute is specified. | SecuritiesOrderParameters | MinimumQuantity |
| SecuritiesQuantity | MaximumQuantityRelatedQuote | NaN | Quote process for which a maximum quantity of securities is specified. | Quote | MaximumQuantity |
| SecuritiesQuantity | UnavailableQuantityBalance | NaN | Securities balance which contains the unavailable quantity. | SecuritiesBalance | UnavailableQuantity |
| SecuritiesQuantity | MatchIncrementOrderParameters | NaN | Securities order parameters for which a match increment quantity is provided. | SecuritiesOrderParameters | MatchIncrement |
| SecuritiesQuantity | RelatedIssuance | NaN | Issuance for which a minimum subscription quantity of securities is specified. | Issuance | Minimum |
| SecuritiesQuantity | Pairoff | NaN | Pair off process for which a quantity has been specified. | PairOff | PairedOffQuantity |
| SecuritiesQuantity | Issuance | NaN | Issuance for which the nominal amount is specified. | Issuance | IssueNominalAmount |
| SecuritiesQuantity | IntermediateToUnderlyingDenominatorDistributionInformation | NaN | Cash and securities distribution information for which an intermediate to underlying denominator quantity is specified. | SecuritiesAndCashDistribution | IntermediateToUnderlyingDenominator |
| SecuritiesQuantity | MaximumHoldingDistributionInformation | NaN | Cash and securities distribution information for which a maximum holding quantity is specified. | SecuritiesAndCashDistribution | MaximumHolding |
| SecuritiesQuantity | MaximumExercisableQuantityDistributionInformation | NaN | Cash and securities distribution information for which a maximum exercisable quantity is specified. | SecuritiesAndCashDistribution | MaximumExercisableQuantity |
| SecuritiesQuantity | MinimumExercisableQuantityDistributionInformation | NaN | Cash and securities distribution information for which a minimum exercisable quantity is specified. | SecuritiesAndCashDistribution | MinimumExercisableQuantity |
| SecuritiesQuantity | DistributedToUnderlyingDenominatorDistributionInformation | NaN | Cash and securities distribution information for which a distributed to underlying denominator quantity is specified. | SecuritiesAndCashDistribution | DistributedToUnderlyingDenominator |
| SecuritiesQuantity | IntermediateToUnderlyingNumeratorDistributionInformation | NaN | Cash and securities distribution information for which an intermediate to underlying numerator quantity is specified. | SecuritiesAndCashDistribution | IntermediateToUnderlyingNumerator |
| SecuritiesQuantity | MinimumHoldingDistributionInformation | NaN | Cash and securities distribution information for which a minimum holding quantity is specified. | SecuritiesAndCashDistribution | MinimumHolding |
| SecuritiesQuantity | DistributedToUnderlyingNumeratorDistributionInformation | NaN | Cash and securities distribution information for which a distributed to underlying numerator quantity is specified. | SecuritiesAndCashDistribution | DistributedToUnderlyingNumerator |
| SecuritiesQuantity | MaximumHoldingRelatedSecuritiesDistribution | NaN | Securities distribution for which a maximum holding quantity is provided. | SecuritiesDistribution | MaximumHolding |
| SecuritiesQuantity | IntermediateToUnderlyingNumeratorRelatedSecuritiesDistribution | NaN | Securities distribution for which an intermediate to underlying numerator quantity is provided. | SecuritiesDistribution | IntermediateToUnderlyingNumerator |
| SecuritiesQuantity | IntermediateToUnderlyingDenominatorRelatedSecuritiesDistribution | NaN | Securities distribution for which an intermediate to underlying denominator quantity is provided. | SecuritiesDistribution | IntermediateToUnderlyingDenominator |
| SecuritiesQuantity | DistributedToUnderlyingDenominatorRelatedSecuritiesDistribution | NaN | Securities distribution for which a distributed to underlying denominator quantity is provided. | SecuritiesDistribution | DistributedToUnderlyingDenominator |
| SecuritiesQuantity | DistributedToUnderlyingNumeratorRelatedSecuritiesDistribution | NaN | Securities distribution for which a distributed to underlying numerator quantity is provided. | SecuritiesDistribution | DistributedToUnderlyingNumerator |
| SecuritiesQuantity | MinimumHoldingRelatedSecuritiesDistribution | NaN | Securities distribution for which a minimum holding quantity is provided. | SecuritiesDistribution | MinimumHolding |
| SecuritiesQuantity | MaximumTradedQuantityMarket | NaN | Market for which a maximum traded quantity is specified. | TradingMarket | MaximumTradedNominalQuantity |
| SecuritiesQuantity | QuantityRelatedQuote | NaN | Quote process for which a quantity of securities is specified. | Quote | Quantity |
| SecuritiesQuantity | MinimumQuantityRelatedQuote | NaN | Quote process for which a minimum quantity of securities is specified. | Quote | MinimumQuantity |
| SecuritiesQuantity | NetAssetValueCalculation | NaN | Net asset value calculation parameters. | NetAssetValueCalculation | SecuritiesQuantity |
| SecuritiesQuantity | SidePocket | NaN | Side pocket for which a quantity is specified. | SidePocket | SidePocketQuantity |
| SecuritiesQuantity | Netting | NaN | Netting process for which a net quantity of securities has been calculated. | Netting | NetQuantity |
| SecuritiesQuantity | RelatedOrderStatus | NaN | Order status for which a remaining quantity is specified. | SecuritiesOrderStatus | RemainingQuantity |
| SecuritiesQuantity | SecuritiesOrderStatus | NaN | Order status for which a cumulative quantity is specified. | SecuritiesOrderStatus | CumulativeQuantity |
| SecuritiesQuantity | RelatedTurnaroundSettlement | NaN | Securities settlement process for which a turned quantity is specified. | SecuritiesSettlement | TurnedQuantity |
| SecuritiesQuantity | RelatedCashFlow | NaN | Cash flow for which quantities are specified. | FundsCashFlow | CashFlowQuantity |
| SecuritiesQuantity | Position | NaN | Position which contains the net quantity. | Position | NetQuantity |
| SecuritiesQuantity | MaximumQuantityBiddingConditions | NaN | Bidding conditions for which a maximum quantity is specified. | BiddingConditions | MaximumQuantity |
| SecuritiesQuantity | FrontEndOddLotBiddingConditions | NaN | Bidding conditions for which a front end odd lot is specified. | BiddingConditions | FrontEndOddLotQuantity |
| SecuritiesQuantity | MinimumQuantityBiddingConditions | NaN | Bidding conditions for which a minimum quantity is specified. | BiddingConditions | MinimumQuantitySought |
| SecuritiesQuantity | RelatedCorporateActionProtectProcess | NaN | Protect process which selected a quantity of securities. | CorporateActionProtectProcess | UncoveredProtectQuantity |
| SecuritiesQuantity | DigitalTokenUnit | NaN | Quantity of digital tokens expressed as a number, for example, a number of blockchain tokens. | DecimalNumber | NaN |
| SecuritiesTrade | NaN | Trade | Specifies trades linked to securities operations such as the exchange of securities, the lending of securities and the transactions related to investment funds. | NaN | NaN |
| SecuritiesTrade | SecuritiesTradeRelatedIdentifications | NaN | Specifies the different identifications associated with a securities trade. | SecuritiesTradeIdentification | IdentifiedTrade |
| SecuritiesTrade | TradeAmount | NaN | Total amount of the trade. Is equal to the executed trade quantity multiplied by the executed trade price. | CurrencyAndAmount | NaN |
| SecuritiesTrade | OpeningClosingIndicator | NaN | Specifies additional information relative to the processing of the trade. | OpeningClosingCode | NaN |
| SecuritiesTrade | TradeTransactionCondition | NaN | Indicates the conditions under which the order/trade is to be/was executed. | TradeTransactionConditionCode | NaN |
| SecuritiesTrade | SecuritiesTradeStatus | NaN | Specifies the status of a trade. | SecuritiesTradeStatus | SecuritiesTrade |
| SecuritiesTrade | Activity | NaN | Specifies the type of activity to which the trade relates. | TransactionActivityCode | NaN |
| SecuritiesTrade | TradeQuantity | NaN | Specifies the total quantity of a financial instrument involved in a trade. It is derived from the ordered quantity or from the quantity specified in a leg of a financing agreement. | SecuritiesQuantity | Trade |
| SecuritiesTrade | TradeOriginationDate | NaN | Indicates the date and time of the agreement in principal between counter-parties prior to actual trade date.Used with fixed income for municipal new issue markets. | ISODateTime | NaN |
| SecuritiesTrade | ClearingFeeType | NaN | Indicates the type of fee for trade executions at an exchange. | ClearingFeeTypeCode | NaN |
| SecuritiesTrade | Security | NaN | Security involved in a trade. | Security | SecuritiesTrade |
| SecuritiesTrade | TradePrice | NaN | Specifies the executed trade price which is derived from the different deal prices. | SecuritiesPricing | SecuritiesTrade |
| SecuritiesTrade | PartyRole | NaN | Specifies each role linked to a securities trade and played by a party at that step in a securities transaction flow. | SecuritiesTradePartyRole | SecuritiesTrade |
| SecuritiesTrade | SecuritiesFinancingClosingData | NaN | Financing process for which a closing leg is specified. | SecuritiesFinancing | ClosingLegExecution |
| SecuritiesTrade | TradingExecution | NaN | The realisation of the trade over one or more transactions. | SecuritiesTradeExecution | RelatedTrade |
| SecuritiesTrade | TradeAllocation | NaN | Information about the allocation of the trade. | Allocation | SecuritiesTrade |
| SecuritiesTrade | RelatedOrder | NaN | Order which is executed by a trade. | SecuritiesOrder | OrderExecution |
| SecuritiesTrade | SecuritiesFinancingOpeningData | NaN | Financing process for which an opening leg is specified. | SecuritiesFinancing | OpeningLegExecution |
| SecuritiesTrade | TransactionType | NaN | Indicates the type of transaction of which the order is a component. | TradeTypeCode | NaN |
| SecuritiesTrade | LegalFramework | NaN | Legal framework of the transaction. | LegalFrameworkCode | NaN |
| SecuritiesTrade | SecuritiesTransactionType | NaN | Underlying information about the settlement transaction. | SecuritiesTransactionTypeV2Code | NaN |
| InvestmentFundTransaction | NaN | SecuritiesTrade | Process of buying, selling, switching or transferring fund units. | NaN | NaN |
| InvestmentFundTransaction | InvestmentFundOrder | NaN | An investor's instruction to either subscribe or redeem an amount of money or its equivalent, eg, other assets, into or out of an investment fund. | InvestmentFundOrder | RelatedTransaction |
| InvestmentFundTransaction | ClientReference | NaN | Unique and unambiguous investor's identification of an order assigned by a client. | Max35Text | NaN |
| InvestmentFundTransaction | Type | NaN | Type of investment fund transaction. | InvestmentFundTransactionTypeCode | NaN |
| InvestmentFundTransaction | TransactionCharge | NaN | Charge for the placement of an order and/or for its execution. | Charges | InvestmentFundTransaction |
| InvestmentFundTransaction | InvestmentAccount | NaN | Account related to an investment fund transaction. | InvestmentAccount | InvestmentFundTransaction |
| InvestmentFundTransaction | InvestmentFundClass | NaN | Investment fund class to which an investment fund order and its execution are related. | InvestmentFundClass | InvestmentFundTransaction |
| InvestmentFundTransaction | TransactionTax | NaN | Tax applicable to an investment fund order and/or to its execution. | InvestmentFundTax | Transaction |
| InvestmentFundTransaction | CreditDebitIndicator | NaN | Direction of the transaction, ie, securities are received (credited) or delivered (debited). | DebitCreditCode | NaN |
| InvestmentFundTransaction | InvestmentFundOrderExecution | NaN | Creation/cancellation of investment units on the books of the fund or its designated agent, as a result of executing an investment fund order. | InvestmentFundOrderExecution | InvestmentFundTransaction |
| StatusReason | NaN | NaN | Specifies the underlying reason for the status of an object. | NaN | NaN |
| StatusReason | Status | NaN | Status for which a reason is provided. | Status | StatusReason |
| StatusReason | Reason | NaN | Reason provided for the status. | Max35Text | NaN |
| StatusReason | NoSpecifiedReason | NaN | Indicates that there is no reason available or to report. | NoReasonCode | NaN |
| StatusReason | DataSourceScheme | NaN | Proprietary identification of the reason for the status. | GenericIdentification | RelatedStatusReason |
| StatusReason | RejectedStatusReason | NaN | Reason for the rejected status. | RejectedStatusReasonCode | NaN |
| StatusReason | FailingReason | NaN | Reason why a transaction has a failing status. | PendingFailingReasonCode | NaN |
| StatusReason | CancellationReason | NaN | Specifies the reason why the related instruction is cancelled, or the related cancellation request is executed. | CancelledStatusReasonV2Code | NaN |
| StatusReason | PendingReason | NaN | Specifies the reason why the instruction processing is pending. | PendingFailingReasonCode | NaN |
| StatusReason | RejectionReason | NaN | Specifies the reason why the instruction/request has a repair or rejection status. | RejectionReasonV3Code | NaN |
| StatusReason | AcknowledgedAcceptedReason | NaN | Specifies additional information about the processed instruction. | AcknowledgementReasonCode | NaN |
| StatusReason | RelatedClosureReason | NaN | Related reason of closure of the contract. | RegisteredContract | ClosureReason |
| Cheque | NaN | FinancialDocument | Negotiable instrument instructing a financial institution to pay a specific amount of a specific currency from the account of the drawer with that institution. | NaN | NaN |
| Cheque | ChequeDelivery | NaN | Specifies the parameters related to the delivery of the cheque. | ChequeIssue | Cheque |
| Cheque | Number | NaN | Unique and unambiguous identifier for a cheque as assigned by the financial institution. | Max35Text | NaN |
| Cheque | ChequeType | NaN | Specifies the type of cheque. | ChequeTypeCode | NaN |
| Cheque | MaturityDate | NaN | Date when the draft becomes payable and the debtor's account is debited. | ISODate | NaN |
| Cheque | FormsCode | NaN | Code agreed between the initiating party and the debtor's agent, that specifies the cheque layout, company logo and digitised signature to be used to print the cheque. | Max35Text | NaN |
| Cheque | MemoField | NaN | Information that needs to be printed on a cheque, used by the payer to add miscellaneous information. | Max35Text | NaN |
| Cheque | RegionalClearingZone | NaN | Regional area in which the cheque can be cleared, when a country has no nation-wide cheque clearing organisation. | Max35Text | NaN |
| Cheque | RelatedPayment | NaN | Payment which uses a cheque. | ChequePayment | Cheque |
| Cheque | ChequePartyRole | NaN | Specifies each role played by a party in the process of paying by cheque. | ChequePartyRole | Cheque |
| Cheque | CashAccount | NaN | Cash account on which a cheque is drawn. | CashAccount | Cheque |
| InsuranceCertificate | NaN | Document | Formal document used to record a fact and used as proof of the fact that goods have been insured under an insurance policy. | NaN | NaN |
| InsuranceCertificate | EffectiveDate | NaN | Date upon which cover under an insurance policy becomes effective. | ISODate | NaN |
| InsuranceCertificate | InsuredAmount | NaN | Value of the goods as insured under the insurance policy. | CurrencyAndAmount | NaN |
| InsuranceCertificate | InsuranceConditions | NaN | Description of the conditions and exclusion clauses under which insurance is granted. | Max350Text | NaN |
| InsuranceCertificate | InsuranceClauses | NaN | Standard insurance clauses defined by the Institute of London Underwriters (or the American Institute of marine Underwriters). | InsuranceClausesCode | NaN |
| InsuranceCertificate | ClaimsPayableAt | NaN | Place where claims under the insurance policy will be paid. | Location | InsuranceCertificate |
| InsuranceCertificate | ClaimsPayableIn | NaN | Currency in which claims, if valid, will be paid. | CurrencyCode | NaN |
| InsuranceCertificate | InsurancePartyRole | NaN | Role played by a party in the context of insurance. | InsurancePartyRole | InsuranceCertificate |
| InsuranceCertificate | ProductDelivery | NaN | Delivery parameters of a trade. | ProductDelivery | InsuranceCertificate |
| InsuranceCertificate | InsuranceType | NaN | Specifies the type of insurance. | InsuranceCode | NaN |
| InsuranceCertificate | RelatedInvestmentPlan | NaN | Investment plan covered by an insurance contract. | InvestmentPlan | Insurance |
| SecuritiesTransfer | NaN | ObligationFulfilment | Completion of a securities settlement instruction, wherein securities are delivered/debited from a securities account and received/credited to the designated securities account. | NaN | NaN |
| SecuritiesTransfer | Identification | NaN | Unique and unambiguous identification of a transfer, as assigned by the instructing party. | Max35Text | NaN |
| SecuritiesTransfer | TransferredQuantity | NaN | Total quantity of securities settled. | SecuritiesQuantity | SecuritiesTransfer |
| SecuritiesTransfer | Account | NaN | Specifies the account from/to which the securities are transferred. | SecuritiesAccount | RelatedTransfer |
| SecuritiesTransfer | TransferType | NaN | Specifies whether the financial instrument is transferred as an asset or as cash. | TransferTypeCode | NaN |
| SecuritiesTransfer | RelatedSettlement | NaN | Settlement process which is the source of the transfer operation. | SecuritiesSettlement | TransferOperation |
| SecuritiesTransfer | OwnAccountTransferIndicator | NaN | Indicates whether the transfer results in a change of beneficial owner. | YesNoIndicator | NaN |
| SecuritiesTransfer | PhysicalDelivery | NaN | Information related to physical delivery of the securities. | PhysicalDelivery | RelatedTransfer |
| SecuritiesTransfer | LateDeliveryDate | NaN | Date and time after the settlement date specified in the trade, used for pool trades resulting from the original To Be Assigned (TBA) securities. | ISODateTime | NaN |
| SecuritiesTransfer | TransferTax | NaN | Tax related to the transfer of a financial instrument. | Tax | SecuritiesTransfer |
| SecuritiesTransfer | TransferReason | NaN | Identifies the transfer reason. | TransferReasonCode | NaN |
| SecuritiesTransfer | PartialSettlementType | NaN | Information about partial settlement. | PartialSettlementCode | NaN |
| SecuritiesTransfer | SecuritiesDeliveryObligation | NaN | Obligation for one party to deliver securities to another party. | SecuritiesDeliveryObligation | SecuritiesTransfer |
| SecuritiesTransfer | BookEntry | NaN | Record in a securities account resulting from the transfer of a security. | SecuritiesEntry | TriggeringSecuritiesTransfer |
| SecuritiesTransfer | TransactionIdentification | NaN | Unambiguous identification of a securities transfer. | Max35Text | NaN |
| SecuritiesTransfer | Security | NaN | Security which is transferred. | Security | SecuritiesTransfer |
| SecuritiesTransfer | Status | NaN | Status of a securities transfer. | SecuritiesTradeStatus | RelatedSecuritiesTransfer |
| PortfolioTransfer | NaN | NaN | Transfer by the delivering account servicer to the receiving account servicer of a retail or institutional client portfolio. A portfolio can be any grouping of investments, for example stocks, bonds, options, warrants. held by an institution or an individual. | NaN | NaN |
| PortfolioTransfer | TransferredYear | NaN | Specifies the year during which the investment plan to be transferred was issued. | ISOYear | NaN |
| PortfolioTransfer | CashComponentIndicator | NaN | Indicates whether an ISA investment plan contains a cash component asset for transfer. | YesNoIndicator | NaN |
| PortfolioTransfer | AccountFrom | NaN | Specifies the account owned by an investor and from which the assets are transferred. | InvestmentAccount | DebitPortfolioTransfer |
| PortfolioTransfer | AccountTo | NaN | Specifies the account owned by an investor and to which the assets are transferred. | InvestmentAccount | CreditPortfolioTransfer |
| PortfolioTransfer | PaymentObligation | NaN | Specifies the cash amount to be transferred in relation with a portfolio transfer. | PaymentObligation | PaymentSourcePortfolioTransfer |
| PortfolioTransfer | TransferredPortfolio | NaN | Specifies the portfolio which has to be transferred. | Portfolio | Transfer |
| PortfolioTransfer | SecuritiesDeliveryObligation | NaN | Specifies the financial instrument to be transferred in relation with a portfolio transfer. | SecuritiesDeliveryObligation | RelatedPortfolioTransfer |
| PortfolioTransfer | TransferredAmount | NaN | Quantity of financial instrument to transfer expressed as an amount of money. | CurrencyAndAmount | NaN |
| PortfolioTransfer | TransferredPercentage | NaN | Quantity of financial instrument to transfer expressed as a percentage of the investor's total holding. | PercentageRate | NaN |
| PortfolioTransfer | TransferDate | NaN | Execution date of the transfer instruction. | ISODateTime | NaN |
| PortfolioTransfer | NomineeAccount | NaN | Account held in the name of a party that is not the name of the beneficial owner of the shares. | InvestmentAccount | RelatedPortfolioTransfer |
| PortfolioTransfer | PEPOrISAPlan | NaN | Specifies whether the investment plan is a PEP or ISA type. | PEPISACode | NaN |
| PortfolioTransfer | CurrentYearISAType | NaN | Current year ISA is an ISA that was issued during the current fiscal year. | ISATypeCode | NaN |
| InvestmentFundOrderExecution | NaN | SecuritiesTradeExecution | Creation/cancellation of investment units on the books of the fund or its designated agent, as a result of executing an investment fund order. | NaN | NaN |
| InvestmentFundOrderExecution | UnitsNumber | NaN | Number of investment fund units subscribed or redeemed. | SecuritiesQuantity | RelatedOrderExecution |
| InvestmentFundOrderExecution | NonStandardSettlementInformation | NaN | Additional specific settlement information for non-regulated traded funds. | Max350Text | NaN |
| InvestmentFundOrderExecution | Order | NaN | Order which is executed. | InvestmentFundOrder | InvestmentFundOrderExecution |
| InvestmentFundOrderExecution | DealIdentification | NaN | Unique and unambiguous identifier for an order execution, as assigned by a confirming party. | Max35Text | NaN |
| InvestmentFundOrderExecution | ExecutedTradePrice | NaN | Price at which the order was executed. | SecuritiesPricing | FundOrderRelatedToExecutedPrice |
| InvestmentFundOrderExecution | PartiallyExecutedIndicator | NaN | Indicates whether the order has been partially executed, ie, the confirmed quantity does not match the ordered quantity for a given financial instrument. | YesNoIndicator | NaN |
| InvestmentFundOrderExecution | InterimProfitAmount | NaN | Part of the price deemed as accrued income or profit rather than capital. The interim profit amount is used for tax purposes. | CurrencyAndAmount | NaN |
| InvestmentFundOrderExecution | InformativePrice | NaN | Other quoted price than the one at which the order was executed. | SecuritiesPricing | FundOrderRelatedToInformativePrice |
| InvestmentFundOrderExecution | BestExecution | NaN | Specifies that the execution was subject to best execution rules as defined by MiFID. | BestExecutionCode | NaN |
| InvestmentFundOrderExecution | PartialSettlementOfUnits | NaN | Percentage of units partially settled. | PercentageRate | NaN |
| InvestmentFundOrderExecution | PartialSettlementOfCash | NaN | Percentage of cash partially settled. | PercentageRate | NaN |
| InvestmentFundOrderExecution | LateReport | NaN | Specifies whether the order execution confirmation is late. | LateReportCode | NaN |
| InvestmentFundOrderExecution | SettledIndicator | NaN | Indicates whether the cash payment with respect to the executed order is settled. | YesNoIndicator | NaN |
| InvestmentFundOrderExecution | RegisteredIndicator | NaN | Indicates whether the executed order has a registered status on the books of the transfer agent. | YesNoIndicator | NaN |
| InvestmentFundOrderExecution | ExecutedAmount | NaN | Amount of money invested or redeemed as a result of an investment fund order. | CurrencyAndAmount | NaN |
| InvestmentFundOrderExecution | InvestmentFundTransaction | NaN | Transaction which is executed. | InvestmentFundTransaction | InvestmentFundOrderExecution |
| InvestmentFundOrderExecution | CashFlow | NaN | Specifies the cash flow resulting from the execution of an order. | FundsCashFlow | RelatedOrder |
| InvestmentFundOrderExecution | SourceOfCash | NaN | Source of cash used for the settlement of the execution. | SourceOfCashCode | NaN |
| SubscriptionExecution | NaN | InvestmentFundOrderExecution | Execution of a subscription order. | NaN | NaN |
| SubscriptionExecution | EquityComponent | NaN | Amount subscribed into equity (not including dividends). | CurrencyAndAmount | NaN |
| SubscriptionExecution | CashComponent | NaN | Amount subscribed into cash. | CurrencyAndAmount | NaN |
| SubscriptionExecution | InvestedNetAmount | NaN | Net amount of money invested in a specific financial instrument by an investor, expressed in the currency requested by the investor. | CurrencyAndAmount | NaN |
| SubscriptionExecution | Refund | NaN | Return of cash that has been overpaid for a subscription. | CurrencyAndAmount | NaN |
| SubscriptionExecution | SubscriptionInterest | NaN | Interest received when a subscription amount is paid in advance and then invested by the fund. | CurrencyAndAmount | NaN |
| SubscriptionExecution | TaxEfficientProduct | NaN | Characteristics of a tax efficient product. | TaxEfficientProduct | CurrentYearSubscription |
| Portfolio | NaN | NaN | Wrapper for a specific product or a specific sub-product owned by a set of beneficial owners. | NaN | NaN |
| Portfolio | Valuation | NaN | Valuation process for the portfolio. | PortfolioValuation | Portfolio |
| Portfolio | Transfer | NaN | Transfer information related to a portfolio. | PortfolioTransfer | TransferredPortfolio |
| Portfolio | AssetDescription | NaN | Specifies the assets included in the portfolio together with their value. | Asset | Portfolio |
| Portfolio | Name | NaN | Name of the portfolio. | Max350Text | NaN |
| Portfolio | Identification | NaN | Identification of the portfolio. | Max35Text | NaN |
| Portfolio | Strategy | NaN | Strategy set for the portfolio. | PortfolioStrategy | Portfolio |
| Portfolio | Benchmark | NaN | Information on the benchmark set for the portfolio. | PortfolioBenchmark | Portfolio |
| Portfolio | InvestmentPlan | NaN | Investment plan associated with a portfolio. | InvestmentPlan | Portfolio |
| Portfolio | Account | NaN | Account on which the portfolio is held. | InvestmentAccount | Portfolio |
| AssetHolding | NaN | NaN | Specifies in terms of value and quantity the assets. | NaN | NaN |
| AssetHolding | HoldingValue | NaN | Value of the balance of an individual securities holding. | ActiveOrHistoricCurrencyAndAmount | NaN |
| AssetHolding | BookValue | NaN | Value of a security, as booked/acquired in an account. Book value is often different from the current market value of the security. | CurrencyAndAmount | NaN |
| AssetHolding | FaceAmount | NaN | Quantity expressed as an amount representing the face amount, ie, the principal, of a debt instrument. | CurrencyAndAmount | NaN |
| AssetHolding | AmortisedFaceValue | NaN | Quantity expressed as an amount representing the current amortised face amount of a bond, for example, a periodic reduction/increase of a bond's principal amount. | CurrencyAndAmount | NaN |
| AssetHolding | MarketValue | NaN | Value of the asset holding based on current market prices. | ActiveCurrencyAndAmount | NaN |
| AssetHolding | Balance | NaN | Specifies the balance of the asset holding. | Balance | AssetHolding |
| AssetHolding | UnrealisedGainOrLoss | NaN | Difference between the holding value and the book value of the asset. | CurrencyAndAmount | NaN |
| AssetHolding | Asset | NaN | Specifies the asset included in the holding. | Asset | AssetValue |
| AssetHolding | Haircut | NaN | Percentage by which an asset's market value is reduced for the purpose of calculating capital requirement, margin and collateral levels. | HaircutValuation | AssetHolding |
| AssetHolding | EligibleCollateralValue | NaN | Value of the position eligible for collateral purposes. This corresponds to the sub balance with a type AvailableForCollateral. | ActiveCurrencyAndAmount | NaN |
| AssetHolding | ExchangeRate | NaN | Specifies the exchange rate between the currency of the asset and the reporting currency. | CurrencyExchange | CalculatedAssetValue |
| AssetHolding | CapValue | NaN | Maximum notional value for a financial instrument that is capped. | CurrencyAndAmount | NaN |
| AssetHolding | RiskAdjustedValue | NaN | Value of the asset holding after deduction of a percentage (the haircut) that reflects the perceived risk associated with holding this asset. | ActiveCurrencyAndAmount | NaN |
| AssetHolding | RealisedGainOrLoss | NaN | Difference between the realised value caused by the actual trade/re-evaluation and the book value of the asset. | CurrencyAndAmount | NaN |
| AssetHolding | UnrealisedType | NaN | Specifies whether the unrealised amount is a gain or a loss. | UnrealisedCode | NaN |
| AssetHolding | PostHaircutValue | NaN | Value of the collateral after deduction of a percentage (the haircut) that reflects the perceived risk associated with holding this collateral. | CurrencyAndAmount | NaN |
| AssetHolding | Interest | NaN | interest relative to the asset and the parameters used to calculate it. | Interest | RelatedAssetHolding |
| AssetHolding | Collateral | NaN | Specifies the collateral information in relation with some assets. | Collateral | AssetHolding |
| AssetHolding | FinancialAssetType | NaN | Specifies the asset type. | FinancialAssetBalanceTypeCode | NaN |
| AssetHolding | VariationMarginCollateral | NaN | Specifies the collateral information in relation with the segregated independent amount asset holding. | Collateral | VariationMarginAssetHolding |
| AssetHolding | IndependentAmountCollateral | NaN | Specifies the collateral information in relation with the segregated independent amount asset holding. | Collateral | SegregatedIndependentAmountAssetHolding |
| AssetHolding | HoldingType | NaN | Specifies the type of holding. | BlockedReasonCode | NaN |
| AssetHolding | GuaranteeAmount | NaN | Amount of the bank guarantee. | CurrencyAndAmount | NaN |
| PaymentExecution | NaN | NaN | Process required for executing an end to end payment. It consists of a payment initiation which may be followed by a series of instructions. | NaN | NaN |
| PaymentExecution | CreditDebitIndicator | NaN | Indicates whether the payment is a debit or a credit. | DebitCreditCode | NaN |
| PaymentExecution | CreationDate | NaN | Date and time at which the payment execution was created by the instructing agent. | ISODateTime | NaN |
| PaymentExecution | AcceptanceDateTime | NaN | Date and time at which all processing conditions for execution of the payment are met and adequate financial cover is available at the account servicing agent. | ISODateTime | NaN |
| PaymentExecution | Payment | NaN | Specifies the end to end payment which is at the origin of the payment instruction. | Payment | PaymentExecution |
| PaymentExecution | ProcessingInstructions | NaN | Specifies how the payment must be processed, for instance through which specific clearing channel. | PaymentProcessing | PaymentExecution |
| PaymentExecution | RequestedExecutionDate | NaN | Date at which the initiating party requests the clearing agent to process the payment. Usage: This is the date on which the debtor's account is to be debited. If payment by cheque, the date when the cheque must be generated by the bank. | ISODateTime | NaN |
| PaymentExecution | RelatedInvestigationCase | NaN | Investigation case assigned to the payment execution. | PaymentInvestigationCase | UnderlyingInstruction |
| PaymentExecution | RelatedInvestigationCaseResolution | NaN | Payment investigation case resolution which is the source of the corrected payment execution. | PaymentInvestigationCaseResolution | PaymentExecutionCorrection |
| PaymentExecution | Next | NaN | Specifies the next payment instruction in the payment end-to-end chain. | PaymentInstruction | Previous |
| PaymentExecution | CurrencyExchange | NaN | Rate used to transform the original amount into the credited amount. | CurrencyExchange | PaymentExecution |
| PaymentInstruction | NaN | PaymentExecution | Instruction to pay an amount of money to an ultimate beneficiary, on behalf of an originator. This instruction may have to be forwarded several times to complete the settlement chain. | NaN | NaN |
| PaymentInstruction | ProcessingValidityTime | NaN | Date and time range within which the payment instruction must be processed. | DateTimePeriod | PaymentInstruction |
| PaymentInstruction | InstructionForNextAgent | NaN | Further information related to the processing of the payment instruction that may need to be acted upon by the next agent. Usage: The next agent may not be the creditor agent. The instruction can relate to a level of service, can be an instruction that has to be executed by the agent, or can be information required by the next agent. | InstructionCode | NaN |
| PaymentInstruction | SettlementInstruction | NaN | Instruction for the cash settlement between two clearing agents. | CashSettlement | RelatedPaymentInstruction |
| PaymentInstruction | ClearingChargeAmount | NaN | Amount of money taken by a clearing agent as compensation for the processing of the payment instruction. This charge is paid either by the debtor or by the creditor or shared between them. | CurrencyAndAmount | NaN |
| PaymentInstruction | StandingOrder | NaN | Instruction given by an account holder to an account servicer to make regular transfers on given dates to the same beneficiary. | StandingOrder | PaymentInstructionTrigger |
| PaymentInstruction | Previous | NaN | Specifies that a payment instruction may be preceeded by another payment instruction. | PaymentExecution | Next |
| System | NaN | RolePlayer | Set of integrated applications that provides centralised services such as clearing, netting, reconciliation, trading and/or settlement. | NaN | NaN |
| System | SystemIdentification | NaN | Identification of the system. | SystemIdentification | IdentificationForSystem |
| System | Location | NaN | Location, address and country in which the system is located. | Location | System |
| System | Reconciliation | NaN | Reconciliation process provided by the system. | Reconciliation | System |
| System | Availability | NaN | Information about the activity or non-activity of the system. | SystemAvailability | System |
| System | Event | NaN | Specific point in time associated with the system's processing cycle. Operations of a system are composed of a series of processes, the closing, or completion, of which constitutes an event with an associated time stamp. An event may have a series of time stamps associated with it, such as the scheduled and effective completion times. | SystemEventInformation | System |
| System | PartyRole | NaN | Specifies each role linked to a system. | SystemPartyRole | RelatedSystem |
| System | Status | NaN | Status of the system. | SystemStatus | System |
| System | SystemGeneratedInformation | NaN | Business details provided for an information system. | SystemBusinessInformation | System |
| System | VersionValidityPeriod | NaN | Date at, or period of time during which, the stipulated version is in effect. | DateTimePeriod | System |
| System | SystemDateTime | NaN | Date time of a system performing a task. | ISODateTime | NaN |
| System | Negotiation | NaN | Negotiation process which uses a ssystem. | Negotiation | TradingSystem |
| System | Account | NaN | Account managed by a system and held by a system member. | Account | System |
| System | Trade | NaN | Trade processed by a system. | Trade | System |
| System | Assessment | NaN | Assessment associated with a system. | Assessment | System |
| System | TradesPosition | NaN | Specifies the status of trades and their value inside a system. | Position | System |
| System | SystemLanguage | NaN | Specifies the language used by the system. | ISO2ALanguageCode | NaN |
| SystemIdentification | NaN | NaN | Parameters that identify a system. | NaN | NaN |
| SystemIdentification | IdentificationForSystem | NaN | System which is identified. | System | SystemIdentification |
| SystemIdentification | Model | NaN | Identification of a model for a given manufacturer. | Max35Text | NaN |
| SystemIdentification | SerialNumber | NaN | Serial number of a component. | Max35Text | NaN |
| SystemIdentification | ApprovalNumber | NaN | Unique approval number for a component, delivered by a certification body. | Max70Text | NaN |
| SystemIdentification | SystemVersion | NaN | Version of the system, eg, "4.0.1" to indicate version 4.0.1. | Max35Text | NaN |
| SystemIdentification | SystemName | NaN | Name by which a system is known. | SystemName | SystemIdentification |
| SystemIdentification | Identification | NaN | Identification of a system. | GenericIdentification | RelatedSystemIdentification |
| ClearingSystem | NaN | System | Specifies the system which plays a role in the clearing process. | NaN | NaN |
| ClearingSystem | Clearing | NaN | Specifies the clearing process for which a clearing system is used. | Clearing | ClearingSystem |
| ClearingSystem | CentralClearingCounterparty | NaN | Central counterparty which is related to a clearing system. | CentralClearingCounterpartyRole | System |
| ClearingSystem | DefaultFund | NaN | Assets posted by participants in a clearing fund that can be used in the event of a default by a participant to compensate non-defaulting participants for losses they suffer due to this default. | DefaultFund | ClearingSystem |
| ClearingSystem | CollateralManagement | NaN | Collateral activities related to a clearing system. | CollateralManagement | ClearingSystem |
| CashClearingSystem | NaN | ClearingSystem | Clearing system that processes only cash transfers. | NaN | NaN |
| CashClearingSystem | Identification | NaN | Information used to identify a cash clearing system. | CashClearingSystemCode | NaN |
| CashClearingSystem | TransactionAdministrator | NaN | Set of integrated applications that provides centralised services such as clearing and settlement. | TransactionAdministrator | CashClearingSystem |
| CashClearingSystem | SystemRole | NaN | Specifies the role played by the cash clearing system. | SettlementInstructionSystemRole | System |
| CashClearingSystem | Type | NaN | Specifies the category of cash clearing system, eg, cheque clearing. | CashSystemTypeCode | NaN |
| CashClearingSystem | CashSettlementSystem | NaN | Specifies the cash settlement system used. | CashSettlementSystemCode | NaN |
| SystemPartyRole | NaN | Role | Role played by a party in a system. | NaN | NaN |
| SystemPartyRole | RelatedSystem | NaN | Specifies the system for which a party plays a role | System | PartyRole |
| SystemMemberRole | NaN | SystemPartyRole | Information about the members of a system. | NaN | NaN |
| SystemMemberRole | CashBalance | NaN | Cash balance for which a counterparty is specified. | CashBalance | Counterparty |
| SystemMemberRole | Type | NaN | Nature of the relationship a member has with a system. | MemberTypeCode | NaN |
| SystemMemberRole | MemberStatus | NaN | Specifies the status of a member. | SystemStatus | SystemMemberRole |
| SystemMemberRole | Limit | NaN | Cash management feature limiting the maximum risk a party accepts to take with respect to a counterparty or a set of counterparties. A risk management limit is either bilateral, ie, for a counterparty, or multilateral, ie, for a set of counterparties or all other members in a system.The limit may also apply to sponsored members, ie, indirect members. In principle, a risk management limit is calculated on the net position between two members and is expressed as a credit or debit limit, from the point of view of the party setting the limit. | RiskManagementLimit | Counterparty |
| SystemMemberRole | Account | NaN | Account owned by the member of a system with the system. | Account | SystemMember |
| ClearingMemberRole | NaN | SystemPartyRole | Member of an exchange's clearing corporation, responsible for executing client trades and involved in the clearing of trades. | NaN | NaN |
| ClearingMemberRole | ClearingSystemMemberIdentification | NaN | Unique and unambiguous identifier of a clearing system member, assigned by the system or system administrator. | CashClearingSystemMember | ClearingMember |
| ClearingMemberRole | Side | NaN | Specifies the side of the clearing member. | ClearingSideCode | NaN |
| ClearingMemberRole | ClearingAccount | NaN | Identifies the clearing member account at the CCP through which the trade must be cleared (sometimes called position account). | SecuritiesAccount | ClearingAccountOwner |
| ClearingMemberRole | MarginAccount | NaN | Margin account where the negociation and liquidation risks will be calculated. | SecuritiesAccount | MarginAccountOwner |
| ClearingMemberRole | DeliveryAccount | NaN | Account opened by the central counterparty in the name of the clearing member within the account structure, for settlement purposes (gives information about the clearing member account at central counterparty). | SecuritiesAccount | DeliveryAccountOwner |
| ClearingMemberRole | DefaultFundAccount | NaN | Specifies the account identification of the clearing member at the ICSD (International Central Securities Depository) or at the Central Bank. | Account | DefaultFundAccountOwner |
| ClearingMemberRole | ClearingSegment | NaN | Clearing segment within a clearing organisation that allows the segregation of flows coming from clearing counterparty's clearing system. | ClearingMemberRole | RelatedClearingMemberRole |
| ClearingMemberRole | RelatedClearingMemberRole | NaN | Clearing member for which a clearing segment is specified. | ClearingMemberRole | ClearingSegment |
| PaymentIdentification | NaN | TradeIdentification | Specifies the different identifications associated with a payment transaction. | NaN | NaN |
| PaymentIdentification | ExecutionIdentification | NaN | Unique and unambiguous identifier for a payment execution, as assigned by the clearing agent or the initiating party. | Max35Text | NaN |
| PaymentIdentification | EndToEndIdentification | NaN | Unique and unambiguous identifier for a payment as assigned by the originator. The payment transaction reference is used for reconciliation or to link tasks relating to the payment. | Max35Text | NaN |
| PaymentIdentification | InstructionIdentification | NaN | Unique identification assigned by an instructing party for an instructed party to unambiguously identify the instruction. | Max35Text | NaN |
| PaymentIdentification | TransactionIdentification | NaN | Unique identification assigned by the first instructing agent to unambiguously identify the transaction and passed on, unchanged, throughout the entire interbank chain. | Max35Text | NaN |
| PaymentIdentification | ClearingSystemReference | NaN | Unique and unambiguous identifier for a payment instruction, as assigned by the clearing system. | Max35Text | NaN |
| PaymentIdentification | CreditorReference | NaN | Unique and unambiguous reference assigned by the creditor to refer to the payment obligation. | Max35Text | NaN |
| PaymentIdentification | Payment | NaN | Payment for which identifications are provided. | Payment | PaymentRelatedIdentifications |
| PaymentIdentification | UETR | NaN | Universally unique identifier to provide an end-to-end reference of a payment transaction. | UUIDv4Identifier | NaN |
| Settlement | NaN | NaN | Process which consists in transferring the proceeds related to a trade from one party to the next one. | NaN | NaN |
| Settlement | CentralCounterpartyEligibilityIndicator | NaN | Specifies whether the settlement transaction is CCP (Central Counterparty) eligible. | YesNoIndicator | NaN |
| Settlement | StandingSettlementInstruction | NaN | Settlement Standing Instruction database to be used for settlement. | StandingSettlementInstruction | Settlement |
| Settlement | SettlementPartyRole | NaN | Specifies roles played by a party in the settlement process. | SettlementPartyRole | Settlement |
| Settlement | Trade | NaN | Trade for which settlement information is provided. | Trade | Settlement |
| CashSettlement | NaN | Settlement | Instruction between two financial institutions stipulating the cash transfer characteristics between the two parties. | NaN | NaN |
| CashSettlement | InterbankSettlementAmount | NaN | Amount of money moved between the instructing agent and the instructed agent. | CurrencyAndAmount | NaN |
| CashSettlement | InterbankSettlementDate | NaN | Date on which the amount of money ceases to be available to the agent that owes it and when the amount of money becomes available to the agent to which it is due. | ISODateTime | NaN |
| CashSettlement | RTGS | NaN | Qualifies the RTGS status. | Max4AlphaNumericText | NaN |
| CashSettlement | CreditDateTime | NaN | Information on the occurred settlement time(s) of the payment transaction for the credit side. | ISODateTime | NaN |
| CashSettlement | RelatedPaymentInstruction | NaN | PaymentInstruction which is the source of the settlement instruction. | PaymentInstruction | SettlementInstruction |
| CashSettlement | SettlementMethod | NaN | Method used to settle the (batch of) payment instructions. | SettlementMethodCode | NaN |
| CashSettlement | SettlementAccount | NaN | A specific purpose account used to post debit and credit entries as a result of the transaction. | CashAccount | RelatedSettlementInstruction |
| CashSettlement | DebitDateTime | NaN | Information on the occurred settlement time(s) of the payment transaction for the debit side. | ISODateTime | NaN |
| CashSettlement | PartyRole | NaN | Specifies each role linked to the settlement of a payment and played by a party at that step in a payment flow. | CashSettlementInstructionPartyRole | SettlementInstruction |
| CashSettlement | RelatedTransactionAdministrator | NaN | Transaction administrator which manages the related settlement instructions. | TransactionAdministrator | SettlementInstruction |
| CashSettlement | BookEntry | NaN | Movement of cash between two accounts in the same financial institution, resulting from the settlement of an instruction. | BookEntry | RelatedSettlementInstruction |
| CashSettlement | RelatedInvestigationCase | NaN | Case resolution which is the source of the correction of a settlement instruction. | PaymentInvestigationCaseResolution | CoverCorrection |
| CashSettlement | Reservation | NaN | Liquidity set aside by the payer for specific purposes. | Reservation | SettlementInstruction |
| PaymentPartyRole | NaN | Role | Role played by a party in the context of a payment. | NaN | NaN |
| PaymentPartyRole | CashAccount | NaN | Unambiguous identification of the account used in the context of the party role such as debtor account, instructing agent account... | CashAccount | PaymentPartyRole |
| PaymentPartyRole | Payment | NaN | Identifies the payment in which a party plays a role. | Payment | PartyRole |
| InstructingAgentRole | NaN | PaymentPartyRole | Agent that instructs the next party in the chain to carry out the (set of) instruction(s). | NaN | NaN |
| InstructingAgentRole | Previous | NaN | Agent immediately prior to the instructing agent. | YesNoIndicator | NaN |
| InstructedAgentRole | NaN | PaymentPartyRole | Agent that is instructed by the previous party in the chain to carry out the (set of) instruction(s). | NaN | NaN |
| Limit | NaN | NaN | Value used for risk containment in a system or towards counterparts. The limit may be a current limit or a default limit. | NaN | NaN |
| Limit | Type | NaN | Nature of the limit. | LimitTypeCode | NaN |
| Limit | Amount | NaN | Amount of money of the limit, expressed in a currency. | CurrencyAndAmount | NaN |
| Limit | CreditDebitIndicator | NaN | Specifies if a limit is a debit limit or a credit limit. | FloorLimitTypeCode | NaN |
| Limit | UsedAmount | NaN | Actual usage of the limit expressed as an amount. | CurrencyAndAmount | NaN |
| Limit | UsedPercentage | NaN | Actual usage of the limit expressed as a percentage. | PercentageRate | NaN |
| Limit | Currency | NaN | Currency unit used to specify the limit amount. | CurrencyCode | NaN |
| Limit | LimitStatus | NaN | Current status of the limit. | LimitStatus | Limit |
| Limit | Percentage | NaN | Specifies that the limit is a percentage of a related amount. | PercentageRate | NaN |
| Limit | RelatedDebitCreditFacility | NaN | Overdraft conditions for which limit parameters are specified. | DebitCreditFacility | CreditLine |
| Limit | Periodicity | NaN | Specifies the periodicity linked to a limit for example the periodicity can indicate that the limit can be reached daily or monthly. | FrequencyCode | NaN |
| Limit | Quantity | NaN | Specifies that the limit is a quantity. | DecimalNumber | NaN |
| Limit | ValidityPeriod | NaN | Period at which the limit is effective. | DateTimePeriod | RelatedLimit |
| Limit | RelatedPaymentCard | NaN | Payment card for which a limit is specified. | PaymentCard | Limit |
| Limit | AvailableAmount | NaN | Remaining amount of money of the limit. | CurrencyAndAmount | NaN |
| RiskManagementLimit | NaN | Limit | Cash management feature limiting the maximum risk that a party accepts to take with respect to a counterparty or a set of counterparties. A risk management limit is either bilateral, for a counterparty, or multilateral, for a set of counterparties or all other members in a system.The limit may also apply to sponsored or indirect members. In principle, a risk management limit is calculated on the net position between two members and is expressed as a credit or debit limit, from the point of view of the party setting the limit. | NaN | NaN |
| RiskManagementLimit | CashManagementService | NaN | Cash management service which offers limit management services. | CashManagementService | RiskManagementLimit |
| RiskManagementLimit | Counterparty | NaN | Identification of the system member for which the limit is established. | SystemMemberRole | Limit |
| TransactionAdministrator | NaN | SystemPartyRole | Set of integrated applications that provides centralised services such as clearing and settlement. | NaN | NaN |
| TransactionAdministrator | CashClearingSystem | NaN | System where the clearing takes place. | CashClearingSystem | TransactionAdministrator |
| TransactionAdministrator | Currency | NaN | Currency which may be processed by the system. A system may process transactions in a single currency or in multiple currencies. | CurrencyCode | NaN |
| TransactionAdministrator | CurrencyExchange | NaN | Static data maintained by the transaction administrator and related to currency exchange details as maintained for system operations. | CurrencyExchange | CurrencyExchangeForTransactionAdministrator |
| TransactionAdministrator | CashManagementService | NaN | Set of applications that provides services which facilitate the management of cash positions on an account. | CashManagementService | RelatedTransactionAdministrator |
| TransactionAdministrator | SettlementInstruction | NaN | Specifies the settlement instruction managed by the transaction administrator. | CashSettlement | RelatedTransactionAdministrator |
| Reservation | NaN | Limit | Liquidity set aside by the payer for specific purposes. | NaN | NaN |
| Reservation | ReservationType | NaN | Nature of the reservation. | ReservationTypeCode | NaN |
| Reservation | RelatedIntraPositionTransfer | NaN | Transfer process for which reservation information is provided. | IntraPositionTransfer | Reservation |
| Reservation | SettlementInstruction | NaN | Specifies the instruction which originated the reservation. | CashSettlement | Reservation |
| Reservation | AccountService | NaN | Account services for which reservation information is specified. | AccountService | Reservation |
| Balance | NaN | NaN | Numerical representation of the net increases and decreases in an account at a specific point in time. | NaN | NaN |
| Balance | Type | NaN | Specifies the nature of a balance. | BalanceTypeCode | NaN |
| Balance | ValueDate | NaN | Date and time at which the balance is or will be available. | ISODateTime | NaN |
| Balance | CreditDebitIndicator | NaN | Indicates whether the balance is a credit or a debit balance. A zero balance is considered to be a credit balance | DebitCreditCode | NaN |
| Balance | AssetHolding | NaN | Specifies in terms of value and quantity the assets held in a balance. | AssetHolding | Balance |
| Balance | CalculationDate | NaN | Specifies the date and time at which the balance is calculated. | ISODateTime | NaN |
| Balance | Adjustment | NaN | Specifies the balance adjustments. | Adjustment | AdjustedBalance |
| Balance | Account | NaN | Account or sub-account for which a balance is calculated. | Account | Balance |
| Balance | Interest | NaN | Set of elements used to provide interest information that applies to the balance. | Interest | AccountBalance |
| Balance | BalanceEntry | NaN | Credit or debit postings used to calculate a balance. | Entry | Balance |
| Balance | ProcessingRestriction | NaN | Specifies the type of balance processing restrictions that must be applied. | ProcessingTypeCode | NaN |
| Balance | OpeningClosingCode | NaN | Specifies whether the balance is an opening or a closing one. | OpeningClosingCode | NaN |
| CashBalance | NaN | Balance | Numerical representation of the net increases and decreases in an account at a specific point in time. A cash balance is calculated from a sum of cash credits minus a sum of cash debits. | NaN | NaN |
| CashBalance | CashAccount | NaN | Cash account for which a balance is calculated. | CashAccount | CashBalance |
| CashBalance | CalculationType | NaN | Specifies whether the balance is calculated against one other party or against a group of parties. | BalanceCounterpartyCode | NaN |
| CashBalance | Counterparty | NaN | Party against which a balance is calculated (from the point of view of the account owner). A bilateral balance is calculated against one other party; a multilateral balance is calculated against a group of parties. | SystemMemberRole | CashBalance |
| CashBalance | Amount | NaN | Currency and amount of money of the cash balance. | CurrencyAndAmount | NaN |
| CashBalance | Availability | NaN | Elements used to indicate when the booked amount of money will become available, that is can be accessed and start generating interest. | CashAvailability | CashBalance |
| CashBalance | CashBalanceEntry | NaN | Credit or debit postings used to calculate a balance. | CashEntry | CashBalance |
| CashBalance | BalanceAdjustmentCode | NaN | Defines the type of allowed balance adjustment. | BalanceAdjustmentTypeCode | NaN |
| CashBalance | RelatedCardPaymentValidationProcess | NaN | Validation process which verifies the balance attached to the card. | CardPaymentValidation | Balance |
| CashBalance | CutOffDate | NaN | Predetermined date in a billing or processing cycle when account activity for the previous reporting period is summarized (when checks written against an account are collected and summarized in a monthly statement). Checks paid or deposits received after the cut-off date are included in the next month's statement. | ISODate | NaN |
| CashBalance | RelatedRegisteredContract | NaN | Related contract balance on date of contract registration. | RegisteredContract | ContractBalance |
| SystemEventInformation | NaN | NaN | Detailed information about an event occurring on a system, whether planned, for example, cut-off time for a specific type of eligible transfer, or unplanned, for example, an unsolicited failure, as stipulated in the specifications of the system. | NaN | NaN |
| SystemEventInformation | Type | NaN | Nature of the event that has occurred. | SystemEventTypeCode | NaN |
| SystemEventInformation | Time | NaN | Date and time at which the event occurred. | ISODateTime | NaN |
| SystemEventInformation | System | NaN | System for which event information is provided. | System | Event |
| AmountRange | NaN | NaN | Range of amount values. | NaN | NaN |
| AmountRange | FromAmount | NaN | Lower boundary of a range of amount values. | AmountRangeBoundary | FromAmountRange |
| AmountRange | ToAmount | NaN | Upper boundary of a range of amount values. | AmountRangeBoundary | ToAmountRange |
| AmountRange | EqualAmount | NaN | Exact value an amount must match to be considered valid. | CurrencyAndAmount | NaN |
| AmountRange | NotEqualAmount | NaN | Value that an amount must not match to be considered valid. | CurrencyAndAmount | NaN |
| AmountRange | CreditDebitIndicator | NaN | Indicates whether the amount is a credited or debited amount. | DebitCreditCode | NaN |
| AmountRange | Currency | NaN | Medium of exchange of value, used to qualify an amount. | CurrencyCode | NaN |
| AmountRange | RelatedInterest | NaN | Interest which applies on a specific amount range. | InterestCalculation | RateValidityRange |
| AmountRangeBoundary | NaN | NaN | Limit for an amount range. | NaN | NaN |
| AmountRangeBoundary | FromAmountRange | NaN | Amount range for which a lower boundary is provided. | AmountRange | FromAmount |
| AmountRangeBoundary | BoundaryAmount | NaN | Amount value of the range limit. | ImpliedCurrencyAndAmount | NaN |
| AmountRangeBoundary | Included | NaN | Indicates whether the boundary amount is included in the range of amount values. | YesNoIndicator | NaN |
| AmountRangeBoundary | ToAmountRange | NaN | Amount range for which an upper boundary is provided. | AmountRange | ToAmount |
| StandingOrder | NaN | NaN | Instruction given by an account holder to an account servicer to make regular transfers on given dates to the same beneficiary. | NaN | NaN |
| StandingOrder | Identification | NaN | Unique and unambiguous identification for a standing order, as assigned by the account servicer or the account owner. | Max35Text | NaN |
| StandingOrder | Type | NaN | Type of the standing order. | StandingOrderTypeCode | NaN |
| StandingOrder | ValidityPeriod | NaN | Dates during which the standing order is in effect. | DateTimePeriod | RelatedStandingOrder |
| StandingOrder | LinkSetIdentification | NaN | Unique identification to unambiguously identiy the link set in which the standing order is defined. | Max35Text | NaN |
| StandingOrder | StandingOrderSequence | NaN | Specifies the sequence in which the system will execute the liquidity transfers standing order within the link set when additional liquidity is required. | Number | NaN |
| StandingOrder | Amount | NaN | Currency and amount of the periodical payments. When the standing order is related to a fund investment plan, this is the cash part of the invested amount. | CurrencyAndAmount | NaN |
| StandingOrder | CreditAccount | NaN | Cash account credited from a standing order mechanism. | CashAccount | RelatedCreditStandingOrder |
| StandingOrder | DebitAccount | NaN | Cash account debited from a standing order mechanism. | CashAccount | RelatedDebitStandingOrder |
| StandingOrder | Frequency | NaN | Frequency of the investment or divestment, eg, daily, weekly, or monthly. | FrequencyCode | NaN |
| StandingOrder | EventDescription | NaN | Describes the event which triggers the exercise of a standing order for instance the reception of a report or the closing of an account. | Max140Text | NaN |
| StandingOrder | Day | NaN | Specifies the date in a month for instance the 30th. | Number | NaN |
| StandingOrder | TimeSpecification | NaN | Specifies the period for the time event, for instance end of day. | Max35Text | NaN |
| StandingOrder | PaymentInstructionTrigger | NaN | Standing order causes a payment instruction at regular intervals, eg, as specified by its frequency. | PaymentInstruction | StandingOrder |
| StandingOrder | IncludedStandingOrder | NaN | Specifies the standing order included in the linkset. | StandingOrder | LinkSet |
| StandingOrder | LinkSet | NaN | Collection of standing orders defined in a specific sequence. | StandingOrder | IncludedStandingOrder |
| CashStandingOrder | NaN | StandingOrder | Instruction given by a party that has explicit authority to instruct a debit on the account, ie, either the debit account owner or originating party, to a first agent, to process cash transfers at specified intervals during an implicit or explicit period of time. A standing order is given once and is valid for an open or closed period of time. | NaN | NaN |
| CashStandingOrder | ZeroSweepIndicator | NaN | Indicates whether the liquidity transfer standing order is defined as a zero sweeping order. When true, the liquidity transfer standing order will transfer all amount of money out of the account so the resulting balance is zero. | TrueFalseIndicator | NaN |
| CashStandingOrder | RelatedCashServices | NaN | Cash management services which provide standing order facilities. | CashManagementService | StandingOrder |
| CashStandingOrder | CreditDebitIndicator | NaN | Specifies if the account is debited or credited by the standing order. | DebitCreditCode | NaN |
| CashStandingOrder | CreditTransfer | NaN | Standing order causes a payment instruction at regular intervals, eg, as specified by its frequency. | CreditTransfer | RelatedStandingOrder |
| CashStandingOrder | FloorAmount | NaN | Minimum amount of money that should remain on the debtor's account, for cash management purposes. | CurrencyAndAmount | NaN |
| CashStandingOrder | CashAccount | NaN | Cash account for which a standing order applies. | CashAccount | CashStandingOrder |
| AccountResponsiblePartyRole | NaN | AccountPartyRole | Party which is responsible for creating and managing an account owned by another party. | NaN | NaN |
| StandingOrderResponsible | NaN | AccountResponsiblePartyRole | Party responsible for creating, maintaining and deleting a standing order. | NaN | NaN |
| PaymentStatus | NaN | Status | Specifies the status of a payment at a specified time. | NaN | NaN |
| PaymentStatus | Status | NaN | Specifies the status of the payment execution. | PaymentStatusCode | NaN |
| PaymentStatus | Payment | NaN | Payment for which a status is provided. | Payment | PaymentStatus |
| PaymentStatus | UnmatchedStatusReason | NaN | Reason the transaction/instruction is unmatched. | TransferUnmatchedReasonCode | NaN |
| PaymentStatus | SuspendedStatusReason | NaN | Reason the transaction/instruction is suspended. | SuspendedStatusReasonCode | NaN |
| PaymentStatus | PendingSettlement | NaN | Reason the instruction is pending settlement, ie, delivery or receipt of the financial instrument. Settlement on the instructed settlement date is still possible. | PendingSettlementStatusReasonCode | NaN |
| PaymentStatus | InstructionStatus | NaN | Specifies the state of a payment instruction. | PaymentInstructionStatusCode | NaN |
| PaymentStatus | TransactionRejectionReason | NaN | Specifies the reason to reject, return or reverse the transaction. | TransactionReasonCode | NaN |
| PaymentStatus | RelatedInvestigationCase | NaN | Specifies an investigation case in relation with the payment status. | PaymentInvestigationCase | PaymentStatus |
| PaymentStatus | NotificationStatus | NaN | Specifies the status of the payment in comparison with the notification to receive. | NotificationToReceiveStatusCode | NaN |
| PaymentStatus | TransactionStatus | NaN | Specifies the processing status of an investment fund transaction. | TransactionStatusCode | NaN |
| PaymentStatus | CashPaymentStatus | NaN | Specifies a generic status of a payment at a specified time. | CashPaymentStatusCode | NaN |
| PaymentStatus | UnsuccessfulStatusReason | NaN | Reason provided for the status of a transaction.The reason may be in coded or free text form. | ExternalStatusReasonCode | NaN |
| PaymentStatus | CancellationReason | NaN | Reason for the cancellation of the payment. | CancellationReasonCode | NaN |
| PaymentStatus | MandateRejectionReason | NaN | Reason for requesting the cancellation or the amendment of a mandate. | MandateReasonCode | NaN |
| PaymentStatus | PendingFailingSettlement | NaN | Reason the transaction/instruction is pending due to failing settlement. | PendingFailingSettlementCode | NaN |
| DebtorRole | NaN | PaymentPartyRole | Party that owes an amount of money to the (ultimate) creditor. For example, as a result of receipt of goods, assets, services, gifts, or charity payments. | NaN | NaN |
| PaymentProcessing | NaN | NaN | Specifies how a payment must be processed, for instance through which specific clearing channel. | NaN | NaN |
| PaymentProcessing | Priority | NaN | Indicator of the urgency or order of importance that the instructing party would like the instructed party to apply to the processing of the instruction. | PriorityCode | NaN |
| PaymentProcessing | ServiceLevel | NaN | Agreement under which or rules under which the transaction should be processed. | ServiceLevel | PaymentProcessing |
| PaymentProcessing | ClearingChannel | NaN | Specifies the clearing channel to be used to process the payment instruction. | ClearingChannelCode | NaN |
| PaymentProcessing | LocalInstrument | NaN | User community specific instrument.Usage : When available, codes provided by local authorities should be used. | ExternalLocalInstrumentCode | NaN |
| PaymentProcessing | CategoryPurpose | NaN | Specifies the high level purpose of the instruction based on a set of pre-defined categories. | PaymentCategoryPurposeCode | NaN |
| PaymentProcessing | PaymentExecution | NaN | Payment execution process for which processing parameters are specified. | PaymentExecution | ProcessingInstructions |
| PaymentProcessing | SequenceType | NaN | Identifies the payment sequence where applicable. | SequenceTypeCode | NaN |
| PaymentProcessing | RelatedMandate | NaN | Mandate for which payment processing parametres are specified. | Mandate | MandatePaymentType |
| PaymentProcessing | BankTransaction | NaN | Code of the underlying bank transaction. | BankTransaction | RelatedPayment |
| PaymentProcessing | ContactPoint | NaN | Specifies the notification method to be used to inform the beneficiary. | ContactPoint | RelatedPayment |
| PaymentProcessing | AdviceType | NaN | Specifies the type of advice to report back for the transaction. | AdviceTypeCode | NaN |
| AssetPartyRole | NaN | Role | Specifies roles played by a party that are linked to the handling of assets but not related to a specific process. | NaN | NaN |
| AssetPartyRole | Asset | NaN | Specifies the asset for which the party plays a role. | Asset | AssetPartyRole |
| SecuritiesPartyRole | NaN | AssetPartyRole | Specifies roles played by a party that are linked to the handling of securities but not related to a specific process. | NaN | NaN |
| SecuritiesPartyRole | SecuritiesAccount | NaN | Unambiguous identification of the securities account used in the context of the securities party role (such as investor securities account used for a corporate action securities distribution) | SecuritiesAccount | SecuritiesPartyRole |
| SecuritiesPartyRole | CashAccount | NaN | Unambiguous identification of the cash account used in the context of the securities party role (such as investor cash account used for a corporate action cash distribution) | CashAccount | SecuritiesPartyRole |
| SecuritiesPartyRole | Security | NaN | Specifies the security for which the party plays a role. | Security | PartyRole |
| SettlementPartyRole | NaN | Role | Role played by a party in a settlement process. | NaN | NaN |
| SettlementPartyRole | SettlementAccount | NaN | Account which is used for settlement. | Account | SettlementPartyRole |
| SettlementPartyRole | Settlement | NaN | Specifies the settlement process for which the party plays a role. | Settlement | SettlementPartyRole |
| SecuritiesSettlementPartyRole | NaN | SettlementPartyRole | Role played by a party in the context of the settlement of securities. | NaN | NaN |
| SecuritiesSettlementPartyRole | SecuritiesSettlement | NaN | Specifies the settlement process in which a party plays a role. | SecuritiesSettlement | PartyRole |
| SecuritiesSettlementPartyRole | SecuritiesSettlementSystem | NaN | Specifies the system which may be used by a party in a settlement process. | SecuritiesSettlementSystem | SettlementParty |
| SecuritiesSettlementPartyRole | SettlingCapacity | NaN | Role of a party in the settlement of the transaction. | SettlingCapacityCode | NaN |
| SecuritiesSettlementPartyRole | TaxCapacity | NaN | Tax role capacity of the instructing party. | TaxLiabilityCode | NaN |
| ReceivingSettlementParty | NaN | SecuritiesSettlementPartyRole | Party that receives securities as part of a chain of settlement parties or as ultimate party. | NaN | NaN |
| ReceivingSettlementParty | ReceivingSettlementParty | NaN | Specifies the settlement party which is followed by another party. | ReceivingSettlementParty | NextParty |
| ReceivingSettlementParty | NextParty | NaN | Next party in the receiving side of the settlement transaction chain. | ReceivingSettlementParty | ReceivingSettlementParty |
| SecuritiesSettlement | NaN | Settlement | Settlement of the securities in a securities transaction, that is, the instruction to deliver or receive securities, involving the payment of an amount of money or not. | NaN | NaN |
| SecuritiesSettlement | TransferOperation | NaN | Set of processes resulting in a securities transfer. | SecuritiesTransfer | RelatedSettlement |
| SecuritiesSettlement | SettlementDate | NaN | Date and time at which a transaction is completed and cleared. It can be an effective settlement date, that is, payment is effected and securities are delivered or an intended settlement date that is, the date and time at which the amount of money is intended to be moved. | ISODateTime | NaN |
| SecuritiesSettlement | PartyRole | NaN | Specifies each role linked to the settlement of securities and played by a party at that step in a securities transaction flow. | SecuritiesSettlementPartyRole | SecuritiesSettlement |
| SecuritiesSettlement | SettlementAmount | NaN | Amount of money settled or to be settled. | ActiveCurrencyAndAmount | NaN |
| SecuritiesSettlement | HoldingsPlanType | NaN | Identifies whether or not saving plan or withdrawal or switch plan are included in the holdings. | Max35Text | NaN |
| SecuritiesSettlement | SecuritiesMovementType | NaN | Specifies if the movement on a securities account results from a deliver or a receive instruction. | ReceiveDeliveryCode | NaN |
| SecuritiesSettlement | SettlementQuantity | NaN | Total quantity of securities to be settled. | SecuritiesQuantity | SecuritiesSettlement |
| SecuritiesSettlement | SecuritiesTradeExecution | NaN | Specifies the trade which originates the settlement process. | SecuritiesTradeExecution | SecuritiesSettlement |
| SecuritiesSettlement | CurrencyToBuy | NaN | Account servicer is instructed to buy the indicated currency after the receipt of cash proceeds. | CurrencyCode | NaN |
| SecuritiesSettlement | CurrencyToSell | NaN | Account servicer is instructed to sell a currency in order to obtain the currency needed to fund the transaction. | CurrencyCode | NaN |
| SecuritiesSettlement | DenominationChoice | NaN | Denomination (stated value found on financial instruments) of the security to be received or delivered. | Max35Text | NaN |
| SecuritiesSettlement | SettlementTransactionCondition | NaN | Conditions under which the order/trade is to be settled. | SettlementTransactionConditionCode | NaN |
| SecuritiesSettlement | BeneficialOwnershipIndicator | NaN | Specifies whether there is change of beneficial ownership. | YesNoIndicator | NaN |
| SecuritiesSettlement | MarketClientSide | NaN | Specifies if an instruction is for a market side or a client side transaction. | MarketClientSideCode | NaN |
| SecuritiesSettlement | Tracking | NaN | Specifies whether the loan and/or collateral is tracked. | YesNoIndicator | NaN |
| SecuritiesSettlement | LetterOfGuarantee | NaN | Specifies whether physical settlement may be executed using a letter of guarantee or if the physical certificates should be used. | YesNoIndicator | NaN |
| SecuritiesSettlement | EligibleForCollateral | NaN | Specifies whether securities should be included in the pool of securities eligible for collateral purposes. | YesNoIndicator | NaN |
| SecuritiesSettlement | AccruedInterestIndicator | NaN | Indicates whether the net proceeds include interest accrued on the financial instrument. | YesNoIndicator | NaN |
| SecuritiesSettlement | PreConfirmation | NaN | Pre-confirmation of the cash transfer pending the securities transfer, or vice versa. | PreConfirmationCode | NaN |
| SecuritiesSettlement | SecuritiesRealTimeGrossSettlement | NaN | Specifies whether the settlement transaction is to be settled through an RTGS or a non RTGS system. | YesNoIndicator | NaN |
| SecuritiesSettlement | BlockTrade | NaN | Specifies whether the settlement instruction is a block parent or child. | BlockTradeCode | NaN |
| SecuritiesSettlement | SettlementSystemMethod | NaN | Specifies whether the settlement instruction is to be settled through the default or the alternate settlement system. | SettlementSystemMethodCode | NaN |
| SecuritiesSettlement | AutomaticBorrowing | NaN | Condition for automatic borrowing. | AutoBorrowingCode | NaN |
| SecuritiesSettlement | PartialSettlementIndicator | NaN | Specifies whether partial settlement is allowed. | YesNoIndicator | NaN |
| SecuritiesSettlement | HoldIndicator | NaN | Specifies whether the transaction is on hold/blocked/frozen. | YesNoIndicator | NaN |
| SecuritiesSettlement | RequestedSafekeepingPlace | NaN | Place requested as the place of safekeeping. | SafekeepingPlace | SecuritiesSettlement |
| SecuritiesSettlement | PairOff | NaN | Buy and sell trades are settled in cash, based on the difference in the prices between the off-setting trades. | PairOff | RelatedSecuritiesSettlement |
| SecuritiesSettlement | AccruedInterest | NaN | Interest included in the settlement. | Interest | SecuritiesSettlement |
| SecuritiesSettlement | SecuritiesClearing | NaN | Clearing process which triggers the settlement process. | SecuritiesClearing | SecuritiesSettlement |
| SecuritiesSettlement | Payment | NaN | Specifies the cash payment information of a securities settlement. | Payment | RelatedSecuritiesSettlement |
| SecuritiesSettlement | SettledAllocation | NaN | Allocation which is settled. | Allocation | SettlementExecutionParameters |
| SecuritiesSettlement | RelatedForeignExchangeOperation | NaN | Entry details related to currency exchange information. | ForeignExchangeTrade | CurrencyExchangeForSecuritiesSettlement |
| SecuritiesSettlement | Security | NaN | Security which is settled. | Security | SecuritiesSettlement |
| SecuritiesSettlement | Position | NaN | Information on the quantities and amounts to be settled in a position. | Position | SecuritiesSettlement |
| SecuritiesSettlement | Rollover | NaN | Process whereby a financial instrument is reinvested at maturity. | Rollover | SecuritiesSettlement |
| SecuritiesSettlement | TurnedQuantity | NaN | Relates to a turnaround: the same security is bought and sold to settle the same day, to or from different brokers. | SecuritiesQuantity | RelatedTurnaroundSettlement |
| SecuritiesSettlement | SettlementReason | NaN | Specifies the reason for the settlement related to the type of underlying trade. | ObligationTypeCode | NaN |
| SecuritiesSettlement | SettlementType | NaN | Specifies how the transaction is to be settled, eg, against payment. | DeliveryReceiptTypeCode | NaN |
| SecuritiesSettlement | BuyInState | NaN | Status of the buy-in transaction. | BuyInStateCode | NaN |
| SecuritiesSettlement | BuyInDeferral | NaN | Specifies if the buy-in transaction was deferred or not. | BuyInDeferralCode | NaN |
| SecuritiesSettlement | CashCompensationAmount | NaN | Amount of money that has to be paid by the failing trading party in case of an unsuccessful or partially successful buy-in transaction. | ActiveCurrencyAndAmount | NaN |
| LotBreakdown | NaN | NaN | Number of securities purchased or sold in one transaction. In terms of options, a lot represents the number of contracts contained in one derivative security. | NaN | NaN |
| LotBreakdown | LotUnit | NaN | Quantity of securities included in the lot. | DecimalNumber | NaN |
| LotBreakdown | SecuritiesQuantity | NaN | Number of securities included in a lot. | SecuritiesQuantity | LotBreakdown |
| LotBreakdown | LotNumber | NaN | Specifies the number of the lot. | GenericIdentification | IdentificationForLot |
| LotBreakdown | LotDateTime | NaN | Date and time at which the lot was purchased. | ISODateTime | NaN |
| LotBreakdown | LotPrice | NaN | Specifies the price of the lot. | SecuritiesPricing | LotBreakdown |
| LotBreakdown | LotIdentifier | NaN | Identifies the lot constituting an asset backed or mortgage backed security issue. | Max35Text | NaN |
| LotBreakdown | TradeLotMarket | NaN | Market for which a trade lot is specified. | TradingMarket | TradeLotSize |
| LotBreakdown | QuoteLotMarket | NaN | Market for which a quote lot is specified. | TradingMarket | QuoteLot |
| LotBreakdown | RoundLotMarket | NaN | Market for which a round lot size is specified. | TradingMarket | RoundLot |
| Price | NaN | NaN | Amount of money for which goods, services or assets are offered, sold, or bought. | NaN | NaN |
| Price | Amount | NaN | Price expressed as a currency and value. | CurrencyAndAmount | NaN |
| Price | Option | NaN | Option for which a strike price is specified. | Option | StrikePrice |
| Price | UnitPriceProduct | NaN | Product for which a unit price is specified. | Product | UnitPrice |
| Price | NetPriceProduct | NaN | Product for which a net price is specified. | Product | NetPrice |
| Price | PriceAdjustment | NaN | Variance on price for the goods and services. | Adjustment | Price |
| Price | GrossPriceProduct | NaN | Product for which a gross price is specified. | Product | GrossPrice |
| Price | UnitOfMeasure | NaN | Specifies the unit of measurement. For example: kilo, tons. | UnitOfMeasureCode | NaN |
| Price | PriceTolerance | NaN | Variance allowed on the price of goods. | Tolerance | Price |
| Price | Currency | NaN | Currency code in which the price is expressed. | CurrencyCode | NaN |
| Price | Factor | NaN | Multiplication factor of measurement values. For example: 36 pieces. | Max15NumericText | NaN |
| Price | Netting | NaN | Netting for which an average price is specified. | Netting | AverageDealPrice |
| Price | SecuritiesPricing | NaN | Pricing parameters for a security. | SecuritiesPricing | Price |
| Price | RelatedEnergy | NaN | Specifies related energy price. | Energy | Price |
| AmountAndPrice | NaN | NaN | Expression of amount. | NaN | NaN |
| AmountAndPrice | Amount | NaN | Amount expressed as an amount of money. | CurrencyAndAmount | NaN |
| AmountAndPrice | Price | NaN | Amount expressed as a price. | NaN | NaN |
| Charges | NaN | Adjustment | Amount of money associated with a service. | NaN | NaN |
| Charges | ChargeType | NaN | Type of service for which a charge is asked or paid. | ChargeTypeCode | NaN |
| Charges | CalculationBasis | NaN | Calculation basis for the charge or fee. | CalculationBasisCode | NaN |
| Charges | BearerType | NaN | Specifies which party/parties will bear the charges associated with the processing of the payment transaction. | ChargeBearerTypeCode | NaN |
| Charges | ChargesDebitAccount | NaN | Account from which a charge is debited. | CashAccount | Charges |
| Charges | CashEntry | NaN | Entry which contains the charges. | CashEntry | Charges |
| Charges | CreditDebitIndicator | NaN | Indicates whether a charge is a credit or a debit. | DebitCreditCode | NaN |
| Charges | MaximumAmount | NaN | Maximum amount of money asked or paid for the charge for example depending on the type of investors. | CurrencyAndAmount | NaN |
| Charges | InvestmentFundTransaction | NaN | Investment fund transaction for which charges are specified. | InvestmentFundTransaction | TransactionCharge |
| Charges | LogisticsChargeLineItem | NaN | Specifies the line item to which the logistics charge applies. | LineItem | LogisticsCharge |
| Charges | Transport | NaN | Specifies the transport process to which the charges apply. | Transport | TransportCharges |
| Charges | Services | NaN | Account services for which account administration charges are specified. | AccountService | AccountAdministrationCharge |
| Charges | RelatedUndertaking | NaN | Undertaking for which charges are specified. | Undertaking | Charges |
| Charges | LineItem | NaN | Line item for which charges are specified | LineItem | Charges |
| Charges | NetPriceChargeLineItem | NaN | Specifies the line item to which the net price charge applies. | LineItem | NetPriceCharge |
| Charges | BaseAmount | NaN | Amount on which the charges are calculated. | CurrencyAndAmount | NaN |
| Charges | MaximumRate | NaN | Maximum rate used to calculate the amount of the charge or fee for example depending on the type of investors. | PercentageRate | NaN |
| Charges | MinimumRate | NaN | Minimum rate used to calculate the amount of the charge or fee for example depending on the type of investors. | PercentageRate | NaN |
| Charges | MinimumAmount | NaN | Minimum amount of money asked or paid for the charge for example depending on the type of investors. | CurrencyAndAmount | NaN |
| Charges | RelatedInterest | NaN | Interest on which charges are applied. | InterestCalculation | Charges |
| Charges | ChargePaymentMethod | NaN | Specifies how charges are paid. | ChargePaymentMethodCode | NaN |
| SecuritiesRelatedFees | NaN | Charges | Fees related to securities trades. | NaN | NaN |
| SecuritiesRelatedFees | Security | NaN | Security for which fees are specified. | Security | Fees |
| SecuritiesRelatedFees | PostageFeeAmount | NaN | Amount of money paid for delivery by regular post mail. | CurrencyAndAmount | NaN |
| SecuritiesRelatedFees | RegulatoryFeesAmount | NaN | Amount of money charged by a regulatory authority, eg, Securities and Exchange fees. | CurrencyAndAmount | NaN |
| SecuritiesRelatedFees | ShippingFeesAmount | NaN | Amount of money (including insurance) paid for delivery by carrier. | CurrencyAndAmount | NaN |
| SecuritiesRelatedFees | ResearchFee | NaN | Charge or commission paid by the investor to a distributor/intermediary or other service provider for the provision of financial research. | CurrencyAndAmount | NaN |
| ValuationStatistics | NaN | NaN | Statistical data related to the price change of a security. | NaN | NaN |
| ValuationStatistics | Currency | NaN | Currency of the net asset value calculation. | CurrencyCode | NaN |
| ValuationStatistics | PriceTypeChangeBasis | NaN | Type of price from which the change is calculated, eg, bid, offer, or single. | TypeOfPriceCode | NaN |
| ValuationStatistics | PriceChange | NaN | Change in price since the last valuation. | SecuritiesPricing | PriceChangeRelatedStatistics |
| ValuationStatistics | Yield | NaN | Rate of income from the financial instrument, usually calculated as total dividends or coupon interest available to investors in the last year,divided by the current price. | PercentageRate | NaN |
| ValuationStatistics | HighestPriceValue | NaN | Highest price for the referenced period. | SecuritiesPricing | HighestPriceValueRelatedStatistics |
| ValuationStatistics | LowestPriceValue | NaN | Lowest price for the referenced period. | SecuritiesPricing | LowestPriceValueRelatedStatistics |
| ValuationStatistics | Period | NaN | Reference period for the valuation. | DateTimePeriod | ValuationStatistics |
| ValuationStatistics | NetAssetValueCalculation | NaN | Information related to the price valuation of an investment fund class. | NetAssetValueCalculation | ValuationStatistics |
| ValuationStatistics | NetAssetValueChangeRate | NaN | Rate of change of the net asset value. | PercentageRate | NaN |
| FundManagerRole | NaN | InvestmentFundPartyRole | Legal entity that sets up a fund, appoints agents, decides and implements an investment strategy. That is, selects portfolio investments in accordance with the objectives and strategy in the fund's prospectus, and places orders to effect or liquidate selected investments in accordance with net flow of capital into or out of the fund. Also called fund promoter or fund sponsor. | NaN | NaN |
| PerformanceFactors | NaN | NaN | Performance factors of the investment fund / fund class. | NaN | NaN |
| PerformanceFactors | NetAssetValueCalculation | NaN | Calculation for which the performance factors are obtained. | NetAssetValueCalculation | InvestmentFundPerformanceFactors |
| PerformanceFactors | CorporateActionFactor | NaN | Value of the NAV before all corporate events of the valuation date, divided by the value of the NAV after the corporate event. | DecimalNumber | NaN |
| PerformanceFactors | CumulativeCorporateActionFactor | NaN | Value of the NAV before a corporate event, divided by the value of the NAV after the corporate event, accumulated for a number of corporate events over the defined period of time. | DecimalNumber | NaN |
| PerformanceFactors | AccumulationPeriod | NaN | Period of time for the calculation of the cumulative corporate action factor. | DateTimePeriod | PerformanceFactors |
| PerformanceFactors | NormalPerformance | NaN | Normal performance value of the NAV. | DecimalNumber | NaN |
| CashAccountContract | NaN | AccountContract | Account contract established between the organisation or the group to which the organisation belongs, and the account servicer. | NaN | NaN |
| CashAccountContract | CashAccount | NaN | Specifies the account which is managed by the stipulations of the contract. it is derived from the association between AccountContract and Account. | CashAccount | CashAccountContract |
| CashAccountContract | TransferCashAccount | NaN | Identification of the account to/from which the balance of the account must be transferred. | CashAccount | ClosedAccountContract |
| CashAccountContract | Services | NaN | Operations on a bank account that are allowed as part of the services offered to the owners of a bank account. It is derived from the association between AccountContract and AccountService. | CashAccountService | CashAccountContract |
| CashAccountContract | BalanceTransfer | NaN | Specifies the transfer of a positive balance (fully or partially) or the transfer of cash to compensate a negative balance. This transfer occurs at the closing of the account. It contains the identification of the account to which or from which the amount must be transferred. | PaymentObligation | RelatedAccountClosingTerms |
| CashAccountContract | CashAccountMandate | NaN | Mandate associated with a cash account contract. | CashAccountMandate | CashAccountContract |
| CashAccountService | NaN | AccountService | Services linked to an account which are available to the account owner or to the holder of a mandate. The exercise of these services may be submitted to a limit. | NaN | NaN |
| CashAccountService | CashAccountMandate | NaN | Mandate which specifies the services that can be operated by the mandate holder. | CashAccountMandate | Services |
| CashAccountService | CompensationMethod | NaN | Defines if and how charges and taxes due are paid to the account servicer. | CompensationMethodCode | NaN |
| CashAccountService | BillingCurrency | NaN | Currency used for billing the services related to the account. | BillingCurrencyTypeCode | NaN |
| CashAccountService | BillingChargeMethod | NaN | Defines how the billing charge is calculated. | BillingChargeMethodCode | NaN |
| CashAccountService | PaymentMethod | NaN | Specifies the different payment methods for an account service. | ServicePaymentMethodCode | NaN |
| CashAccountService | CashAccountContract | NaN | Cash account contract which specifies the services linked to a cash account. It is derived from the association between AccountService and AccountContract. | CashAccountContract | Services |
| CashAccountService | Identification | NaN | Identifies the bank operation. | GenericIdentification | RelatedCashAccountService |
| CashAccountService | CashAccount | NaN | Cash account for which services are specified. It is derived from the association between AccountService and Account. | CashAccount | CashAccountService |
| CashManagementService | NaN | CashAccountService | Set of applications that provides services which facilitate the management of cash positions on an account. | NaN | NaN |
| CashManagementService | RiskManagementLimit | NaN | Maximum amount value applied to or by a party versus a specific counterparty or a set of counterparts. The limit can be expressed as a debit limit or a credit limit. | RiskManagementLimit | CashManagementService |
| CashManagementService | StandingOrder | NaN | Specifies standing orders that must be executed in the context of cash management. This service may be offered by a transaction administrator. | CashStandingOrder | RelatedCashServices |
| CashManagementService | RelatedTransactionAdministrator | NaN | Transaction administrator of a cash management service. | TransactionAdministrator | CashManagementService |
| CashManagementService | LiquidityManagementLimit | NaN | Cash management feature limiting the amount of liquidity needed to perform clearing and settlement operations. At any point in time during the process, the limit imposes the maximum amount of liquidity available for operations concerning the system or other managed elements, eg, transaction amount or counterparty. | LiquidityManagementLimit | RelatedCashServices |
| CashManagementService | CallInType | NaN | Type of call when additional funding from a settlement member is requested by a central settlement system. | CallInCode | NaN |
| AccountRestriction | NaN | NaN | Restriction on capability or operations allowed. | NaN | NaN |
| AccountRestriction | Account | NaN | Account on which restrictions are specified. | Account | AccountRestriction |
| AccountRestriction | RestrictionType | NaN | Type of the restriction. | Max35Text | NaN |
| AccountRestriction | ValidityPeriod | NaN | Period during which the restriction is effective. | DateTimePeriod | AccountRestriction |
| SystemStatus | NaN | Status | Status of a system and the period of time during which the status is valid. | NaN | NaN |
| SystemStatus | Status | NaN | Current status of a system. | SystemStatusCode | NaN |
| SystemStatus | MemberStatus | NaN | Status of a member in a system, eg, enabled or deleted. | MemberStatusCode | NaN |
| SystemStatus | System | NaN | System for which a status is specified. | System | Status |
| SystemStatus | SystemMemberRole | NaN | System member role for which a member status is specified. | SystemMemberRole | MemberStatus |
| SystemAvailability | NaN | NaN | information about the periods of activity and non-activity of a system. | NaN | NaN |
| SystemAvailability | AvailableSessionPeriod | NaN | Time window of system activity. | TimePeriod | SystemAvailability |
| SystemAvailability | System | NaN | System for which the system availability is provided. | System | Availability |
| SystemAvailability | ClosureInformation | NaN | System availability parameters which contain closure information. | SystemClosureInformation | SystemAvailability |
| SystemAvailability | Date | NaN | Date for which the availability information is provided. | ISODate | NaN |
| SystemAvailability | ClosurePeriod | NaN | Period for which the system is closed/not operating. | DateTimePeriod | RelatedSystemAvailability |
| TimePeriod | NaN | NaN | Particular time span specified between a start time and an end time. The time period cannot exceed 24 hours. | NaN | NaN |
| TimePeriod | SystemAvailability | NaN | System for which a session period is specified. | SystemAvailability | AvailableSessionPeriod |
| TimePeriod | FromTime | NaN | Time at which the time span starts. | ISOTime | NaN |
| TimePeriod | ToTime | NaN | Time at which the time span ends. | ISOTime | NaN |
| SystemClosureInformation | NaN | NaN | Information about inactivity of a system. | NaN | NaN |
| SystemClosureInformation | Period | NaN | Period of time when the system is closed/not operating. | NaN | NaN |
| SystemClosureInformation | SystemAvailability | NaN | System for which closure information is specified. | SystemAvailability | ClosureInformation |
| SystemClosureInformation | ClosureReason | NaN | Reason the system is closed/not operating. | SystemClosureReasonCode | NaN |
| SystemBusinessInformation | NaN | NaN | Details about business information related to a system. | NaN | NaN |
| SystemBusinessInformation | Qualifier | NaN | Further information about the criticality or importance of a general business information system. | InformationQualifier | SystemBusinessInformation |
| SystemBusinessInformation | Subject | NaN | Subject line of an item of general business information, summarizing the topic and intended destination of the information. | Max35Text | NaN |
| SystemBusinessInformation | SubjectDetails | NaN | General business information, in unstructured form. | Max350Text | NaN |
| SystemBusinessInformation | Identification | NaN | Unique and unambiguous identification of a general business information system, as assigned by the system transaction administrator. | Max35Text | NaN |
| SystemBusinessInformation | Reference | NaN | Unique and unambiguous reference assigned to a general business information system. | Max35Text | NaN |
| SystemBusinessInformation | System | NaN | System for which business information is generated. | System | SystemGeneratedInformation |
| InformationQualifier | NaN | NaN | Further qualifies the information provided in terms of its importance and its format. | NaN | NaN |
| InformationQualifier | SystemBusinessInformation | NaN | System for which a qualifier is specified. | SystemBusinessInformation | Qualifier |
| InformationQualifier | IsFormatted | NaN | Indicates whether the information is formatted. | YesNoIndicator | NaN |
| InformationQualifier | Priority | NaN | Priority of the information. | PriorityCode | NaN |
| LimitStatus | NaN | Status | Current status of the limit. | NaN | NaN |
| LimitStatus | Limit | NaN | Limit for which a status is provided. | Limit | LimitStatus |
| LimitStatus | Status | NaN | Current status of the limit. | LimitStatusCode | NaN |
| BookEntry | NaN | CreditInstrument | Movement of cash between two accounts. One account is debited and the other account is credited. | NaN | NaN |
| BookEntry | CashEntry | NaN | Specifies the amount transferred on the account. An account entry may result in several cash entries for instance net amount (credited) and charges (debited). | CashEntry | RelatedBookEntry |
| BookEntry | DebitEntry | NaN | Specifies the debit entry resuling from a settlement instruction. | CashEntry | DebitRelatedBookEntry |
| BookEntry | CreditEntry | NaN | Specifies the credit entry resuling from a settlement instruction. | CashEntry | CreditRelatedBookEntry |
| BookEntry | TransferAdvice | NaN | Indicates that when an amount of money has been transferred in the books of the account servicer, an advice should be sent back to the account owner. | YesNoIndicator | NaN |
| BookEntry | FundSubscriptionCashInFlow | NaN | Amount of money received from investors as a result of a subscription. | FundsCashFlow | FundSubscriptionAccountEntry |
| BookEntry | FundRedemptionCashOutFlow | NaN | Amount of money paid to investors as a result of a redemption. | FundsCashFlow | FundRedemptionAccountEntry |
| BookEntry | RelatedSettlementInstruction | NaN | Related settlement instruction wich is the source of the book entry. | CashSettlement | BookEntry |
| SecuritiesEntry | NaN | Entry | Posting to a securities account as a result of a securities creation, deletion or transfer in the context of a securities transaction. | NaN | NaN |
| SecuritiesEntry | AcquisitionDate | NaN | Date upon which the investor purchased the financial instrument. | ISODate | NaN |
| SecuritiesEntry | FinancialInstrumentQuantity | NaN | Quantity of financial instrument. | SecuritiesQuantity | Entry |
| SecuritiesEntry | SecuritiesAccount | NaN | Securities account on which the quantity of the entry is debited or credited. It is derived from the association between Entry and Account. | SecuritiesAccount | SecuritiesEntry |
| SecuritiesEntry | SecuritiesBalance | NaN | Amount that is the result of the sum of the entries from or to an account. It is derived from the association between Entry and Balance. | SecuritiesBalance | SecuritiesEntry |
| SecuritiesEntry | TriggeringSecuritiesTransfer | NaN | Transfer which is at the origin of the entry in the securities account. | SecuritiesTransfer | BookEntry |
| SecuritiesCertificate | NaN | NaN | Physical representation of a security. | NaN | NaN |
| SecuritiesCertificate | Number | NaN | Identifier of a certificate assigned by the issuer. | GenericIdentification | IdentificationForSecuritiesCertificate |
| SecuritiesCertificate | BasicRegistration | NaN | Registration process which requires a securities certificate. | BasicSecuritiesRegistration | SecuritiesCertificate |
| SecuritiesCertificate | RelatedDelivery | NaN | Delivery parameters which specify the certificate parameters. | PhysicalDelivery | IssuedCertificateNumber |
| Interest | NaN | NaN | Consideration, such as amount of money, paid or received in exchange for an asset that has been invested, loaned or borrowed for a certain period. The interest is expressed as a fixed amount or percentage of the amount upon which the interest is applied. | NaN | NaN |
| Interest | AccruedInterestAmount | NaN | Interest amount that has accrued in between coupon payment periods. | CurrencyAndAmount | NaN |
| Interest | InterestCalculation | NaN | Calculation parameters used to obtain the interest amount. | InterestCalculation | Interest |
| Interest | Amount | NaN | Amount of money representing interest payments. | CurrencyAndAmount | NaN |
| Interest | Rate | NaN | The actual interest rate used for the payment of the interest for the specified interest period. | PercentageRate | NaN |
| Interest | RelatedCashProceedsDefinition | NaN | Cash proceeds definition for which an interest is provided. | CashProceedsDefinition | Interest |
| Interest | SecuritiesFinancing | NaN | Specifies the financing trade on which this interest apply. | SecuritiesFinancing | Interest |
| Interest | InterestTax | NaN | Specifies the tax on interest. | Tax | Interest |
| Interest | CreditDebitIndicator | NaN | Indicates whether the interest is a debit or credit. | DebitCreditCode | NaN |
| Interest | CashEntry | NaN | Entry which contains the interest. | CashEntry | Interest |
| Interest | PaymentDate | NaN | Date of the next interest payment. | ISODate | NaN |
| Interest | RelatedInterestManagement | NaN | Management of interest which consists into calculating the interest, requesting its payment or distributing the interest proceeds. | InterestManagement | Interest |
| Interest | RelatedUndertakingAmount | NaN | Undertaking amount for which an interest is specified. | UndertakingAmount | Interest |
| Interest | RelatedDebitCreditFacility | NaN | Debit and credit facilities on which the interest applies. | DebitCreditFacility | CashAccountInterest |
| Interest | SecuritiesSettlement | NaN | Securities settlement process for which an accrued interest is specified. | SecuritiesSettlement | AccruedInterest |
| Interest | InterestName | NaN | Interest rate expressed as a rate name. | GenericIdentification | IdentificationForInterestName |
| Interest | RelatedAssetHolding | NaN | Asset holding on which interest is paid. | AssetHolding | Interest |
| Interest | Deposit | NaN | Deposit for which an interest is specified. | Deposit | Interest |
| Interest | AccountBalance | NaN | Balance for which an interest is calculated. | Balance | Interest |
| Interest | RelatedAccountContract | NaN | Account contract for which interest parameters are specified. | AccountContract | Interest |
| Interest | RelatedNetAssetValueCalculation | NaN | Net asset value calculation for which an accrued interest is specified. | NetAssetValueCalculation | Interest |
| Interest | TypeOfInterest | NaN | Specifies the type of interest associated with a trade. | InterestTypeCode | NaN |
| Interest | RelatedPaymentCard | NaN | Payment card for which interest on due amounts is specified. | PaymentCard | Interest |
| SafekeepingPlace | NaN | SecuritiesPartyRole | Organisation used as the safekeeping place for the securities. | NaN | NaN |
| SafekeepingPlace | SafekeepingPlaceType | NaN | Place of safekeeping. | SafekeepingPlaceCode | NaN |
| SafekeepingPlace | Country | NaN | Country where the financial instruments are/will be safekept. | Country | CountryForSafekeepingPlace |
| SafekeepingPlace | RelatedSecuritiesAccount | NaN | Account at the safekeeping place where financial instruments are safekept. | SecuritiesAccount | SafekeepingPlace |
| SafekeepingPlace | SecuritiesBalance | NaN | Balance which is held at a safekeeping place. | SecuritiesBalance | SafekeepingPlace |
| SafekeepingPlace | SecuritiesSettlement | NaN | Specifies the settlement operation which uses the safekeeping place. | SecuritiesSettlement | RequestedSafekeepingPlace |
| PhysicalDelivery | NaN | NaN | Parameters of a physical delivery. | NaN | NaN |
| PhysicalDelivery | RelatedTransfer | NaN | Transfer process which requires physical delivery of the securities. | SecuritiesTransfer | PhysicalDelivery |
| PhysicalDelivery | RegisteredAddressIndicator | NaN | Indicates whether the address for the physical delivery is the registered address. | YesNoIndicator | NaN |
| PhysicalDelivery | IssuedCertificateNumber | NaN | Certificate representing a security that is delivered. | SecuritiesCertificate | RelatedDelivery |
| PhysicalDelivery | Address | NaN | Address for physical delivery. | PostalAddress | PhysicalDelivery |
| PhysicalDelivery | Type | NaN | Specifies the type of delivery. | PhysicalTransferTypeCode | NaN |
| SecuritiesTradeExecution | NaN | NaN | Transaction between two counterparties in which they agree to buy and sell a financial instrument. A trade transaction occurs with the matching of the two counterparties orders. There could be several trade transactions necessary to execute the trade. | NaN | NaN |
| SecuritiesTradeExecution | StampDutyIndicator | NaN | Whether the net proceeds include stamp duty amount. | YesNoIndicator | NaN |
| SecuritiesTradeExecution | ProcessingPosition | NaN | When the transaction is to be executed relative to a linked transaction. | ProcessingPositionCode | NaN |
| SecuritiesTradeExecution | SecuritiesSettlement | NaN | Process of settling securities. | SecuritiesSettlement | SecuritiesTradeExecution |
| SecuritiesTradeExecution | DealPrice | NaN | Specifies the price of the traded financial instrument.This is the deal price of the individual trade transaction. If there is only one trade transaction for the execution of the trade, then the deal price could equal the executed trade price (unless, for example, the price includes commissions or rounding, or some other factor has been applied to the deal price or the executed trade price, or both). | SecuritiesPricing | SecuritiesTradeExecution |
| SecuritiesTradeExecution | MarginAmount | NaN | Difference in prices at which a dealer will buy and sell. | CurrencyAndAmount | NaN |
| SecuritiesTradeExecution | ExecutedTradeQuantity | NaN | Quantity of financial instrument executed by the trading party. | SecuritiesQuantity | SecuritiesTradeExecution |
| SecuritiesTradeExecution | OffMarketReason | NaN | Reason for which the trade was executed off-market. | OffMarketCode | NaN |
| SecuritiesTradeExecution | RelatedTrade | NaN | Trade which is executed through one or more execution trades. | SecuritiesTrade | TradingExecution |
| SecuritiesTradeExecution | DealExecutionAmount | NaN | Deal price multiplied by the quantity of a financial instrument traded for the specific trade transaction i.e. the partially filled quantity. | CurrencyAndAmount | NaN |
| SecuritiesTradeExecution | PaymentObligation | NaN | Specifies the cash delivery obligations resulting from the trade. | PaymentObligation | ExecutedSecuritiesTrade |
| SecuritiesTradeExecution | SecuritiesDeliveryObligation | NaN | Specifies the securities delivery obligations resulting from the trade. | SecuritiesDeliveryObligation | SecuritiesTradeExecution |
| SecuritiesTradeExecution | ReportingType | NaN | Specifies that a trade is to be reported to a third party. | ReportingCode | NaN |
| ContactPersonRole | NaN | Role | Person to be contacted in a given organisation. In the corporate action domain (including meeting notifications) , it is the contact person at the party organising the meeting, at the issuer or at an intermediary. | NaN | NaN |
| ContactPersonRole | Role | NaN | Role for which a contact person is specified. | Role | ContactPersonRole |
| ContactPersonRole | Meeting | NaN | Meeting for which a person is the contact. | Meeting | Person |
| ContactPersonRole | Person | NaN | Identifies the person which plays the role of contact. | Person | ContactPersonRole |
| DeliveringSettlementParty | NaN | SecuritiesSettlementPartyRole | Party that is responsible for delivering securities as part of a chain of settlement parties or as party that sells them. | NaN | NaN |
| DeliveringSettlementParty | DeliveringSettlementParty | NaN | Specifies the settlement party which is followed by another party. | DeliveringSettlementParty | NextParty |
| DeliveringSettlementParty | NextParty | NaN | Next party in the delivering side of the settlement the transaction chain. | DeliveringSettlementParty | DeliveringSettlementParty |
| SecuritiesSettlementSystem | NaN | System | Specifies the system used in a settlement process. | NaN | NaN |
| SecuritiesSettlementSystem | SettlementParty | NaN | Party which settles through a system. | SecuritiesSettlementPartyRole | SecuritiesSettlementSystem |
| SecuritiesTradeStatus | NaN | Status | Status of a securities trade. | NaN | NaN |
| SecuritiesTradeStatus | MatchingStatus | NaN | Status of matching of a trade. | MatchingStatusCode | NaN |
| SecuritiesTradeStatus | AffirmationStatus | NaN | Status of affirmation of a trade. | AffirmationStatusCode | NaN |
| SecuritiesTradeStatus | Reason | NaN | Specifies the reasons for the status. It is derived from the relationship between Status and Status Reason. | SecuritiesTradeStatusReason | SecuritiesTradeStatus |
| SecuritiesTradeStatus | SecuritiesTrade | NaN | Specifies the trade which has a specific status. | SecuritiesTrade | SecuritiesTradeStatus |
| SecuritiesTradeStatus | TransactionStatus | NaN | Status of an investment fund transaction. | TransactionStatusCode | NaN |
| SecuritiesTradeStatus | ReplacementProcessingStatus | NaN | Provides the processing status of the replacement request. | ReplacementProcessingStatusCode | NaN |
| SecuritiesTradeStatus | CancellationStatus | NaN | Status of the cancellation of a trade. | CancellationStatusCode | NaN |
| SecuritiesTradeStatus | CancellationRight | NaN | Cancellation right of an investor with respect to an order. | CancellationRightCode | NaN |
| SecuritiesTradeStatus | TransferStatus | NaN | Status of the transfer is accepted, sent to next party, matched, already executed, or settled. | TransferStatusCode | NaN |
| SecuritiesTradeStatus | AllegedStatus | NaN | Provides the status of an allegement. | AllegementStatusCode | NaN |
| SecuritiesTradeStatus | CollateralAllocationStatus | NaN | Provides the status of allocation of collateral to cover the instruction. | AllocationStatusCode | NaN |
| SecuritiesTradeStatus | RepoCallRequestStatus | NaN | Specifies additional information about the status of the repurchase agreement call processed instruction. | RepoCallRequestStatusCode | NaN |
| SecuritiesTradeStatus | SettlementConditionModificationStatus | NaN | Provides the status of the securities settlement condition modification request. | SettlementConditionModificationStatusStatusCode | NaN |
| SecuritiesTradeStatus | MatchingProcess | NaN | Specifies the matching status of a trade. | MatchingProcessCode | NaN |
| SecuritiesTradeStatus | RelatedSecuritiesTransfer | NaN | Transfer operation for which a status is provided | SecuritiesTransfer | Status |
| SecuritiesTradeStatus | TradeConfirmationStatus | NaN | Specifies whether the contract was electronically confirmed, non-electronically confirmed or remains unconfirmed. | TradeConfirmationTypeCode | NaN |
| SecuritiesTradeStatusReason | NaN | StatusReason | Specifies the underlying reason for a status of a securities trade. | NaN | NaN |
| SecuritiesTradeStatusReason | UnmatchedReason | NaN | Reason for the unmatched status. | UnmatchedReasonCode | NaN |
| SecuritiesTradeStatusReason | DeniedReason | NaN | Specifies the reason why the request was denied. | DeniedReasonCode | NaN |
| SecuritiesTradeStatusReason | SecuritiesTradeStatus | NaN | Status for which a reason is provided. It is derived from the association between StatusReason and Status. | SecuritiesTradeStatus | Reason |
| SecuritiesTradeStatusReason | GeneratedReason | NaN | Specifies the reason why the transaction was generated. | GeneratedReasonCode | NaN |
| SecuritiesTradeStatusReason | AllegementReason | NaN | Reason why the instruction has an allegement status. | AllegementReasonCode | NaN |
| SecuritiesTradeStatusReason | PendingSettlementReason | NaN | Reason for the settlement pending status. | PendingSettlementStatusReasonCode | NaN |
| SecuritiesTradeStatusReason | RepoCallAcknowledgementReason | NaN | Specifies additional information about the processed instruction. | RepoCallAcknowledgementReasonCode | NaN |
| SecuritiesTradeStatusReason | RepairReason | NaN | Specifies the reason why the instruction/request has a repair status. | RepairReasonV2Code | NaN |
| SecuritiesTradeStatusReason | DeliveryReturnReason | NaN | Reason why the trade was returned. | DeliveryReturnCode | NaN |
| SecuritiesTradeStatusReason | CounterpartyStatusReason | NaN | Specifies the counterparty action which is the reason of the trade status. | CounterpartyResponseStatusReasonCode | NaN |
| SecuritiesTradeStatusReason | ModifiedStatusReason | NaN | Specifies the reason why the related instruction is modified. | ModifiedStatusReasonCode | NaN |
| CorporateActionStatus | NaN | Status | Status of the corporate action process. | NaN | NaN |
| CorporateActionStatus | AgentStandingInstructionStatus | NaN | Specifies the state or the condition. | Max350Text | NaN |
| CorporateActionStatus | ProcessingStatus | NaN | Specifies the status of the details of the event. | ProcessingStatusCode | NaN |
| CorporateActionStatus | EventProcessingStatus | NaN | Processing status of the corporate action event. | CorporateActionEventProcessingStatusCode | NaN |
| CorporateActionStatus | CorporateActionStatusReason | NaN | Specifies the reasons for the status. It is derived from the relationship between Status and Status Reason. | CorporateActionStatusReason | CorporateActionStatus |
| CorporateActionStatus | InstructionCancellationStatus | NaN | Status of the instruction cancellation process. | CorporateActionInstructionCancellationProcessingStatusCode | NaN |
| CorporateActionStatus | CorporateActionInstructionProcessingStatus | NaN | Status of the corporate action instruction process. | CorporateActionInstructionProcessingStatusCode | NaN |
| CorporateActionStatus | RateStatus | NaN | Specifies whether the rate is indicative or actual. | RateStatusCode | NaN |
| CorporateActionStatus | OptionAvailabilityStatus | NaN | Availability status of the option. | OptionAvailabilityStatusCode | NaN |
| CorporateActionStatus | CorporateActionEvent | NaN | Corporate event for which a status is provided. | CorporateActionEvent | CorporateActionStatus |
| CorporateActionStatus | EventStatus | NaN | Status of the corporate action event. | CorporateActionEventStatusCode | NaN |
| CorporateActionStatus | RelatedInstructionProcessedStatus | NaN | Information on the status of the processing of an instruction related to a corporate action. | CorporateActionProcessedStatusCode | NaN |
| CorporateActionStatus | DeactivationDateAndTime | NaN | Date and time at which the the corporate action event or the option is deactivated. | ISODateTime | NaN |
| CorporateActionStatus | EventConfirmationStatus | NaN | Indicates the status of the occurrence of an event. | EventConfirmationStatusCode | NaN |
| CorporateActionStatus | EventCompletenessStatus | NaN | Indicates whether the details provided about an event are complete or incomplete. | EventCompletenessStatusCode | NaN |
| SecuritiesDeliveryObligation | NaN | Obligation | Obligation for one party to deliver securities to another party. | NaN | NaN |
| SecuritiesDeliveryObligation | CCPEligibility | NaN | Specifies whether the settlement transaction is CCP (Central Counterparty) eligible. | YesNoIndicator | NaN |
| SecuritiesDeliveryObligation | NettingEligibility | NaN | Specifies whether the settlement transaction is eligible for netting. | YesNoIndicator | NaN |
| SecuritiesDeliveryObligation | TransferInstructionDate | NaN | Date at which the instructing party places the transfer instruction. | ISODateTime | NaN |
| SecuritiesDeliveryObligation | TransferCurrency | NaN | Identifies the currency to be used to transfer the holdings. | CurrencyCode | NaN |
| SecuritiesDeliveryObligation | RelatedCorporateAction | NaN | Corporate action processes which are the source of the securities delivery obligation. | CorporateActionProceedsDeliveryInstruction | SecuritiesProceedsMovement |
| SecuritiesDeliveryObligation | RelatedCollateralMovement | NaN | Collateral movement which is the source of the obligation. | CollateralMovement | SecuritiesCollateralMovement |
| SecuritiesDeliveryObligation | SecuritiesTradeExecution | NaN | Specifies the trade which originates the delivery obligation. | SecuritiesTradeExecution | SecuritiesDeliveryObligation |
| SecuritiesDeliveryObligation | RelatedPortfolioTransfer | NaN | Portfolio transfer which is the source of the securities delivery obligation. | PortfolioTransfer | SecuritiesDeliveryObligation |
| SecuritiesDeliveryObligation | SecuritiesTransfer | NaN | Completion of a securities settlement instruction, wherein securities are delivered/debited from a securities account and received/credited to the designated securities account. | SecuritiesTransfer | SecuritiesDeliveryObligation |
| SecuritiesDeliveryObligation | SettlementInstructionGeneration | NaN | Specifies whether the ETC provider should generate settlement instructions or not. | YesNoIndicator | NaN |
| SecuritiesDeliveryObligation | SettlementDateCode | NaN | Requested date of trade settlement, in coded form, for example, trade date +1). | SettlementDateCode | NaN |
| SecuritiesDeliveryObligation | SecuritiesLending | NaN | Securities lending process which covers the delivery of securities by the seller. | SecuritiesLending | SecuritiesDeliveryObligation |
| CurrencyExchange | NaN | NaN | Information needed to process a currency exchange or conversion. | NaN | NaN |
| CurrencyExchange | OriginalAmount | NaN | Amount in its original currency when conversion from/into another currency has occurred. | CurrencyAndAmount | NaN |
| CurrencyExchange | CurrencyExchangeForForeignExchangeTrade | NaN | Trade which uses the specified exchange rate. | ForeignExchangeTrade | AgreedRate |
| CurrencyExchange | UnitCurrency | NaN | Currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP = xxxCUR, the unit currency is GBP. | CurrencyCode | NaN |
| CurrencyExchange | QuotedCurrency | NaN | Currency into which the base currency is converted, in a currency exchange. | CurrencyCode | NaN |
| CurrencyExchange | ExchangeRate | NaN | The value of one currency expressed in relation to another currency. ExchangeRate expresses the ratio between UnitCurrency and QuotedCurrency (ExchangeRate = UnitCurrency/QuotedCurrency). | BaseOneRate | NaN |
| CurrencyExchange | ResultingAmount | NaN | Amount of money resulting from a foreign exchange transaction. | CurrencyAndAmount | NaN |
| CurrencyExchange | RelatedCorporateActionEvent | NaN | Corporate action for which the offeror/issuer has specified an exchange rate for the payment in a currency different from the announced one. | CorporateActionEvent | ExchangeRate |
| CurrencyExchange | CurrencyExchangeForSecuritiesBalance | NaN | Specifies a securities balance which used a specific exchange rate. | SecuritiesBalance | ExchangeRate |
| CurrencyExchange | QuotationDate | NaN | Date and time at which an exchange rate is quoted. | ISODateTime | NaN |
| CurrencyExchange | CalculatedAssetValue | NaN | Asset value calculated in a different currency. | AssetHolding | ExchangeRate |
| CurrencyExchange | SourceCurrency | NaN | Currency of the amount to be converted in a currency conversion. | CurrencyCode | NaN |
| CurrencyExchange | TargetCurrency | NaN | Currency into which an amount is to be converted in a currency conversion. | CurrencyCode | NaN |
| CurrencyExchange | CurrencyExchangeForCashEntry | NaN | Cash entry to which the currency exchange parameters apply. | CashEntry | CurrencyExchange |
| CurrencyExchange | RelatedPayment | NaN | Payment for which currency exchange parameters are specified. | Payment | CurrencyExchange |
| CurrencyExchange | RateType | NaN | Specifies the type used to complete the currency exchange. | ExchangeRateTypeCode | NaN |
| CurrencyExchange | RelatedLimitManagement | NaN | Limit for which an exchange rate is specified. | LiquidityManagementLimit | CurrencyExchange |
| CurrencyExchange | FixingConditions | NaN | Set of parameters used to calculate a rate for instance, the fixing rate to be applied to a non-deliverable agreement. | FixingCondition | FixingRate |
| CurrencyExchange | Tax | NaN | Tax for which exchange information is provided. | Tax | CurrencyExchange |
| CurrencyExchange | RelatedInvoice | NaN | Invoice for which currency exchange information is specified. | Invoice | CurrencyExchange |
| CurrencyExchange | CurrencyExchangeForTransactionAdministrator | NaN | Set of applications which use currency exchange information. | TransactionAdministrator | CurrencyExchange |
| CurrencyExchange | ReportedAccount | NaN | Specifies the account which uses an exchange rate to report entries and balances. | Account | CurrencyExchange |
| CurrencyExchange | CurrencyExchangeForCorporateActionCashEntitlement | NaN | Cash entitlement for which an exchange rate is specified. | CorporateActionCashEntitlement | ExchangeRate |
| CurrencyExchange | PaymentExecution | NaN | Payment execution process for which currrency exchange information is provided. | PaymentExecution | CurrencyExchange |
| CurrencyExchange | CurrencyExchangeForSecuritiesQuote | NaN | Quote which uses currency exchange information. | Quote | QuotedRate |
| CurrencyExchange | CurrencyExchangeForSecuritiesConversion | NaN | Securities conversion for which a conversion currency is specified. | SecuritiesConversion | ConversionUnitCurrency |
| CurrencyExchange | CurrencyExchangeForCashDistribution | NaN | Cash distribution for which a conversion currency is specified. | CashDistribution | DistributionCurrencyExchangeInformation |
| CurrencyExchange | Adjustment | NaN | Fees or commission applied to the currency exchange. | Adjustment | CurrencyExchange |
| CurrencyExchange | RelatedPaymentTracker | NaN | Payment tracker to what the Informations of the currency exchange are related to. | PaymentTracker | ExchangeRateData |
| CurrencyExchange | ExchangeRateBase | NaN | <p>Expresses the ratio between the base of the denomination of the Unit Currency to the base of the denomination of the Quoted Currency.</p> | PositiveNumber | NaN |
| CorporateActionEventRegistration | NaN | NaN | Specifies the official date and identification of the event. | NaN | NaN |
| CorporateActionEventRegistration | CorporateActionEventIdentification | NaN | Identification given to the event. | Max35Text | NaN |
| CorporateActionEventRegistration | OfficialCorporateActionEventIdentification | NaN | Identification of a corporate action assigned by an official central body/entity within a given market. | Max35Text | NaN |
| CorporateActionEventRegistration | OfficialAnnouncementPublicationDate | NaN | Date/time at which the corporate action is legally announced by an official body, for example, publication by a governmental administration. | ISODateTime | NaN |
| CorporateActionEventRegistration | CorporateActionEvent | NaN | Corporate event for which a registration is specified. | CorporateActionEvent | CorporateActionEventRegistration |
| TradeOriginatorRole | NaN | TradePartyRole | Specifies the trading party at the source of the transaction. | NaN | NaN |
| TradeOriginatorRole | OriginatorRole | NaN | Specifies the role of the trading party in the transaction. | OriginatorRoleCode | NaN |
| TreasuryTrade | NaN | Trade | Specifies trades linked to treasury operations such as the exchange of currencies, the lending of cash amounts and the related derivatives trades (options and non deliverable trades). | NaN | NaN |
| TreasuryTrade | TreasuryTradeSettlementStatus | NaN | Specifies the settlement status of a treasury trade. | TreasuryTradeSettlementStatus | TreasuryTrade |
| TreasuryTrade | InformationPartyRole | NaN | Party which provides prices, interest rates or exchange rates. | InformationPartyRole | TreasuryTrade |
| TreasuryTrade | TreasurySettlementPartyRole | NaN | Role played by a party in the context of the settlement of a treasury trade. | TreasurySettlementPartyRole | TreasuryTrade |
| TreasuryTrade | PartyRole | NaN | Specifies each role played by a party in a treasury trade. | TreasuryTradePartyRole | TreasuryTrade |
| ForeignExchangeTrade | NaN | TreasuryTrade | Agreement between two parties in which one party buys a currency and the other party sells a different currency. | NaN | NaN |
| ForeignExchangeTrade | AgreedRate | NaN | Exchange rate between two currencies. The rate is agreed by the trading parties during the negotiation process. | CurrencyExchange | CurrencyExchangeForForeignExchangeTrade |
| ForeignExchangeTrade | TypeOfProduct | NaN | Specifies the type of trade. | Max35Text | NaN |
| ForeignExchangeTrade | BuyAmount | NaN | Currency and amount bought in a foreign exchange trade. | CurrencyAndAmount | NaN |
| ForeignExchangeTrade | SellAmount | NaN | Currency and amount sold in a foreign exchange trade. | CurrencyAndAmount | NaN |
| ForeignExchangeTrade | ResultingSettlement | NaN | Payment of the settlement amount to the account(s) of the final beneficiary. A payment may be settled gross, through split amounts at several agents of the buyer, or netted with several other treasury agreements. | PaymentObligation | ExchangeRateInformation |
| ForeignExchangeTrade | CurrencyExchangeForSecuritiesSettlement | NaN | Securities settlement process for which a currency exchange is provided. | SecuritiesSettlement | RelatedForeignExchangeOperation |
| ForeignExchangeTrade | OpeningLegRelatedNonDeliverableTrade | NaN | Non deliverable trade for which an opening closing leg is specified. | NonDeliverableTrade | OpeningLeg |
| ForeignExchangeTrade | ClosingLegRelatedNonDeliverableTrade | NaN | Non deliverable trade for which a closing leg is specified. | NonDeliverableTrade | ClosingLeg |
| ForeignExchangeTrade | RelatedSwap | NaN | FX swap for which the FX trade is one leg. | ForeignExchangeSwap | SwapLeg |
| ForeignExchangeTrade | RelatedOption | NaN | Option which is executed by one (or more) FX trade. | CurrencyOption | ExercisedOption |
| ForeignExchangeTrade | CurrencyExchangeForTaxVoucher | NaN | Tax voucher for which currency exchange information is specified. | TaxVoucher | ForeignExchangeTransaction |
| ForeignExchangeTrade | ExchangeForwardPoint | NaN | Difference between the foreign exchange spot rate and the foreign exchange forward rate expressed in basis points quoted in accordance with the prevailing market conventions for the currency pair. | DecimalNumber | NaN |
| InterestCalculation | NaN | NaN | Set of parameters used to calculate an interest amount. | NaN | NaN |
| InterestCalculation | DayCountBasis | NaN | Identifies the computation method of accrued interest of the related financial instrument. | InterestComputationMethodCode | NaN |
| InterestCalculation | Rate | NaN | Percentage charged for the use of an amount of money, usually expressed at an annual rate. The interest rate is the ratio of the amount of interest paid during a certain period of time compared to the principal amount of the interest bearing financial instrument. | PercentageRate | NaN |
| InterestCalculation | Interest | NaN | Interest resulting from the interest calculation. | Interest | InterestCalculation |
| InterestCalculation | RateType | NaN | Specifies the type of rate used to calculate the interest. | InterestRateTypeCode | NaN |
| InterestCalculation | InterestPeriod | NaN | Period during which the interest rate has been applied. | DateTimePeriod | RelatedInterestCalculation |
| InterestCalculation | RelatedIndex | NaN | Index rate related to the interest rate of the forthcoming interest payment. | PercentageRate | NaN |
| InterestCalculation | InterestAccrualDate | NaN | Start date used for calculating accrued interest on debt instruments which are being sold between interest payment dates. Often but not always the same as the issue date and the dated date. | ISODateTime | NaN |
| InterestCalculation | CalculationMethod | NaN | Specifies whether the interest is simple or compounded. | CalculationMethodCode | NaN |
| InterestCalculation | VariableInterest | NaN | Specifies the parameters to be used for variable interest payments. | VariableInterest | InterestCalculation |
| InterestCalculation | InterestType | NaN | Specifies the type of interest. | InterestCode | NaN |
| InterestCalculation | RateValidityRange | NaN | Specifies the amount range for which the interest rate is applicable. | AmountRange | RelatedInterest |
| InterestCalculation | InterestMethod | NaN | Indicates whether the interest will be settled in cash or rolled in the existing collateral balance. | InterestMethodCode | NaN |
| InterestCalculation | CalculationFrequency | NaN | Specifies the periodicity of the calculation of the interest. | FrequencyCode | NaN |
| InterestCalculation | CalculationDate | NaN | Indicates the calculation date of the interest amount. | ISODate | NaN |
| InterestCalculation | Charges | NaN | Specifies the charges on interest. | Charges | RelatedInterest |
| InterestCalculation | DebtInstrument | NaN | Debt for which a next interest is specified. | Debt | NextInterest |
| InterestCalculation | Spread | NaN | Specifies the difference between two interests. | Spread | RelatedInterest |
| InterestCalculation | PaymentFrequency | NaN | Specifies the frequency of an interest payment. | FrequencyCode | NaN |
| InterestCalculation | RelatedInterestManagement | NaN | Interest management process which requires interest calculation. | InterestManagement | InterestCalculation |
| Debt | NaN | Security | Financial instruments evidencing moneys owed by the issuer to the holder on terms as specified. | NaN | NaN |
| Debt | PaymentDirectionIndicator | NaN | Indicates the direction of payment for asset or mortgage backed securities, ie, whether the repaid capital is distributed (payment direction is down) or capitalized (payment direction is up). | PaymentDirectionIndicator | NaN |
| Debt | NextCallableDate | NaN | Next date/time at which the issuer has the right to pay the securitiy prior to maturity. | ISODateTime | NaN |
| Debt | PutableDate | NaN | Date at which the holder has the right to ask for redemption of the security prior to final maturity. | ISODateTime | NaN |
| Debt | DatedDate | NaN | First date/time at which a security begins to accrue interest. | ISODateTime | NaN |
| Debt | FirstPaymentDate | NaN | Date/time at which the first interest payment is due to holders of the security. | ISODateTime | NaN |
| Debt | Factor | NaN | Rate that defines the outstanding principal of the factored security. Factored securities are debt instruments that have a factor that is used in the calculation of net money and market value. Factors can be specified as current, next, previous or end factors. End factor: portion of principal that is still due at the end of the financing period. Previous factor: portion of principal that is still due before the current factor becomes applicable. Next factor: rate that will be applicable as of the next factor date. | PercentageRate | NaN |
| Debt | PoolNumber | NaN | Number identifying a group of underlying assets assigned by the issuer of a factored security. | Max15NumericText | NaN |
| Debt | VariableRateIndicator | NaN | Indicates whether the interest rate of an interest bearing instrument is reset periodically. | YesNoIndicator | NaN |
| Debt | CallableIndicator | NaN | Indicates whether the issuer has the right to pay the security prior to maturity. Also called RetractableIndicator. | YesNoIndicator | NaN |
| Debt | PutableIndicator | NaN | Indicates whether the holder has the right to ask for redemption of the security prior to final maturity. Also called RedeemableIndicator. | YesNoIndicator | NaN |
| Debt | YieldToMaturityRate | NaN | Rate of return anticipated on a bond when held until maturity date. | PercentageRate | NaN |
| Debt | AccruedCapitalisationAmount | NaN | Amount of unpaid interest (on bonds which have defaulted and have subsequently restructured), which is capitalized and added to the original principal amount of the bond. | CurrencyAndAmount | NaN |
| Debt | NextCouponDate | NaN | Next payment date of an interest bearing financial instrument. | ISODateTime | NaN |
| Debt | NextFactorDate | NaN | The date that the current factor will be changed to a new factor. | ISODateTime | NaN |
| Debt | OddCouponIndicator | NaN | Specifies whether the payment of the coupon (interest) on a bond is off the normal schedule. | YesNoIndicator | NaN |
| Debt | CPProgram | NaN | The program under which a commercial paper is issued. The values that are most used are:0 = N/A1 = 3(a)32 = 4(2)3 = 3(a)44 = 3(c)75 = 144A6 = 3(a)299 = Other | Number | NaN |
| Debt | CPRegistrationType | NaN | Registration type of a commercial paper issuance. | Max350Text | NaN |
| Debt | ConvertibleIndicator | NaN | Indicates whether the interest bearing security is convertible into another type of security. | YesNoIndicator | NaN |
| Debt | PreFundedIndicator | NaN | Indicates whether an interest bearing instrument is deposited in a fund that will be used to pay debt service on refunded securities. | YesNoIndicator | NaN |
| Debt | EscrowedIndicator | NaN | Indicates whether an interest bearing instrument is being escrowed or collateralized either by direct obligations guaranteed by the US government, or by other types of securities. The maturity schedules of the securities in the escrow fund are determined in such a way to pay the maturity value, coupon, and premium payments (if any) of the refunded bonds. | YesNoIndicator | NaN |
| Debt | PerpetualIndicator | NaN | Indicates whether the security has no maturity date. | YesNoIndicator | NaN |
| Debt | SubordinatedIndicator | NaN | Indicates whether the security is a subordinated security. | YesNoIndicator | NaN |
| Debt | ExtendibleIndicator | NaN | Indicates whether the security is extendible,eg, repayment may be extended or maturity changed. | YesNoIndicator | NaN |
| Debt | ExtendiblePeriod | NaN | Period during which a date might be extended. | DateTimePeriod | ExtendiblePeriodDebt |
| Debt | OverAllotmentAmount | NaN | Amount for which a security can be overalloted (as in greenshoe option). | CurrencyAndAmount | NaN |
| Debt | OverAllotmentRate | NaN | Percentage for which a security can be overalloted (as in greenshoe option). | PercentageRate | NaN |
| Debt | AmortisableIndicator | NaN | Indicates whether repayment is made via regular principal and interest payments over time. | YesNoIndicator | NaN |
| Debt | CapitalisedInterest | NaN | Specifies whether the interest amount is capitalised until maturity date or paid out at each interest payment date. | DistributionPolicyCode | NaN |
| Debt | ActualDenominationAmount | NaN | Nominal value per security unit. | CurrencyAndAmount | NaN |
| Debt | Pieces | NaN | Number of pieces composing a pool of financial assets. | DecimalNumber | NaN |
| Debt | PoolsMaximum | NaN | Collection of assets by which a security is backed. | DecimalNumber | NaN |
| Debt | PoolsPerMillion | NaN | Indicates per million the collection of loans, mortgages or other assets assembled by an originator as the basis for a security. | DecimalNumber | NaN |
| Debt | PoolsPerLot | NaN | Indicates per lot the collection of loans, mortgages or other assets assembled by an originator as the basis for a security. | DecimalNumber | NaN |
| Debt | PoolsPerTrade | NaN | Indicates per trade the collection of loans, mortgages or other assets assembled by an originator as the basis for a security. | DecimalNumber | NaN |
| Debt | ConstantPrePaymentPenalty | NaN | Indicates whether a penalty might be imposed to the borrower of a mortgage in case of prepayments occurring during the lockout period. | YesNoIndicator | NaN |
| Debt | PrePaymentSpeed | NaN | Speed of unscheduled partial or complete payment of the principal amount outstanding on a debt obligation before its due date. | PrePaymentSpeedCode | NaN |
| Debt | ConstantPrePaymentYield | NaN | Measure of prepayment as a yield of the current outstanding loan balance. | PercentageRate | NaN |
| Debt | WeightedAverageCoupon | NaN | Contains the weighted average coupon of the fixed income instrument (expressed as a percentage). | PercentageRate | NaN |
| Debt | WeightedAverageLife | NaN | Contains the weighted average life of the fixed income instrument (expressed in months). | DecimalNumber | NaN |
| Debt | WeightedAverageLoan | NaN | Contains the weighted average loan of the fixed income instrument (expressed in months). | DecimalNumber | NaN |
| Debt | WeightedAverageMaturity | NaN | Contains the weighted average maturity of the fixed income instrument (expressed in months). | DecimalNumber | NaN |
| Debt | InsuredIndicator | NaN | Indicates whether the instruments is backed by any kind of asset or not. | YesNoIndicator | NaN |
| Debt | BankQualified | NaN | Indicates whether the security is bank qualified (usually applies to loan products). | YesNoIndicator | NaN |
| Debt | AutoReinvestment | NaN | Indicates an instruction to reinvest dividends in the underlying security (or proceeds at maturity in a similar instrument) if the current rate equals the rate specified or better. | PercentageRate | NaN |
| Debt | CustomDate | NaN | Indicates an instruction to override an investment's default start and/or end date with a custom date. | DateTimePeriod | CustomDateDebt |
| Debt | LookBack | NaN | Indicates an instruction or attribute giving the number of days to be included in the look-back period for the investment. Some options allow exercise based on the underlying asset's optimal value over the look-back period. | Number | NaN |
| Debt | MinimumDenomination | NaN | Indicates the minimum denomination of a security. | SecuritiesQuantity | MinimumDenominationDebt |
| Debt | MaximumSubstitution | NaN | Maximum number of time the collateral can be substitute. | Number | NaN |
| Debt | MinimumIncrement | NaN | Indicates the minimum tradable increments of a security. | SecuritiesQuantity | MinimumIncrementDebt |
| Debt | Production | NaN | Indicates a search criterion used when looking to buy a bond, particularly an mortgage back security (MBS), issued in a particular year. | Max350Text | NaN |
| Debt | Restricted | NaN | Identifies if the securities is restricted or not (as per Rule 144). | YesNoIndicator | NaN |
| Debt | PriceFrequency | NaN | Indicates the frequency at which the bond is re-rated and therefore re-priced (bond attribute, particularly of floating rate and index linked instruments). | FrequencyCode | NaN |
| Debt | SubstitutionFrequency | NaN | Indicates the maximum number of times collateral can be substituted. | FrequencyCode | NaN |
| Debt | SubstitutionLeft | NaN | Number of remaining times the collateral can be substitute. | Number | NaN |
| Debt | WholePool | NaN | Indicates a search criterion when looking to buy an mortgage back security (MBS) that either is [yes] or is not [no] an entire pool. | YesNoIndicator | NaN |
| Debt | AlternativeMinimumTax | NaN | Identifies whether the issue is subject to alternative minimum taxation (used for municipal bonds). | YesNoIndicator | NaN |
| Debt | NextInterest | NaN | Specifies the interest applicable to the next interest payment period. | InterestCalculation | DebtInstrument |
| Debt | ExtendibleDate | NaN | Date/time to which a date might be extended. | ISODateTime | NaN |
| Debt | SinkableIndicator | NaN | Indicates whether the security is a sinkung fund. A sinking fund is a bond in which part of the total principal amount is repaid according to agreed schedules of dates, amounts and prices. | YesNoIndicator | NaN |
| Debt | Insured | NaN | Identifies whether the lender is assured partial or full payment by a third party if the borrower defaults. | YesNoIndicator | NaN |
| Debt | Geographics | NaN | Type of stipulation expressing geographical constraints on a fixed income instrument. It is expressed with a state or country abbreviation and a minimum or maximum percentage. Example: CA 0-80 (minimum of 80 percent in Californian assets). | Max35Text | NaN |
| Debt | PaymentCurrency | NaN | Currency of the payment. | CurrencyCode | NaN |
| Debt | DirtyPrice | NaN | Price that includes interest that has accrued since issue of the most recent coupon payment. | NaN | NaN |
| Debt | DebtSeniority | NaN | Seniority of a specific debt instrument, that is the order of repayment in the event of a sale or bankruptcy of the issuer of the debt. | DebtInstrumentSeniorityTypeCode | NaN |
| SecuritiesStatus | NaN | Status | Specifies the status of the security within its lifecycle. | NaN | NaN |
| SecuritiesStatus | PaymentStatus | NaN | Status of payment of a security at a particular time. | SecuritiesPaymentStatusCode | NaN |
| SecuritiesStatus | Status | NaN | Specifies the status of the security within its lifecycle. | SecurityStatusCode | NaN |
| SecuritiesStatus | RegistrationStatus | NaN | Specifies the status of the registration of the securities. | RegistrationProcessingStatusCode | NaN |
| SecuritiesStatus | Security | NaN | Security for which a status is provided. | Security | SecurityStatus |
| VariableInterest | NaN | NaN | Specifies the estimated interest rate and the parameters used for determining its value. | NaN | NaN |
| VariableInterest | VariableRateChangeFrequency | NaN | Specifies the frequency of change to the variable rate of an interest bearing instrument. | FrequencyCode | NaN |
| VariableInterest | FixingDate | NaN | Date/time at which the rate determination is made, also called determination date, for instance the date the interest rate of a floating rate note will be/was calculated, according to the terms of the issue. | ISODateTime | NaN |
| VariableInterest | InterestCalculation | NaN | Interest calculation for which a variable interest is used. | InterestCalculation | VariableInterest |
| VariableInterest | ReportingDate | NaN | Last date the new interest rate must be reported to the market. | ISODateTime | NaN |
| VariableInterest | ResetDate | NaN | Date/time at which the interest rate of an interest bearing instrument will be reset, according to the terms of the issue. | ISODateTime | NaN |
| VariableInterest | Arrears | NaN | Indicates that the rate reset will occur at the end of the payment period (True case) | Max16Text | NaN |
| VariableInterest | Index | NaN | Identifies the index used for calculating the interest | Index | VariableInterest |
| VariableInterest | YieldCalculation | NaN | Yield calculation for which a variable interest is used. | YieldCalculation | VariableInterest |
| VariableInterest | BenchmarkReference | NaN | Benchmark rate against which variable rate instruments are measured to determine the interest rate, for example, LIBOR. | Security | RelatedVariableInterest |
| VariableInterest | EstimatedInterestRate | NaN | Estimated per annum ratio of interest paid to the principal amount of the financial instrument for a specific period of time. | PercentageRate | NaN |
| VariableInterest | VariableRateValueDate | NaN | Date/time as of which the variable rate is valid. | ISODateTime | NaN |
| VariableInterest | LifeCalculation | NaN | Lfe calculation for which a variable interest is used. | LifeCalculation | VariableInterest |
| VariableInterest | DurationCalculation | NaN | Duration calculation for which a variable interest is used. | DurationCalculation | VariableInterest |
| Equity | NaN | Security | Financial instrument that represents a title of ownership in a company. That is, the shareholder is entitled to a part of the company's profit - usually by payment of a dividend - and to voting rights, if any. Each company issues generally different classes of shares, for example, ordinary or common shares, which have no guaranteed amount of dividend but carry voting rights, or preferred shares, which receive dividends before ordinary shares but have no voting right. | NaN | NaN |
| Equity | PreferenceToIncome | NaN | Indicates the level of priority to claim on income and assets of the company in case of the payment of dividends and in the event of a bankruptcy, for example, ordinary/common stocks, preferred stocks, subordinated debt, etc. | PreferenceToIncomeCode | NaN |
| Equity | ConvertibleIndicator | NaN | Indicates whether the investor or the issuer has a conversion option. | YesNoIndicator | NaN |
| Equity | NonPaidAmount | NaN | Nominal amount which is not paid yet. | CurrencyAndAmount | NaN |
| Equity | ParValue | NaN | Nominal value of an equity security. | CurrencyAndAmount | NaN |
| Equity | VotingRightsPerShare | NaN | Number of voting rights per share. | Number | NaN |
| AssetClassification | NaN | NaN | Other classification type of the security, ie, other than ISO 10962. | NaN | NaN |
| AssetClassification | ClassificationType | NaN | Classification type of the financial instrument, as per the ISO Classification of Financial Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered. | CFIOct2015Identifier | NaN |
| AssetClassification | Asset | NaN | Asset for which classification information is provided. | Asset | AssetClassification |
| AssetClassification | Language | NaN | Language in which the asset classification is expressed. | LanguageCode | NaN |
| AssetClassification | AssetClassScheme | NaN | Information regarding the entity that assigns the asset classification. | Scheme | AssetClassification |
| AssetClassification | ProductType | NaN | Identifies the product type. | ProductTypeCode | NaN |
| AssetClassification | Strategy | NaN | Strategy related to a class of assets. | AssetClassStrategy | AssetClass |
| AssetClassification | ClassificationSubType | NaN | Provides information about the sub-class according to one of the segmentation criteria. | NonEquitySubClassSegmentationCriteriaCode | NaN |
| Derivative | NaN | Asset | Specifies the parameters of a derivative instrument based on a specific asset. | NaN | NaN |
| Derivative | UnderlyingAsset | NaN | Specifies the underlying asset of the derivative. | Asset | Derivative |
| Derivative | NotionalCurrencyAndAmount | NaN | Amount underlying a financial derivatives contract necessary for calculating payments or receipts. | CurrencyAndAmount | NaN |
| Derivative | DerivativeCovered | NaN | Indicates whether the derivative product is covered or not by an underlying financial instrument position. | YesNoIndicator | NaN |
| Derivative | ExerciseDate | NaN | Date on which the derivative is exercised. | ISODateTime | NaN |
| Derivative | InterestIncludedInPrice | NaN | Indicates whether the given derivative price includes a prorated accrued interest component. | YesNoIndicator | NaN |
| Derivative | Tick | NaN | Minimum price increment with which the contract may be traded. | SecuritiesPricing | RelatedFuture |
| Derivative | ExercisePrice | NaN | Predetermined price at which the holder of a derivative will have to buy or sell the underlying instrument. | SecuritiesPricing | Derivative |
| Derivative | NotionalCurrency | NaN | Currency of the underlying a financial derivatives contract necessary for calculating payments or receipts. | CurrencyCode | NaN |
| Derivative | VersionNumber | NaN | Number allocated by options exchanges to record that an option has undergone a change in its contract specifications (particularly adjustment of the strike price) | Number | NaN |
| Derivative | Event | NaN | Describes the state transition of the derivative. | DerivativeEvent | RelatedDerivative |
| Option | NaN | Derivative | Contracts which grant to the holder either the privilege to purchase or the privilege to sell the assets specified at a predetermined price or formula at or within a time in the future. | NaN | NaN |
| Option | InstrumentAssignmentMethod | NaN | Method under which assignment was conducted. | AssignmentMethodCode | NaN |
| Option | SettleStyle | NaN | Specifies whether the option contract settles at the open or close of the market. | SettleStyleCode | NaN |
| Option | Standardisation | NaN | Specifies whether the terms of the security (underlying instruments, expiration date, contract size) are defined according to the exchange specifications or whether they can be user defined. | StandardisationCode | NaN |
| Option | PositionLimit | NaN | Indicates the maximum number of listed option contracts on a single security which can be held by an investor or group of investors acting jointly. | Number | NaN |
| Option | UnderlyingType | NaN | Specifies the type of underlying to which the option relates. | UnderlyingTypeCode | NaN |
| Option | CoverIndicator | NaN | Indicates whether the underlying financial instrument of an option is owned by the writer of the option. | YesNoIndicator | NaN |
| Option | OptionConversionInformation | NaN | Information on the conversion exchange of an option into another form of securities. | SecuritiesConversion | RelatedOption |
| Option | OptionRatio | NaN | Expresses the risk of an option leg. Value must be between -1 and 1. A Call Option will require a ratio value between 0 and 1. A Put Option will require a ratio value between -1 and 0. | PercentageRate | NaN |
| Option | SecuritiesOptionTrade | NaN | Specifies the trade elements for the option. | SecuritiesOptionTrade | Option |
| Option | SettlementType | NaN | Indicates whether the trade is to be settled as principal or netted off against another trade. | SettlementTypeCode | NaN |
| Option | StrikeMultiplier | NaN | Multiplier applied to the strike price for the purpose of calculating the settlement value (Used for derivatives). | Number | NaN |
| Option | ExpiryLocation | NaN | Financial center where option expires. | Max4AlphaNumericText | NaN |
| Option | FinalSettlementDate | NaN | Date on which the trade is settled. i.e., the amounts are due. | ISODate | NaN |
| Option | OptionStyle | NaN | Specifies how an option can be exercised (American, European, Bermudan) | OptionStyleCode | NaN |
| Option | CurrencyOption | NaN | Information specific to a currency option. | CurrencyOption | OptionDefinition |
| Option | EarliestExerciseDate | NaN | First date on which an american option can be exercised. | ISODateTime | NaN |
| Option | SettlementDays | NaN | Number of business days between the hit date and the payment date in case of settlement at hit. | Number | NaN |
| Option | StrikePrice | NaN | Predetermined price at which the holder will have to buy or sell the underlying instrument. | Price | Option |
| Option | OptionStartDate | NaN | First date on which an option becomes effective. | ISODateTime | NaN |
| Option | ExpiryDateAndTime | NaN | For European options, date on which the option holder can only exercise the right or let it lapse. For American options, the option holder can exercise the right up to the expiry date. | ISODateTime | NaN |
| Option | OptionType | NaN | Specifies whether it is a Call option (right to purchase a specific underlying asset) or a Put option (right to sell a specific underlying asset). | OptionDefinitionTypeCode | NaN |
| Option | StrikeValue | NaN | Number of shares/units for the financial instrument involved in the option trade (Used for derivatives). | Number | NaN |
| Option | SettlementPeriodType | NaN | Specifies how settlement will take place for instance at expiration or at hit. | Max35Text | NaN |
| CouponAttached | NaN | NaN | Physical certificates representing rights attached to the physical certificates representing a security. | NaN | NaN |
| CouponAttached | Date | NaN | Date of the coupon attached to the physical security. | ISODate | NaN |
| CouponAttached | Number | NaN | Number of the coupon attached to the physical security. | Max3NumericText | NaN |
| CouponAttached | Security | NaN | Instrument to which a coupon is specified. | Security | CouponAttached |
| CouponAttached | CouponClippingDate | NaN | Date on which the coupons are to be/were submitted for payment of interest. | ISODateTime | NaN |
| CouponAttached | Identification | NaN | Identification of the coupon. | Max35Text | NaN |
| Issuance | NaN | NaN | Preparation/bringing to market of a security (also known as primary market or Initial Public Offering (IPO) issuance). | NaN | NaN |
| Issuance | IssueDate | NaN | Date/time at which the security was made available. | ISODateTime | NaN |
| Issuance | IssueDiscountAllowance | NaN | Discount on a new issue or tranche of an existing issue. | CurrencyAndAmount | NaN |
| Issuance | InterestShortfall | NaN | For structured security issues where there is a set schedule of principal and interest payments for the life of the issue, this is the difference between the actual rate of the interest payment and the expected or scheduled rate of the interest payment . | RateAndAmount | InterestRelatedIssuance |
| Issuance | RealisedLoss | NaN | For structured security issues where there is a set schedule of principal and interest payments for the life of the issue, this is the difference between the actual rate of the capital or principal repayment and the scheduled capital repayment. | RateAndAmount | LossRelatedIssuance |
| Issuance | Purpose | NaN | Reason for which money is raised through the issuance of a security. | Max256Text | NaN |
| Issuance | IssueSize | NaN | Identifies the issue size range. | Number | NaN |
| Issuance | IssueNominalAmount | NaN | Total original amount or quantity published. | SecuritiesQuantity | Issuance |
| Issuance | EventInformation | NaN | Parameters of the event. | CorporateActionEvent | Issuance |
| Issuance | IssuedAsset | NaN | Asset which is issued. | Asset | Issuance |
| Issuance | OriginalIssueDiscount | NaN | Discount from par value at the time the security is issued. | SecuritiesPricing | Issuance |
| Issuance | IssuePlace | NaN | Primary market or country where an asset is issued by the issuer or its agent. | TradingMarket | Issuance |
| Issuance | GlobalNoteType | NaN | Identifies if the security will be issued in New Global Note (NGN) or Classical Global Note (CGN). New Global Note (NGN): Form of global certificate which refers to the books and records of the ICSDs to determine the issue outstanding amount (IOA). Classical Global Note (CGN): Form of global certificate which requires physical annotation on the attached schedule to reflect changes in the issue outstanding amount (IOA). | GlobalNoteCode | NaN |
| Issuance | CapitalRaised | NaN | Capital raised through the issuance of an asset. | Capital | AssetIssuance |
| Issuance | SubscriptionPeriod | NaN | Period during which the security can be subscribed to. | DateTimePeriod | Issuance |
| Issuance | Minimum | NaN | Minimum or incremental denomination required for the transfer or change of ownership of a security. | SecuritiesQuantity | RelatedIssuance |
| Issuance | IssuePrice | NaN | Initial issue price of a financial instrument. | CurrencyAndAmount | NaN |
| Index | NaN | NaN | Identifies the index. | NaN | NaN |
| Index | IndexRateBasis | NaN | Specifies the reference rate. | PercentageRate | NaN |
| Index | IndexFactor | NaN | Index rate applied to the amount paid to adjust it for instance to inflation. | RateAndAmount | Index |
| Index | IndexPoints | NaN | Number of points above the index used to calculate a price. | DecimalNumber | NaN |
| Index | IndexFixingDate | NaN | Date/time at which an index rate will be determined . | ISODateTime | NaN |
| Index | Identification | NaN | Identifies the index by a name for instance LIBOR. | Max35Text | NaN |
| Index | ReferenceSource | NaN | Identifies the reference source. The source can be the fixing agent or a system. | Max35Text | NaN |
| Index | IndexRateCurrency | NaN | Specifies the currency of the reference rate for fixed income instruments where the price of the instrument is indexed to the price of an underlying benchmark. | CurrencyCode | NaN |
| Index | IndexRateFrequency | NaN | Frequency at which the index changes. | FrequencyCode | NaN |
| Index | IndexRateMultiplier | NaN | Multiplier for the variable rate. | DecimalNumber | NaN |
| Index | Spread | NaN | Percentage to be added to or deducted from the index rate to calculate the effective rate. | Spread | Index |
| Index | PortfolioBenchmark | NaN | Portfolio benchmark which uses an index for decomposition, | PortfolioBenchmark | Index |
| Index | VariableInterest | NaN | Variable interest which uises the index. | VariableInterest | Index |
| Index | SecuritiesPricing | NaN | Pricing which uses an index. | SecuritiesPricing | Index |
| Future | NaN | Derivative | Parameters for contracts which obligate the buyer to receive and the seller to deliver in the future the assets specified at an agreed price. | NaN | NaN |
| Future | FutureDate | NaN | Date on which future contracts settle. | ISODateTime | NaN |
| Future | MinimumSize | NaN | Specifies the minimum ratio or multiply factor used to convert from contracts to shares. | CurrencyAndAmount | NaN |
| Future | UnitOfMeasure | NaN | Used to indicate the size of the underlying commodity on which the contract is based (e.g., 2500 lbs of lean cattle, 1000 barrels of crude oil, 1000 bushels of corn, etc.) | UnitOfMeasureCode | NaN |
| Future | LastDeliveryDate | NaN | Last date/time by which the option for physical delivery may still be exercised. | ISODateTime | NaN |
| Future | Standardisation | NaN | Specifies whether the terms of the security (underlying instruments, expiration date, contract size) are defined according to the exchange specifications or whether they can be user defined. | StandardisationCode | NaN |
| Future | UnderlyingType | NaN | Specifies the type of underlying to which the option relates. | UnderlyingTypeCode | NaN |
| Future | FutureRule | NaN | Rule attached to a future on debt. | FutureRule | RelatedFutureInstrument |
| Warrant | NaN | Security | Financial instrument that gives the holder the right to purchase shares or bonds at a given price within a specified time. | NaN | NaN |
| Warrant | SubscriptionPrice | NaN | Pre-determined price at which the holder of a warrant is entitled to buy the underlying instrument. | SecuritiesPricing | RelatedWarrant |
| Warrant | Multiplier | NaN | Specifies the ratio or multiply factor used to convert from contracts to shares. | BaseOneRate | NaN |
| Warrant | Style | NaN | Specifies the expiration style of the warrant. | WarrantStyleCode | NaN |
| Warrant | WarrantParity | NaN | Provides the ratio between the quantity of warrants and the quantity of underlying securities. | QuantityRatio | Warrant |
| SecuritiesConversion | NaN | NaN | Conversion exchange of securities, generally convertible bonds or preferred equities, into another form of securities, usually common equities. | NaN | NaN |
| SecuritiesConversion | ConversionPrice | NaN | Price of one target security in the conversion. | SecuritiesPricing | RelatedSecuritiesConversion |
| SecuritiesConversion | ConversionDate | NaN | Deadline by which a convertible security must be converted according to the terms of the issue. | ISODateTime | NaN |
| SecuritiesConversion | MinimumExercisableQuantity | NaN | Minimum quantity of financial instrument or lot of rights/warrants that must be exercised. | SecuritiesQuantity | MinimumExercisableQuantitySecuritiesConversion |
| SecuritiesConversion | MinimumExercisableMultipleQuantity | NaN | Minimum multiple quantity of financial instrument or lot of rights/warrants that must be exercised. | SecuritiesQuantity | MinimumExercisableMultipleQuantitySecuritiesConversion |
| SecuritiesConversion | MaximumExercisableQuantity | NaN | Indicates the maximum quantity of financial instrument that may be exercised in the event. | SecuritiesQuantity | MaximumExercisableQuantitySecuritiesConversion |
| SecuritiesConversion | ConversionType | NaN | Specifies the conversion type of an instrument. | ConversionTypeCode | NaN |
| SecuritiesConversion | ConversionPeriod | NaN | Period during which a convertible security may be converted according to the terms of the issue. | DateTimePeriod | SecuritiesConversion |
| SecuritiesConversion | ConversionRatioDenominator | NaN | Number of held securities for the conversion. | SecuritiesQuantity | RatioDenominatorSecuritiesConversion |
| SecuritiesConversion | ConversionRatioNumerator | NaN | Number of target securities for the conversion. | SecuritiesQuantity | RatioNumeratorSecuritiesConversion |
| SecuritiesConversion | Ratio | NaN | Ratio applied to convert the related security. | UnderlyingRatio | SecuritiesConversion |
| SecuritiesConversion | ConversionUnitCurrency | NaN | Currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP = xxxCUR, the unit currency is GBP. | CurrencyExchange | CurrencyExchangeForSecuritiesConversion |
| SecuritiesConversion | RelatedOption | NaN | Option for which securities conversion information is provided. | Option | OptionConversionInformation |
| SecuritiesConversion | BusinessDayConvention | NaN | Convention used for adjusting a date when it is not a business day. | BusinessDayConventionCode | NaN |
| SecuritiesConversion | ConversionChoice | NaN | Specifies whether the conversion is mandatory or optional. | ChoiceCode | NaN |
| SecuritiesConversion | ConversionFixedExchangeRate | NaN | Currency exchange rate between the bond currency and the underlying equity currency used to calculate the convertion ratio. | BaseOneRate | NaN |
| SecuritiesConversion | ConversionMarginAmount | NaN | Amount of cash needed for the conversion. | CurrencyAndAmount | NaN |
| SecuritiesConversion | ConversionOption | NaN | Specifies information about the choices offered to the holder of a conversion. | CorporateActionOptionCode | NaN |
| SecuritiesConversion | ConversionQuotedCurrency | NaN | Currency into which the base currency is converted, in a currency exchange. | CurrencyCode | NaN |
| SecuritiesConversion | FinancialCenter | NaN | Financial place taken into account to adjust the date and time, as defined within the business day convention. | FinancialCenterCode | NaN |
| SecuritiesConversion | MinimumNoticeDays | NaN | Minimum number of days that must be given by either the issuer or the holder before conversion can take place. | Number | NaN |
| SecuritiesConversion | NoticePeriodType | NaN | Specifies the type of notice period. | NoticePeriodTypeCode | NaN |
| SecuritiesConversion | ProtectionAgainstDilutionIndicator | NaN | Indicates whether the security is protected against dilution with regards to capital events. | YesNoIndicator | NaN |
| SecuritiesConversion | ReverseConversionIndicator | NaN | Indicates whether the bond is convertible into an equity and back to the bond. | YesNoIndicator | NaN |
| SecuritiesConversion | SecurityIdentification | NaN | ISIN identification of the related financial instrument into which this security can be converted. | Security | Conversion |
| SecuritiesConversion | PartyType | NaN | Specifies if the issuer or the holder are allowed to convert the security into another one. | PartyTypeCode | NaN |
| SecuritiesConversion | ContractSize | NaN | Ratio or multiplying factor used to convert one contract into a quantity. | BaseOneRate | NaN |
| CashSettlementInstructionPartyRole | NaN | SettlementPartyRole | Role played by a party in cash settlement. | NaN | NaN |
| CashSettlementInstructionPartyRole | CashAccount | NaN | Unambiguous identification of the account used in the context of the party role such as instructing reimbursement agent account... | CashAccount | CashSettlementPartyRole |
| CashSettlementInstructionPartyRole | SettlementInstruction | NaN | Identifies the settlement instruction in which a party plays a role. | CashSettlement | PartyRole |
| SettlementInstructionSystemRole | NaN | CashSettlementInstructionPartyRole | Identification of a specific system or set of rules and/or processes to be applied at the settlement place. | NaN | NaN |
| SettlementInstructionSystemRole | System | NaN | Specifies the system which plays a role in the settlement of a payment. | CashClearingSystem | SystemRole |
| ExposureTerm | NaN | NaN | Specifies the terms used to calculate a risk exposure and its coverage. | NaN | NaN |
| ExposureTerm | ExposureType | NaN | Specifies the underlying business area/type of trade causing the collateral movement. | ExposureTypeV2Code | NaN |
| ExposureTerm | MinimumTransferAmount | NaN | Minimum amount to pay/receive as specified in the agreement in the base currency (to avoid the need to transfer an inconveniently small amount of variation margin). | ActiveCurrencyAndAmount | NaN |
| ExposureTerm | RoundingAmount | NaN | Amount specified to avoid the need to transfer uneven amounts of collateral. | ActiveCurrencyAndAmount | NaN |
| ExposureTerm | RoundingMethod | NaN | Defines how the rounding amount is applied in the calculation to avoid the need to transfer uneven amounts of collateral. For example, should the amount of collateral required be rounded up, down, to the closer integral multiple specified or not rounded. | RoundingMethodCode | NaN |
| ExposureTerm | RelatedCollateralAgreement | NaN | Agreement in which the exposure terms are specified. | CollateralAgreement | ExposureTerm |
| ExposureTerm | MinimumRequirementDeposit | NaN | Minimum requirement for a participant if their requirement falls below a specific amount set by the central counterparty. | ActiveCurrencyAndAmount | NaN |
| StandingSettlementInstruction | NaN | NaN | Settlement instruction database information. | NaN | NaN |
| StandingSettlementInstruction | Settlement | NaN | Settlement process to which the settlement instruction database applies. | Settlement | StandingSettlementInstruction |
| StandingSettlementInstruction | FXStandingInstruction | NaN | Specifies whether the forex standing instruction in place should apply. | YesNoIndicator | NaN |
| StandingSettlementInstruction | SettlementStandingInstructionDatabase | NaN | Specifies what settlement standing instruction database is to be used to derive the settlement parties involved in the transaction. | SettlementStandingInstructionDatabaseCode | NaN |
| StandingSettlementInstruction | Identification | NaN | Identification of the standing instruction. | Max35Text | NaN |
| StandingSettlementInstruction | RelatedCollateralAgreement | NaN | Collateral agreement for which standing settlement instructions are specified. | CollateralAgreement | StandingSettlementInstructions |
| StandingSettlementInstruction | SSIDatabaseName | NaN | Specifies the settlement standing instruction database to be used to derive the settlement parties involved in a transaction. | Max350Text | NaN |
| StandingSettlementInstruction | SSIDatabaseProvider | NaN | Party which provides information on the parties and accounts to be used to settle a transaction. | SSIDatabaseProvider | StandingSettlementDatabase |
| StandingSettlementInstruction | ValidityPeriod | NaN | Period during which the SSI is valid. | DateTimePeriod | RelatedStandingSettlementInstruction |
| StandingSettlementInstruction | Currency | NaN | Currency of the payment to which the SSI applies. | CurrencyCode | NaN |
| StandingSettlementInstruction | Asset | NaN | Inidicates the asset for the standing settlement instruction. | Asset | StandingSettlementInstruction |
| BasicSecuritiesRegistration | NaN | NaN | Information related to registration of securities. | NaN | NaN |
| BasicSecuritiesRegistration | Security | NaN | Security for which registration information is provided. | Security | Registration |
| BasicSecuritiesRegistration | RegistrationInstruction | NaN | Specifies whether registration should occur upon receipt. | RegistrationCode | NaN |
| BasicSecuritiesRegistration | CertificationIdentification | NaN | Identification assigned to a deposit. | Max35Text | NaN |
| BasicSecuritiesRegistration | CertificationDate | NaN | Date/time at which the certificates in the deposit were validated by the agent. | ISODateTime | NaN |
| BasicSecuritiesRegistration | SecuritiesCertificate | NaN | Unique and unambiguous identification of a certificate assigned by the issuer. | SecuritiesCertificate | BasicRegistration |
| BasicSecuritiesRegistration | SplitPeriod | NaN | Period during which a physical certificate can be split. | DateTimePeriod | RelatedSecuritiesRegistration |
| SecuritiesRestriction | NaN | NaN | Restrictions applicable to the security. | NaN | NaN |
| SecuritiesRestriction | Security | NaN | Security for which restriction information is provided. | Security | Restriction |
| SecuritiesRestriction | LegalRestrictionType | NaN | Specifies the regulatory restrictions applicable to a security. | LegalRestrictionsCode | NaN |
| SecuritiesRestriction | Jurisdiction | NaN | Jurisdiction (country, county, state, province, city) where the restriction applies. | Jurisdiction | SecuritiesRestriction |
| SecuritiesRestriction | RestrictionType | NaN | Type of the restriction, for example, selling restriction, buying restriction, placing restriction. | RestrictionTypeCode | NaN |
| SecuritiesRestriction | InvestorStatusRestrictionType | NaN | Specifies whether the restriction to be applied is relevant for citizen, resident, country. | InvestorRestrictionTypeCode | NaN |
| SecuritiesRestriction | EffectivePeriod | NaN | Period during which the restriction applies. | NaN | NaN |
| SecuritiesRestriction | Rate | NaN | Rate used for the calculation of the restriction. | PercentageRate | NaN |
| SecuritiesRestriction | InvestorType | NaN | Type of investor that is allowed to hold the security. | InvestorTypeCode | NaN |
| SecuritiesFinancing | NaN | SecuritiesTrade | Process of lending or borrowing cash or securities against securities or cash collateral. It aims at optimising liquidity, support a trading strategy, or increase settlement efficiency. | NaN | NaN |
| SecuritiesFinancing | ReturnLegInstruction | NaN | Specifies whether, for a securities lending/borrowing settlement transaction, the lender will instruct the return leg as agreed with the borrower. | YesNoIndicator | NaN |
| SecuritiesFinancing | Type | NaN | Specifies the type of securities financing transaction, that is, repurchase agreement, reverse repurchase agreement, securities lending or securities borrowing. | SecuritiesTransactionTypeV2Code | NaN |
| SecuritiesFinancing | TerminationDateTime | NaN | Closing date/time or maturity date/time of the repo transaction. | ISODateTime | NaN |
| SecuritiesFinancing | RateChangeDateTime | NaN | Date/Time at which rate change has taken place. | ISODateTime | NaN |
| SecuritiesFinancing | RevaluationIndicator | NaN | Specifies whether the collateral position should be subject to automatic revaluation by the account servicer. | YesNoIndicator | NaN |
| SecuritiesFinancing | InterestPayment | NaN | Specifies whether the interest is to be paid to the collateral taker. If set to no, the interest is paid to the collateral giver. | YesNoIndicator | NaN |
| SecuritiesFinancing | VariableRateSupport | NaN | Index or support rate used together with the spread to calculate the repurchase rate. | Max35Text | NaN |
| SecuritiesFinancing | RepurchaseRate | NaN | Rate to be used to recalculate the repurchase amount. | PercentageRate | NaN |
| SecuritiesFinancing | StockLoanMargin | NaN | Percentage mark-up on a loan consideration used to reflect the lender's risk. | PercentageRate | NaN |
| SecuritiesFinancing | Interest | NaN | Interest to be paid on the transaction amount. | Interest | SecuritiesFinancing |
| SecuritiesFinancing | RepurchaseSpread | NaN | Repurchase spread expressed as a rate; margin over or under an index that determines the repurchase rate. | Spread | SecuritiesFinancing |
| SecuritiesFinancing | TransactionCallDelay | NaN | Minimum number of days' notice a counterparty needs for terminating the transaction. | Max3NumericText | NaN |
| SecuritiesFinancing | TotalNumberOfCollateralInstructions | NaN | Indicates the total Number of collateral instructions involved in the transaction. | Max3NumericText | NaN |
| SecuritiesFinancing | DealAmount | NaN | Deal amount of the second leg. | CurrencyAndAmount | NaN |
| SecuritiesFinancing | ForfeitRepurchaseAmount | NaN | Fixed amount which has to be paid (instead of interest) in the case of a recall. | CurrencyAndAmount | NaN |
| SecuritiesFinancing | PremiumAmount | NaN | Difference between the cash amount of the first leg and the cash amount of the second leg of the repurchase agreement. | CurrencyAndAmount | NaN |
| SecuritiesFinancing | TerminationAmountPerPieceOfCollateral | NaN | Amount of money to be settled per piece of collateral to terminate the transaction. | CurrencyAndAmount | NaN |
| SecuritiesFinancing | TerminationTransactionAmount | NaN | Total amount of money to be settled to terminate the transaction. | CurrencyAndAmount | NaN |
| SecuritiesFinancing | MaturityDateModification | NaN | Specifies whether the maturity date of the securities financing transaction may be modified. | YesNoIndicator | NaN |
| SecuritiesFinancing | EarliestCallBackDate | NaN | Earliest date/time at which the call back can take place. | ISODateTime | NaN |
| SecuritiesFinancing | OpeningSettlementDate | NaN | Date and time at which the securities are to be delivered or received. | ISODateTime | NaN |
| SecuritiesFinancing | RepurchaseType | NaN | Specifies the type of repurchase transaction. | RepurchaseTypeCode | NaN |
| SecuritiesFinancing | EndPrice | NaN | Negotiated fixed price of the security to buy it back. | SecuritiesPricing | RelatedSecuritiesFinancing |
| SecuritiesFinancing | SpreadTransaction | NaN | Specifies that there will be one price and one transaction when two contracts are carried out simultaneously, one to buy and the other one to sell with two different expiration dates. | YesNoIndicator | NaN |
| SecuritiesFinancing | FinancingAgreement | NaN | Provides the contractual details related to the agreement between parties. | SecuritiesFinancingAgreement | SecuritiesFinancingTrade |
| SecuritiesFinancing | OpeningSettlementAmount | NaN | Total amount of money to be paid or received in exchange for the securities at the opening of a securities financing transaction. | CurrencyAndAmount | NaN |
| SecuritiesFinancing | ClosingLegExecution | NaN | Repayment of the previously received cash by one party in exchange of the return of the security by the counterparty. | SecuritiesTrade | SecuritiesFinancingClosingData |
| SecuritiesFinancing | OpeningLegExecution | NaN | Transfer of cash to a party against the legal transfer of securities. The cash receiver agrees to buy the same security from the counterparty at a fixed price at some later date. | SecuritiesTrade | SecuritiesFinancingOpeningData |
| SecuritiesFinancing | RelatedIndicationOfInterest | NaN | Indication of interest process which is the source of a securities financing process. | BuyOrSellIndicationOfInterest | TwoLegTransaction |
| SecuritiesFinancing | Identification | NaN | Unique identification of the repurchase agreement. | Max35Text | NaN |
| SecuritiesFinancing | TerminationOption | NaN | Indicates the termination option for a repurchase agreement. | RepoTerminationOptionCode | NaN |
| ProceedsDefinition | NaN | NaN | Definition of exchanges of cash and/or securities available in the processing of corporate actions. | NaN | NaN |
| ProceedsDefinition | SpecialConcessionAmount | NaN | Amount of drawdown or other reduction from or in addition to the deal price. | CurrencyAndAmount | NaN |
| ProceedsDefinition | CreditDebitIndicator | NaN | Specifies whether the value is a debit or credit. | DebitCreditCode | NaN |
| ProceedsDefinition | EarliestPaymentDate | NaN | Date on which a payment can be made, eg, if payment date is a non-business day or to indicate the first payment date of an offer. | ISODateTime | NaN |
| ProceedsDefinition | ValueDate | NaN | Date/time at which assets become available to the account owner (in a credit entry), or cease to be available to the account owner (in a debit entry). | ISODateTime | NaN |
| ProceedsDefinition | NonEligibleProceedsIndicator | NaN | Specifies information regarding outturn resources that cannot be processed by the CSD. Special delivery instruction is required from the account owner for the CA outcome to be credited. | NonEligibleProceedsIndicatorCode | NaN |
| ProceedsDefinition | IssuerOfferorTaxabilityIndicator | NaN | Proceeds are taxable according to the information provided by the issuer / offeror. | Max35Text | NaN |
| ProceedsDefinition | OfferPriceFixingDate | NaN | Date/time at which an offer price is determined (as compared to its reset date if applicable). | ISODateTime | NaN |
| ProceedsDefinition | Option | NaN | Option for which proceeds are specified. | CorporateActionOption | ProceedsDefinition |
| ProceedsDefinition | CorporateAction | NaN | Corporate action for which the proceeds are specified. | CorporateActionEvent | ProceedsDefinition |
| ProceedsDefinition | CountryOfIncomeSource | NaN | Indicates the country from which the income originates. | CountryCode | NaN |
| SecuritiesBalance | NaN | Balance | Net position of a segregated holding, in a single security, within the overall position held in a securities account. A securities balance is calculated from the sum of securities' receipts minus the sum of securities' deliveries. | NaN | NaN |
| SecuritiesBalance | NetGainLoss | NaN | Amount representing the difference between the cost and the current price of a security. In the context of securities settlement, it is the amount paid or received when the instructions are netted or paired off. | CurrencyAndAmount | NaN |
| SecuritiesBalance | SecuritiesAccount | NaN | Account or sub-account for which a balance is calculated. It is derived from the association between Balance and Account. | SecuritiesAccount | SecuritiesBalance |
| SecuritiesBalance | EligibleBalanceRelatedEntitlement | NaN | Corporate action entitlement for which an eligible balance is specified. | CorporateActionEntitlement | EligibleBalance |
| SecuritiesBalance | ShortLong | NaN | Indication that the position is short or long. | ShortLongCode | NaN |
| SecuritiesBalance | AggregateQuantity | NaN | Total quantity of financial instruments of the balance. | SecuritiesQuantity | AggregateQuantityBalance |
| SecuritiesBalance | CorporateActionEntitlement | NaN | Corporate action entitlement for which a balance is specified. | CorporateActionEntitlement | SecuritiesBalance |
| SecuritiesBalance | InstructedBalanceRelatedEntitlement | NaN | Corporate action entitlement for which an instructed balance is specified. | CorporateActionEntitlement | InstructedBalance |
| SecuritiesBalance | UninstructedBalanceRelatedEntitlement | NaN | Corporate action entitlement for which an uninstructed balance is specified. | CorporateActionEntitlement | UninstructedBalance |
| SecuritiesBalance | MainSecuritiesBalance | NaN | Balance which is divided in sub-balances. | SecuritiesBalance | SecuritiesSubBalance |
| SecuritiesBalance | SecuritiesSubBalance | NaN | Net position of a segregated holding of a single security within the overall position held in an account, eg, sub-balance per status. | SecuritiesBalance | MainSecuritiesBalance |
| SecuritiesBalance | SecuritiesBalanceType | NaN | Reason a security is not available or additional information about the financial instrument for which the balance is given, for example, unregistered, registered in nominee name. | SecuritiesBalanceTypeV2Code | NaN |
| SecuritiesBalance | SubBalanceQuantity | NaN | Net position of a segregated holding of a single security within the overall position held in a securities account, for instance. sub-balance per type. | SecuritiesQuantity | RelatedSubBalance |
| SecuritiesBalance | Security | NaN | Security for which a balance is calculated. | Security | Balance |
| SecuritiesBalance | ExchangeRate | NaN | Specifies the exchange rate used to convert the balance value in another currency. | CurrencyExchange | CurrencyExchangeForSecuritiesBalance |
| SecuritiesBalance | AvailabilityIndicator | NaN | Indicates whether the quantity of securities on the balance is available. | YesNoIndicator | NaN |
| SecuritiesBalance | AvailableQuantity | NaN | Total quantity of financial instruments of the balance that is available. | SecuritiesQuantity | AvailableQuantityBalance |
| SecuritiesBalance | RelatedMeetingEntitlement | NaN | Entitlement for which an eligible posistion is specified. | MeetingEntitlement | EligiblePosition |
| SecuritiesBalance | UnavailableQuantity | NaN | Total quantity of financial instruments of the balance that is not available. | SecuritiesQuantity | UnavailableQuantityBalance |
| SecuritiesBalance | SafekeepingPlace | NaN | Safekeeping place at which the securities are held. | SafekeepingPlace | SecuritiesBalance |
| SecuritiesBalance | SecuritiesEntry | NaN | Postings used to calculate a balance. It is derived from the association between Balance and Entry | SecuritiesEntry | SecuritiesBalance |
| SecuritiesBalance | NotEligibleBalanceRelatedEntitlement | NaN | Corporate action entitlement for which a non eligible balance is specified. | CorporateActionEntitlement | NotEligibleBalance |
| SecuritiesBalance | RelatedIntraPositionTransfer | NaN | Transfer between two balances or sub balances. | IntraPositionTransfer | SecuritiesBalance |
| SecuritiesBalance | CostAdjustment | NaN | Specifies the amount added or substracted to the original cost of a transaction. | CurrencyAndAmount | NaN |
| SecuritiesBalance | Pledgee | NaN | Pledgee at which the securities are held. | Pledgee | SecuritiesBalance |
| Collateral | NaN | NaN | Assets pledged by a debtor to secure a loan or an exposure and subject to seizure in the event of default. | NaN | NaN |
| Collateral | CollateralAmount | NaN | Value of the collateral as an amount. | CurrencyAndAmount | NaN |
| Collateral | Valuation | NaN | Valuation process of specific collateral elements. | CollateralValuation | Collateral |
| Collateral | CollateralType | NaN | Specifies the type of collateral. | CollateralTypeCode | NaN |
| Collateral | BaseCurrencyAmount | NaN | Value of the collateral in the currency used for reporting. | ActiveCurrencyAndAmount | NaN |
| Collateral | CollateralPurpose | NaN | Specifies whether the collateral has been posted against the variation margin or the segregated independent amount. | CollateralPurposeCode | NaN |
| Collateral | CollateralBalance | NaN | Collateral balance which contain specific collateral elements. | CollateralBalance | CollateralDescription |
| Collateral | CollateralAccount | NaN | Account from or to which collateral is delivered. | Account | RelatedCollateralProcess |
| Collateral | CollateralManagement | NaN | Series of processes which are related to the collateral processes. | CollateralManagement | Collateral |
| Collateral | CollateralPartyRole | NaN | Specifies the roles played by a party in the context of collateral processes. | CollateralPartyRole | Collateral |
| Collateral | Status | NaN | Specifies the status of the collateral or of an event related to collateral. | CollateralStatus | Collateral |
| Collateral | AssetHolding | NaN | Specifies the securities or physical entities given as collateral. | AssetHolding | Collateral |
| Collateral | VariationMarginAssetHolding | NaN | Specifies in terms of value and quantity the assets held as collateral against the variation margin. | AssetHolding | VariationMarginCollateral |
| Collateral | SegregatedIndependentAmountAssetHolding | NaN | Specifies in terms of value and quantity the assets held as collateral against the segregated independent amount. | AssetHolding | IndependentAmountCollateral |
| Collateral | CollateralAgreement | NaN | Collateral agreement which governs the collateral. | CollateralAgreement | Collateral |
| Collateral | CollateralOwnership | NaN | Specifies who is the owner of the collateral. | Max35Text | NaN |
| Collateral | RelatedCollateralSubstitution | NaN | Collateral substitution for which new collateral is replacing the returned one. | CollateralSubstitution | NewCollateral |
| Collateral | CollateralDeliveryMethod | NaN | Specifies whether the collateral is subject to a title transfer collateral arrangement, a securities interest collateral arrangement, or a securities interest with the right of use. | CollateralDeliveryMethodCode | NaN |
| Collateral | CollateralQualityType | NaN | Risk classification of the security used as collateral. | CollateralQualityTypeCode | NaN |
| Collateral | DeliveryByValue | NaN | Specifies whether the transaction was settled using the Delivery-by-Value (DBV) mechanism. | TrueFalseIndicator | NaN |
| Collateral | CollateralReinvestment | NaN | Provides details on the type of the cash reinvestment in a given currency and on the cash reinvestment rate. | CollateralReinvestment | RelatedCollateral |
| Collateral | CollateralTransactionType | NaN | Collateral transaction type. | CollateralTransactionTypeCode | NaN |
| RegistrarRole | NaN | SecuritiesPartyRole | Party responsible for keeping track of the owners of securities. | NaN | NaN |
| RegistrarRole | RegistrarAccount | NaN | Account at the registrar where financial instruments are registered. | SecuritiesAccount | RelatedRegistrar |
| RegistrarRole | RegisterName | NaN | Name of the register managed by a registration authority. | Max35Text | NaN |
| IssuerRole | NaN | AssetPartyRole | Legal entity that has the right to issue securities. | NaN | NaN |
| CorporateActionNotification | NaN | NaN | The process of notifying of an upcoming corporate action. It provides corporate action details including the different options. | NaN | NaN |
| CorporateActionNotification | RelatedServicing | NaN | Process which groups the activities related to corporate action servicing. | CorporateActionServicing | CorporateActionEventNotification |
| CorporateActionNotification | CorporateActionNotificationIdentification | NaN | Identifies the corporate action notification. | Max35Text | NaN |
| CorporateActionNotification | NotificationType | NaN | Specifies the type of notification. | CorporateActionNotificationTypeCode | NaN |
| CorporateActionNotification | CreationDateTime | NaN | Specifies the date and time when the notification was issued. | ISODateTime | NaN |
| CorporateActionStatusReason | NaN | StatusReason | Specifies the underlying reason for a status of a corporate action. | NaN | NaN |
| CorporateActionStatusReason | CorporateActionCancellationReason | NaN | Specifies reasons for cancellation of a corporate action event. | CorporateActionCancellationReasonCode | NaN |
| CorporateActionStatusReason | CorporateActionStatus | NaN | Corporate actions status for which a reason is provided. | CorporateActionStatus | CorporateActionStatusReason |
| CorporateActionStatusReason | AcceptedReason | NaN | Specifies additional information about the processed instruction. | AcknowledgementReasonCode | NaN |
| CorporateActionStatusReason | ReversalReason | NaN | Reason for the reversal. | CorporateActionReversalReasonCode | NaN |
| CorporateActionStatusReason | MovementFailureReason | NaN | The reason for the failure. | FailedSettlementReasonCode | NaN |
| CorporateActionStatusReason | MovementRejectionReason | NaN | Provides information about the rejection status. | RejectionReasonV3Code | NaN |
| CorporateActionEvent | NaN | NaN | An event determined by a corporation's board of directors, that changes the existing corporate capital structure or financial condition. | NaN | NaN |
| CorporateActionEvent | Type | NaN | Type of corporate action event. | CorporateActionEventTypeV6Code | NaN |
| CorporateActionEvent | MandatoryVoluntaryEventType | NaN | Specifies whether the event is mandatory, mandatory with options or voluntary. | CorporateActionMandatoryVoluntaryCode | NaN |
| CorporateActionEvent | UnderlyingSecurity | NaN | Security to which this instruction or event applies. | Security | CorporateEvent |
| CorporateActionEvent | CorporateActionPrice | NaN | Specifies prices related to a corporate action. | CorporateActionPrice | CorporateActionEvent |
| CorporateActionEvent | ExchangeRate | NaN | Rate, specified by the issuer, when the paid amount is not in the same currency as the specified amount. | CurrencyExchange | RelatedCorporateActionEvent |
| CorporateActionEvent | RegistrationDetails | NaN | Provides information required for the registration. | Max350Text | NaN |
| CorporateActionEvent | BasketOrIndexInformation | NaN | Provides additional information on the basket or index underlying a security, for example a warrant. | Max350Text | NaN |
| CorporateActionEvent | Deadline | NaN | Specifies the different deadlines related to a corporate event. | Deadline | RelatedCorporateActionEvent |
| CorporateActionEvent | AdditionalBusinessProcess | NaN | Specifies the type of the additional business process linked to a corporate action event such as a claim compensation or tax refund. | AdditionalBusinessProcessCode | NaN |
| CorporateActionEvent | TradingDate | NaN | Date/time at which the deal (rights) was agreed. | ISODateTime | NaN |
| CorporateActionEvent | CorporateActionCharge | NaN | Specifies the charges relative to a corporate action event. | CorporateActionFeesAndCharges | CorporateAction |
| CorporateActionEvent | PariPassuDate | NaN | Date on which security will assimilate, become fungible, or have the same rights to dividends as the parent issue. | ISODateTime | NaN |
| CorporateActionEvent | InformationConditions | NaN | Provides conditional information related to the event, eg, an offer is subject to 50% acceptance, the offeror allows the securities holder to set some conditions. | Max350Text | NaN |
| CorporateActionEvent | FractionalQuantity | NaN | Fractional quantity resulting from an event which will be paid with cash in lieu. | SecuritiesQuantity | RelatedEventForFractionalQuantity |
| CorporateActionEvent | EventProcessingType | NaN | Type of processing involved by a Corporate Action. | CorporateActionEventProcessingTypeCode | NaN |
| CorporateActionEvent | CorporateActionStatus | NaN | Status of the corporate action process. | CorporateActionStatus | CorporateActionEvent |
| CorporateActionEvent | AnnouncementDate | NaN | Date/time at which the issuer announced that a corporate action event will occur such as the issue of securities or an official meeting. | ISODateTime | NaN |
| CorporateActionEvent | EffectiveDate | NaN | Date/time at which an event is officially effective from the issuer's perspective. | ISODateTime | NaN |
| CorporateActionEvent | FurtherDetailsAnnouncementDate | NaN | Date/time at which additional information on the event will be announced, for instance exchange ratio announcement date. | ISODateTime | NaN |
| CorporateActionEvent | MarginFixingDate | NaN | Date/time at which the margin rate will be determined . | ISODateTime | NaN |
| CorporateActionEvent | ResultPublicationDate | NaN | Date on which results are published, eg, results of an offer, of a meeting. | ISODate | NaN |
| CorporateActionEvent | UnconditionalDate | NaN | Date upon which the terms of the take-over become unconditional as to acceptances. | ISODateTime | NaN |
| CorporateActionEvent | WhollyUnconditionalDate | NaN | Date on which all conditions, including regulatory, legal etc. pertaining to the take-over, have been met. | ISODateTime | NaN |
| CorporateActionEvent | LapsedDate | NaN | Date/time at which an event/offer is terminated or lapsed. | ISODateTime | NaN |
| CorporateActionEvent | BookClosurePeriod | NaN | Period defining the last date on which shareholder registration will be accepted by the issuer and the date on which shareholder registration will resume. | DateTimePeriod | BookClosureCorporateAction |
| CorporateActionEvent | SecuritiesQuantity | NaN | Provides information about securities quantity linked to a corporate action. | SecuritiesQuantity | CorporateActionEvent |
| CorporateActionEvent | RestrictionIndicator | NaN | Indicates whether there are legal or other restrictions associated with a rights offer or other corporate event, for example, domicile, citizenship, residency, type of investor. Yes = There are restrictions. No = There are no restrictions. | YesNoIndicator | NaN |
| CorporateActionEvent | EventStage | NaN | Stage in the corporate action event life cycle. | CorporateActionEventStageCode | NaN |
| CorporateActionEvent | DocumentationLocation | NaN | Information on where additional information published for the event, can be received. for instance the address for the Universal Resource Locator (URL), eg, used over the www (HTTP) service. | ContactPoint | RelatedCorporateActionEvent |
| CorporateActionEvent | SecuritiesQuantitySought | NaN | Quantity of securities the offeror/issuer will purchase or redeem under the terms of the event. This can be a number or the term "any and all". | SecuritiesQuantity | RelatedCorporateActionEvent |
| CorporateActionEvent | PartialElectionIndicator | NaN | Specifies if the issuer will allow the agent to accept partial elections. It is to allow split voting over options. It allows the client to elect more than one option to be selected per designated holding. | YesNoIndicator | NaN |
| CorporateActionEvent | CorporateActionPartyRole | NaN | Specifies the role played by a party in the context of a corporate action. | CorporateActionPartyRole | CorporateActionEvent |
| CorporateActionEvent | MarketClaim | NaN | Market claim information. | MarketClaim | RelatedCorporateEvent |
| CorporateActionEvent | BiddingConditions | NaN | Specifies the conditions under which securities can be acquired as part of a corporate action. | BiddingConditions | Event |
| CorporateActionEvent | RelatedClassAction | NaN | Specifies the underlying class action related to the event. | ClassAction | CorporateEvent |
| CorporateActionEvent | CorporateActionEventRegistration | NaN | Official registration of the event. | CorporateActionEventRegistration | CorporateActionEvent |
| CorporateActionEvent | SuspensionPeriod | NaN | Period defining the last date for which an action will be accepted and the date on which the suspension will be released and normal processing will resume. | SuspensionPeriod | CorporateActionEvent |
| CorporateActionEvent | Lottery | NaN | Organisation of draws for cash prizes on bonds (instead of coupon payments). Every issued bond (similar to a lottery ticket) has an equal opportunity at winning payments in the draws. | Lottery | RelatedCorporateEvent |
| CorporateActionEvent | MarginType | NaN | Specifies the margin type for a remarketing procedure. | RemarketingMarginTypeCode | NaN |
| CorporateActionEvent | RelatedMeeting | NaN | Provides information on the meeting related to the corporate event. | Meeting | CorporateEvent |
| CorporateActionEvent | Services | NaN | Specifies the different services linked to a corporate action event. | CorporateActionServicing | Event |
| CorporateActionEvent | Issuance | NaN | Information specified when the corporate event relates to the issuance of securities. | Issuance | EventInformation |
| CorporateActionEvent | SecuritiesModification | NaN | Modification of the reference data of a security or of the organisation that issued it. | SecuritiesModification | RelatedCorporateEvent |
| CorporateActionEvent | TradingPeriod | NaN | Period during which a financial instrument is available for trading. | DateTimePeriod | RelatedCorporateAction |
| CorporateActionEvent | TransactionTax | NaN | Tax rate of financial transactions related to an event. | Tax | CorporateActionEvent |
| CorporateActionEvent | ConsentType | NaN | Corporate actions may be approved by shareholders without a meeting or a vote by means of execution of a consent by a majority of shareholders entitled to vote. | ConsentTypeCode | NaN |
| CorporateActionEvent | ProceedsDefinition | NaN | Specifies the proceeds of a corporate action. | ProceedsDefinition | CorporateAction |
| CorporateActionEvent | TaxOnNonDistributedProceedsIndicator | NaN | Specifies the tax regulation being attributed to the non- distributed proceeds event. | NaN | NaN |
| ClassAction | NaN | NaN | Form of lawsuit in which a group of shareholders collectively bring a claim to court, mainly because it would be too expensive for each individual shareholder to launch their own lawsuit. | NaN | NaN |
| ClassAction | ClassActionNumber | NaN | Reference assigned by a court to a class action. | Max35Text | NaN |
| ClassAction | LeadPlaintiffDeadline | NaN | Last day an investor can become a lead plaintiff. | ISODateTime | NaN |
| ClassAction | CourtApprovalDate | NaN | Date upon which the High Court provided approval. | ISODateTime | NaN |
| ClassAction | ClaimPeriod | NaN | Period assigned by the court in a class action. It determines the client's eligible transactions that will be included in the class action and used to determine the resulting entitlement. | DateTimePeriod | ClassAction |
| ClassAction | FilingDate | NaN | Date on which the action was filed at the applicable court. | ISODateTime | NaN |
| ClassAction | HearingDate | NaN | Date for the hearing between the plaintiff and defendant, as set by the court. | ISODateTime | NaN |
| ClassAction | CorporateEvent | NaN | Corporate event for which class action is specified. | CorporateActionEvent | RelatedClassAction |
| CorporateActionEntitlement | NaN | NaN | Rights entitled to the account owner based on the terms of the corporate action event and the balance of underlying securities. | NaN | NaN |
| CorporateActionEntitlement | EligibleBalance | NaN | Total balance of securities eligible for this corporate action event. The entitlement calculation is based on this balance. | SecuritiesBalance | EligibleBalanceRelatedEntitlement |
| CorporateActionEntitlement | SecuritiesBalance | NaN | Specifies any type of balance related to a corporate action entitlement. | SecuritiesBalance | CorporateActionEntitlement |
| CorporateActionEntitlement | InstructedBalance | NaN | Balance of instructed position. | SecuritiesBalance | InstructedBalanceRelatedEntitlement |
| CorporateActionEntitlement | UninstructedBalance | NaN | Balance of uninstructed position. | SecuritiesBalance | UninstructedBalanceRelatedEntitlement |
| CorporateActionEntitlement | EligibleBalanceIndicator | NaN | Indicates whether the eligible balance is final except for a voluntary corporate action event where it can represent the current eligible balance when communicated before expiration date of that event. | YesNoIndicator | NaN |
| CorporateActionEntitlement | RelatedServicing | NaN | Process which groups the activities related to corporate action servicing. | CorporateActionServicing | CorporateActionEntitlement |
| CorporateActionEntitlement | NotEligibleBalance | NaN | Total balance of securities which are not eligible for this corporate action event. | SecuritiesBalance | NotEligibleBalanceRelatedEntitlement |
| BeneficialOwner | NaN | SecuritiesPartyRole | Characteristics of an individual or entity that is ultimately entitled to the benefit of income and rights in a security, as opposed to a nominal or legal owner. | NaN | NaN |
| BeneficialOwner | CertificationType | NaN | Type of certification which is required. | BeneficiaryCertificationTypeCode | NaN |
| BeneficialOwner | NonDomicileCountry | NaN | The holder of the security has to certify, in line with the terms of the corporate action, that it is not domiciled in the country indicated. | Country | CountryForBeneficialOwner |
| BeneficialOwner | CertificationIndicator | NaN | Indicates whether or not certification is required from the account owner, for instance a certification is required to participate to a corporate action event. Y: certification required N: no certification required | YesNoIndicator | NaN |
| BeneficialOwner | CertificationFormat | NaN | Specifies the certification format required, that is, physical or electronic format. | CertificationFormatTypeCode | NaN |
| BeneficialOwner | ERISAEligibility | NaN | Eligibility to federal Employee Retirement Income Security Act. | ERISAEligibilityCode | NaN |
| BeneficialOwner | ERISARate | NaN | Federal Employee Retirement Income Security Act (ERISA) rate. | PercentageRate | NaN |
| BeneficialOwner | BenefitPlanDeclarationIndicator | NaN | Indicates whether the investor is a benefit plan investor. | YesNoIndicator | NaN |
| CorporateActionOption | NaN | NaN | Provides information about the alternatives available to an account owner when participating to a corporate action event. This is defined at a general level without looking at the specificities of the securities balances. | NaN | NaN |
| CorporateActionOption | OptionNumber | NaN | Number identifying the available corporate action options. | Exact3NumericText | NaN |
| CorporateActionOption | OptionType | NaN | Type of corporate action options available to the account owner. | CorporateActionOptionCode | NaN |
| CorporateActionOption | FractionDisposition | NaN | Treatment of the fractions resulting from derived securities will be processed or how prorated decisions will be rounding, if provided with a pro ration rate. | FractionDispositionTypeCode | NaN |
| CorporateActionOption | CurrencyOption | NaN | Currency choice given to the investor. | CurrencyCode | NaN |
| CorporateActionOption | RelatedChoiceCorporateAction | NaN | Corporate action for which one or more options are provided. | ChoiceCorporateAction | CorporateActionOptionDefinition |
| CorporateActionOption | CorporateActionElection | NaN | Election process which selected a specific option. | CorporateActionElection | Option |
| CorporateActionOption | OptionFeatures | NaN | Features that may apply to a corporate action option. | OptionFeaturesCode | NaN |
| CorporateActionOption | ActionPeriod | NaN | Period during which the specified option remains valid, eg, offer period. | DateTimePeriod | CorporateActionOption |
| CorporateActionOption | OfferType | NaN | Conditions that apply to the offer. | OfferTypeV2Code | NaN |
| CorporateActionOption | ChargesAppliedIndicator | NaN | Indicates whether charges apply to the holder, for instance redemption charges. | YesNoIndicator | NaN |
| CorporateActionOption | WithdrawalAllowedIndicator | NaN | Indicates whether withdrawal of instruction is allowed. | YesNoIndicator | NaN |
| CorporateActionOption | ChangeAllowedIndicator | NaN | Indicates whether change of instruction is allowed. | YesNoIndicator | NaN |
| CorporateActionOption | CorporateActionOptionServicing | NaN | Calculation of the entitlement on the basis of the proposed option. | CorporateActionOptionServicing | RelatedOption |
| CorporateActionOption | ProceedsDefinition | NaN | Definition of exchanges of cash and / or securities available in the processing of corporate actions. | ProceedsDefinition | Option |
| CorporateActionOption | Distribution | NaN | Distribution process for which an option is selected. | CorporateActionDistribution | Option |
| CorporateActionOption | Default | NaN | Specifies whether the option is the default option or not. | YesNoIndicator | NaN |
| SecuritiesModification | NaN | NaN | Modification of the reference data of a security or of the organisation that issued it. | NaN | NaN |
| SecuritiesModification | ChangeType | NaN | Type of changes affecting the security form. | CorporateActionChangeTypeCode | NaN |
| SecuritiesModification | NewOrganisationInformation | NaN | New name of a company following a name change. | Organisation | SecuritiesModification |
| SecuritiesModification | RelatedCorporateEvent | NaN | Specifies the parameters of the event related to the modification of the securities. | CorporateActionEvent | SecuritiesModification |
| SecuritiesModification | NewSecurityReferenceData | NaN | Specifies the updated information of the new security. | Security | Modification |
| SecuritiesModification | NumberOfSharesIssued | NaN | The number of shares the issuer is creating as part of the event | Number | NaN |
| SecuritiesModification | LastTradingDate | NaN | Date/time at which the securities to be reorganised will cease to be tradeable. | ISODateTime | NaN |
| SecuritiesProceedsDefinition | NaN | ProceedsDefinition | The definition of the securities proceeds for a corporate action in generic terms; that is, before applying it to specific securities holding. An example would be the definition of a bonus rights issue where all the information will be given in general on a per share basis. | NaN | NaN |
| SecuritiesProceedsDefinition | SecuritiesQuantity | NaN | The quantity of financial instruments that is posted. | SecuritiesQuantity | SecuritiesProceedsDefinition |
| SecuritiesProceedsDefinition | ConditionalQuantity | NaN | Minimum quantity of securities to be accepted (used in the framework of conditional privilege on election). In case of proration, if this minimum quantity is not reached then the instruction is void. | SecuritiesQuantity | ConditionalQuantitySecuritiesProceeds |
| SecuritiesProceedsDefinition | OverAndAboveNormalEnsuredEntitlementQuantity | NaN | Quantity instructed to be received over and above normal ensured entitlement. | SecuritiesQuantity | OverAndAboveQuantitySecuritiesProceeds |
| SecuritiesProceedsDefinition | QuantityToReceive | NaN | Quantity of the benefits that the account owner wants to receive, for example, as a result of dividend reinvestment. | SecuritiesQuantity | ExpectedQuantitySecuritiesProceeds |
| SecuritiesProceedsDefinition | StatusQuantity | NaN | Quantity of securities that has been assigned the status indicated. | SecuritiesQuantity | StatusRelatedSecuritiesProceeds |
| SecuritiesProceedsDefinition | ParallelTradingPeriod | NaN | Period during which both old and new equity may be traded simultaneously, eg, consolidation of equity or splitting of equity. | DateTimePeriod | ParallelTradingProceedsDefinition |
| SecuritiesProceedsDefinition | AdditionalQuantityForSubscribedResultantSecurities | NaN | Quantity of additional intermediate securities/new equities awarded for a given quantity of securities derived from subscription. | QuantityRatio | AdditionalQuantityForResultantSecuritiesProceedsDefinition |
| SecuritiesProceedsDefinition | AdditionalQuantityForExistingSecurities | NaN | Quantity of additional securities for a given quantity of underlying securities where underlying securities are not exchanged or debited, eg, 1 for 1: 1 new equity credited for every 1 underlying equity = 2 resulting equities. | QuantityRatio | AdditionalQuantityForSubscribedSecuritiesProceedsDefinition |
| SecuritiesProceedsDefinition | NewToOld | NaN | Quantity of new securities for a given quantity of underlying securities, where the underlying securities will be exchanged or debited, eg, 2 for 1: 2 new equities credited for every 1 underlying equity debited = 2 resulting equities. | QuantityRatio | NewToOldProceedsDefinition |
| SecuritiesProceedsDefinition | NewSecuritiesToUnderlyingSecurities | NaN | Quantity of new equities that will be derived by the exercise of a given quantity of intermediate securities. | QuantityRatio | NewToUnderlyingProceedsDefinition |
| SecuritiesProceedsDefinition | ReinvestmentAmount | NaN | Amount of money reinvested in additional securities. | CurrencyAndAmount | NaN |
| SecuritiesProceedsDefinition | IntermediateSecuritiesDistributionType | NaN | Type of intermediate securities distribution, eg, stock dividend, reverse right. | IntermediateSecurityDistributionTypeCode | NaN |
| SecuritiesProceedsDefinition | BoardLotSecuritiesQuantity | NaN | Quantity of equity that makes up a board lot. | SecuritiesQuantity | BoardLotSecuritiesProceeds |
| SecuritiesProceedsDefinition | NewDenominationSecuritiesQuantity | NaN | New denomination of the financial instrument following, eg, an increase or decrease in nominal value. | SecuritiesQuantity | NewDenominationSecuritiesProceeds |
| SecuritiesProceedsDefinition | IntermediateSecuritiesToUnderlyingRatio | NaN | Quantity of intermediate securities awarded for a given quantity of underlying security. | QuantityRatio | IntermediateSecuritiesProceedsDefinition |
| SecuritiesProceedsDefinition | ReinvestmentDiscountToMarket | NaN | Rate of discount for securities purchased through a reinvestment scheme as compared to the current market price of security. | PercentageRate | NaN |
| SecuritiesProceedsDefinition | RedemptionDate | NaN | Date on which the securities will be redeemed (early) for payment of principal. | ISODateTime | NaN |
| SecuritiesProceedsDefinition | AssentedLinePeriod | NaN | Period during which the assented line is available. | DateTimePeriod | AssentedLinePeriodProceedsDefinition |
| SecuritiesProceedsDefinition | SellThruIssuerPeriod | NaN | Period (last day included) during which an account owner can surrender or sell securities to the issuer and receive the sale proceeds. | DateTimePeriod | SellThruIssuerProceedsDefinition |
| SecuritiesProceedsDefinition | ShareRanking | NaN | Specifies whether the shares are ranking for dividend or pari passu. | ShareRankingCode | NaN |
| CorporateActionElection | NaN | NaN | Decision taken by the account holder regarding the corporate action event. | NaN | NaN |
| CorporateActionElection | ExecutionRequestedDateTime | NaN | Date/time at which the instructing party requests the instruction to be executed. | ISODateTime | NaN |
| CorporateActionElection | Option | NaN | Option on which the investor makes its decision. | CorporateActionOption | CorporateActionElection |
| CorporateActionElection | CashAccount | NaN | Specifies the account(s) used in relation with the election of an option. | CashAccount | RelatedCorporateActionElection |
| CorporateActionElection | ElectionType | NaN | Specifies whether the election results in a change of balance type that transfers control of the underlying securities or the transfer of underlying securities themselves. | ElectionMovementTypeCode | NaN |
| CorporateActionElection | Quantity | NaN | Specifies the quantity of securities elected for the associated option. | SecuritiesQuantity | CorporateActionElection |
| CorporateActionElection | AmendmentReason | NaN | Reason explaining the amendment of the election. | Max350Text | NaN |
| CorporateActionElection | RelatedServicing | NaN | Process which groups the activities related to corporate action servicing. | CorporateActionServicing | CorporateActionElection |
| CorporateActionElection | ProtectProcess | NaN | Provides detailed information on protect and cover protect instructions. | CorporateActionProtectProcess | RelatedCorporateActionElection |
| ChoiceCorporateAction | NaN | MandatoryCorporateAction | Mandatory with choice corporate action event that involves a choice on behalf of the owner of the securities. The shareholders are given a chance to choose among several options. | NaN | NaN |
| ChoiceCorporateAction | CorporateActionOptionDefinition | NaN | Definition of the option of a corporate event. | CorporateActionOption | RelatedChoiceCorporateAction |
| BiddingConditions | NaN | NaN | Specifies the conditions under which securities can be acquired as part of a corporate action. | NaN | NaN |
| BiddingConditions | ProposedRate | NaN | Rate proposed in a remarketing of variable rate notes. | PercentageRate | NaN |
| BiddingConditions | OversubscriptionRate | NaN | Rate of allowed over-subscription. | PercentageRate | NaN |
| BiddingConditions | InformationToComplyWith | NaN | Provides information conditions to the account owner that are to be complied with, eg, not open to US/Canadian residents, QIB or SIL to be provided. | Max350Text | NaN |
| BiddingConditions | SubscriptionCostDebitDate | NaN | Date by which cash must be in place in order to take part in the event. | ISODateTime | NaN |
| BiddingConditions | MaximumAllowedOverSubscription | NaN | A maximum percentage of shares available through the over subscription privilege, usually a percentage of the basic subscription shares, eg, an account owner subscribing to 100 shares may over subscribe to a maximum of 50 additional shares when the over subscription maximum is 50%. | RateAndAmount | MaximumAllowedBiddingConditions |
| BiddingConditions | ProrationRate | NaN | Proportionate allocation used for the offer. | PercentageRate | NaN |
| BiddingConditions | ApplicableRate | NaN | Rate applicable to the event announced, eg, redemption rate for a redemption event. | RateAndAmount | RateBiddingConditions |
| BiddingConditions | FrontEndOddLotQuantity | NaN | Specifies that if an order is prorated holders of odd lots who tender their full position will not have tendered position prorated but rather accepted in full. | SecuritiesQuantity | FrontEndOddLotBiddingConditions |
| BiddingConditions | BackEndOddLotQuantity | NaN | Represents the presence of a back end odd lot provision and the quantity of equity required after proration to be eligible for this privilege. | SecuritiesQuantity | BackEndOddLotBiddingConditions |
| BiddingConditions | TransformationRate | NaN | Rate used to determine the cash consideration split across outturn settlement transactions that are the result of a transformation of the parent transaction. | PercentageRate | NaN |
| BiddingConditions | ProrationDate | NaN | Date (and time) at which an issuer will determine the proration amount/quantity of an offer. | ISODateTime | NaN |
| BiddingConditions | CompulsoryPurchasePeriod | NaN | Period during a take-over where any outstanding equity must be purchased by the take-over company. | DateTimePeriod | BiddingConditions |
| BiddingConditions | PercentageSought | NaN | Percentage of securities the offeror/issuer will purchase or redeem under the terms of the event. This can be a number or the term "any and all". | PercentageRate | NaN |
| BiddingConditions | BidInterval | NaN | Acceptable price increment used for submitting a bid. | CurrencyAndAmount | NaN |
| BiddingConditions | MaximumPrice | NaN | Maximum or cap price at which a holder can bid, e.g. on a Dutch auction offer. | SecuritiesPricing | MaximumPriceBiddingConditions |
| BiddingConditions | MinimumPrice | NaN | Minimum or floor price at which a holder can bid, e.g. on a Dutch auction offer. | SecuritiesPricing | MinimumPriceBiddingConditions |
| BiddingConditions | MaximumQuantity | NaN | Maximum number of securities the offeror is requesting to complete the event. | SecuritiesQuantity | MaximumQuantityBiddingConditions |
| BiddingConditions | MinimumQuantitySought | NaN | Minimum quantity of securities the offeror/issuer will purchase or redeem under the terms of the event. This can be a number or the term "any and all". | SecuritiesQuantity | MinimumQuantityBiddingConditions |
| BiddingConditions | BaseDenomination | NaN | The minimum integral amount of securities that each account owner must have remaining after the called amounts are applied. | SecuritiesQuantity | BiddingConditions |
| BiddingConditions | CalculationMethod | NaN | The method of calculation of drawings and partial redemptions. | CorporateActionCalculationMethodCode | NaN |
| BiddingConditions | AdditionalSubscriptionCost | NaN | Additional costs - coming on top of the subscription costs - which the subscriber should pay as per the subscription process. | CurrencyAndAmount | NaN |
| BiddingConditions | Event | NaN | Event to which the bidding conditions apply. | CorporateActionEvent | BiddingConditions |
| TaxVoucher | NaN | NaN | Statement showing the amount or value of a distribution and either the tax credit to which the recipient is entitled in respect of that distribution; or the amount of tax deducted from the distribution. | NaN | NaN |
| TaxVoucher | RequestedTaxationRate | NaN | Requested tax rate in case of breakdown of tax rate, for example, used for adjustment of tax rate. This is the new requested applicable rate. | PercentageRate | NaN |
| TaxVoucher | CreditRate | NaN | Applicable tax rate on the tax credit amount. | PercentageRate | NaN |
| TaxVoucher | RelatedSecurityTax | NaN | Specifies tax elements on the security which is involved in the corporate event. | SecuritiesTax | TaxVoucher |
| TaxVoucher | SundryOrOtherAmount | NaN | Amount of money related to taxable income that cannot be categorised. | CurrencyAndAmount | NaN |
| TaxVoucher | CreditAmount | NaN | Amount of money per equity allocated as the result of a tax credit. | CurrencyAndAmount | NaN |
| TaxVoucher | CashAmountBroughtForward | NaN | Cash amount retained from previous dividend or interest payment. | CurrencyAndAmount | NaN |
| TaxVoucher | CashAmountCarriedForward | NaN | Cash amount carried forward to next dividend or interest payment. | CurrencyAndAmount | NaN |
| TaxVoucher | NotionalTaxAmount | NaN | Tax on the amount of cash that would have been paid when new securities are issued in lieu of a cash dividend. | CurrencyAndAmount | NaN |
| TaxVoucher | Distribution | NaN | Corporate action distribution process for which tax voucher information is provided. | CorporateActionDistribution | TaxVoucher |
| TaxVoucher | Identification | NaN | Unique and unambiguous identification for the tax voucher. | Max35Text | NaN |
| TaxVoucher | BargainDate | NaN | Date on which DRIP purchase completed. | ISODate | NaN |
| TaxVoucher | BargainSettlementDate | NaN | Settlement date of the DRIP purchase transaction. | ISODate | NaN |
| TaxVoucher | TaxVoucherRate | NaN | Distribution rate per share. | BaseOneRate | NaN |
| TaxVoucher | RecordDateHolding | NaN | Securities holding on record date. | SecuritiesQuantity | TaxVoucher |
| TaxVoucher | ScripDividendReinvestmentPricePerShare | NaN | Cost per share of new shares allotted. | SecuritiesPricing | TaxVoucher |
| TaxVoucher | AllotedSharesCost | NaN | Total cash amount required to purchase shares allotted. | ActiveCurrencyAndAmount | NaN |
| TaxVoucher | ForeignExchangeTransaction | NaN | Provides information about the foreign exchange transaction. | ForeignExchangeTrade | CurrencyExchangeForTaxVoucher |
| CorporateActionPrice | NaN | NaN | Prices related to a corporate action. | NaN | NaN |
| CorporateActionPrice | CorporateActionEvent | NaN | Corporate event for which a price is specified. | CorporateActionEvent | CorporateActionPrice |
| CorporateActionPrice | CorporateActionExercisePrice | NaN | 1. Price at which security will be purchased/sold if warrant is exercised, either as an actual amount or a percentage. 2. Price at which a bond is converted to underlying security either as an actual amount or a percentage. 3. Strike price of an option, represented either as an actual amount or a percentage. | SecuritiesPricing | ExercisePriceRelatedEvent |
| CorporateActionPrice | GenericCashPriceReceivedPerProduct | NaN | Generic cash price received per product by the underlying security holder either as a percentage or an amount, eg, redemption price. | SecuritiesPricing | GenericCashPriceReceivedPerProductRelatedEvent |
| CorporateActionPrice | GenericCashPricePaidPerProduct | NaN | Amount included in the dividend/NAV that is identified as gains directly or indirectly derived from interest payments within the scope of the EU Savings directive. | SecuritiesPricing | GenericCashPricePaidPerProductRelatedEvent |
| CorporateActionPrice | CashInLieuOfSharePrice | NaN | Cash disbursement in lieu of equities; usually in lieu of fractional quantity. | SecuritiesPricing | CashInLieuOfSharePriceRelatedEvent |
| CorporateActionPrice | OverSubscriptionDepositPrice | NaN | Amount of money required per over-subscribed equity as defined by the issuer. | SecuritiesPricing | OverSubscriptionDepositPriceRelatedEvent |
| CorporateActionPrice | CashValueForTax | NaN | Cash value of resulting securities proceeds for tax calculation and/or reporting. | SecuritiesPricing | CashValueForTaxRelatedEvent |
| CorporateActionPrice | PricingCalculation | NaN | Specifies the parameters taken into account to calculate the price. | SecuritiesPricing | RelatedCorporateActionPrice |
| CorporateActionPrice | MinimumMultipleCashToInstruct | NaN | Mimimum multiple of a cash amount that may be instructed. | SecuritiesPricing | MinimumMultipleCashToInstructRelatedEvent |
| CorporateActionPrice | MaximumCashToInstruct | NaN | Maximum cash amount that may be instructed. | SecuritiesPricing | MaximumCashToInstructRelatedEvent |
| CorporateActionPrice | MinimumCashToInstruct | NaN | Minimum cash amount that may be instructed. | SecuritiesPricing | MinimumCashToInstructRelatedEvent |
| AmountAndQuantity | NaN | NaN | Value expressed as an amount or a quantity. For example, the value of a financial instrument. | NaN | NaN |
| AmountAndQuantity | SecuritiesPricing | NaN | Pricing which uses the amount and quantity as format. | SecuritiesPricing | AmountPricePerFinancialInstrumentQuantity |
| AmountAndQuantity | Amount | NaN | A number of monetary units specified in a currency. | CurrencyAndAmount | NaN |
| AmountAndQuantity | Quantity | NaN | A number of non-monetary units. | DecimalNumber | NaN |
| AmountRatio | NaN | NaN | Ratio expressed as a quotient of amounts. | NaN | NaN |
| AmountRatio | SecuritiesPricing | NaN | Pricing which uses the ratio as format. | SecuritiesPricing | AmountPricePerAmount |
| AmountRatio | Amount1 | NaN | Numerator of the quotient of amounts. | ActiveCurrencyAndAmount | NaN |
| AmountRatio | Amount2 | NaN | Denominator of the quotient of amounts | ActiveCurrencyAndAmount | NaN |
| CorporateActionServicing | NaN | FinancialService | Services which consists in notifying the investor or its agent of a corporate event and calculating its proceeds based on its holdings. | NaN | NaN |
| CorporateActionServicing | SecuritiesAccount | NaN | Account on which the entitlement is calculated. | SecuritiesAccount | CorporateActionServicing |
| CorporateActionServicing | CorporateActionEventNotification | NaN | Service which consists in notifying the investor or its agent of a corporate event. | CorporateActionNotification | RelatedServicing |
| CorporateActionServicing | CorporateActionDistribution | NaN | Distribution of cash or securities as a result of a corporate action election. | CorporateActionDistribution | RelatedServicing |
| CorporateActionServicing | CorporateActionOptionServicing | NaN | Service which consists in notifying the investor or its entitlement per option. | CorporateActionOptionServicing | RelatedServicing |
| CorporateActionServicing | Event | NaN | Specifies the event which is at the origin of the action. | CorporateActionEvent | Services |
| CorporateActionServicing | CorporateActionElection | NaN | Service which consists in validating, calculating and transferring the investor's instruction. | CorporateActionElection | RelatedServicing |
| CorporateActionServicing | CorporateActionEntitlement | NaN | Calculation of the proceeds based on the balance in the account. | CorporateActionEntitlement | RelatedServicing |
| CorporateActionProceedsDeliveryInstruction | NaN | NaN | Specifies the delivery instructions for the securities and cash proceeds at any stage of the Corporate Action process. | NaN | NaN |
| CorporateActionProceedsDeliveryInstruction | RelatedDistribution | NaN | Parameters of the distribution of the proceeds of a CA event. | CorporateActionDistribution | CorporateActionProceedsDeliveryInstruction |
| CorporateActionProceedsDeliveryInstruction | SecuritiesProceedsMovement | NaN | Instructions for the movement of securities related to a corporate action. | SecuritiesDeliveryObligation | RelatedCorporateAction |
| CorporateActionProceedsDeliveryInstruction | CashProceedsMovement | NaN | Instructions for the movement of cash related to a corporate action. | PaymentObligation | RelatedCorporateAction |
| CorporateActionProceedsDeliveryInstruction | SettlementAccount | NaN | Information relative to the account(s) to be used for the delivery of the proceeds (cash or securities) | Account | RelatedProceedsDelivery |
| CorporateActionProceedsDeliveryInstruction | CorporateActionStandingInstruction | NaN | Standing instruction related to a corporate action. | AgentCorporateActionStandingInstruction | RelatedDeliveryInstructions |
| Deadline | NaN | NaN | Specifies the different deadlines available for the different processes related to corporate action processes. | NaN | NaN |
| Deadline | RelatedCorporateActionEvent | NaN | Related corporate action event. | CorporateActionEvent | Deadline |
| Deadline | MarketDeadline | NaN | Date by which the action should have been completed. This deadline is set by the issuer. | ISODateTime | NaN |
| Deadline | IntermediaryDeadline | NaN | Date by which the action should have been completed. This deadline is set by an intermediary. | ISODateTime | NaN |
| Deadline | STPDeadline | NaN | Date by which the action should have been completed. This deadline is set by the issuer. (STP or Electronic mode) | ISODateTime | NaN |
| Deadline | RelatedMeeting | NaN | Meeting for which deadlines are specified. | Meeting | Deadline |
| CorporateActionFeesAndCharges | NaN | Charges | The definition of all the charges related to a corporate action event. | NaN | NaN |
| CorporateActionFeesAndCharges | CorporateAction | NaN | Corporate action for which fees and charges are specified. | CorporateActionEvent | CorporateActionCharge |
| CorporateActionFeesAndCharges | SolicitationFee | NaN | Cash amount made available in a corporate event in order to encourage participation in the event or to vote with management's position. Payment is made to a third party who has solicited an entity to take part in the offer. Also called consent fee. | RateAndAmount | SolicitationFeeCorporateActionParameters |
| CorporateActionFeesAndCharges | EarlySolicitationFeeRate | NaN | Cash rate made available, as an incentive, in addition to the solicitation fee, in order to encourage early participation in an offer. | RateAndAmount | EarlySolicitationFeeCorporateActionParameters |
| CorporateActionFeesAndCharges | Commission | NaN | Commission associated with a corporate action. | Commission | CorporateActionFeesAndCharges |
| RateAndAmount | NaN | NaN | Specifies the value expressed as a rate or an amount. For example, the value of a tax or a commission. | NaN | NaN |
| RateAndAmount | FinalDividendParameters | NaN | Dividend information for which a final dividend rate is specified. | Dividend | FinalDividend |
| RateAndAmount | FullyFrankedRateAndAmountDividendParameters | NaN | Dividend information for which a fully franked rate and amount is specified. | Dividend | FullyFrankedRateAndAmount |
| RateAndAmount | GrossDividendParameters | NaN | Dividend information for which a gross dividend rate is specified. | Dividend | GrossDividend |
| RateAndAmount | Amount | NaN | Value expressed as an amount. | CurrencyAndAmount | NaN |
| RateAndAmount | Index | NaN | Index for which a factor is specified. | Index | IndexFactor |
| RateAndAmount | NetDividendParameters | NaN | Dividend information for which a net dividend rate is specified. | Dividend | NetDividend |
| RateAndAmount | MaximumAllowedBiddingConditions | NaN | Bidding conditions for which a maximum amount is specified. | BiddingConditions | MaximumAllowedOverSubscription |
| RateAndAmount | ProvisionalDividendParameters | NaN | Dividend information for which a provisional dividend rate is specified. | Dividend | ProvisionalDividend |
| RateAndAmount | SolicitationFeeCorporateActionParameters | NaN | Corporate event for which a solicitation fee is specified. | CorporateActionFeesAndCharges | SolicitationFee |
| RateAndAmount | Rate | NaN | Value expressed as a rate. | PercentageRate | NaN |
| RateAndAmount | RateBiddingConditions | NaN | Bidding conditions for which a rate is specified. | BiddingConditions | ApplicableRate |
| RateAndAmount | SecuritiesTax | NaN | Tax for which a percentage of the gross dividend rate is specified. | SecuritiesTax | RelatedTax |
| RateAndAmount | EarlySolicitationFeeCorporateActionParameters | NaN | Corporate event for which an early solicitation fee is specified. | CorporateActionFeesAndCharges | EarlySolicitationFeeRate |
| RateAndAmount | InterestRelatedIssuance | NaN | Issuance for which an interest shortfall has been specified. | Issuance | InterestShortfall |
| RateAndAmount | LossRelatedIssuance | NaN | Issuance for which a realised loss has been specified. | Issuance | RealisedLoss |
| RateAndAmount | AbsoluteValue | NaN | Absolute value determined with a number. | Number | NaN |
| RateAndAmount | Operator | NaN | Provides the relationship between a variable and a fixed value. | OperatorCode | NaN |
| RateAndAmount | RelatedYieldCalculation | NaN | Yield calculation which uses a yield range. | YieldCalculation | YieldRange |
| RateAndAmount | ConduitForeignIncomeAmountDividendParameters | NaN | Dividend information for which a conduit foreign income amount is specified. | Dividend | ConduitForeignIncomeAmount |
| RateAndAmount | DeemedAmountDividendParameters | NaN | Dividend information for which a deemed amount is specified. | Dividend | DeemedAmount |
| CashProceedsDefinition | NaN | ProceedsDefinition | Definition of the cash proceeds for a corporate action in generic terms; that is, before applying it to specific securities holding. An example would be the definition of a dividend payment where all the information will be given in general on a per share basis. | NaN | NaN |
| CashProceedsDefinition | CashIncentiveRate | NaN | Cash premium made available if the securities holder consents or participates to an event, e.g. consent fees. | PercentageRate | NaN |
| CashProceedsDefinition | ContractualPaymentIndicator | NaN | Indicates exceptions to contractual payment service. | PaymentCode | NaN |
| CashProceedsDefinition | IncomeType | NaN | Specifies the type of income. The lists of income type codes to be used, are available on the SMPG website at www.smpg.info. | GenericIdentification | IdentificationForCashProceedsIncome |
| CashProceedsDefinition | IndemnityAmount | NaN | (Unique to France) Amount due to a buyer of securities dealt prior to ex date which may be subject to different rate of taxation. | CurrencyAndAmount | NaN |
| CashProceedsDefinition | CashIncentiveAmount | NaN | Rate of the cash premium made available if the securities holder consents or participates to an event, e.g. consent fees. | ActiveCurrencyAndAmount | NaN |
| CashProceedsDefinition | PrincipalOrCorpus | NaN | Amount of money representing a distribution of a bond's principal, eg, repayment of outstanding debt. | CurrencyAndAmount | NaN |
| CashProceedsDefinition | RedemptionPremiumAmount | NaN | Amount of money (not interest) in addition to the principal at the redemption of a bond. | CurrencyAndAmount | NaN |
| CashProceedsDefinition | IncomePortion | NaN | Amount relating to the underlying security for which income is distributed. | CurrencyAndAmount | NaN |
| CashProceedsDefinition | Interest | NaN | Interest paid as the proceeds of a CA event. | Interest | RelatedCashProceedsDefinition |
| CashProceedsDefinition | Amount | NaN | Cash amount which is posted. | CurrencyAndAmount | NaN |
| CashProceedsDefinition | Dividend | NaN | Distribution of earnings to shareholders, paid for in cash, stock, scrip issue or, rarely, in kind, eg, company products or property. The dividend amount is decided by the board of directors. | Dividend | CashProceeds |
| CashProceedsDefinition | PaymentCurrency | NaN | Currency for the payment of the cash proceeds. | CurrencyCode | NaN |
| CashProceedsDefinition | StatusCashAmount | NaN | Amount of cash subscribed that has been assigned the status indicated. | CurrencyAndAmount | NaN |
| CorporateActionDistribution | NaN | NaN | Distribution of the proceeds of a CA event. | NaN | NaN |
| CorporateActionDistribution | PostingQuantity | NaN | Quantity of securities that have been posted (credit or debit) to the account. | SecuritiesQuantity | CorporateActionDistribution |
| CorporateActionDistribution | PostingDateTime | NaN | Date of the posting (credit or debit) to the account. | ISODateTime | NaN |
| CorporateActionDistribution | MovementDate | NaN | Date/time at which the movement is due to take place (cash and/or securities). | ISODate | NaN |
| CorporateActionDistribution | PostingAmount | NaN | Amount of money that is to be/was posted to the account. | CurrencyAndAmount | NaN |
| CorporateActionDistribution | TaxVoucher | NaN | Specifies tax vouchers in the framework of a corporate action event. | TaxVoucher | Distribution |
| CorporateActionDistribution | RelatedServicing | NaN | Process which groups the activities related to corporate action servicing. | CorporateActionServicing | CorporateActionDistribution |
| CorporateActionDistribution | OrderType | NaN | Type of movement instruction. | DistributionTypeCode | NaN |
| CorporateActionDistribution | MovementType | NaN | Type of movement. | DistributionInstructionTypeCode | NaN |
| CorporateActionDistribution | HighPriorityIndicator | NaN | Indicates whether the movement is a high priority or not. Meaning when true: High priority Meaning when false: Standard | YesNoIndicator | NaN |
| CorporateActionDistribution | RequestedExecutionDate | NaN | Date at which the distribution movement must be executed. | ISODate | NaN |
| CorporateActionDistribution | FractionTreatment | NaN | Specifies the rounding direction. | RoundingDirectionCode | NaN |
| CorporateActionDistribution | CreditDebitIndicator | NaN | Specifies whether the posting amount is a debit or credit. | DebitCreditCode | NaN |
| CorporateActionDistribution | Option | NaN | Option on which the distribution is based. | CorporateActionOption | Distribution |
| CorporateActionDistribution | NetAmount | NaN | Cash amount after any deductions and allowances have been made | CurrencyAndAmount | NaN |
| CorporateActionDistribution | GrossAmount | NaN | Cash amount before any deductions and allowances have been made. | CurrencyAndAmount | NaN |
| CorporateActionDistribution | FinancialTransaction | NaN | Financial transaction to which the CA distribution belongs. | FinancialTransaction | CorporateActionDistribution |
| CorporateActionDistribution | CorporateActionProceedsDeliveryInstruction | NaN | Specifies the delivery instructions for the securities and cash proceeds at any stage of the Corporate Action process. | CorporateActionProceedsDeliveryInstruction | RelatedDistribution |
| QuantityRatio | NaN | NaN | Ratio expressed as a quotient of quantities. | NaN | NaN |
| QuantityRatio | AdditionalQuantityForResultantSecuritiesProceedsDefinition | NaN | Securities proceeds for which an additional quantity for subscribed resultant securities is specified. | SecuritiesProceedsDefinition | AdditionalQuantityForSubscribedResultantSecurities |
| QuantityRatio | Quantity1 | NaN | Numerator of the quotient of quantities. | DecimalNumber | NaN |
| QuantityRatio | Quantity2 | NaN | Denominator of the quotient of quantities. | DecimalNumber | NaN |
| QuantityRatio | AdditionalQuantityForSubscribedSecuritiesProceedsDefinition | NaN | Securities proceeds for which an additional quantity for existing securities is specified. | SecuritiesProceedsDefinition | AdditionalQuantityForExistingSecurities |
| QuantityRatio | NewToOldProceedsDefinition | NaN | Securities procceds for which a nwe to old ratio is specified. | SecuritiesProceedsDefinition | NewToOld |
| QuantityRatio | NewToUnderlyingProceedsDefinition | NaN | Securities proceeds for which a new to underlying ratio is specified. | SecuritiesProceedsDefinition | NewSecuritiesToUnderlyingSecurities |
| QuantityRatio | IntermediateSecuritiesProceedsDefinition | NaN | Securities proceeds for which a quantity of intermediate securities is specified. | SecuritiesProceedsDefinition | IntermediateSecuritiesToUnderlyingRatio |
| QuantityRatio | Warrant | NaN | Provides the warrant for the related quantity or the underlying quantity. | Warrant | WarrantParity |
| CorporateActionCashEntitlement | NaN | CorporateActionEntitlement | Rights for cash entitled to the account owner based on the terms of the corporate action event and the balance of underlying securities. | NaN | NaN |
| CorporateActionCashEntitlement | GrossCashAmount | NaN | Amount of money before any deductions and allowances have been made. | CurrencyAndAmount | NaN |
| CorporateActionCashEntitlement | NetCashAmount | NaN | Amount of money after deductions and allowances have been made, if any, ie, the total amount +/- charges/fees. | CurrencyAndAmount | NaN |
| CorporateActionCashEntitlement | CashInLieuOfShare | NaN | Cash disbursement in lieu of a fractional quantity of, eg, equity. | CurrencyAndAmount | NaN |
| CorporateActionCashEntitlement | CapitalGain | NaN | Amount of money distributed as the result of a capital gain. | CurrencyAndAmount | NaN |
| CorporateActionCashEntitlement | EntitledCashAmount | NaN | Cash amount based on terms of corporate action event and balance of underlying securities, entitled to/from account owner (which may be positive or negative). | CurrencyAndAmount | NaN |
| CorporateActionCashEntitlement | ExchangeRate | NaN | Specifies the exchange rate used to convert the cash entitlement value in another currency. | CurrencyExchange | CurrencyExchangeForCorporateActionCashEntitlement |
| MarketClaim | NaN | NaN | Processes that reallocate corporate action proceeds to the entitled party and that compensate financial penalties or indirect costs due to late delivery or payment. | NaN | NaN |
| MarketClaim | MarketClaimAmount | NaN | Amount of money resulting from a market claim. | CurrencyAndAmount | NaN |
| MarketClaim | MarketClaimTrackingEndDate | NaN | Date by which the depository stops monitoring activities of the event, for instance, accounting and tracking activities for due bills end. | ISODateTime | NaN |
| MarketClaim | RelatedCorporateEvent | NaN | Corporate event for which market claim information is provided. | CorporateActionEvent | MarketClaim |
| FixingCondition | NaN | NaN | Set of parameters used to calculate a rate for instance the fixing rate to be applied to a non-deliverable agreement. | NaN | NaN |
| FixingCondition | FixingDateTime | NaN | Date and time at which a rate is observed. | ISODateTime | NaN |
| FixingCondition | NonDeliverableTrade | NaN | Non Deliverable trade for which fixing conditions are specified. | NonDeliverableTrade | FixingConditions |
| FixingCondition | FixingRate | NaN | Rate obtained at fixing time by following the fixing conditions (agreed upon by the trading parties). | CurrencyExchange | FixingConditions |
| FixingCondition | SettlementRateOption | NaN | Source used for determining the fixing rate, as provided by various financial publishing organisations. | Max35Text | NaN |
| FixingCondition | FinancialCenter | NaN | Financial place taken into account to adjust the date and time, as defined within the business day convention. | FinancialCenterCode | NaN |
| FixingCondition | DisruptionFallback | NaN | Method that gives rise to either an alternative basis for determining the settlement rate, or an alternative basis for settling a transaction when a disruption event has occurred. | DisruptionFallbackCode | NaN |
| FixingCondition | BusinessDayConvention | NaN | Convention used for adjusting a date when it is not a business day. | BusinessDayConventionCode | NaN |
| Equalisation | NaN | NaN | Part of an investor's subscription amount that is held by the fund in order to pay incentive / performance fees at the end of the fiscal year. | NaN | NaN |
| Equalisation | Amount | NaN | Amount of money resulting from the calculation of the equalisation. | CurrencyAndAmount | NaN |
| Equalisation | Date | NaN | Date on which all or part of any holding bought in a unit trust is subject to being treated as capital rather than income. This is normally one day after the previous distribution's ex date. | ISODateTime | NaN |
| Equalisation | Rate | NaN | Rate used for calculation of the equalisation. | PercentageRate | NaN |
| Equalisation | RelatedInvestmentFundTransaction | NaN | Investment fund transaction for which equalisation is specified. | InvestmentFundClass | Equalisation |
| Equalisation | CreditDebitIndicator | NaN | Debit for a negative amount or credit for a positive amount. | DebitCreditCode | NaN |
| Equalisation | DepreciationDepositPerUnit | NaN | <p>Performance fee to be paid by the investor when the net asset value reaches the high-watermark if the net asset value was under the high-watermark on subscription date.</p> | ActiveOrHistoricCurrencyAndAmount | NaN |
| Equalisation | CreditPerUnit | NaN | <p>Prepayment amount to be paid by the investor at the moment of the subscription. The amount is based on the positive difference between the gross asset value at subscription and the high-watermark, when the investment fund units are subscribed to above their high-watermark.</p> | ActiveOrHistoricCurrencyAndAmount | NaN |
| Equalisation | MethodologyType | NaN | <p>Methodology used for the allocation of the performance fees.</p> | EqualisationMethodologyTypeCode | NaN |
| Equalisation | HighWatermark | NaN | <p>The highest net asset value at the end of any previous calculation period, when a performance fee was payable (after the deduction of any such performance fee); or the initial net asset value.</p> | ActiveOrHistoricCurrencyAndAmount | NaN |
| Equalisation | GrossAssetValue | NaN | <p>Value of the investment fund on subscription date before accruals for performance fees.</p> | ActiveOrHistoricCurrencyAndAmount | NaN |
| Equalisation | ContingentLiquidationPerUnit | NaN | <p>Performance fee to be paid by the investor when the value of the investment fund units were below their applicable high-watermark on subscription date, and above the high-watermark on redemption date. </p> | ActiveOrHistoricCurrencyAndAmount | NaN |
| SuspensionPeriod | NaN | NaN | Period defining the last date for which an action will be accepted and the date on which the suspension will be released and normal processing will resume. | NaN | NaN |
| SuspensionPeriod | PrivilegeSuspensionPeriod | NaN | Period during which the privilege is not available, eg, this can happen whenever a meeting takes place or whenever a coupon payment is due. | DateTimePeriod | PrivilegeSuspensionCorporateAction |
| SuspensionPeriod | DepositorySuspensionPeriodForWithdrawal | NaN | Period defining the last date on which withdrawal in street name requests on the outturn security will be accepted and the date on which the suspension will be released and withdrawal by transfer processing on the outturn security will resume. | DateTimePeriod | WithdrawalSuspensionRelatedEvent |
| SuspensionPeriod | DepositorySuspensionPeriodForBookEntryTransfer | NaN | Period defining the last date for which book entry transfers will be accepted and the date on which the suspension will be released and book entry transfer processing will resume. | DateTimePeriod | BookEntryTransferSuspensionRelatedEvent |
| SuspensionPeriod | DepositorySuspensionPeriodForDepositAtAgent | NaN | Period defining the last date for which deposits, into nominee name, at the agent will be accepted and the date on which the suspension will be released and deposits at agent will resume. | DateTimePeriod | DepositAtAgentSuspensionRelatedEvent |
| SuspensionPeriod | DepositorySuspensionPeriodForDeposit | NaN | Period defining the last date for which deposits will be accepted and the date on which the suspension will be released and deposits will resume. | DateTimePeriod | DepositSuspensionRelatedEvent |
| SuspensionPeriod | DepositorySuspensionPeriodForPledge | NaN | Period defining the last date for which pledges will be accepted and the date on which the suspension will be released and pledge processing will resume. | DateTimePeriod | PledgeSuspensionRelatedEvent |
| SuspensionPeriod | DepositorySuspensionPeriodForSegregation | NaN | Period defining the last date for which intra-position balances can be segregated and the date on which the suspension will be released and the ability to segregate intra-position balances will resume. | DateTimePeriod | SegregationPeriodRelatedEvent |
| SuspensionPeriod | DepositorySuspensionPeriodForWithdrawalAtAgent | NaN | Period defining the last date for which withdrawals, from nominee name at the agent will be accepted and the date on which the suspension will be released and withdrawals at agent processing will resume. | DateTimePeriod | WithdrawalAtAgentSuspensionRelatedEvent |
| SuspensionPeriod | DepositorySuspensionPeriodForWithdrawalInNomineeName | NaN | Period defining the last date for which physical withdrawals in the nominee's name will be accepted and the date on which the suspension will be released and physical withdrawals in the nominee's name will resume. | DateTimePeriod | WithdrawalInNomineeNameSuspensionRelatedEvent |
| SuspensionPeriod | DepositorySuspensionPeriodForWithdrawalInStreetName | NaN | Period defining the last date on which withdrawal requests in street name's will be accepted on the event security and the date on which the suspension will be released and withdrawal in street name's processing on the event security will resume. | DateTimePeriod | WithdrawalInStreetNameSuspensionRelatedEvent |
| SuspensionPeriod | CoDepositoriesSuspensionPeriod | NaN | Period during which the settlement activities at the co-depositories are suspended in order to stabilise the holdings at the CSD. | DateTimePeriod | CoDepositoriesSuspensionRelatedEvent |
| SuspensionPeriod | CorporateActionEvent | NaN | Corporate action event for which a depository suspension period is specified. | CorporateActionEvent | SuspensionPeriod |
| CorporateActionSecuritiesEntitlement | NaN | CorporateActionEntitlement | Rights for securities entitled to the account owner based on the terms of the corporate action event and the balance of underlying securities. | NaN | NaN |
| CorporateActionSecuritiesEntitlement | EntitledSecuritiesQuantity | NaN | Quantity of securities based on the terms of the corporate action event and balance of underlying securities entitled to the account owner. (This quantity can be positive or negative). | SecuritiesQuantity | SecuritiesEntitlement |
| CorporateActionSecuritiesEntitlement | RenounceableEntitlementStatusType | NaN | Specifies whether terms of the event allow resale of the rights. | RenounceableStatusCode | NaN |
| Lottery | NaN | NaN | The parameters required to manage the organisation of a lottery. | NaN | NaN |
| Lottery | LotteryDate | NaN | Date on which the lottery is run and applied to the holder's positions. This is also applicable to partial calls. | ISODateTime | NaN |
| Lottery | IncrementalDenomination | NaN | Amount used when the called amount is not met by running the lottery with the base denomination. | SecuritiesQuantity | Lottery |
| Lottery | LotteryType | NaN | Specifies the type of lottery announced. | LotteryTypeCode | NaN |
| Lottery | RelatedCorporateEvent | NaN | Corporate event for which lottery information is provided. | CorporateActionEvent | Lottery |
| Meeting | NaN | NaN | Specifies the physical parameters of a general meeting. Several dates and places can be defined for a meeting. | NaN | NaN |
| Meeting | DateAndTime | NaN | Date and time at which the meeting will take place. | ISODateTime | NaN |
| Meeting | DateStatus | NaN | Indicates the status of a meeting date. | MeetingDateStatusCode | NaN |
| Meeting | MeetingLocation | NaN | Place of the company meeting for the scheduled meeting date. | ContactPoint | ContactPointForMeeting |
| Meeting | Identification | NaN | Identification assigned to a general meeting by the party notifying the meeting. It must be unique for the party notifying the meeting. | Max35Text | NaN |
| Meeting | Deadline | NaN | Specifies the different deadlines available for the different processes related to meeting attendance, proxy voting and entitlement assessment. | Deadline | RelatedMeeting |
| Meeting | MeetingServicing | NaN | Servicing processes related to the organisation of a meeting. | MeetingServicing | MeetingSpecification |
| Meeting | Person | NaN | Specifies the person who is the contact for a meeting. | ContactPersonRole | Meeting |
| Meeting | PartyRole | NaN | Specifies the role played by a party in the context of a meeting. | MeetingPartyRole | Meeting |
| Meeting | Status | NaN | Status of the imeeting and of the related nstructions. | MeetingStatus | Meeting |
| Meeting | CorporateEvent | NaN | Corporate event for which a meeting is organised. | CorporateActionEvent | RelatedMeeting |
| Meeting | Quorum | NaN | Specifies whether a quorum is required or not together with the quorum parameters. | Quorum | Meeting |
| Meeting | VotingCondition | NaN | Specifies the different voting types, channels and premium. | VotingCondition | Meeting |
| Meeting | AttendanceRequired | NaN | Indicates whether physical participation to a meeting is required in order to be allowed to vote. | YesNoIndicator | NaN |
| Meeting | AttendanceConfirmation | NaN | Indicates how to order the attendance card or to give notice of attendance. | Max350Text | NaN |
| Meeting | IncentivePremium | NaN | Cash premium made available to encourage participation by a certain deadline (avoids to have a second call). | IncentivePremium | Meeting |
| Meeting | Participation | NaN | Potential participation to the voting process. | MeetingParticipation | Meeting |
| Meeting | ResolutionProposalConditions | NaN | Specifies the conditions to fulfill in order to be able to propose a resolution. | ResolutionProposal | Meeting |
| Meeting | AgendaItem | NaN | Item proposed for the vote or presented for information only. | Resolution | Meeting |
| Meeting | ProxyAppointmentConditions | NaN | Information on how to appoint proxy. | ProxyAppointmentCondition | Meeting |
| Meeting | AdditionalRight | NaN | Specifies how the additional rights can be granted to the shareholder. These rights can be exercised at shareholders meetings (for example, the right to ask questions, the right to add items to the agenda or table draft resolutions). | AdditionalRight | Meeting |
| Meeting | Type | NaN | Specifies the type of meeting for which an invitation is sent. | MeetingTypeCode | NaN |
| Meeting | PowerOfAttorneyRequirements | NaN | Specifies the conditions to be filled in to obtain a valid power of attorney. | PowerOfAttorneyRequirements | Meeting |
| Meeting | MeetingEventClassification | NaN | Classifies the meeting. | MeetingTypeClassificationCode | NaN |
| Meeting | AttendanceAdmissionConditions | NaN | Conditions for physical admittance to general meeting. | AttendanceAdmissionConditionsCode | NaN |
| SecuritiesBlockingDeadline | NaN | Deadline | Date by which the securities should be blocked. | NaN | NaN |
| SecuritiesBlockingDeadline | BlockingPeriod | NaN | Period during which the securities are blocked, ie, not available for exchange. | NaN | NaN |
| Spread | NaN | NaN | Margin over or under an index which determines a rate. | NaN | NaN |
| Spread | BenchmarkSecurity | NaN | Security used as a reference to express the value of another security. | Security | Spread |
| Spread | SecuritiesFinancing | NaN | Securities financing process for which a repurchase spread is specified. | SecuritiesFinancing | RepurchaseSpread |
| Spread | SpreadRate | NaN | Margin over or under an index which determines the interest rate of an interest bearing instrument. | PercentageRate | NaN |
| Spread | BasisPointSpread | NaN | Specifies the number of points to be added or substracted to the rate. | Number | NaN |
| Spread | Index | NaN | Index for which a spread is specified. | Index | Spread |
| Spread | BenchmarkPrice | NaN | Identifies the price of the benchmark security. | SecuritiesPricing | Spread |
| Spread | RelatedIndicationOfInterest | NaN | Indication of interest process for which a spread to benchmark is specified. | BuyOrSellIndicationOfInterest | SpreadToBenchmark |
| Spread | IndicationOfInterest | NaN | Indication of interest process for which a spread is specified. | BuyOrSellIndicationOfInterest | SwapSpread |
| Spread | RelatedInterest | NaN | Interest calculation process for which a spread is provided. | InterestCalculation | Spread |
| Spread | BenchmarkCurve | NaN | Describes a benchmark curve. | Curve | Spread |
| Spread | PriceOffset | NaN | Either a swap spread or spread to benchmark depending upon order type. In case of a spread to benchmark, the price offset is expressed in terms of basis points relative to a benchmark - this can be a positive or a negative spread. In case of a swap spread, the price offset is target spread for a swap. | DecimalNumber | NaN |
| IntraPositionTransfer | NaN | SecuritiesTransfer | Transfer of securities from one sub-balance to another or from one balance status to another. | NaN | NaN |
| IntraPositionTransfer | Reservation | NaN | Quantity of securities set aside by a party for specific purpose. | Reservation | RelatedIntraPositionTransfer |
| IntraPositionTransfer | CollateralAmount | NaN | Value of the collateral available for the delivery settlement process. | CurrencyAndAmount | NaN |
| IntraPositionTransfer | SecuritiesBalance | NaN | Specifies the securities balance or sub-balance from/to which the securities are transferred. | SecuritiesBalance | RelatedIntraPositionTransfer |
| SourceOfPrice | NaN | InformationPartyRole | Place from which the price was obtained. | NaN | NaN |
| SourceOfPrice | MarketIdentification | NaN | Market on which this price is valid (MIC - ISO 3166). | TradingMarket | SourceOfPrice |
| SourceOfPrice | Type | NaN | Specifies the type of the source of the price. | PriceSourceCode | NaN |
| HaircutValuation | NaN | NaN | Basic valuation details of an asset's market value. | NaN | NaN |
| HaircutValuation | AssetHolding | NaN | Asset holding for which a haircut is specified. | AssetHolding | Haircut |
| HaircutValuation | Haircut | NaN | Haircut or valuation factor on the security expressed as a percentage. | PercentageRate | NaN |
| HaircutValuation | Sign | NaN | One of the following PlusOrMinusIndicator values must be used: MeaningWhenTrue: Plus (the haircut is added) MeaningWhenFalse: Minus (the haircut is deducted) | PlusOrMinusIndicator | NaN |
| HaircutValuation | PartyRole | NaN | Specifies the role of a party in the haircut valuation process. | InformationPartyRole | HaircutValuation |
| SecuritiesOrder | NaN | Order | Intention to transfer an ownership of a financial instrument. | NaN | NaN |
| SecuritiesOrder | OrderEffectiveDate | NaN | Date/time on which the order is effective. | ISODateTime | NaN |
| SecuritiesOrder | OrderExpiryDate | NaN | Date/time on which the order is to expire. | ISODateTime | NaN |
| SecuritiesOrder | Identification | NaN | Unique identifier for an order, as assigned by the sell-side. The identifier must be unique within a single trading day. | Max35Text | NaN |
| SecuritiesOrder | CashMargin | NaN | Identifies whether an order is a margin order or a non-margin order. This is primarily used when sending orders to Japanese exchanges to indicate sell margin or buy to cover. The same tag could be assigned also by buy-side to indicate the intent to sell or buy margin and the sell-side to accept or reject (base on some validation criteria) the margin request. | CashMarginOrderCode | NaN |
| SecuritiesOrder | Side | NaN | Coded list to specify the side of the order. | SideCode | NaN |
| SecuritiesOrder | SolicitedOrder | NaN | Indicates that an order has been generated in response to an advertisement or an indication of interest. | YesNoIndicator | NaN |
| SecuritiesOrder | CustomerCapacity | NaN | Capacity of customer placing the order. Primarily used by futures exchanges to indicate the CTI code (customer type indicator) as required by the US CFTC (Commodity Futures Trading Commission). | CustomerOrderCapacityCode | NaN |
| SecuritiesOrder | PositionEffect | NaN | Indicates whether the resulting position after a trade should be an opening position or closing position. Used for omnibus accounting - where accounts are held on a gross basis instead of being netted together. | PositionEffectCode | NaN |
| SecuritiesOrder | ForeignExchangeExecutionRequested | NaN | Indicates a request for a foreign exchange accommodation trade to be executed along with security transaction. | YesNoIndicator | NaN |
| SecuritiesOrder | SettlementCurrency | NaN | Currency to be used for settlement. | CurrencyCode | NaN |
| SecuritiesOrder | OrderOriginatorEligibility | NaN | Counterparties eligibility as defined by article 24 of the EU MiFID Directive applicable to transactions executed by investment firms for eligible counterparties. | EligibilityCode | NaN |
| SecuritiesOrder | OrderedQuantity | NaN | Quantity of financial instrument to be ordered. | SecuritiesQuantity | RelatedOrder |
| SecuritiesOrder | BusinessProcessType | NaN | Type of business process model used to carry out the transaction. | BusinessProcessTypeCode | NaN |
| SecuritiesOrder | PlaceOfTrade | NaN | Market at which the order is to be traded. | TradingMarket | RelatedOrder |
| SecuritiesOrder | OrderedAmount | NaN | Cash amount to be used to derive the appropriate quantity of financial instrument to be bought or sold. | CurrencyAndAmount | NaN |
| SecuritiesOrder | GiveUpNumberOfDays | NaN | Specifies the number of days from trade date that the counterparty on the other side of the trade should be "given up" or divulged. | Max3Number | NaN |
| SecuritiesOrder | TradeRegulatoryConditionsType | NaN | Specifies the regulatory conditions type of the trade. | TradeRegulatoryConditionsCode | NaN |
| SecuritiesOrder | DayOrderQuantity | NaN | For good till orders, the order quantity less all quantity (adjusted for stock splits) that traded on previous days. | SecuritiesQuantity | PreviousDayOrder |
| SecuritiesOrder | SecuritiesOrderPartyRole | NaN | Specifies the party which plays a role in the process of ordering securities. | SecuritiesOrderPartyRole | SecuritiesOrder |
| SecuritiesOrder | Status | NaN | Indicates the status of an order at a specific point in time. | SecuritiesOrderStatus | SecuritiesOrder |
| SecuritiesOrder | RelatedNegotiation | NaN | Negotiation which resulted in an order. | Negotiation | SecuritiesOrder |
| SecuritiesOrder | Adjustments | NaN | Charges and commissions associated with a securities order. | Adjustment | SecuritiesOrder |
| SecuritiesOrder | LegalParameters | NaN | Legal parameters required in a securities order for regulatory purposes. | SecuritiesRegulatoryDetails | RelatedOrder |
| SecuritiesOrder | OrderPrice | NaN | Indicates the requested price for the order. This can be a "stop" price a "limit" price or a "deal" price. | SecuritiesPricing | Order |
| SecuritiesOrder | StopPrice | NaN | Indicates the stop price in case of a stop order or a stop limit order. | SecuritiesPricing | StopPriceOrder |
| SecuritiesOrder | SecuritiesOrderAllocation | NaN | Information about the pre-allocation of an order. | Allocation | SecuritiesOrder |
| SecuritiesOrder | OrderExecutionParameters | NaN | Conditions under which a securities order must be executed. | SecuritiesOrderParameters | RelatedSecuritiesOrder |
| SecuritiesOrder | OrderExecution | NaN | Result of a securities order. | SecuritiesTrade | RelatedOrder |
| SecuritiesOrder | OrderingAccount | NaN | Account impacted by a security transaction. | SecuritiesAccount | RelatedOrder |
| SecuritiesOrder | Quote | NaN | Quote for which the order conditions are specified. | SecuritiesQuoteVariable | SecuritiesOrder |
| SecuritiesOrder | FundTransactionDirectionIndicator | NaN | Indicates the type of investment funds transaction. | InvestmentFundTransactionTypeCode | NaN |
| SecuritiesOrder | OrderDate | NaN | Date/time on which the order was placed by the investor with the trading party. | ISODateTime | NaN |
| SecuritiesOrder | PegDifference | NaN | Price difference for a pegged order. | CurrencyAndAmount | NaN |
| SecuritiesOrder | SecuritiesOrderTradingSession | NaN | Details of a specific trading session associated with a securities order. | TradingSession | SecuritiesOrder |
| SecuritiesOrder | RelatedOrderBook | NaN | Order book whichgenerates an order. | OrderBook | Order |
| SecuritiesOrder | ListTrading | NaN | List trading information containing a serie of orders. | ListTrading | SecuritiesListOrder |
| SecuritiesOrder | BuySideRelatedCrossTrade | NaN | Cross trade for which the buy side information is provided. | CrossTrade | BuySideOrder |
| SecuritiesOrder | SellSideRelatedCrossTrade | NaN | Cross trade for which the sell side information is provided. | CrossTrade | SellSideOrder |
| SecuritiesOrder | OrderedSecurity | NaN | Security for which an order is specified. | Security | SecuritiesOrder |
| SecuritiesOrder | BookingInstructions | NaN | Information about the booking of executions. | SecuritiesPostTradeBooking | RelatedOrder |
| SecuritiesOrder | ExchangeForPhysicalTrade | NaN | Conditions under which an exchange for physical trade takes place in the case of a non disclosed bid. | ExchangeForPhysicalTrade | SecuritiesOrder |
| SecuritiesOrder | QuantityType | NaN | Describes how the quantity is specified, that is by quantity of units or by amount of money. | OrderQuantityTypeCode | NaN |
| SecuritiesOrder | ClientOrderIdentification | NaN | Unique identifier for the order as assigned by the buy-side. Uniqueness must be guaranteed within a single trading day. Firms, particularly those that electronically submit multi-day orders, trade globally or throughout market close periods, should ensure uniqueness across days, for example by embedding a date within the ClientOrderIdentification element. | Max35Text | NaN |
| SecuritiesOrder | ExecutionInstructions | NaN | Execution instructions in which securities order parameters are defined. | SecuritiesOrderExecutionInstruction | RelatedOrder |
| SecuritiesOrder | Type | NaN | Indicates the type of instruction to a broker or dealer to buy or sell a financial instrument. | OrderTypeCode | NaN |
| SecuritiesOrder | LiquidityProvisionActivity | NaN | Indicates whether an order is submitted to a trading venue as part of a market making strategy. USAGE: when absent, default value is false. | TrueFalseIndicator | NaN |
| SecuritiesOrder | EventType | NaN | Events affecting the orders in financial instruments. | EventTypeCode | NaN |
| SecuritiesOrder | PegPrice | NaN | The maximum price at which a pegged order to buy can trade or the minimum price at which a pegged order to sell can trade. | NaN | NaN |
| SecuritiesOrder | LimitPrice | NaN | The maximum price at which a buy order can trade or the minimum price at which a sell order can trade. | NaN | NaN |
| ListTrading | NaN | NaN | Provides the details for negotiating and trading a large number of securities contained in or comprising a portfolio. One example is index arbitrage, which consists in the purchase or sale of a basket of stocks in conjunction with the sale or purchase of a derivative product (for example index futures) to profit from price differences between the basket and the derivative product. Other examples include liquidation of EFP (Exchange for Physical) stock positions, portfolio realignment and portfolio liquidation. | NaN | NaN |
| ListTrading | ListIdentification | NaN | Unique identifier for a list, as assigned by the trading party. The identifier must be unique within a single trading day. | Max35Text | NaN |
| ListTrading | SecuritiesListOrder | NaN | Order list containing the details of the individual orders within the program. | SecuritiesOrder | ListTrading |
| ListTrading | ListTradingSession | NaN | Details of a specific trading session for a list trading. | TradingSession | ListTrading |
| ListTrading | ListName | NaN | Provides the name of the order list. | Max140Text | NaN |
| ListTrading | BasisPriceType | NaN | Represents the basis price type in a bid order (list trading). | BasisPriceTypeCode | NaN |
| ListTrading | StrikeTime | NaN | Time at which current market prices are used to determine the value of a basket. | ISODateTime | NaN |
| ListTrading | GrossAmountIndicator | NaN | Indicates whether an amount is a gross amount (including all charges, commissions and tax), or a net amount. | YesNoIndicator | NaN |
| ListTrading | SellSideIdentification | NaN | Unique identifier for a bid, as assigned by the the sell-side (broker, exchange, electronic communication network (ECN)). The identifier must be unique within a single trading day. | Max35Text | NaN |
| ListTrading | BuySideIdentification | NaN | Unique identifier for a bid, as assigned by the buy-side institution. The identifier must be unique within a single trading day. | Max35Text | NaN |
| ListTrading | Liquidity | NaN | Information on the liquidity of a financial instrument. | Liquidity | ListTrading |
| ListTrading | BidType | NaN | Indicates the type of bid for a list order. | BidTypeCode | NaN |
| Clearing | NaN | ObligationFulfilment | Mechanism allowing financial institutions that are members of a clearing house to pay and to receive the amounts linked to the transactions that they have executed on the market. The addition of all the positions per product results in one net position (due or to receive) with the clearing house or the central clearing counterparty. | NaN | NaN |
| Clearing | ClearingThresholdIndicator | NaN | Specifies whether the contract is above or below the clearing threshold. Where N indicates the contract is below the clearing threshold and Y indicates the contract is above the clearing threshold. | YesNoIndicator | NaN |
| Clearing | ClearedIdentification | NaN | Reference number assigned by the Central Counterparty (CCP). | Max35Text | NaN |
| Clearing | GuaranteedTrade | NaN | Indicates if the central counterparty has to novate and guarantee the trade or not. | YesNoIndicator | NaN |
| Clearing | TradePostingType | NaN | Indicates how a trade is maintained in the clearing account. | TradePostingCode | NaN |
| Clearing | ClearingSystem | NaN | Specifies the system which plays a role in the clearing of securities or cash. | ClearingSystem | Clearing |
| SecuritiesTradePartyRole | NaN | TradePartyRole | Role played by a party in the context of a securities trade. | NaN | NaN |
| SecuritiesTradePartyRole | SecuritiesTrade | NaN | Specifies the trade in which a party plays a role. | SecuritiesTrade | PartyRole |
| AffirmingPartyRole | NaN | SecuritiesTradePartyRole | Party (buyer or seller) that positively affirms the details of a previously agreed security trade confirmation. | NaN | NaN |
| BuyerRole | NaN | TradePartyRole | Party that buys assets, good or services. | NaN | NaN |
| Borrower | NaN | TradePartyRole | Party that has applied, met specific requirements, and received a monetary or securities loan from a lender. | NaN | NaN |
| SellerRole | NaN | TradePartyRole | Party that sells assets, goods or services. | NaN | NaN |
| Lender | NaN | TradePartyRole | Party that has accepted under specific requirements to provide a monetary or securities loan to a borrower. | NaN | NaN |
| TradingSession | NaN | NaN | Established constraints under which a market operates | NaN | NaN |
| TradingSession | TradingSessionName | NaN | Identification of a specific execution time bracket code through its trading session name or description. | Max140Text | NaN |
| TradingSession | TimeBracket | NaN | Specifies the time bracket of a trading session in actual date and time format. | DateTimePeriod | TradingSession |
| TradingSession | Market | NaN | Market for which trading session information is specified.. | TradingMarket | TradingSession |
| TradingSession | Quote | NaN | Quote to which a trading session is associated. | SecuritiesQuoteVariable | QuoteTradingSession |
| TradingSession | SecuritiesOrder | NaN | Securities order associated with a trading session. | SecuritiesOrder | SecuritiesOrderTradingSession |
| TradingSession | TradingSessionIndicator | NaN | Indicates the trading phase at the stock exchange, eg, opening auction phase, main trading phase, closing auction phase, etc. | TradingSessionCode | NaN |
| TradingSession | TradingSessionPhase | NaN | Specific execution time period expressed through its trading session identifier. This identifier is for example used by exchanges, electronic communication networks (ECNs) and alternative trading systems (ATSs) to identify opening and closing hours of a trading session. | TradeExecutionSessionCode | NaN |
| TradingSession | USFuturesTradingSession | NaN | Identification of a specific execution time bracket code, required by US regulations. This only applies to the US futures market. | Max140Text | NaN |
| TradingSession | ListTrading | NaN | List trading process for which a trading session is specified. | ListTrading | ListTradingSession |
| TradeRegulator | NaN | TradePartyRole | Institution to which a trade must be reported. | NaN | NaN |
| PrePaymentSpeed | NaN | NaN | Specifies the type and rate of prepayment speed of the fixed income instrument. | NaN | NaN |
| PrePaymentSpeed | Type | NaN | Specifies the type of prepayment speed of the fixed income instrument in coded form. | PrePaymentSpeedCode | NaN |
| PrePaymentSpeed | Rate | NaN | Rate of prepayment speed of the fixed income instrument. | PercentageRate | NaN |
| YieldCalculation | NaN | NaN | Characteristics related to the yield. | NaN | NaN |
| YieldCalculation | RedemptionPrice | NaN | Price on which the yield is computed. | SecuritiesPricing | YieldCalculation |
| YieldCalculation | Value | NaN | Result of the yield calculation. | PercentageRate | NaN |
| YieldCalculation | CalculationType | NaN | Specifies the type of calculation. | CalculationTypeCode | NaN |
| YieldCalculation | ValueDate | NaN | Date/time on which the calculation is based, for example, valuation on October 1 (price date) based on price of September 19 ( value date). | ISODateTime | NaN |
| YieldCalculation | ValuePeriod | NaN | Period on which the calculation is based. | DateTimePeriod | YieldCalculation |
| YieldCalculation | YieldCalculationDate | NaN | Clarifies the yield irregularities associated with the date to which the yield has been calculated, eg, when it falls on a non-business day. | ISODateTime | NaN |
| YieldCalculation | YieldRange | NaN | Range of allowed yield. | RateAndAmount | RelatedYieldCalculation |
| YieldCalculation | VariableInterest | NaN | Variable interest used for the calculation. | VariableInterest | YieldCalculation |
| FutureRule | NaN | NaN | Timing characteristics of the maturity of the future. | NaN | NaN |
| FutureRule | TimeType | NaN | Indicates whether the time to maturity is measured in months or years. | TimeUnitCode | NaN |
| FutureRule | RelatedFutureInstrument | NaN | Future instrument for which a rule is specified. | Future | FutureRule |
| FutureRule | MaximumTimeToMaturity | NaN | Maximum number of time types up to maturity or first redemption option. | Number | NaN |
| FutureRule | MinimumTimeToMaturity | NaN | Minimum number of time types up to maturity or first redemption option. | Number | NaN |
| FutureRule | BaseInterestRate | NaN | Nominal interest rate of synthetic bond. | PercentageRate | NaN |
| Rating | NaN | NaN | Assessment of securities credit and investment risk. | NaN | NaN |
| Rating | Security | NaN | Security for which a rating is provided. | Security | Rating |
| Rating | RatingScheme | NaN | Information regarding the entity that assigns the rating. | Scheme | Rating |
| Rating | ValueDate | NaN | Date/time as from which the rating is valid. | ISODateTime | NaN |
| Rating | Value | NaN | Specifies the rating, which has been assigned to a security by a rating agency. | RatingValueIdentifier | NaN |
| Leg | NaN | NaN | Separate transactions which combined together form a trade. | NaN | NaN |
| Leg | RelatedAsset | NaN | Asset for which leg information is provided. | Asset | LegAdditionalInformation |
| Leg | RatioQuantity | NaN | Only for multileg instrument - Ratio of quantity for an individual leg relative to the entire multileg security. | PercentageRate | NaN |
| Leg | Currency | NaN | Only for multileg instrument - Currency associated with a particular Leg's quantity. | CurrencyCode | NaN |
| Leg | SwapType | NaN | For Fixed Income, used instead of LegQty or LegOrderQty to requests the respondent to calculate the quantity based on the quantity on the opposite side of the swap. | Max35Text | NaN |
| Leg | Pool | NaN | For Fixed Income, identifies MBS / ABS pool for a specific leg of a multi-leg instrument. | Number | NaN |
| Leg | Trade | NaN | Trade which is composed of several legs. | Trade | Leg |
| Allocation | NaN | NaN | Distribution of the (block) trade (transactions) by the investor or investment manager to different underlying clients, ie, investment funds. | NaN | NaN |
| Allocation | Percentage | NaN | Percent of the securities quantity that this allocation represents. | PercentageRate | NaN |
| Allocation | AllocatedQuantity | NaN | Quantity of a specific security allocated from a block trade, based upon the distribution of the trade to different accounts. | SecuritiesQuantity | Allocation |
| Allocation | SettlementCurrency | NaN | Currency to be used for settlement of the allocation. | CurrencyCode | NaN |
| Allocation | AllocationAccount | NaN | Account to or from which an allocation must be made. | SecuritiesAccount | RelatedAllocation |
| Allocation | AllocatedPrice | NaN | Executed price used in an allocation. | SecuritiesPricing | Allocation |
| Allocation | AllocationAmount | NaN | Allocated quantity of security multiplied by the allocated price. | CurrencyAndAmount | NaN |
| Allocation | Method | NaN | Indicates the method of pre-allocation, that is the factors that are/were applied in the pre-allocation process. | RoundingDirectionCode | NaN |
| Allocation | AveragePricePrecision | NaN | Number of decimal places used for average pricing. | DecimalNumber | NaN |
| Allocation | SettlementExecutionParameters | NaN | Parameters used to execute the settlement of a securities allocation. | SecuritiesSettlement | SettledAllocation |
| Allocation | SecuritiesOrder | NaN | Securites order which is allocated. | SecuritiesOrder | SecuritiesOrderAllocation |
| Allocation | SecuritiesTrade | NaN | Trade which is allocated. | SecuritiesTrade | TradeAllocation |
| Allocation | Identification | NaN | Identifies the allocation. | Max35Text | NaN |
| CollateralValuation | NaN | NaN | Provides details about the valuation of each piece of collateral that is posted. | NaN | NaN |
| CollateralValuation | Collateral | NaN | Collateral which is the subject of the valuation. | Collateral | Valuation |
| CollateralValuation | CollateralValuationDate | NaN | Valuation date of the collateral. | ISODateTime | NaN |
| CollateralValuation | RelatedManagementProcess | NaN | Process which groups the activities related to collateral. | CollateralManagement | CollateralValuation |
| CollateralValuation | ReportedCurrencyAndAmount | NaN | Specifies the total amount of the collateral in the reporting currency. | CurrencyAndAmount | NaN |
| CollateralValuation | MarketValueAmount | NaN | Specifies the total market to market value of the collateral in the reporting currency. It is the dirty price, that is, the accrued interest is included if any. | CurrencyAndAmount | NaN |
| CollateralValuation | AdjustedRate | NaN | Percentage by which the collateral amount needs to be adjusted. | BaseOneRate | NaN |
| CollateralValuation | CollateralValuationCurrency | NaN | Currency used for the valuation. | CurrencyCode | NaN |
| Sector | NaN | NaN | Type of business of the organisation, for example, pharmaceutical. | NaN | NaN |
| Sector | Security | NaN | Security for which a sector is specified. | Security | Sector |
| Sector | Scheme | NaN | Information regarding the entity that assigns the sector code. | Scheme | Sector |
| Sector | Organisation | NaN | Organisation which belongs to a specific sector. | Organisation | Sector |
| Sector | Identification | NaN | Type of business of the organisation, for example, pharmaceutical. | Max35Text | NaN |
| Sector | Strategy | NaN | Strategy based on sector. | SectorStrategy | Sector |
| SecuritiesOrderExecutionInstruction | NaN | NaN | Identifies the instructions for order handling | NaN | NaN |
| SecuritiesOrderExecutionInstruction | AllOrNone | NaN | Round-lot market or limit-price order that must be executed in its entirety or not at all; unlike Fill or Kill orders, AON orders are not treated as canceled if they are not executed as soon as represented in the Trading Crowd. | AllOrNoneIndicator | NaN |
| SecuritiesOrderExecutionInstruction | CallFirst | NaN | Refers to the client before trading in order to catch all verbal instructions on trading strategy usually because the strategy is too complex or cannot be represented in the trading application. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | Cross | NaN | Allow crossing of an order. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | CustomerDisplay | NaN | Exchange or ECN required by the SEC to display limit orders in the public order book. A customer can choose not to have his limit order displayed to the public. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | Hold | NaN | Indicates whether the firm executing the order is held to best execution requirements and may be able to make some discretionary decisions. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | Increase | NaN | Indicates whether the order is to be increased in shares on the ex-dividend date as a result of a stock dividend or distribution. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | InstitutionsOnly | NaN | Identifies that the broker is restricted to dealing with other buy side firms. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | NonNegotiable | NaN | Qualifies an asset (usually a payment instrument) of which rights cannot be transferred to a party other then the original debtor and creditor. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | OverTheDay | NaN | Indicates whether to execute parts of the order over the course of the day. Usually done with large block orders. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | ParticipateDontInitiate | NaN | An order that may participate in a transaction initiated by another party, but may not initiate a transaction. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | PercentOfVolume | NaN | Indicates that the Sender does not want all of the volume on the floor. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | Scale | NaN | An order to buy (or sell) a financial instrument which specifies the total amount to be bought (or sold) and the amount to be bought (or sold) at specified price variations. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | StayOnSide | NaN | Specifies the order limit based on the offer/bid at the time of the order submission. | StayOnSideTypeCode | NaN |
| SecuritiesOrderExecutionInstruction | Work | NaN | Make the order active until notified. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | GoAlong | NaN | Used for listed equity securities. Buy or sell at prices that randomly occur on the floor, participating in whattrades the specialist and other players will allow. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | TryScale | NaN | Order to buy (sell) a security that specifies the total amount to be bought (sold) and the amount to be bought (sold) at successively decreasing (increasing) price intervals; often placed in order to average the price. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | DoNotReduce | NaN | Indicates whether to buy, to stop order to sell, or to stop limit order to sell that is not to be reduced in price by the amount of an ordinary cash dividend on the ex-dividend date. A "do not reduce" order applies only to ordinary cash dividends; it should be reduced for other distributions - such as when a stock goes ex stock dividend or ex rights. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | CancelOnSystemFailure | NaN | If a system failure interrupts trading or order routing, attempt to cancel this order or attempt to reinstate this order, subject to time in force limitations. Note that depending on the type and severity of the failure, this might not be possible. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | CancelOnTradingHalt | NaN | If trading in this instrument is halted, cancel this order or reinstate this order when/if trading resumes, subject to time in force limitations. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | TradeAlong | NaN | Indicates whether the broker has permission to handle and place the order in the market even if the broker already has its own proprietary orders for the same financial instrument placed in the market. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | StrictLimit | NaN | Limit order that must be traded at the exact limit price specified without any price improvement. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | IgnorePriceValidityChecks | NaN | Disables validity checking of price fields for an order or change request. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | ReinstateOnSystemFailure | NaN | If a system failure interrupts trading or order routing, attempt to reinstate this order, subject to time in force limitations. Depending on the type and severity of the failure, this might not be possible. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | ReinstateOnTradingHalt | NaN | If trading in this instrument is halted, reinstate this order when/if trading resumes, subject to time in force limitations. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | CancelIfNotBest | NaN | Indicates that an order should be cancelled if it is no longer the best bid if buying, or the best offer if selling. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | ExternalRoutingAllowed | NaN | Indicates that an order sent to one market may be routed by that market to other external markets, especially in cases where the order locks or crosses the market and it can be executed against another marketÂ’s superior price. The absence of this instruction does not imply that an order should not be routed externally; rather, the order receiverÂ’s default will apply. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | ExternalRoutingNotAllowed | NaN | Indicates that an order sent to one market may never be routed by that market to other external markets. Should the order lock or cross the market but be unable to execute due to price protection reasons, a market may have to take alternate action, which might include rejecting the order, depending on the marketÂ’s rules.The absence of this instruction does not imply that an order should be routed externally; rather, the order receiverÂ’s default will apply. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | ImbalanceOnly | NaN | Indicates that the order can only hit the imbalance during a call auction. The imbalance is the remaining quantity when other buy and sell orders are matched at the auction clearing price. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | IntermarketSweep | NaN | Indicates that the party sending the order has taken responsibility for price protection, and the recipient of the order should execute it, if possible, without regard to protection of other marketsÂ’ prices. While the term "Intermarket sweep" is specific to the United States, it may be used in other markets, where appropriate, to indicate an order that should be executed without regard to price protection. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | Netting | NaN | Used when sending multiple orders indicating that you would be 'netting' the F/X later. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | RelatedOrder | NaN | Order which is executed. | SecuritiesOrder | ExecutionInstructions |
| SecuritiesOrderExecutionInstruction | ForeignExchangeNetting | NaN | Reduction of transfers of cash (resulting of a foreign exchange operation between subsidiaries or separate companies) to a net amount. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | StrictScale | NaN | Order to buy (sell) a security that strictly specifies the total amount to be bought (sold) and the amount to be bought (sold) at successively decreasing (increasing) price intervals; often placed in order to average the price. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | Suspend | NaN | Used in specialist driven markets to direct the specialist to try to suspend the order. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | TryToStop | NaN | Used in specialist driven markets to direct the specialist to try and stop the order. | YesNoIndicator | NaN |
| SecuritiesOrderExecutionInstruction | OrderPriceStrategy | NaN | Strategy used to obtain the order price. | Discretion | RelatedOrderExecution |
| SecuritiesPostTradeBooking | NaN | NaN | Information used to book the executions of a trade. | NaN | NaN |
| SecuritiesPostTradeBooking | DayBooking | NaN | Indicates whether or not automatic booking can occur. | DayBookingInstructionCode | NaN |
| SecuritiesPostTradeBooking | BookingUnit | NaN | Indicates what constitutes a bookable unit, ie, a partial execution, or an aggregated execution. | BookingUnitCode | NaN |
| SecuritiesPostTradeBooking | PreAllocationMethod | NaN | Indicates the method of preallocation. | PreAllocationMethodCode | NaN |
| SecuritiesPostTradeBooking | BookingType | NaN | Method for booking out an order. | BookingTypeCode | NaN |
| SecuritiesPostTradeBooking | RelatedOrder | NaN | Order for which booking instructions are specified. | SecuritiesOrder | BookingInstructions |
| Broker | NaN | TradePartyRole | Party that identifies a broker when required (for example, authorised broker, prime broker, etc). | NaN | NaN |
| Broker | RemunerationAmount | NaN | Amount of any remuneration other than commission received or to be received by the broker in connection with a trade. | ActiveCurrencyAndAmount | NaN |
| Broker | Commission | NaN | Amount of money paid to a broker as a commission. | Commission | Broker |
| SecuritiesOrderPartyRole | NaN | Role | Role played by a party associated with an order to buy or sell securities. | NaN | NaN |
| SecuritiesOrderPartyRole | SecuritiesOrder | NaN | Specifies the order for which a party plays a role. | SecuritiesOrder | SecuritiesOrderPartyRole |
| IntroducingFirm | NaN | SecuritiesOrderPartyRole | Party (broker or other intermediary) that owns the relationship with the investor. It can relay an order directly to the trading floor, or give clients direct access to the floor. | NaN | NaN |
| StepInBroker | NaN | Broker | Broker to which the investment manager directs the execution of a portion of the trade. | NaN | NaN |
| StepOutBroker | NaN | Broker | Brokerage firm that executes an order, but gives other firms credit and some of the commission for the trade. | NaN | NaN |
| ClearingBroker | NaN | Broker | Party which acts as a liaison between an investor and a clearing corporation. | NaN | NaN |
| ExecutingBrokerRole | NaN | Broker | Party responsible for executing an order (e.g. an executing or give-up broker). | NaN | NaN |
| ExecutingBrokerRole | ExecutingTrader | NaN | Trader at the executing broker | ExecutingTrader | ExecutingBroker |
| SecuritiesLending | NaN | SecuritiesFinancing | Lending of securities by one party to another. The terms of the loan are governed by an agreement that requires the borrower to provide the lender with collateral of value equal to or greater than the loaned securities. As payment for the loan, the parties negotiate a fee, quoted as an annualised percentage of the value of the loaned securities. | NaN | NaN |
| SecuritiesLending | BorrowingFee | NaN | Amount to be paid by the borrower to the lender for the securities borrowed calculated based on the bond loan rate. | CurrencyAndAmount | NaN |
| SecuritiesLending | CallableTradeIndicator | NaN | Indicates whether the trade is callable or not. | YesNoIndicator | NaN |
| SecuritiesLending | LendingTransactionMethod | NaN | Method applied to a lending transaction. | LendingTransactionMethodCode | NaN |
| SecuritiesLending | BorrowingReason | NaN | Underlying reason for the borrowing, for instance, sale on my behalf or on behalf of a third party. | BorrowingReasonCode | NaN |
| SecuritiesLending | Reversible | NaN | Indicates the possibility to terminate the securitiesc lending contract either by the borrower or lender before the expiration date. | ReversibleCode | NaN |
| SecuritiesLending | SecuritiesLendingType | NaN | Type of securities lending. | SecuritiesLendingTypeCode | NaN |
| SecuritiesLending | LendingWithCollateral | NaN | Indicates if the contract is with or without an exchange of collateral. | YesNoIndicator | NaN |
| SecuritiesLending | MinimumDateForCallBack | NaN | Minimum date at which the borrower is allowed to give back the securities. | ISODate | NaN |
| SecuritiesLending | NumberOfDaysLendingBorrowing | NaN | Number of days the securities are lent or borrowed for a contract which has an agreed closing date. | Max4NumericText | NaN |
| SecuritiesLending | PeriodicPayment | NaN | Indicates whether the securities lending fees can be paid periodically or at the end of the contract. | YesNoIndicator | NaN |
| SecuritiesLending | Rollover | NaN | Indicates that the contract can be rolled over. | YesNoIndicator | NaN |
| SecuritiesLending | BorrowingRate | NaN | Rate paid by the borrower to the lender for the securities borrowed. | PercentageRate | NaN |
| SecuritiesLending | SecuritiesDeliveryObligation | NaN | Obligation covered by the lending of securities. | SecuritiesDeliveryObligation | SecuritiesLending |
| UnderlyingRatio | NaN | NaN | Related financial instrument into which the security can be converted. | NaN | NaN |
| UnderlyingRatio | SecuritiesConversion | NaN | Other parameters used to convert securities. | SecuritiesConversion | Ratio |
| UnderlyingRatio | UnderlyingQuantityDenominator | NaN | Number of held securities for the exercise. | SecuritiesQuantity | DenominatorRatio |
| UnderlyingRatio | UnderlyingQuantityNumerator | NaN | Number of related securities for the exercise. | SecuritiesQuantity | NumeratorRatio |
| SecuritiesFinancingAgreement | NaN | Agreement | Contractual details related to the agreement between parties. | NaN | NaN |
| SecuritiesFinancingAgreement | SecuritiesFinancingTrade | NaN | Specifies a trade using the related financing agreement. | SecuritiesFinancing | FinancingAgreement |
| SecuritiesFinancingAgreement | Currency | NaN | Contractual currency forming the basis of a financing agreement and associated transactions. Usually, but not always, the same as the trade currency. | CurrencyCode | NaN |
| SecuritiesFinancingAgreement | TerminationType | NaN | Type of financing termination. | TerminationTypeCode | NaN |
| SecuritiesFinancingAgreement | DeliveryType | NaN | Identifies type of settlement. | DeliveryTypeCode | NaN |
| SecuritiesFinancingAgreement | MarginRatio | NaN | Fraction of the cash consideration that must be collateralized, expressed as a percent. A margin ratio of 02% indicates that the value of the collateral (after deducting for "haircut") must exceed the cash consideration by 2%. | PercentageRate | NaN |
| RegulatoryReport | NaN | NaN | Information needed due to regulatory and statutory requirements. | NaN | NaN |
| RegulatoryReport | DebitCreditReportingIndicator | NaN | Identifies whether the regulatory reporting information applies to the debit side, to the credit side or to both debit and credit sides of the transaction. | RegulatoryReportingTypeCode | NaN |
| RegulatoryReport | Authority | NaN | Entity requiring the regulatory reporting information. | RegulatoryAuthorityRole | RegulatoryReport |
| RegulatoryReport | Code | NaN | Specifies the nature, purpose, and reason for the transaction to be reported for regulatory and statutory requirements in a coded form. | Max10Text | NaN |
| RegulatoryReport | Amount | NaN | Amount of money to be reported for regulatory and statutory requirements. | CurrencyAndAmount | NaN |
| RegulatoryReport | Description | NaN | Additional details that may be necessary to cater for specific domestic regulatory requirements. | Max35Text | NaN |
| RegulatoryReport | Type | NaN | Specifies the type of the information supplied in the regulatory reporting details. | Max35Text | NaN |
| RegulatoryReport | Date | NaN | Date related to the specified type of regulatory reporting details. | ISODateTime | NaN |
| RegulatoryReport | ReportedTransaction | NaN | Trade for which a regulatory report is provided. | FinancialTransaction | RegulatoryReport |
| RegulatoryReport | UnderlyingProduct | NaN | Specifies the underlying product type. | Max35Text | NaN |
| RegulatoryReport | NonStandardFlag | NaN | Specifies whether the reportable transaction has one or more additional terms or provisions, other than those listed in the required real-time data fields, that materially affects the price of the reportable transaction. | YesNoIndicator | NaN |
| RegulatoryReport | ReportingPartyRole | NaN | Party responsible for providing regulatory reports. | ReportingPartyRole | RegulatoryReport |
| Undertaking | NaN | NaN | Independent undertaking, such as a demand guarantee or standby letter of credit, that provides financial assurance, to be collected on the presentation of documents that comply with its terms and conditions. | NaN | NaN |
| Undertaking | ElectronicSignature | NaN | Digital signature. | ElectronicSignature | Undertaking |
| Undertaking | UndertakingStatus | NaN | Status of the undertaking. | UndertakingStatus | Undertaking |
| Undertaking | Identification | NaN | Unique and unambiguous identifier assigned to the undertaking issued by the guarantor/issuer. This reference is used throughout the life cycle of the undertaking. | Max35Text | NaN |
| Undertaking | Demand | NaN | Document signed by the beneficiary demanding payment under a demand guarantee or standby letter of credit. | Demand | Undertaking |
| Undertaking | TerminationDate | NaN | Date when the undertaking terminates. | ISODate | NaN |
| Undertaking | UndertakingAmount | NaN | Amount of the undertaking. | UndertakingAmount | Undertaking |
| Undertaking | Expiry | NaN | Expiry information about the undertaking. | Expiry | Undertaking |
| Undertaking | PartyRole | NaN | Role played by a party in the context of an undertaking or in the context of the business linked to the undertaking. | UndertakingPartyRole | Undertaking |
| Undertaking | UndertakingAmendment | NaN | Modification of an undertaking such as an guarantee or standby letter of credit. | AmendmentOfUndertaking | Undertaking |
| Undertaking | SpecifiedDocument | NaN | Document related to the undertaking. | UndertakingDocument | Undertaking |
| Undertaking | DateOfAdvice | NaN | Date on which the undertaking or its amendment is advised. | ISODateTime | NaN |
| Undertaking | Purpose | NaN | Description of the purpose of the undertaking. | Max35Text | NaN |
| Undertaking | UndertakingName | NaN | Name of undertaking such as, demand guarantee, standby letter of credit. | UndertakingNameCode | NaN |
| Undertaking | Type | NaN | Type of guarantee or standby letter of credit, for example, performance, payment, etc. | ExternalUndertakingTypeCode | NaN |
| Undertaking | ConfirmationIndicator | NaN | Indicates whether the advising bank (confirmer) is requested to add its confirmation to the undertaking. | YesNoIndicator | NaN |
| Undertaking | CounterUndertakingIndicator | NaN | Indicates whether the undertaking is a counter-undertaking. | YesNoIndicator | NaN |
| Undertaking | RelatedChargesPayableBy | NaN | Indicates whether the applicant/obligor or beneficiary is responsible for payment of the charges. | ExternalTypeOfPartyCode | NaN |
| Undertaking | StandardClaimDocumentIndicator | NaN | Indication as to whether a claim is to utilise a standard claim form of the issuing institution. | YesNoIndicator | NaN |
| Undertaking | UnderlyingTransaction | NaN | Reference information on a commercial obligation between the beneficiary and applicant for which an undertaking is issued. | UnderlyingTransaction | Undertaking |
| Undertaking | ModelForm | NaN | Wording template for the undertaking content made available for use with certain governance rules or made available by particular institutions. | ModelForm | Undertaking |
| Undertaking | MultipleDemandIndicator | NaN | Indicates whether multiple demands are permitted against the undertaking. | YesNoIndicator | NaN |
| Undertaking | PartialDemandIndicator | NaN | Indicates whether partial demands/drawings are permitted against the undertaking. | YesNoIndicator | NaN |
| Undertaking | TransferIndicator | NaN | Indicates whether the undertaking is transferrable. | YesNoIndicator | NaN |
| Undertaking | PredefinedVariation | NaN | Changes that may be made to the undertaking covered by clauses in the existing undertaking and its amendments. | AutomaticVariation | Undertaking |
| Undertaking | Charges | NaN | Amount and currency of the commissions and changes. | Charges | RelatedUndertaking |
| Undertaking | Presentation | NaN | Presentation information related to the undertaking. | Presentation | PresentedUndertaking |
| Undertaking | UndertakingExtension | NaN | Specifies information related to the extension of an undertaking. | UndertakingExtension | Undertaking |
| Signature | NaN | Evidence | Additional security provision attached to a contract. A (numeric) signature can be used as evidence of origin and integrity, i.e., authenticity of the signed data. A judge can accept this evidence as proof. | NaN | NaN |
| Signature | Conditions | NaN | Parameters related to the signature provided. | SignatureCondition | Signature |
| Signature | CardPaymentValidation | NaN | Validation of a payment by card for which a signeture is specified. | CardPaymentValidation | Signature |
| ElectronicSignature | NaN | Signature | Additional security provisions, such as a digital signature. | NaN | NaN |
| ElectronicSignature | Undertaking | NaN | Undertaking for which a signature is provided. | Undertaking | ElectronicSignature |
| ElectronicSignature | RelatedSecurityCertificate | NaN | Certificate linked to a digital signature. | SecurityCertificate | ElectronicSignature |
| RepresentativeOfficer | NaN | AccountPartyRole | Officer who has some rights to represent a given organisation. In account management, it is the person to be contacted by the account servicer. | NaN | NaN |
| RepresentativeOfficer | Organisation | NaN | Organisation which is represented by the representative officer. | Organisation | RepresentativeOfficer |
| TreasuryManager | NaN | AccountPartyRole | Person responsible for the treasury department within an organisation. | NaN | NaN |
| AccountReportedMovement | NaN | NaN | Provides statistical information on the number of movements and their value for a particular account. | NaN | NaN |
| AccountReportedMovement | MonthlyPaymentValue | NaN | Monthly average of the payment amounts (that is, payments going out) over a year. | CurrencyAndAmount | NaN |
| AccountReportedMovement | MonthlyReceivedValue | NaN | Monthly average of the received amounts over a year (that is, payments coming in). | CurrencyAndAmount | NaN |
| AccountReportedMovement | MonthlyTransactionNumber | NaN | Monthly average of the number of payments (coming in and going out) over a year. | Max35Text | NaN |
| AccountReportedMovement | AverageBalance | NaN | Sum of the end of day balances over a month divided by the number of business days in the month. | CurrencyAndAmount | NaN |
| AccountReportedMovement | ReportedCashAccount | NaN | Cash account for which reported movements are calculated. | CashAccount | ReportedMovements |
| Mandate | NaN | Contract | Authorisation given by an issuing party to a holder party to act on the issuer's behalf. | NaN | NaN |
| Mandate | SignatureConditions | NaN | Specifies the signature requirements related to the document. | SignatureCondition | Mandate |
| Mandate | MandateIdentification | NaN | Unique and unambiguous identification of the mandate. | Max35Text | NaN |
| Mandate | OriginalMandate | NaN | Mandate which is amended. | Mandate | Amendment |
| Mandate | Amendment | NaN | Improvement on a mandate. | Mandate | OriginalMandate |
| Mandate | MandatePartyRole | NaN | Specifies each role linked to a mandate and played by a party in that context. | MandatePartyRole | Mandate |
| Mandate | MandateStatus | NaN | Specifies the status of a mandate | MandateStatus | Mandate |
| Mandate | AccountContract | NaN | Contract on which a mandate applies. | AccountContract | AccountAuthorisation |
| Mandate | Authentication | NaN | Specifies the transport authentication details related to the mandate. | Authentication | Mandate |
| Mandate | TrackingDays | NaN | Specifies the number of days the mandate must be tracked. | Max35NumericText | NaN |
| Mandate | TrackingIndicator | NaN | Specifies whether the direct debit instructions should be automatically re-submitted periodically when bilaterally agreed. | TrueFalseIndicator | NaN |
| Mandate | Rate | NaN | Pre-agreed increase or decrease rate that will be applied to the collection amount. | PercentageRate | NaN |
| Mandate | Frequency | NaN | Regularity with which payment instructions are to be created and processed. | FrequencyCode | NaN |
| Mandate | MandatePaymentType | NaN | Identifies the type of mandate (service level and/or paper or electronic) being requested or given by the initiating party. | PaymentProcessing | RelatedMandate |
| CashAccountMandate | NaN | Mandate | Authorisation given to a mandate holder to perform some operation on an account. | NaN | NaN |
| CashAccountMandate | Services | NaN | Services that the holder of an account mandate can exercise. | CashAccountService | CashAccountMandate |
| CashAccountMandate | CashAccountContract | NaN | Contract to which a mandate applies. | CashAccountContract | CashAccountMandate |
| SecurityCertificate | NaN | Document | Certificate linked to a digital signature. | NaN | NaN |
| SecurityCertificate | ElectronicSignature | NaN | Additional security provisions, such as a digital signature. | ElectronicSignature | RelatedSecurityCertificate |
| SecurityCertificate | SecurityCertificatePartyRole | NaN | Role played by a party in the context of a security certificate. | SecurityCertificatePartyRole | SecurityCertificate |
| SecurityCertificate | NetworkAccess | NaN | Network access which uses a security certificate. | NetworkAccess | ClientCertificate |
| SecurityCertificate | CertificateType | NaN | Type of the security certificate. | Max35Text | NaN |
| BankOperation | NaN | CashAccountService | Operation on a bank account. It may be limited in time, amount or type of operation. | NaN | NaN |
| BankOperation | OperationThreshold | NaN | Threshold related to a bank account operation. | OperationThreshold | BankOperation |
| BankOperation | OperationType | NaN | Specifies the type of the operation related to a bank account. | BankTransaction | BankOperation |
| BankOperation | ApplicablePeriod | NaN | Specifies the period, for instance a number of days, for which the bank operations are permitted. | DateTimePeriod | BankOperation |
| OperationThreshold | NaN | NaN | Threshold related to a bank account operation. | NaN | NaN |
| OperationThreshold | BankOperation | NaN | Bank operation for which a threshold is specified. | BankOperation | OperationThreshold |
| OperationThreshold | MininumAmountPerTransaction | NaN | Lower limit for the operation. | CurrencyAndAmount | NaN |
| OperationThreshold | MaximumAmount | NaN | Maximum amount allowed over a specific period of time and/or amount which is the upper limit for an operation. | CurrencyAndAmount | NaN |
| BankTransaction | NaN | NaN | Code of the underlying bank transaction. | NaN | NaN |
| BankTransaction | Domain | NaN | Specifies the business area of the underlying transaction. | ExternalBankTransactionDomainCode | NaN |
| BankTransaction | Family | NaN | Specifies the family within a domain. | ExternalBankTransactionFamilyCode | NaN |
| BankTransaction | SubFamily | NaN | Specifies the sub-product family within a specific family. | ExternalBankTransactionFamilyCode | NaN |
| BankTransaction | ProprietaryIdentification | NaN | Bank transaction code in a proprietary form, as defined by the issuer. | GenericIdentification | IdentificationForBankTransaction |
| BankTransaction | BankOperation | NaN | Bank operation for which a type is detailed. | BankOperation | OperationType |
| BankTransaction | RelatedEntry | NaN | Entry for which a bank transaction code is provided. | Entry | BankTransactionCode |
| BankTransaction | RelatedPayment | NaN | Payment for which bank transaction information is specified. | PaymentProcessing | BankTransaction |
| Presentation | NaN | NaN | Presentation of documents. | NaN | NaN |
| Presentation | CommunicationMethod | NaN | Method by which the document is to be delivered. | ExternalChannelCode | NaN |
| Presentation | PresentedUndertaking | NaN | Specifies the undertaking which is presented and its associated documents. | Undertaking | Presentation |
| Presentation | Medium | NaN | Medium through which the presentation can be submitted such as paper, electronic or both. | PresentationMediumCode | NaN |
| Presentation | PresentedDocument | NaN | Documents which are presented. | Document | Presentation |
| Presentation | ElectronicPresentationAddress | NaN | Electronic address for the presentation of documents. | ElectronicAddress | RelatedPresentation |
| Presentation | PresentationDate | NaN | Date on which the presentation is made. | ISODate | NaN |
| Presentation | ApplicableChannel | NaN | Channel used for the transmission of a document. | CommunicationMethodCode | NaN |
| SecurityCertificatePartyRole | NaN | Role | Role played by a party in the context of a security certificate | NaN | NaN |
| SecurityCertificatePartyRole | SecurityCertificate | NaN | Identifies the security certificate for which a party plays a role. | SecurityCertificate | SecurityCertificatePartyRole |
| SecurityCertificateHolderRole | NaN | SecurityCertificatePartyRole | Holder of the security certificate. | NaN | NaN |
| DebitCreditFacility | NaN | CashAccountService | Specifies the conditions for overdraft on the account or for positive amounts. | NaN | NaN |
| DebitCreditFacility | CreditLine | NaN | Credit or Debit limit applied to a cash account. | Limit | RelatedDebitCreditFacility |
| DebitCreditFacility | CashAccountInterest | NaN | Interest that applies to a cash account at a particular moment in time, as per a contractual relationship. | Interest | RelatedDebitCreditFacility |
| DebitCreditFacility | CreditDebitIndicator | NaN | Specifies if the line is a debit limit or a credit limit. | DebitCreditCode | NaN |
| CashAvailability | NaN | NaN | Indicates when the amount of money will become available, ie can be accessed and start generating interest. | NaN | NaN |
| CashAvailability | CashBalance | NaN | Cash balance for which the availability is provided. | CashBalance | Availability |
| CashAvailability | Date | NaN | Identifies the availability date. | ISODate | NaN |
| CashAvailability | NumberOfDays | NaN | Indicates the number of float days attached to the balance. | Max15NumericText | NaN |
| CashAvailability | Amount | NaN | Available amount. | CurrencyAndAmount | NaN |
| CashAvailability | CashEntry | NaN | Specifies the cash entry for which the availability information is provided. | CashEntry | Availability |
| CashAvailability | CreditDebitIndicator | NaN | Indicates whether the availability balance is a credit or a debit balance. A zero balance is considered to be a credit balance. | DebitCreditCode | NaN |
| DocumentIssuer | NaN | DocumentPartyRole | Party that issues a document such as a bank guarantee or letter of / documentary credit. For instance the inspection company for a trade certificate or the insurance company or its agent for an insurance certificate. | NaN | NaN |
| Discount | NaN | Adjustment | Decrease of the value of goods and / or services by applying a discount rate to the original amount. | NaN | NaN |
| Discount | DiscountAppliedAmount | NaN | Amount of money that results from the application of an agreed discount to the amount due and payable to the creditor. | CurrencyAndAmount | NaN |
| Discount | DiscountType | NaN | Specifies the type of discount applied to the original amount. | DiscountTypeCode | NaN |
| Discount | DiscountBasisAmount | NaN | Amount used as a basis to calculate the discount amount. | CurrencyAndAmount | NaN |
| Invoice | NaN | FinancialDocument | General information about an invoice, such as number, issue date date and monetary amounts. | NaN | NaN |
| Invoice | CreditDebitNoteAmount | NaN | Amount of credit/debit note related to the invoice. | CurrencyAndAmount | NaN |
| Invoice | TotalTaxAmount | NaN | Sum of all tax amounts related to the invoice. It is derived from the association between line item and tax. | CurrencyAndAmount | NaN |
| Invoice | TotalInvoiceAmount | NaN | Total amount of the invoice, being the sum of total invoice lines amounts, total invoice additional amounts (allowances and charges) and total tax amounts. | CurrencyAndAmount | NaN |
| Invoice | InvoiceCurrency | NaN | Code specifying the currency of the invoice. | CurrencyCode | NaN |
| Invoice | PeriodCovered | NaN | Specifies the period covered by an invoice for instance for recurring services. | DateTimePeriod | RelatedInvoice |
| Invoice | TradeSettlement | NaN | Specifies the process which takes place to settle an invoice. | CommercialTradeSettlement | Invoice |
| Invoice | TotalCharge | NaN | Algebraical sum of charges related to the invoice. | CurrencyAndAmount | NaN |
| Invoice | TotalPrepaidAmount | NaN | Monetary value of the total prepaid amount being reported for this settlement. | CurrencyAndAmount | NaN |
| Invoice | LineItem | NaN | Unit of information showing the related provision of products and/or services and monetary summations reported as a discrete line item. | LineItem | Invoice |
| Invoice | TotalNetAmount | NaN | Total amount after taxes, adjustments and charges. | CurrencyAndAmount | NaN |
| Invoice | CurrencyExchange | NaN | Specifies currency exchange information which is used when currency conversion is necessary. | CurrencyExchange | RelatedInvoice |
| Invoice | BillingCompensationType | NaN | Defines the type of billing compensation. | ExternalBillingCompensationTypeCode | NaN |
| Invoice | InvoicePartyRole | NaN | Role played by a party in the context of invoices. | InvoicePartyRole | Invoice |
| Invoice | OriginalInvoice | NaN | Invoice to which another invoice is associated. | Invoice | RelatedInvoice |
| Invoice | RelatedInvoice | NaN | Specifies another invoice linked to the current one, for instance a previous invoice for which a credit note is available. | Invoice | OriginalInvoice |
| Invoice | InvoiceFinancingTransaction | NaN | Financing transaction related to an invoice. | InvoiceFinancingAgreement | Invoice |
| Invoice | BillingCompensationAmount | NaN | Specifies the compensation amount of an incorrect billing. | CurrencyAndAmount | NaN |
| Invoice | InvoiceStatus | NaN | Status of the invoice or of the billing process. | InvoiceStatus | Invoice |
| Invoice | Payment | NaN | Payment related to an invoice. | Payment | InvoiceReconciliation |
| Invoice | CreditDebitIndicator | NaN | Indicates the direction of the invoice amount. | DebitCreditCode | NaN |
| Invoice | LimitedPresentmentIndicator | NaN | Indicates whether the creditor allows limited presentment of the invoice, that is, only the invoice data needed for payment initiation. | TrueFalseIndicator | NaN |
| Invoice | RelatedElectronicInvoiceProcessingService | NaN | Specifies the details for the service for the invoice. | ElectronicInvoiceProcessingService | RelatedInvoice |
| Invoice | ActivationRequestDeliveryParty | NaN | Creditor's electronic invoice provider address to which the debtor activation has to be delivered. | NaN | NaN |
| InvoicePartyRole | NaN | Role | Role played by a party in the context of an invoice. | NaN | NaN |
| InvoicePartyRole | Invoice | NaN | Identifies the invoice for which a party plays a role. | Invoice | InvoicePartyRole |
| InvoiceeRole | NaN | InvoicePartyRole | Party identified as the liable party on the face of a commercial invoice. | NaN | NaN |
| TaxPartyRole | NaN | Role | Role played by a party in the context of a tax due. | NaN | NaN |
| TaxPartyRole | Tax | NaN | Identifies the taxfor which a party plays a role. | Tax | PartyRole |
| TaxPartyRole | VATRegistrationNumber | NaN | Value added tax (VAT) registration number. | Max35Text | NaN |
| CreditSideTaxDebtor | NaN | TaxPartyRole | Party on the credit side of the transaction to which the tax applies. | NaN | NaN |
| TaxPayer | NaN | TaxPartyRole | Party that settles tax amounts. May be different from the tax debtor and tax creditor. | NaN | NaN |
| DebitSideTaxDebtor | NaN | TaxPartyRole | Party on the debit side of the transaction to which the tax applies. | NaN | NaN |
| TaxRecord | NaN | NaN | Record of tax details. | NaN | NaN |
| TaxRecord | Tax | NaN | Tax for which tax record information is provided. | Tax | Record |
| TaxRecord | TaxRecordType | NaN | High level code to identify the type of tax details. | Max35Text | NaN |
| TaxRecord | Category | NaN | Description of the tax that is being paid, including specific representation (code) required by the tax authority. | Max35Text | NaN |
| TaxRecord | Status | NaN | Code provided by local authority to identify the status of the party that has drawn up the settlement document. | Max35Text | NaN |
| TaxRecord | FormsCode | NaN | Code to identify on which template the tax report is to be provided | Max35Text | NaN |
| TaxRecord | Period | NaN | Period of time details related to the tax payment. | TaxPeriod | TaxRecord |
| TaxRecord | Amount | NaN | Amount of the tax record. | ActiveCurrencyAndAmount | NaN |
| TaxRecord | CategoryDescription | NaN | Description of the tax that is being paid, including specific representation required by taxing authority. | Max35Text | NaN |
| TaxPeriod | NaN | NaN | Period of time details related to the tax payment. | NaN | NaN |
| TaxPeriod | TaxRecord | NaN | Tax record for which a period is specified. | TaxRecord | Period |
| TaxPeriod | Year | NaN | Year related to the tax payment. | ISODate | NaN |
| TaxPeriod | Type | NaN | Identification of the period related to the tax payment. | TaxRecordPeriodCode | NaN |
| TaxPeriod | FromToDate | NaN | Range of time between a start date and an end date for which the tax report is provided. | DateTimePeriod | TaxPeriod |
| TaxPeriod | EndOfFiscalYear | NaN | Date on which the fiscal year is closed. | ISODate | NaN |
| CardPaymentAcquiring | NaN | NaN | Payment processes initiated by a payment card. | NaN | NaN |
| CardPaymentAcquiring | PointOfInteraction | NaN | Describes the Point of Interaction through which the payment by card was initiated. | PointOfInteraction | CardPaymentAcquiring |
| CardPaymentAcquiring | CardPaymentService | NaN | Type of service provided by the transaction. | CardPaymentServiceTypeCode | NaN |
| CardPaymentAcquiring | TransactionIdentification | NaN | Identification of the transaction assigned by the POI (Point Of Interaction). | Max35Text | NaN |
| CardPaymentAcquiring | TransactionDateTime | NaN | Local date and time of the transaction assigned by the POI (Point Of Interaction). | ISODateTime | NaN |
| CardPaymentAcquiring | ICCRelatedData | NaN | Data related to the interface of an integrated circuit card application. | Max10000Binary | NaN |
| CardPaymentAcquiring | RelatedCardPayment | NaN | Card payment which is at the origin of the acquiring process. | CardPayment | CardPaymentAcquiring |
| CardPaymentAcquiring | CardPresent | NaN | Indicates whether the transaction has been initiated by a card physically present or not. | TrueFalseIndicator | NaN |
| CardPaymentAcquiring | CardholderPresent | NaN | Indicates whether the transaction has been initiated in presence of the cardholder or not. | TrueFalseIndicator | NaN |
| CardPaymentAcquiring | OnLineContext | NaN | On-line or off-line context of the transaction. | TrueFalseIndicator | NaN |
| CardPaymentAcquiring | AttendanceContext | NaN | Human attendance at the POI location during the transaction. | AttendanceContextCode | NaN |
| CardPaymentAcquiring | TransactionEnvironment | NaN | Indicates the environment of the transaction. | TransactionEnvironmentCode | NaN |
| CardPaymentAcquiring | TransactionChannel | NaN | Identifies the type of the communication channels used by the cardholder to the acceptor system. | TransactionChannelCode | NaN |
| CardPaymentAcquiring | AttendantMessageCapable | NaN | Indicates whether a message can be sent or not on an attendant display (attendant display present or not). | TrueFalseIndicator | NaN |
| CardPaymentAcquiring | AttendantLanguage | NaN | Language used to display messages to the attendant. | ISO2ALanguageCode | NaN |
| CardPaymentAcquiring | CardDataEntryMode | NaN | Entry mode of the card data. | CardDataReadingCode | NaN |
| CardPaymentAcquiring | FallbackIndicator | NaN | Indicator of a transaction fallback. | TrueFalseIndicator | NaN |
| CardPaymentAcquiring | TMSTrigger | NaN | Instructs the POI (Point Of Interaction) how to contact the host of the terminal management system (TMS), to initiate the maintenance of the terminal. | TerminalManagementSystem | CardPaymentAcquiring |
| CardPaymentAcquiring | InitiatorTransactionIdentifier | NaN | Identification of the transaction assigned by the initiating party for the recipient party. | Max35Text | NaN |
| CardPaymentAcquiring | Reversal | NaN | Notify that a previous transaction has to be reversed if this original transaction has been approved by the acquirer. | TrueFalseIndicator | NaN |
| CardPaymentAcquiring | InterchangeData | NaN | Interchange information related to the card scheme. | Max35Text | NaN |
| CardPaymentAcquiring | UnattendedLevelCategory | NaN | Transaction category level on an unattended POI (Point Of Interaction). | Max35NumericText | NaN |
| CardPaymentAcquiring | Validation | NaN | Results and parameters of the card payment verification. | CardPaymentValidation | CardPayment |
| CardPaymentAcquiring | CompletionRequired | NaN | Indicates whether the acquirer requires a further exchange after the completion of the transaction. | TrueFalseIndicator | NaN |
| CardPaymentAcquiring | ActionType | NaN | Type of action to be performed by the POI (Point Of Interaction) system. | ActionTypeCode | NaN |
| CardPaymentAcquiring | ActionMessage | NaN | Message to be displayed or printed to the cardholder or the cashier. | Max256Text | NaN |
| CardPaymentAcquiring | CaptureIndicator | NaN | Indicates whether the transaction is captured or not. | TrueFalseIndicator | NaN |
| CardPaymentAcquiring | RecipientTransactionIdentification | NaN | Identification of the transaction assigned by the recipient party for the initiating party. | Max35Text | NaN |
| CardPaymentAcquiring | Location | NaN | Location category of the place where the merchant actually performed the transaction. | LocationCategoryCode | NaN |
| CardPaymentAcquiring | Country | NaN | Country of the merchant where the transaction took place. | Country | RelatedCardPayment |
| CardPaymentAcquiring | ReSubmissionCounter | NaN | In case a message is sent after the consumption of goods or service, it indicates the number of times the authorisation has been sent to the Acquirer in order to get an approval. | PositiveNumber | NaN |
| CardPaymentAcquiring | BusinessArea | NaN | Defines the business context of this transaction that could imply specific scheme rules. | BusinessAreaCode | NaN |
| PointOfInteraction | NaN | System | Point of interaction (POI) is the entry point to a card payment system. It could be a physical or logical card payment terminal containing software and hardware components, it could be a payment system including a set of card payment terminals linked to a local or remote server, or it could be just an interface to make payments as telephone or Internet browser. | NaN | NaN |
| PointOfInteraction | CardPaymentAcquiring | NaN | Process which uses the point of interaction. | CardPaymentAcquiring | PointOfInteraction |
| PointOfInteraction | CardReadingCapabilities | NaN | Card reading capabilities of the POI performing the transaction. | CardDataReadingCode | NaN |
| PointOfInteraction | CardholderVerificationCapabilities | NaN | Type of cardholder verification that could be performed during a transaction. | CardholderVerificationCapabilityCode | NaN |
| PointOfInteraction | OnLineCapabilities | NaN | On-line and off-line capabilities of the POI. | OnLineCapabilityCode | NaN |
| PointOfInteraction | DisplayCapabilities | NaN | Display interfaces components. | UserInterfaceCode | NaN |
| PointOfInteraction | PrintLineWidth | NaN | Number of columns of the printer component. | Max3NumericText | NaN |
| PointOfInteraction | Component | NaN | Type of components belonging to a POI. | POIComponentTypeCode | NaN |
| PointOfInteraction | ComponentIdentification | NaN | Identification of the POI component assigned by its provider. | Max35Text | NaN |
| PointOfInteraction | GroupIdentifier | NaN | Identifier assigned by the merchant identifying a set of POI terminals performing some categories of transactions. | Max35Text | NaN |
| PointOfInteraction | LineWidth | NaN | Number of columns of the display component. | Max3NumericText | NaN |
| PointOfInteraction | NumberOfLines | NaN | Number of lines of the display component. | Max2NumericText | NaN |
| PointOfInteraction | ErrorLog | NaN | Error logging transferred by the point of interaction to the terminal management system. | Max140Text | NaN |
| PointOfInteraction | ComponentVersionNumber | NaN | Identification of a version of component belonging to a given model. | Max16Text | NaN |
| PointOfInteraction | ControllingTerminalManagementSystem | NaN | Terminal management system for which a point of interaction is specified. | TerminalManagementSystem | ControlledPointOfInteraction |
| SystemName | NaN | NaN | Name of a system. | NaN | NaN |
| SystemName | Name | NaN | Name of a system for instance the common name assigned by the acquirer to the POI system. | Max70Text | NaN |
| SystemName | SystemIdentification | NaN | System identification which contains a name. | SystemIdentification | SystemName |
| InvestigationPartyRole | NaN | Role | Role played by a party in the context of an investigation process. | NaN | NaN |
| InvestigationPartyRole | InvestigationCase | NaN | Identifies the case for which a party plays a role. | InvestigationCase | InvestigationPartyRole |
| InvestigationPartyRole | Status | NaN | Status for which a party plays a role. | Status | PartyRole |
| StatusOriginator | NaN | InvestigationPartyRole | Provides the identification of the originator issuing the transaction reason. | NaN | NaN |
| CashDeposit | NaN | IndividualPayment | Amount of money representing a value paid by a debtor to an agent bank. | NaN | NaN |
| CashDeposit | NoteDenomination | NaN | Specifies the note or coin denomination, including the currency, such as a 50 euro note. | CurrencyAndAmount | NaN |
| CashDeposit | NumberOfNotes | NaN | Specifies the number of notes of the same denomination in the deposit. | Max15NumericText | NaN |
| CashDeposit | DepositAmount | NaN | Specifies the total amount of money in the cash deposit, that is the note denomination times the number of notes. | CurrencyAndAmount | NaN |
| CashDeposit | RelatedBankingTransaction | NaN | Describes the type of transaction associated with a cash deposit. | BankingTransaction | CashDeposit |
| ReconciliationTransaction | NaN | Reconciliation | Totals performed during the reconciliation period, for a certain type of transaction. | NaN | NaN |
| ReconciliationTransaction | ReconciliationIdentification | NaN | Unique identification of the reconciliation period between the acceptor and the acquirer. This identification might be linked to the identification of the settlement for further verification by the merchant. | Max35Text | NaN |
| ReconciliationTransaction | Currency | NaN | Currency associated with thecumulative amount. | CurrencyCode | NaN |
| ReconciliationTransaction | TransactionType | NaN | Identification of the type of transaction. | TypeTransactionTotalsCode | NaN |
| ReconciliationTransaction | TotalNumber | NaN | Total number of transactions during a reconciliation period. | Max35Text | NaN |
| ReconciliationTransaction | CumulativeAmount | NaN | Total amount of a collection of transactions. | ImpliedCurrencyAndAmount | NaN |
| ReconciliationTransaction | ClosePeriod | NaN | Indicates if the exchange requires a closure of the reconciliation period. | TrueFalseIndicator | NaN |
| ReconciliationTransaction | CardPaymentTotal | NaN | Specifies the card payments which are part of the transaction reconciliation. | CardPayment | Reconciliation |
| ProductIdentification | NaN | NaN | Information used to identify a product. | NaN | NaN |
| ProductIdentification | Identifier | NaN | Specifies the product identifier. | Max35Text | NaN |
| ProductIdentification | Product | NaN | Specifies the product for which an identification is specified. | Product | ProductIdentification |
| ProductIdentification | Type | NaN | Specifies the type of product identifier by means of a code. | ProductIdentifierCode | NaN |
| ProductIdentification | GlobalSerialIdentifier | NaN | Unique global serial identifier for a product instance. | Max35Text | NaN |
| ProductQuantity | NaN | NaN | Specifies the ordered quantity of a product. | NaN | NaN |
| ProductQuantity | UnitOfMeasure | NaN | Specifies the unit of measurement. For example, kilo, tons. | UnitOfMeasureCode | NaN |
| ProductQuantity | Value | NaN | Quantity of a product on a line specified by a number. For example, 100 (kgs), 50 (pieces). | DecimalNumber | NaN |
| ProductQuantity | Product | NaN | Specifies the type of goods and services linked to the quantity. | Product | Quantity |
| ProductQuantity | Factor | NaN | Multiplication factor of measurement values. For example: goods that can be ordered by 36 pieces. | Max15NumericText | NaN |
| ProductQuantity | NetWeightRelatedLineItem | NaN | Line item for which a net weight is specified. | LineItem | NetWeight |
| ProductQuantity | BilledQuantityRelatedLineItem | NaN | Line item which contains this quantity. | LineItem | BilledQuantity |
| ProductQuantity | RelatedPackaging | NaN | Packaging for which a quantity is specified. | Packaging | Quantity |
| ProductQuantity | PackagingForUnitQuantity | NaN | Packaging for which a unit quantity per package is specified. | Packaging | PerPackageUnitQuantity |
| ProductQuantity | ChargeFreeQuantityRelatedLineItem | NaN | Line item for which a charge free quantity of product is specified. | LineItem | ChargeFreeQuantity |
| ProductQuantity | MeasureQuantityStart | NaN | Quantity value on which the quantity measurement started for a line item. For instance the start amount of a meter reading for an electricity supplier. | LineItem | MeasureQuantityStartRelatedLineItem |
| ProductQuantity | MeasureQuantityEnd | NaN | Quantity value on which the quantity measurement ended for a line item. For instance the end amount of a meter reading for an electricity supplier. | LineItem | MeasureQuantityEndRelatedLineItem |
| ProductQuantity | QuantityTolerance | NaN | Variance allowed in the quantity of goods. | Tolerance | Quantity |
| ProductQuantity | PackagingForConsignmentlQuantity | NaN | Packaging for which a total consignment quantity is specified. | Packaging | TotalConsignmentQuantity |
| ProductQuantity | PackagingForVolume | NaN | Packaging for which a volume is specified. | Packaging | TotalVolume |
| ProductQuantity | PackagingForWeight | NaN | Packaging for which a weight is specified. | Packaging | TotalWeight |
| ProductQuantity | GrossPriceQuantityRelatedLineItem | NaN | Line item for which gross price quantity is specified. | LineItem | GrossPriceQuantity |
| ProductQuantity | NetPriceQuantityRelatedLineItem | NaN | Line item for which a net price quantity is specified. | LineItem | NetPriceQuantity |
| ProductQuantity | GrossWeightRelatedLineItem | NaN | Line item for which a gross weight is specified. | LineItem | GrossWeight |
| ProductQuantity | TimeUnit | NaN | Unit for the frequency period. | FrequencyCode | NaN |
| ServiceLevel | NaN | NaN | Agreement under which or rules under which the transaction should be processed. | NaN | NaN |
| ServiceLevel | PaymentProcessing | NaN | Payment process for which a service level is specified. | PaymentProcessing | ServiceLevel |
| ServiceLevel | Code | NaN | Identification of a pre-agreed level of service between the parties in a coded form. | ServiceLevelCode | NaN |
| ServiceLevel | Other | NaN | SWIFT defined service level applies to the payment instruction. | SWIFTServiceLevelCode | NaN |
| ServiceLevel | Bilateral | NaN | Unambiguous identification of a pre-agreed level of service between the parties. | Max35Text | NaN |
| DebtorAgentRole | NaN | PaymentPartyRole | Financial institution servicing an account for the debtor. | NaN | NaN |
| PaymentObligationPartyRole | NaN | Role | Role played by a party in the context of a payment obligation. | NaN | NaN |
| PaymentObligationPartyRole | PaymentObligation | NaN | Identifies the payment obligation for which a party plays a role. | PaymentObligation | PartyRole |
| UltimateDebtorRole | NaN | PaymentObligationPartyRole | Ultimate party that owes an amount of money to the (ultimate) creditor. | NaN | NaN |
| ChargePartyRole | NaN | Role | Role played by a party in the context of a paymentof charges. | NaN | NaN |
| ChargePartyRole | Adjustment | NaN | Identifies the adjustment for which a party plays a role. | Adjustment | ChargesPartyRole |
| ChargeAccountAgent | NaN | ChargePartyRole | Agent that services a charge account. | NaN | NaN |
| CreditTransfer | NaN | IndividualPayment | Payment made by transferring an amount of money from a debtor to a creditor. The payment flows through one or more financial institutions or systems. | NaN | NaN |
| CreditTransfer | StandingOrder | NaN | Transaction is a standing order. This information is derived from the presence of detailed standing order specification. | YesNoIndicator | NaN |
| CreditTransfer | RelatedStandingOrder | NaN | Standing order which creates the credit transfers. | CashStandingOrder | CreditTransfer |
| RegulatoryAuthorityRole | NaN | Role | Entity requiring the regulatory reporting information. | NaN | NaN |
| RegulatoryAuthorityRole | RegulatoryReport | NaN | Report which was requested by the regulatory authority. | RegulatoryReport | Authority |
| RegulatoryAuthorityRole | Country | NaN | Country for which the regulatory authority operates. | Country | NationalRegulatoryAuthority |
| UltimateCreditorRole | NaN | PaymentObligationPartyRole | Ultimate party to which an amount of money is due. | NaN | NaN |
| DirectDebitMandate | NaN | Mandate | Authorisation in favour of the creditor given by the debtor to debit its own account. | NaN | NaN |
| DirectDebitMandate | RelatedDirectDebit | NaN | Direct debit to which a mandate applies. | DirectDebit | DirectDebitMandate |
| DirectDebitMandate | FinalCollectionDate | NaN | Date of the final collection of a direct debit as per the mandate. | ISODate | NaN |
| DirectDebitMandate | FirstCollectionDate | NaN | Date of the first collection of a direct debit as per the mandate. | ISODate | NaN |
| DirectDebitMandate | CollectionAmount | NaN | Fixed amount that the debtor has agreed will be collected from their account. | CurrencyAndAmount | NaN |
| DirectDebitMandate | MaximumAmount | NaN | Maximum amount that may be collected from the debtor's account, per instruction. | CurrencyAndAmount | NaN |
| DirectDebitMandate | PreNotification | NaN | Indicates wether a pre-notification must be sent by the creditor to the debtor before a direct debit occurs | TrueFalseIndicator | NaN |
| DirectDebitMandate | PreNotificationThreshold | NaN | Specifies the number of days before the direct debit for notifying the debtor. | Number | NaN |
| DirectDebitMandate | Classification | NaN | Type of direct debit instruction. | MandateClassificationCode | NaN |
| DirectDebitMandate | PointInTime | NaN | Specifies a frequency in terms of an exact point in time or moment within a specified period type. | FrequencyCode | NaN |
| CreditorRole | NaN | PaymentPartyRole | Party to which an amount of money is due. | NaN | NaN |
| CreditorRole | SchemeIdentification | NaN | Credit party that signs a direct debit mandate. | Scheme | CreditorRole |
| InvestigationCase | NaN | NaN | Set of activities performed to handle an exception to a normal transaction flow.. | NaN | NaN |
| InvestigationCase | AssignmentIdentification | NaN | Uniquely identifies the case assignment. | Max35Text | NaN |
| InvestigationCase | CreationDateTime | NaN | Creation date and time of the case. | ISODateTime | NaN |
| InvestigationCase | Identification | NaN | Uniquely identifies the case. | Max35Text | NaN |
| InvestigationCase | Status | NaN | Specifies the status of the case together with the reason and the date and time. | InvestigationCaseStatus | InvestigationCase |
| InvestigationCase | InvestigationPartyRole | NaN | Role played by a party in the context of an investigation process. | InvestigationPartyRole | InvestigationCase |
| InvestigationCase | DuplicateCaseResolution | NaN | Solution which consists in closing the case as it is a duplicate of an original one. | DuplicateCase | DuplicatedCase |
| InvestigationCase | InvestigationResolution | NaN | Specifies the actions taken as a result of an investigation. | InvestigationResolution | InvestigationCase |
| InvestigationCase | OriginalInvestigationCase | NaN | Original case to which another one is linked. | InvestigationCase | LinkedCase |
| InvestigationCase | LinkedCase | NaN | Step in the resolution process of an investigation case. The assigned case is linked to the investigation case in the previous step. | InvestigationCase | OriginalInvestigationCase |
| InvestigationCase | Reassignment | NaN | Action which is taken to forward the case to another party. | Reassignment | ReassignedCase |
| InvestigationCase | EIR | NaN | <p>Unique identifier to provide the end-to-end reference of an investigation.</p> | UUIDv4Identifier | NaN |
| InvestigationCase | RequestorInvestigationIdentification | NaN | <p>Unique identification, as assigned by the requestor, to unambiguously identify the investigation for the requestor.</p> | Max35Text | NaN |
| InvestigationCase | InvestigationSubType | NaN | <p>Sub type of an investigation.</p> | Max35Text | NaN |
| InvestigationCase | InvestigationType | NaN | <p>Type of investigation.</p> | Max35Text | NaN |
| InvestigationCase | ResponderInvestigationIdentification | NaN | <p>Unique identification, as assigned by the responder, to unambiguously identify the investigation for the responder.</p> | Max35Text | NaN |
| PaymentInvestigationCase | NaN | InvestigationCase | Set of activities performed to handle an exception to a normal payment transaction flow, such as: - a payment has not been received. - a payment has been received but is incorrect. - a payment must be corrected or cancelled (requested by the party which ordered the payment). | NaN | NaN |
| PaymentInvestigationCase | PaymentStatus | NaN | Status of a payment which is the reason or the result of an investigation case. | PaymentStatus | RelatedInvestigationCase |
| PaymentInvestigationCase | CancellationReason | NaN | Indicates the reason for cancellation. | CancellationReasonCode | NaN |
| PaymentInvestigationCase | UnderlyingPayment | NaN | Identifies the end to end payment which is the subject of the investigation | Payment | RelatedInvestigationCase |
| PaymentInvestigationCase | MissingCoverIndication | NaN | Indicates whether or not the claim is related to a missing cover. | YesNoIndicator | NaN |
| PaymentInvestigationCase | UnderlyingInstruction | NaN | Identifies the payment instruction under investigation. | PaymentExecution | RelatedInvestigationCase |
| PaymentInvestigationCase | UnderlyingCashEntry | NaN | Identifies the cash entry under investigation. | CashEntry | RelatedInvestigationCase |
| PaymentInvestigationCase | IncorrectInformationReason | NaN | Indicates, in a coded form, the incorrect information. | UnableToApplyIncorrectInfoCode | NaN |
| PaymentInvestigationCase | MissingInformationReason | NaN | Indicates the missing information. | UnableToApplyMissingInformationV2Code | NaN |
| PaymentInvestigationCase | CaseType | NaN | Specifies the type of investigation case. | Max35Text | NaN |
| InstructedReimbursementAgent | NaN | CashSettlementInstructionPartyRole | Agent at which the instructed agent will be reimbursed.Usage: If the instructing and instructed agents have the same reimbursement agent, then only InstructedReimbursementAgent is not allowed.Usage: If InstructedReimbursementAgent contains a branch of the instructed agent, then the instructed agent will claim reimbursement from that branch/will be paid by that branch. | NaN | NaN |
| UndertakingStatusReason | NaN | StatusReason | Specifies the reason for the status or for the action (for instance settlement reason). | NaN | NaN |
| UndertakingStatusReason | Discrepancy | NaN | Demand is refused because of a discrepancy in the demand. | Discrepancy | UndertakingStatusReason |
| UndertakingStatusReason | UndertakingStatus | NaN | Status for which a reason is provided. It is derived from the association between StatusReason and Status. | UndertakingStatus | UndertakingStatusReason |
| UndertakingStatusReason | TerminationReason | NaN | Reason for the termination. | TerminationReasonCode | NaN |
| UndertakingStatusReason | DemandRefusalStatusReason | NaN | Processing status reported by the issuer for the refusal of a demand. | DemandStatusCode | NaN |
| UndertakingStatusReason | SettlementReason | NaN | Specifies the reason for the settlement of an amount. | SettlementAdviceTypeCode | NaN |
| UndertakingStatus | NaN | Status | Status of the undertaking. | NaN | NaN |
| UndertakingStatus | Undertaking | NaN | Undertaking for which a status is specified. | Undertaking | UndertakingStatus |
| UndertakingStatus | DemandStatus | NaN | Processing status reported by the applicant. | DemandStatusCode | NaN |
| UndertakingStatus | Status | NaN | Status of the undertaking. | UndertakingStatusCode | NaN |
| UndertakingStatus | UndertakingStatusReason | NaN | Specifies the reason for the status. it is derived from the association between Status and StatusReason. | UndertakingStatusReason | UndertakingStatus |
| UndertakingStatus | StatusCategory | NaN | Specifies the category of the status. | ExternalUndertakingStatusCategoryCode | NaN |
| UndertakingStatus | PresentationStatus | NaN | Status of the presentation. | UndertakingStatusCode | NaN |
| UndertakingPartyRole | NaN | Role | Role played by a party in the context of an undertaking. | NaN | NaN |
| UndertakingPartyRole | Undertaking | NaN | Identifies the undertaking for which a party plays a role. | Undertaking | PartyRole |
| UndertakingIssuer | NaN | UndertakingPartyRole | Party that issues the undertaking (or counter-undertaking). | NaN | NaN |
| Demand | NaN | NaN | Document signed by the beneficiary demanding payment under a demand guarantee or standby letter of credit. | NaN | NaN |
| Demand | Undertaking | NaN | Undertaking for which a document signed by the beneficiary demanding payment is specified. | Undertaking | Demand |
| Demand | SubmissionDateTime | NaN | Date and time the demand is submitted. | ISODateTime | NaN |
| Demand | DemandAmount | NaN | Amount to be paid. | CurrencyAndAmount | NaN |
| Demand | Type | NaN | Type of demand, for example, pay or extend. | DemandTypeCode | NaN |
| Demand | TotalClaimAmount | NaN | Amount and currency of the total amount claimed (sum of the demand amount plus counterparty commission and charges). | CurrencyAndAmount | NaN |
| Demand | Payment | NaN | Payment of the demand. | PaymentObligation | PaymentSourceUndertakingDemand |
| Demand | AssociatedDocument | NaN | Documents which are associated with a demand. | UndertakingDocument | Demand |
| Discrepancy | NaN | NaN | Identification of a discrepancy. | NaN | NaN |
| Discrepancy | UndertakingStatusReason | NaN | Undertaking status reason for which discrepancy information is provided. | UndertakingStatusReason | Discrepancy |
| Discrepancy | Type | NaN | Type of discrepancy. | ExternalDiscrepancyCode | NaN |
| Discrepancy | Description | NaN | Description of the discrepancy. | Max2000Text | NaN |
| Expiry | NaN | NaN | Expiry parameters. | NaN | NaN |
| Expiry | ExpiryDateTime | NaN | Date and time when the expiry of the undertaking takes effect. | ISODateTime | NaN |
| Expiry | Undertaking | NaN | Undertaking for which expiry information is specified. | Undertaking | Expiry |
| Expiry | ExpiryCondition | NaN | Condition that indicates when the undertaking will cease to be available at the place for presentation. | Max2000Text | NaN |
| Expiry | OpenEndedIndicator | NaN | Specifies whether the expiry period is open ended. | YesNoIndicator | NaN |
| Expiry | ExpiryPlace | NaN | Place where the expiry of the undertaking takes effect. | Location | RelatedExpiry |
| UndertakingDocument | NaN | FinancialDocument | Document presented. | NaN | NaN |
| UndertakingDocument | DocumentType | NaN | Type of document. | ExternalUndertakingDocumentTypeCode | NaN |
| UndertakingDocument | Format | NaN | Format of the document. | ExternalDocumentFormatCode | NaN |
| UndertakingDocument | Undertaking | NaN | Undertaking for which document content is specified. | Undertaking | SpecifiedDocument |
| UndertakingDocument | CopyIndicator | NaN | Indicates whether the document is a copy. | YesNoIndicator | NaN |
| UndertakingDocument | Demand | NaN | Demand for which associated documents are specified. | Demand | AssociatedDocument |
| SettlementTimeRequest | NaN | NaN | Provides information on the requested settlement time(s) of the payment instruction. | NaN | NaN |
| SettlementTimeRequest | Payment | NaN | Payment for which settlement times are specified. | Payment | SettlementTimeRequest |
| SettlementTimeRequest | CLSTime | NaN | Time by which the amount of money must be credited, with confirmation, to the CLS Bank's account at the central bank. Usage: Time must be expressed in Central European Time (CET). | ISODateTime | NaN |
| SettlementTimeRequest | TillTime | NaN | Time until when the payment may be settled. | ISODateTime | NaN |
| SettlementTimeRequest | FromTime | NaN | Time as from when the payment may be settled. | ISODateTime | NaN |
| SettlementTimeRequest | RejectTime | NaN | Time by when the payment must be settled to avoid rejection. | ISODateTime | NaN |
| Assigner | NaN | InvestigationPartyRole | Party who assigns the case. | NaN | NaN |
| Assignee | NaN | InvestigationPartyRole | Party to which the case is assigned. | NaN | NaN |
| IntermediaryAgentRole | NaN | PaymentPartyRole | Agent between the debtor's agent and the creditor's agent. There can be several intermediary agents specified for the execution of a payment. | NaN | NaN |
| IntermediaryAgentRole | IntermediaryAgentRole | NaN | Specifies the settlement party which is followed by another party. | IntermediaryAgentRole | NextParty |
| IntermediaryAgentRole | NextParty | NaN | Next intermediary in the payment. | IntermediaryAgentRole | IntermediaryAgentRole |
| IntermediaryAgentRole | Position | NaN | Number used to show the relative position of an intermediary in the payment. | Number | NaN |
| MandateStatus | NaN | Status | Specifies whether a mandate is accepted or rejected. | NaN | NaN |
| MandateStatus | Accepted | NaN | Indicates whether the mandate request was accepted or rejected. | YesNoIndicator | NaN |
| MandateStatus | RejectReason | NaN | Specifies the reason for the rejection of a mandate request. | ExternalMandateReasonCode | NaN |
| MandateStatus | Mandate | NaN | Mandate for which a status applies. | Mandate | MandateStatus |
| MandateStatus | MandateReason | NaN | Specifies the reason for the request or status of a mandate. | ExternalMandateReasonCode | NaN |
| AmendmentOfUndertaking | NaN | NaN | Modification of an undertaking such as an guarantee or standby letter of credit. | NaN | NaN |
| AmendmentOfUndertaking | DateOfIssuance | NaN | Date the amendment is issued. | ISODateTime | NaN |
| AmendmentOfUndertaking | ChangeOfAmount | NaN | Decrease (negative) or increase (positive) of the undertaking as a result of the amendment. | CurrencyAndAmount | NaN |
| AmendmentOfUndertaking | Undertaking | NaN | Contents of an UndertakingAmendmentResponse message. | Undertaking | UndertakingAmendment |
| AmendmentOfUndertaking | BeneficiaryConsentRequestIndicator | NaN | Indicates whether or not a request for consent is required from the beneficiary. | YesNoIndicator | NaN |
| AmendmentOfUndertaking | AmendmentIdentification | NaN | Identification of the amendment. | Max35Text | NaN |
| UndertakingAmount | NaN | NaN | Amount of an undertaking such as a guarantee or standby letter of credit. | NaN | NaN |
| UndertakingAmount | Undertaking | NaN | Undertaking for which an amount is specified. | Undertaking | UndertakingAmount |
| UndertakingAmount | Amount | NaN | Amount of the undertaking. | CurrencyAndAmount | NaN |
| UndertakingAmount | Tolerance | NaN | Percentage (original or updated in case of amendment) by which the amount claimed under the undertaking may vary. | Tolerance | RelatedUndertakingAmount |
| UndertakingAmount | BalanceAmount | NaN | Calculated undertaking available balance amount resulting from the application of the variation amount. | CurrencyAndAmount | NaN |
| UndertakingAmount | Type | NaN | Qualification of the costs and other amounts covered by the amount of the undertaking. | AmountTypeCode | NaN |
| UndertakingAmount | Interest | NaN | Interest associated with the undertaking amount. | Interest | RelatedUndertakingAmount |
| UndertakingExtension | NaN | NaN | Specifies information related to the extension of an undertaking. | NaN | NaN |
| UndertakingExtension | Undertaking | NaN | Undertaking for which extension parameters are provided. | Undertaking | UndertakingExtension |
| UndertakingExtension | AutoExtensionPeriod | NaN | Requirement for a clause covering an automatic extension of the validity expiry date. | Max35Text | NaN |
| UndertakingExtension | AutoExtensionFinalExpiryDate | NaN | Date after which the undertaking will no longer be subject to automatic extension. | ISODate | NaN |
| UndertakingExtension | NonExtensionNoticePeriod | NaN | Minimum number of days of advance notification that must be given to indicate the undertaking will no longer be extended. | Number | NaN |
| UndertakingExtension | NonExtensionIndicator | NaN | Indicates whether the undertaking can be extended. | YesNoIndicator | NaN |
| UndertakingExtension | AutoExtensionNotificationPeriod | NaN | Minimum number of days of advance notification given to indicate the undertaking will no longer be automatically extended. | Number | NaN |
| UndertakingExtension | NotificationRecipientType | NaN | Type of party to whom the notice of non-extension is intended to be delivered, such as the applicant or beneficiary. | ExternalTypeOfPartyCode | NaN |
| UndertakingDeliveryToParty | NaN | UndertakingPartyRole | Party to which the original undertaking or amendment is intended to be delivered. | NaN | NaN |
| UndertakingAdvisingParty | NaN | UndertakingPartyRole | Party that advises the undertaking at the request of the issuer. For further clarification, reference the applicable rules to which the undertaking is subject. | NaN | NaN |
| UndertakingBeneficiary | NaN | UndertakingPartyRole | Party in whose favour the undertaking (or counter-undertaking) is issued. | NaN | NaN |
| UndertakingUltimateObligor | NaN | UndertakingPartyRole | Party that takes responsibility for indemnifying the issuer. | NaN | NaN |
| UndertakingUltimateObligor | CashAccount | NaN | Accounts nominated by the obligor for the settlement of the amount claimed, or for the settlement of charges or to record the liability amount related to the undertaking. | CashAccount | UltimateObligor |
| UndertakingApplicant | NaN | UndertakingPartyRole | Party named in an undertaking as the party on whose behalf the undertaking is issued. | NaN | NaN |
| UndertakingConfirmer | NaN | UndertakingPartyRole | Party that adds its confirmation to the undertaking. | NaN | NaN |
| Tolerance | NaN | NaN | Variance allowed on a quantity or on a price. | NaN | NaN |
| Tolerance | RelatedUndertakingAmount | NaN | Undertaking amount for which a tolerance is provided. | UndertakingAmount | Tolerance |
| Tolerance | Quantity | NaN | Quantity of product on which a tolerance is allowed. | ProductQuantity | QuantityTolerance |
| Tolerance | PlusPercent | NaN | Variance in percentage allowed over the agreed dimension. For example, plus 10 percent. | PercentageRate | NaN |
| Tolerance | MinusPercent | NaN | Variance in percentage allowed below the agreed dimension. For example, minus 10 percent. | PercentageRate | NaN |
| Tolerance | Price | NaN | Price on which a tolerance is allowed. | Price | PriceTolerance |
| ModelForm | NaN | NaN | Identification of a model form. | NaN | NaN |
| ModelForm | GovernanceRules | NaN | Rules governing an undertaking such as a guarantee or standby letter of credit. | GovernanceRules | ModelForm |
| ModelForm | Undertaking | NaN | Undertaking for which the model form is used. | Undertaking | ModelForm |
| ModelForm | Identification | NaN | Identification of the model form. | ExternalModelFormIdentificationCode | NaN |
| ModelForm | Version | NaN | Version of the model form. | Max35Text | NaN |
| ModelForm | RequestedWordingLanguage | NaN | Language of the standard wording provided by the issuer. | ISO2ALanguageCode | NaN |
| ModelForm | EffectiveDate | NaN | Date on which the use of the model form is effective. | ISODate | NaN |
| GovernanceRules | NaN | NaN | Rules governing an undertaking such as a guarantee or standby letter of credit. | NaN | NaN |
| GovernanceRules | ModelForm | NaN | Model form to which the governance rules apply. | ModelForm | GovernanceRules |
| GovernanceRules | Identification | NaN | Identification of the governance rules. | GovernanceIdentificationCode | NaN |
| GovernanceRules | ApplicableLaw | NaN | Law under which the undertaking has been issued. | Max35Text | NaN |
| GovernanceRules | Jurisdiction | NaN | Jurisdiction which applies to the governance rules. | Jurisdiction | GovernanceRules |
| GovernanceRules | PublicationAgency | NaN | Agency that publishes the governance rules. | Max35Text | NaN |
| Jurisdiction | NaN | NaN | Specifies the jurisdiction (country, county, state, province, city). | NaN | NaN |
| Jurisdiction | GovernanceRules | NaN | Rules for which an applicable law and a jurisdiction are specified. | GovernanceRules | Jurisdiction |
| Jurisdiction | Identification | NaN | Specifies the jurisdiction (country, county, state, province, city). | Location | RelatedJurisdiction |
| Jurisdiction | RegisteredSecurities | NaN | Securities which are registered under a specific jurisdiction. | Security | RegistrationJurisdiction |
| Jurisdiction | AssociatedStrategy | NaN | Strategy which is based on a specific jurisdiction. | JurisdictionStrategy | Jurisdiction |
| Jurisdiction | SecuritiesRestriction | NaN | Securities restrictions which apply in a specific jurisdiction. | SecuritiesRestriction | Jurisdiction |
| Jurisdiction | RelatedSecuritiesTax | NaN | Securities tax for which a jurisdiction is specified. | SecuritiesTax | Jurisdiction |
| Jurisdiction | RelatedMarket | NaN | Market to which the jurisdiction is related. | Market | Jurisdiction |
| Jurisdiction | RelatedAgreement | NaN | Agreement which is subject to a specific jurisdiction. | Agreement | Jurisdiction |
| UnderlyingTransaction | NaN | NaN | Reference information on a commercial obligation between the beneficiary and applicant for which an undertaking is issued. | NaN | NaN |
| UnderlyingTransaction | Undertaking | NaN | Undertaking issued to support a contract. | Undertaking | UnderlyingTransaction |
| UnderlyingTransaction | Type | NaN | Type of commercial obligation such as a tender, order, contract, etc. | ExternalUnderlyingTradeTransactionTypeCode | NaN |
| UnderlyingTransaction | Identification | NaN | Identification of the commercial obligation. | Max35Text | NaN |
| UnderlyingTransaction | IssueDate | NaN | Date the commercial obligation was issued or awarded. | ISODate | NaN |
| UnderlyingTransaction | TenderClosingDate | NaN | Date the tender closes. | ISODate | NaN |
| UnderlyingTransaction | TotalAmount | NaN | Amount of the commercial obligation. | CurrencyAndAmount | NaN |
| UnderlyingTransaction | ContractAmountPercentage | NaN | Percentage of the underlying contract covered by the undertaking. | PercentageRate | NaN |
| UnderlyingTransaction | CommercialTrade | NaN | Commercial trade for which an undertaking is issued. | CommercialTrade | RelatedUndertaking |
| AutomaticVariation | NaN | NaN | Predefined variations that may be attributable to an undertaking such as a guarantee or standby letter of credit. | NaN | NaN |
| AutomaticVariation | Undertaking | NaN | Undertaking for which a predefined variation is specified. | Undertaking | PredefinedVariation |
| AutomaticVariation | Type | NaN | Type of predefined variation. | VariationTypeCode | NaN |
| AutomaticVariation | VariationAmount | NaN | Variation specified as a monetary amount increase or decrease to the undertaking amount. | CurrencyAndAmount | NaN |
| AutomaticVariation | Trigger | NaN | Trigger that causes the variation to come into effect. | Trigger | AutomaticVariation |
| Trigger | NaN | NaN | Trigger that causes the variation to come into effect. | NaN | NaN |
| Trigger | AutomaticVariation | NaN | Variation which was triggered by the event. | AutomaticVariation | Trigger |
| Trigger | TriggerDate | NaN | Date on which the variation comes into effect. | ISODate | NaN |
| Trigger | TriggerEvent | NaN | Event that causes the variation to come into effect. | Max35Text | NaN |
| UndertakingPresenter | NaN | UndertakingPartyRole | Party that makes the presentation. | NaN | NaN |
| UndertakingPlaceOfPresentation | NaN | UndertakingPartyRole | Place at which the documents must be presented. | NaN | NaN |
| UndertakingPlaceOfPresentation | PresentationUnderConfirmation | NaN | Specifies the type of party to which a presentation under confirmation is required. | PresentationPartyCode | NaN |
| UndertakingInstructingParty | NaN | UndertakingPartyRole | Party that instructs the issuance of the undertaking. | NaN | NaN |
| TreasuryTradeSettlementStatus | NaN | Status | Specifies the status of a treasury trade at a specified time. | NaN | NaN |
| TreasuryTradeSettlementStatus | TradeStatus | NaN | Status of a treasury trade in a central matching/settlement system. | TradeStatusCode | NaN |
| TreasuryTradeSettlementStatus | AllegedTrade | NaN | Specifies whether a trade is alleged (notified by the counterparty) or not. | YesNoIndicator | NaN |
| TreasuryTradeSettlementStatus | TreasuryTrade | NaN | Treasury trade for which a settlement status is provided. | TreasuryTrade | TreasuryTradeSettlementStatus |
| TreasuryTradeSettlementStatus | Settlement | NaN | Specifies the status of a settlement eg rejected, settled or awaiting authorisation. | SettlementStatusCode | NaN |
| TreasuryTradeSettlementStatus | RejectedAmount | NaN | Amount that cannot be settled for instance by a settlement system. | ActiveOrHistoricCurrencyAndAmount | NaN |
| TreasuryTradeSettlementStatus | SettlementSuspended | NaN | Cash settlement is suspended. | YesNoIndicator | NaN |
| TreasuryTradeSettlementStatus | PendingSettlement | NaN | Cash settlement is pending. | YesNoIndicator | NaN |
| TreasuryTradeSettlementStatus | SettlementDate | NaN | Date on which the trade is actually settled. | ISODateTime | NaN |
| TreasuryTradeSettlementStatus | WithdrawalReason | NaN | Reason that an alleged trade is withdrawn. | Max35Text | NaN |
| ProductCategory | NaN | NaN | Specifies the category of the product. | NaN | NaN |
| ProductCategory | Product | NaN | Specifies the product for which a category is specified. | Product | ProductCategory |
| ProductCategory | Type | NaN | Specifies the type of product category by means of a code. | ProductCategoryCode | NaN |
| ProductCategory | Category | NaN | Specifies the category of a product. | Max35Text | NaN |
| ProductCategory | RelatedCardPaymentValidation | NaN | Validation process which declined a product code. | CardPaymentValidation | DeclinedProductCode |
| ClearingBrokerIdentification | NaN | NaN | Reference number assigned by the clearing broker. A distinction can be made between the reference for the Central Counterparty (CCP) leg and the reference for the client leg of the transaction. | NaN | NaN |
| ClearingBrokerIdentification | RelatedTradeIdentification | NaN | Other identifications of a trade for which clearing broker identifications are provided. | TradeIdentification | ClearingBrokerIdentification |
| ClearingBrokerIdentification | SideIndicator | NaN | Distinguishes the client leg from the central counterpatry (CCP) leg in the clearing broker identification. | Max35Text | NaN |
| ClearingBrokerIdentification | Identification | NaN | Identification assigned by the clearing broker. | Max35Text | NaN |
| ForeignExchangeSwap | NaN | TreasuryTrade | Combination of two foreign exchange trades, in opposite directions, for different value dates and for the same pair(s) of currencies. | NaN | NaN |
| ForeignExchangeSwap | LinkSwapIdentification | NaN | Correlation identification for the near and far leg of a swap transaction. | Max35Text | NaN |
| ForeignExchangeSwap | SwapLeg | NaN | One-side of a pair of foreign exchange trades executed as part of a swap agreement. | ForeignExchangeTrade | RelatedSwap |
| SubmittingPartyRole | NaN | SystemPartyRole | Specifies the party which submits trade data sets to a system or to a counterparty. | NaN | NaN |
| TreasuryTradePartyRole | NaN | TradePartyRole | Role played by a party in the context of a treasury trade. | NaN | NaN |
| TreasuryTradePartyRole | TreasuryTrade | NaN | Identifies the treasury trade for which a party plays a role. | TreasuryTrade | PartyRole |
| TreasuryTradingParty | NaN | TreasuryTradePartyRole | Party that negotiates and executes treasury transactions on its behalf or on behalf of another party. | NaN | NaN |
| TreasuryTradingParty | InvestmentFund | NaN | Specifies the fund for which a treasury trade is executed. | InvestmentFund | TreasuryTradingParty |
| ReceivingAgent | NaN | SecuritiesSettlementPartyRole | Party that receives securities from the delivering agent at the place of settlement. For example, a central securities depository. | NaN | NaN |
| Negotiation | NaN | NaN | Decision making on the transfer of a financial instrument. | NaN | NaN |
| Negotiation | TradingMethod | NaN | Method used by the trading parties to negotiate and/or execute a deal. | TradingMethodCode | NaN |
| Negotiation | TradeExecution | NaN | Execution of a trade as a result of a successful negotiation between two trading parties. | Trade | RelatedNegotiation |
| Negotiation | TradingSystem | NaN | Electronic system through which parties are able to negotiate trades. | System | Negotiation |
| Negotiation | NegotiationIdentification | NaN | Reference of a negotiation. | Max35Text | NaN |
| Negotiation | Quote | NaN | Quote details shown in a negotiation process. | Quote | RelatedNegotiation |
| Negotiation | IndicationOfInterest | NaN | Indication of interest process which is the start of the negotiation. | BuyOrSellIndicationOfInterest | NegotiationDetails |
| Negotiation | SecuritiesOrder | NaN | Result of a successful negotiation. | SecuritiesOrder | RelatedNegotiation |
| LiquidityManagementLimit | NaN | Limit | Cash management feature limiting the amount of liquidity needed to perform clearing and settlement operations. At any point in time during the process, the limit imposes the maximum amount of liquidity available for operations concerning the system or other managed elements, for example, transaction amount or counterparty. | NaN | NaN |
| LiquidityManagementLimit | VolatilityMargin | NaN | Margin used to decrease long positions and increase short positions for the calculation of the limit usage. | PercentageRate | NaN |
| LiquidityManagementLimit | CurrencyExchange | NaN | Exchange rate used in the calculation of the limit when different currencies are involved. | CurrencyExchange | RelatedLimitManagement |
| LiquidityManagementLimit | RelatedCashServices | NaN | Cash management services which provide standing liquidity management facilities. | CashManagementService | LiquidityManagementLimit |
| LiquidityManagementLimit | LiquidityLimitType | NaN | Type of liquidity management limit. | LiquidityLimitTypeCode | NaN |
| LiquidityManagementLimit | RequiredAmount | NaN | Amount required to cover the needs of liquidity management. | CurrencyAndAmount | NaN |
| Authentication | NaN | NaN | Data related to the authentication of the cardholder. | NaN | NaN |
| Authentication | Cardholder | NaN | Cardholder for which an authentication is provided. | CardholderRole | Authentication |
| Authentication | AuthenticationMethod | NaN | Method used to authenticate a person. | AuthenticationMethodCode | NaN |
| Authentication | AuthenticationEntity | NaN | Entity or object in charge of verifying the person authenticity. | AuthenticationEntityCode | NaN |
| Authentication | AuthenticationValue | NaN | Value used to authenticate the owner of the payment card. | Max70Text | NaN |
| Authentication | PINFormat | NaN | Encrypted personal identification number (PIN) format. | PINFormatCode | NaN |
| Authentication | PIN | NaN | Personal Identification Number (PIN) for authentication. | Max140Binary | NaN |
| Authentication | AuthenticationSupport | NaN | This indicator identifies whether person authentication is supported and data is available. | Max35Text | NaN |
| Authentication | CollectionIndicator | NaN | Identifies in electronic commerce transactions whether customer authentication is supported and data is available. | Max35Text | NaN |
| Authentication | Mandate | NaN | Specifies the mandate related to the transport authentication details mandate. | Mandate | Authentication |
| Authentication | AuthenticationResult | NaN | Specifies the result of the authentication. | AuthenticationResultCode | NaN |
| Authentication | Exemption | NaN | If Strong Customer Authentication is not mandated to process the transaction, this message element must identify the reason of exemption. | ExemptionCode | NaN |
| MerchantRole | NaN | CardPaymentPartyRole | Party performing the card payment transaction. | NaN | NaN |
| MerchantRole | MerchantCategoryCode | NaN | Category code conform to ISO 18245, related to the type of services or goods the merchant provides for the transaction. | Min3Max4Text | NaN |
| MerchantRole | MerchantIdentification | NaN | Number that identifies the merchant to the card issuer. | Max35Text | NaN |
| CreditorAgentRole | NaN | PaymentPartyRole | Financial institution servicing an account for the creditor. | NaN | NaN |
| InvoiceFinancingPartyRole | NaN | InvoicePartyRole | Role played by a party in the context of financing an invoice. | NaN | NaN |
| InvoiceFinancingPartyRole | CashAccount | NaN | Account used in the financing process. | CashAccount | RelatedInvoiceFinancingPartyRole |
| InvoiceFinancingPartyRole | InvoiceFinancingTransaction | NaN | Identifies the invoice financing transaction for which a party plays a role. | InvoiceFinancingAgreement | InvoiceFinancingPartyRole |
| IntermediateAgentRole | NaN | InvoiceFinancingPartyRole | Financial institution that receives a financing request from the financing requestor and forwards it to the first agent for execution. | NaN | NaN |
| AcceptorConfiguration | NaN | NaN | Acceptor parameters to be downloaded from the terminal management system. | NaN | NaN |
| AcceptorConfiguration | ApplicationIdentification | NaN | Identification of the payment application. | Max35Text | NaN |
| AcceptorConfiguration | FinancialCapture | NaN | Mode for the financial capture of the transaction by the acquirer. | FinancialCaptureCode | NaN |
| AcceptorConfiguration | BatchTransferContent | NaN | Types of transaction to include in the batch. | BatchTransactionTypeCode | NaN |
| AcceptorConfiguration | ExchangePolicy | NaN | Exchange policy between parties. | ExchangePolicyCode | NaN |
| AcceptorConfiguration | MaximumNumber | NaN | Maximum number of transactions without exchange. | Number | NaN |
| AcceptorConfiguration | MaximumAmount | NaN | Maximum cumulative amount of the transactions without exchange. | ImpliedCurrencyAndAmount | NaN |
| AcceptorConfiguration | ReconciliationByAcquirer | NaN | Indicates the reconciliation period is assigned by the acquirer instead of the acceptor. | TrueFalseIndicator | NaN |
| AcceptorConfiguration | TotalsPerCurrency | NaN | Indicates the reconciliation total amounts are computed per currency. | TrueFalseIndicator | NaN |
| AcceptorConfiguration | ProtectCardData | NaN | Indicator to require protection of sensitive card data in messages. | TrueFalseIndicator | NaN |
| AcceptorConfiguration | RetailerParameters | NaN | Acceptor parameters dedicated to the retailer. | Max10000Binary | NaN |
| AcceptorConfiguration | ApplicationParameters | NaN | Configuration parameters attached to the payment application. | Max10000Binary | NaN |
| AcceptorConfiguration | TerminalManagementSystem | NaN | Terminal management system for which an acceptor configuration is provided. | TerminalManagementSystem | AcceptorConfiguration |
| AcceptorConfiguration | ApplicationVersion | NaN | Version of the application. | Max35Text | NaN |
| TerminalManagementAction | NaN | NaN | Terminal management action to be performed by the point of interaction. | NaN | NaN |
| TerminalManagementAction | Type | NaN | Types of terminal management action to be performed by a point of interaction. | TerminalManagementActionCode | NaN |
| TerminalManagementAction | Trigger | NaN | Event to start the terminal management action by the point of interaction (POI). | TerminalManagementActionTriggerCode | NaN |
| TerminalManagementAction | AdditionalProcess | NaN | Additional process to perform before starting or after the terminal management action by the point of interaction (POI). | TerminalManagementAdditionalProcessCode | NaN |
| TerminalManagementAction | ActionResult | NaN | List of action result codes. | TerminalManagementActionResultCode | NaN |
| TerminalManagementAction | ActionToProcess | NaN | Action to be processed. | TerminalManagementErrorActionCode | NaN |
| TerminalManagementAction | TerminalManagementSystem | NaN | Terminal management system from which an action took place | TerminalManagementSystem | Action |
| NetworkAccess | NaN | NaN | Parameters used to access a network. | NaN | NaN |
| NetworkAccess | HostIPAddress | NaN | IP address of the host. | Max35Text | NaN |
| NetworkAccess | HostPortNumber | NaN | Port number of the host. | Number | NaN |
| NetworkAccess | UserName | NaN | User name identifying the party accessing the network. | Max35Text | NaN |
| NetworkAccess | AccessCode | NaN | Password authenticating the user | Max35Text | NaN |
| NetworkAccess | ClientCertificate | NaN | Client certificate chain. | SecurityCertificate | NetworkAccess |
| NetworkAccess | TerminalManagementSystem | NaN | Terminal Management System which uses the network. | TerminalManagementSystem | NetworkAccess |
| NetworkAccess | NetworkAddress | NaN | Address used to reach the network on which a message will be carried. | Max1025Text | NaN |
| TerminalManagementSystem | NaN | System | Terminal management system (TMS), has in charge the maintenance of the terminal, including monitoring, software update, configuration parameters management. | NaN | NaN |
| TerminalManagementSystem | AcceptorConfiguration | NaN | Acceptor parameters to be downloaded from the terminal management system. | AcceptorConfiguration | TerminalManagementSystem |
| TerminalManagementSystem | NetworkAccess | NaN | Parameters used to access a network. | NetworkAccess | TerminalManagementSystem |
| TerminalManagementSystem | CardPaymentAcquiring | NaN | Process for which a TMS trigger is specified. | CardPaymentAcquiring | TMSTrigger |
| TerminalManagementSystem | ContactLevel | NaN | Level of urgency in contacting the maintenance. | TMSContactLevelCode | NaN |
| TerminalManagementSystem | ContactDateTime | NaN | Date and time for calling the maintenance. | ISODateTime | NaN |
| TerminalManagementSystem | TerminalManagerRole | NaN | Identifies the party which is the terminal manager (TM) to contact for the maintenance. | TerminalManagerRole | TerminalManagementSystem |
| TerminalManagementSystem | ControlledPointOfInteraction | NaN | Specifies each point of interaction controlled by a TMS. | PointOfInteraction | ControllingTerminalManagementSystem |
| TerminalManagementSystem | Action | NaN | Terminal management action to be performed by the point of interaction. | TerminalManagementAction | TerminalManagementSystem |
| CardPaymentStatus | NaN | Status | Status of a payment by card. | NaN | NaN |
| CardPaymentStatus | RejectionReason | NaN | Reason of the rejection of a request or an advice. | RejectReasonCode | NaN |
| CardPaymentStatus | FailureReason | NaN | List of incidents during the transaction. | FailureReasonCode | NaN |
| CardPaymentStatus | CardPayment | NaN | Card payment for which a status is provided. | CardPayment | CardPaymentStatus |
| AcquirerRole | NaN | CardPaymentPartyRole | Entity acquiring card payment transactions. | NaN | NaN |
| AuthorisationEntity | NaN | CardPaymentPartyRole | Party which has delivered or declined the authorisation. | NaN | NaN |
| Response | NaN | NaN | Response of a requested service. | NaN | NaN |
| Response | ResponseReason | NaN | Detailed result of the transaction. | Max35Text | NaN |
| Response | RelatedCardPaymentValidation | NaN | Validation process to which a response is given. | CardPaymentValidation | Response |
| Response | ResponseToAuthorisation | NaN | Response from the issuer to the authorisation. | ResponseCode | NaN |
| CardPaymentValidation | NaN | NaN | Results and parameters of the card payment verification. | NaN | NaN |
| CardPaymentValidation | TransactionSuccess | NaN | Outcome of the transaction at the acceptor. | TrueFalseIndicator | NaN |
| CardPaymentValidation | MerchantOverride | NaN | Indicate that the acceptor has forced the transaction in spite of the authorisation result (online or offline), or incident to complete the transaction. | TrueFalseIndicator | NaN |
| CardPaymentValidation | ValidityDate | NaN | Transaction authorisation deadline to complete the related payment. | ISODate | NaN |
| CardPaymentValidation | CardPayment | NaN | Card payment to which the validation process applies. | CardPaymentAcquiring | Validation |
| CardPaymentValidation | Response | NaN | Response to an authorisation request. | Response | RelatedCardPaymentValidation |
| CardPaymentValidation | AuthorisationCode | NaN | Value assigned by the authorising party. | Min6Max8Text | NaN |
| CardPaymentValidation | OnLineReason | NaN | Reason to process an online authorisation. | OnLineReasonCode | NaN |
| CardPaymentValidation | Balance | NaN | Balance of the account attached to the payment card. | CashBalance | RelatedCardPaymentValidationProcess |
| CardPaymentValidation | CardholderAddressVerificationResult | NaN | Result of the cardholder verification address checks on the street number and the postal code. | CardholderAddressVerificationResultCode | NaN |
| CardPaymentValidation | CSCResult | NaN | Result of the printed CSC (Card Security Code) validation. | CSCResultCode | NaN |
| CardPaymentValidation | DeclinedProductCode | NaN | Product code for which the payment authorisation was declined. | ProductCategory | RelatedCardPaymentValidation |
| CardPaymentValidation | ElectronicCommerceAuthenticationResult | NaN | Result of an e-commerce authentication process. | Max500Text | NaN |
| CardPaymentValidation | FailureReason | NaN | Incident occuring during the transaction. | FailureReasonCode | NaN |
| CardPaymentValidation | Signature | NaN | Signature of the message to display or print. | Signature | CardPaymentValidation |
| FundsCashFlow | NaN | NaN | Cash movements from or to a fund as a result of investment funds transactions, for example, subscriptions or redemptions. | NaN | NaN |
| FundsCashFlow | ExceptionalCashFlowIndicator | NaN | Indicates whether the cash flow is exceptional , eg, extraordinary cash amounts in or out. | YesNoIndicator | NaN |
| FundsCashFlow | FlowDirection | NaN | Specifies the direction of the cash flow from the perspective of the fund. | FlowDirectionTypeCode | NaN |
| FundsCashFlow | FundSubscriptionAccountEntry | NaN | Account entry which is linked to a fund subscription process. | BookEntry | FundSubscriptionCashInFlow |
| FundsCashFlow | FundRedemptionAccountEntry | NaN | Account entry which is linked to a fund redemption process. | BookEntry | FundRedemptionCashOutFlow |
| FundsCashFlow | RelatedOrder | NaN | Trade which is the source for the calculation of the cash flow movements. | InvestmentFundOrderExecution | CashFlow |
| FundsCashFlow | NetIndicator | NaN | Indicates whether the cash flow is the result of netting. | YesNoIndicator | NaN |
| FundsCashFlow | NetAssetValueCalculation | NaN | Net asset value incorporating the net cash flow for a valuation date. | NetAssetValueCalculation | FundsCashFlow |
| FundsCashFlow | CashFlowQuantity | NaN | Value and quantity of the cash flow. | SecuritiesQuantity | RelatedCashFlow |
| SecuritiesOrderStatus | NaN | Status | Status of a securities order or of the processing of a securities order. | NaN | NaN |
| SecuritiesOrderStatus | ConfirmationRejectedStatusReason | NaN | Specifies the reason for a confirmation rejected status. | RejectedConfirmationStatusReasonCode | NaN |
| SecuritiesOrderStatus | ConfirmationStatus | NaN | Status of the confirmation of a status order. | OrderConfirmationStatusCode | NaN |
| SecuritiesOrderStatus | CancellationStatus | NaN | Status of the cancellation of a securities order. | OrderCancellationStatusCode | NaN |
| SecuritiesOrderStatus | PartiallySettledStatusReason | NaN | Reason for the partially settled status. | PartiallySettledStatusReasonCode | NaN |
| SecuritiesOrderStatus | SuspendedStatusReason | NaN | Reason for the suspended status. | SuspendedStatusReasonCode | NaN |
| SecuritiesOrderStatus | ListOrderStatus | NaN | Specifies the status of a list order. | ListStatusTypeCode | NaN |
| SecuritiesOrderStatus | SecuritiesOrder | NaN | Order for which a status is specified. | SecuritiesOrder | Status |
| SecuritiesOrderStatus | InvestmentFundOrder | NaN | Investment fund order for which a status is provided. | InvestmentFundOrder | OrderStatus |
| SecuritiesOrderStatus | CumulativeQuantity | NaN | Total quantity (for instance number of shares) filled. | SecuritiesQuantity | SecuritiesOrderStatus |
| SecuritiesOrderStatus | RemainingQuantity | NaN | Quantity opened for further execution. | SecuritiesQuantity | RelatedOrderStatus |
| SecuritiesOrderStatus | ConditionallyAcceptedStatus | NaN | Reason for the conditionally accepted status. | ConditionallyAcceptedStatusReasonCode | NaN |
| SecuritiesOrderStatus | OrderStatus | NaN | Indicates the status of an order at a specific point in time. | OrderStatusCode | NaN |
| RedemptionOrder | NaN | InvestmentFundOrder | Instruction from an investor to sell investment fund units back to the fund. | NaN | NaN |
| RedemptionOrder | HoldingsRedemptionRate | NaN | Portion of the investor's holdings, in a specific investment fund/ fund class, that is redeemed. | PercentageRate | NaN |
| SwitchOrder | NaN | InvestmentFundOrder | Transfer from one investment fund/fund class to another investment fund or investment fund class by the investor. A switch is composed of one or several subscription legs, and one or several redemption legs. | NaN | NaN |
| SwitchOrder | AdditionalCashIn | NaN | Additional amount of money paid by the investor in addition to the switch redemption amount. | CurrencyAndAmount | NaN |
| SwitchOrder | ResultingCashOut | NaN | Amount of money that results from a switch-out, that is not reinvested in another investment fund, and is repaid to the investor. | CurrencyAndAmount | NaN |
| SwitchOrder | TotalRedemptionAmount | NaN | Amount of money used to derive the quantity of investment fund units to be redeemed. | CurrencyAndAmount | NaN |
| SwitchOrder | TotalSubscriptionAmount | NaN | Amount of money used to derive the quantity of investment fund units to be subscribed. | CurrencyAndAmount | NaN |
| SwitchOrder | RedemptionLeg | NaN | Part of an investment fund switch order that is a redemption. | SwitchRedemptionLeg | RedemptionRelatedSwitchOrder |
| SwitchOrder | SubscriptionLeg | NaN | Part of an investment fund switch order that is a subscription. | SwitchSubscriptionLeg | SubscriptionRelatedSwitchOrder |
| RedemptionExecution | NaN | InvestmentFundOrderExecution | Execution of a redemption order. | NaN | NaN |
| RedemptionExecution | RedeemedNetAmount | NaN | Net amount of money paid to the investor as a result of the redemption. | CurrencyAndAmount | NaN |
| RedemptionExecution | PartialRedemptionWithholdingAmount | NaN | Amount retained by the Fund and paid out later at a time decided by the Fund. | CurrencyAndAmount | NaN |
| RedemptionExecution | SettlementDate | NaN | Date on which the amount of money for the redemption is paid. | ISODate | NaN |
| SubscriptionOrder | NaN | InvestmentFundOrder | Order to invest the investor's principal in an investment fund. | NaN | NaN |
| SwitchExecution | NaN | InvestmentFundOrderExecution | Execution of a switch order. | NaN | NaN |
| SwitchExecution | RedemptionLeg | NaN | Redemption leg of a switch order execution. | SwitchExecutionRedemptionLeg | RelatedSwitchExecution |
| SwitchExecution | SubscriptionLeg | NaN | Subscription leg of a switch order execution. | SwitchExecutionSubscriptionLeg | RelatedSwitchExecution |
| SwitchRedemptionLeg | NaN | RedemptionOrder | Redemption leg, or switch-out, of a switch transaction. | NaN | NaN |
| SwitchRedemptionLeg | RedemptionRelatedSwitchOrder | NaN | Switch order to which the redemption leg refers. | SwitchOrder | RedemptionLeg |
| SwitchRedemptionLeg | PercentageOfTotalSubscriptionAmount | NaN | Percentage of the total switch amount (buy-driven) to be invested in a particular investment fund or investment fund class. | PercentageRate | NaN |
| SwitchSubscriptionLeg | NaN | SubscriptionOrder | Subscription leg, or switch-in, of a switch order. | NaN | NaN |
| SwitchSubscriptionLeg | SubscriptionRelatedSwitchOrder | NaN | Switch order to which the subscription leg refers. | SwitchOrder | SubscriptionLeg |
| SwitchSubscriptionLeg | PercentageOfTotalRedemptionAmount | NaN | Percentage of the total redemption amount used for the subscription in an investment fund or investment fund class. | PercentageRate | NaN |
| SwitchExecutionRedemptionLeg | NaN | RedemptionExecution | Execution of the redemption part, in a switch between investment funds or investment fund classes. | NaN | NaN |
| SwitchExecutionRedemptionLeg | RelatedSwitchExecution | NaN | Switch execution process for which a redemption leg is specified. | SwitchExecution | RedemptionLeg |
| SwitchExecutionRedemptionLeg | PercentageOfTotalSubscriptionAmount | NaN | Percentage of the total amount subscribed, and that came from redemption of investment funds or investment fund classes. | PercentageRate | NaN |
| SwitchExecutionSubscriptionLeg | NaN | SubscriptionExecution | Execution of the subscription part, in a switch between investment funds or investment fund classes. | NaN | NaN |
| SwitchExecutionSubscriptionLeg | RelatedSwitchExecution | NaN | Switch execution process for which a subcription leg is specified. | SwitchExecution | SubscriptionLeg |
| SwitchExecutionSubscriptionLeg | PercentageOfTotalRedemptionAmount | NaN | Percentage of the total redemption amount used for the subscription in an investment fund or investment fund class. | PercentageRate | NaN |
| NonFinancialInstitution | NaN | Organisation | An organisation primarily established to offer and perform services other than financial services. | NaN | NaN |
| DebitAuthorisation | NaN | NaN | Permission given by an account owner to debit its account as the result of a cancelled payment. The authoriser is the party whose account was credited as the result of a payment instruction. | NaN | NaN |
| DebitAuthorisation | ValueDateToDebit | NaN | Value date for debiting the amount. | ISODate | NaN |
| DebitAuthorisation | DebitAuthorisationDecision | NaN | Code expressing the decision taken by the account owner relative to the request for debit authorization. | YesNoIndicator | NaN |
| DebitAuthorisation | AmountToDebit | NaN | Specifies the amount to debit when the amount is lower than the amount of the underlying transaction. | CurrencyAndAmount | NaN |
| DebitAuthorisation | Reason | NaN | Justification of the (partial) debit authorisation. | Max140Text | NaN |
| DebitAuthorisation | AuthorisedReturn | NaN | Authorisation given by a credited party to return the payment which was the reason for the credit and therefore to debit its account. | Payment | RelatedDebitAuthorisation |
| DebitAuthorisation | RelatedInvestigationCaseResolution | NaN | Payment investigation case resolution which is the source of the debit authorisation. | PaymentInvestigationCaseResolution | DebitAuthorisationConfirmation |
| FirstAgentRole | NaN | InvoiceFinancingPartyRole | Organisation offering invoice financing services. | NaN | NaN |
| InvestigationResolution | NaN | NaN | Specifies the actions taken as a result of an investigation. | NaN | NaN |
| InvestigationResolution | InvestigationCase | NaN | Case for which a resolution is provided. | InvestigationCase | InvestigationResolution |
| InvestigationResolution | InvestigationCaseReference | NaN | Identifies the case for which a resolution is provided. | Max35Text | NaN |
| PaymentInvestigationCaseResolution | NaN | InvestigationResolution | Specifies the status of an investigation case and the actions taken as a result of this status. | NaN | NaN |
| PaymentInvestigationCaseResolution | InvestigationStatus | NaN | Status of the investigation. | InvestigationExecutionConfirmationCode | NaN |
| PaymentInvestigationCaseResolution | DebitAuthorisationConfirmation | NaN | Permission given by an account owner to debit its account as the result of a cancelled payment. The authoriser is the party whose account was credited as the result of a payment instruction. | DebitAuthorisation | RelatedInvestigationCaseResolution |
| PaymentInvestigationCaseResolution | CoverCorrection | NaN | Elements provided to correct the cover instruction for the resolution of the claim non receipt initiated case. | CashSettlement | RelatedInvestigationCase |
| PaymentInvestigationCaseResolution | EntryCorrection | NaN | The case resolution leads to the correction of a cash entry into an account. | CashEntry | RelatedInvestigationCaseResolution |
| PaymentInvestigationCaseResolution | PaymentCorrection | NaN | The case resolution leads to the correction of a payment. | Payment | RelatedInvestigationCaseResolution |
| PaymentInvestigationCaseResolution | PaymentExecutionCorrection | NaN | The case resolution leads to the correction of a payment execution. | PaymentExecution | RelatedInvestigationCaseResolution |
| PaymentInvestigationCaseResolution | InvestigationCaseRejection | NaN | Specifies the rejection of an activity linked to a payment. The rejected activity may be the assignment of an investigation case, the cancellation or the modification of a payment. | PaymentInvestigationCaseRejection | RelatedInvestigationCaseResolution |
| PaymentInvestigationCaseResolution | DuplicateCase | NaN | Outcome that results in closing a case as duplicate because the same issue has been reported by another party. | DuplicateCase | RelatedCaseResolution |
| PaymentInvestigationCaseRejection | NaN | NaN | Specifies the rejection of an activity linked to a payment. The rejected activity may be the assignment of an investigation case, the cancellation or the modification of a payment. | NaN | NaN |
| PaymentInvestigationCaseRejection | RejectedModification | NaN | Reason for the rejection of a modification request. | PaymentModificationRejectionV2Code | NaN |
| PaymentInvestigationCaseRejection | RejectedCancellation | NaN | Justification for the rejection of the cancellation. | PaymentCancellationRejectionCode | NaN |
| PaymentInvestigationCaseRejection | RejectedCancellationReason | NaN | Free text justification for rejecting a cancellation. | Max140Text | NaN |
| PaymentInvestigationCaseRejection | AssignmentCancellationConfirmation | NaN | If yes, it means the cancellation of the assignment is confirmed.If no, it means the cancellation of the assignment is rejected and the investigation process will continue. | YesNoIndicator | NaN |
| PaymentInvestigationCaseRejection | RejectionReason | NaN | Reason for the rejection of a case assignment, in a coded form. | CaseAssignmentRejectionCode | NaN |
| PaymentInvestigationCaseRejection | RelatedInvestigationCaseResolution | NaN | Resolution which consists in rejecting the case. | PaymentInvestigationCaseResolution | InvestigationCaseRejection |
| PaymentInvestigationCaseRejection | InvestigationRejection | NaN | Reason for the rejection of a case assignment. | InvestigationRejectionCode | NaN |
| Reassignment | NaN | InvestigationResolution | Action that consists in forwarding an investigation case assignment to another party which becomes the new assignee. | NaN | NaN |
| Reassignment | Justification | NaN | Justification for the forward action. | CaseForwardingNotificationCode | NaN |
| Reassignment | ReassignedCase | NaN | Specifies the investigation case that is assigned. | InvestigationCase | Reassignment |
| InvestigationCaseStatus | NaN | Status | Status of an investigation case. | NaN | NaN |
| InvestigationCaseStatus | CaseStatus | NaN | Status of the case. | CaseStatusCode | NaN |
| InvestigationCaseStatus | InvestigationCase | NaN | Case for which a status is reported. | InvestigationCase | Status |
| MeetingNotice | NaN | NaN | Information about the general meeting, specifying the participation requirements and the voting procedures. Alternatively, it may indicate where such information may be obtained. | NaN | NaN |
| MeetingNotice | RelatedServicing | NaN | Meeting servicing process which comprises the notification of a meeting. | MeetingServicing | MeetingNotice |
| MeetingNotice | BeneficialOwnerExclusiveIndicator | NaN | Indicates that only the beneficial owner may participate in the event, ie no proxy or nominee voting is allowed. | YesNoIndicator | NaN |
| MeetingNotice | ParticipationMethod | NaN | Method of voting participation to the general meeting and related voting deadline per method of participation. | VotingParticipationMethodCode | NaN |
| CorporateActionPartyRole | NaN | Role | Role played by a party in the context of a corporate action. | NaN | NaN |
| CorporateActionPartyRole | CorporateActionEvent | NaN | Specifies the event for which a party plays a role. | CorporateActionEvent | CorporateActionPartyRole |
| CorporateActionPartyRole | Account | NaN | Unambiguous identification of the account used in the context of the corporate action party role. | Account | RelatedCorporateActionPartyRole |
| MeetingPartyRole | NaN | CorporateActionPartyRole | Role played by a party in the context of a meeting. | NaN | NaN |
| MeetingPartyRole | Meeting | NaN | Specifies the meeting for which a party plays a role. | Meeting | PartyRole |
| MeetingInitiatorRole | NaN | MeetingPartyRole | Specifies a party, other than the issuer, that requested that the meeting take place. It may be a court of justice or an association of security holders. | NaN | NaN |
| AssignedProxyRole | NaN | MeetingPartyRole | Party appointed by the rights holder to attend a meeting and vote in its name. The proxy can be the chairman of the meeting or another party selected by the issuer. The proxy can also be a third party selected by the rights holder. The proxy can be assigned by a specific instruction or pre-assigned by the issuer of the meeting. | NaN | NaN |
| AssignedProxyRole | ProxyPerson | NaN | Specifies the person who is the assigned proxy for a meeting. | Person | RelatedRole |
| AssignedProxyRole | PreAssignedProxyRole | NaN | Identifies a proxy that has been assigned by the issuer of the meeting. | Person | PreAssignedProxyPerson |
| ProxyAppointment | NaN | NaN | Specifies that a proxy has been appointed to represent a party authorised to vote at a general meeting. | NaN | NaN |
| ProxyAppointment | ProxyType | NaN | Specifies the type of proxy. | ProxyTypeCode | NaN |
| ProxyAppointment | RelatedMeetingInstruction | NaN | Instruction in which the parameters for proxy appointment are included. | InstructionForMeeting | ProxyAppointment |
| ProxyAppointment | Identification | NaN | Uniquely identifies a proxy card. | Max35Text | NaN |
| ProxyAppointment | Vote | NaN | Voting instructions for the proxy. | VoteInstructionRequest | RelatedProxyAppointment |
| ProxyAppointment | AdditionalParticipationCost | NaN | Aditional fee associated to the participation of a proxy person such as hotel expenses. | CurrencyAndAmount | NaN |
| ResolutionProposal | NaN | NaN | Conditions that must be met to propose a resolution. | NaN | NaN |
| ResolutionProposal | ResolutionProposalThreshold | NaN | Specifies the minimum stake in share capital or cash value or number of security holders required to table resolutions. | Max350Text | NaN |
| ResolutionProposal | ResolutionProposalThresholdPercentage | NaN | Specifies the minimum stake in share capital or cash value or number of security holders required to table resolutions. This minimum is expressed as a percentage. | PercentageRate | NaN |
| ResolutionProposal | Meeting | NaN | Meeting for which conditions for proposing a resolution are specified. | Meeting | ResolutionProposalConditions |
| IssuerMeeting | NaN | Meeting | Information about the meeting, specifying the participation requirements and the voting procedures. | NaN | NaN |
| IssuerMeeting | IssuerMeetingIdentification | NaN | Identification assigned to a meeting by the issuer. It must be unique for the issuer. | Max35Text | NaN |
| IssuerMeeting | NomineePowerOfAttorneyIndicator | NaN | Indicates that a power of attorney must be provided by the beneficial owner to the nominee in order for the nominee to vote on behalf of the beneficial owner. | YesNoIndicator | NaN |
| IssuerMeeting | NomineeVotingIndicator | NaN | Indicates whether an agent can vote on behalf of the beneficial owners. | YesNoIndicator | NaN |
| IssuerMeeting | NomineeBeneficialOwnerIndicator | NaN | Indicates whether the beneficiary details, for example, name and address, must be supplied in order to take part in the event. | YesNoIndicator | NaN |
| IssuerMeeting | ProxyVotingIndicator | NaN | Indicates that the beneficial owner may give authority to a third party to vote on his behalf. | YesNoIndicator | NaN |
| IssuerMeeting | ProxyBeneficialOwnerIndicator | NaN | Indicates whether the beneficiary details of the proxy, for example, name and address, must be supplied in order to take part in the event. | YesNoIndicator | NaN |
| IssuerMeeting | ProxyPowerOfAttorneyIndicator | NaN | Indicates that a power of attorney must be provided by the beneficial owner to the proxy in order for the proxy to vote on behalf of the beneficial owner. | YesNoIndicator | NaN |
| IssuerMeeting | ValidCreditorIndicator | NaN | Indicates that the participant must be a creditor of the company in order to vote on the resolutions of the meeting. | YesNoIndicator | NaN |
| IssuerMeeting | CapitalStock | NaN | Total amount of stock, common or preferred, that a corporation has issued uder its certificate of incorporation or charter. | CurrencyAndAmount | NaN |
| ProxyAppointmentCondition | NaN | NaN | Conditions that must be met to appoint a proxy. | NaN | NaN |
| ProxyAppointmentCondition | NotificationAddress | NaN | Address where the information on the proxy should be sent. | ContactPoint | RelatedProxyAppointment |
| ProxyAppointmentCondition | Meeting | NaN | Specifies the meeting to which the proxy appointment conditions aplly. | Meeting | ProxyAppointmentConditions |
| ProxyAppointmentCondition | RegistrationMethod | NaN | Indicates how to register a proxy. | Max350Text | NaN |
| ProxyAppointmentCondition | AllowedProxyType | NaN | Specifies who can be assigned as a proxy. | ProxyTypeCode | NaN |
| MeetingParticipation | NaN | NaN | Specifies the number of voting rights and of outstanding securities. | NaN | NaN |
| MeetingParticipation | TotalNumberOfSecuritiesOutstanding | NaN | Number of securities admitted to the vote, expressed as an amount and a currency. | CurrencyAndAmount | NaN |
| MeetingParticipation | TotalNumberOfVotingRights | NaN | Number of rights admitted to the vote. | Number | NaN |
| MeetingParticipation | CalculationDate | NaN | Date of calculation of the total number of oustanding securities. | ISODate | NaN |
| MeetingParticipation | TotalNumberOfSecurities | NaN | Number of securities admitted to the vote, expressed as a number of securities. | Number | NaN |
| MeetingParticipation | Meeting | NaN | Meeting for which participation conditions are specified. | Meeting | Participation |
| Quorum | NaN | NaN | Specifies whether a quorum is required or not together with the quorum parameters. | NaN | NaN |
| Quorum | Quantity | NaN | Minimum quantity of securities required to hold a meeting. | Max35Text | NaN |
| Quorum | Percentage | NaN | Minimum quantity of securities, expressed as a percentage, required to hold a meeting. | PercentageRate | NaN |
| Quorum | QuorumRequired | NaN | Specifies whether a minimum number of security representation is required to hold a meeting. | YesNoIndicator | NaN |
| Quorum | Meeting | NaN | Meeting for which a quorum is specified. | Meeting | Quorum |
| MeetingEntitlement | NaN | NaN | Notification of the entitlement that one party has in relation with a specific meeting. | NaN | NaN |
| MeetingEntitlement | EntitlementFixingDate | NaN | Date at which the positions are struck to note which parties will receive the entitlement, e.g. record date, book close date... | ISODate | NaN |
| MeetingEntitlement | EntitlementRatio | NaN | Number of votes assigned to one security. | Number | NaN |
| MeetingEntitlement | EligiblePosition | NaN | Amount of securities that are eligible for the vote. | SecuritiesBalance | RelatedMeetingEntitlement |
| MeetingEntitlement | RelatedServicing | NaN | Services which include the entitlement calculation. | MeetingServicing | MeetingEntitlement |
| MeetingEntitlement | EntitlementCalculationDate | NaN | Date at which the positions are calculated. | ISODate | NaN |
| Resolution | NaN | NaN | Specifies an item in the agenda of the meeting. Some resolutions are submitted to the vote of the security holders, some are presented for information only. | NaN | NaN |
| Resolution | IssuerLabel | NaN | Numbering of the resolution as specified by the issuer or its agent. | Max35Text | NaN |
| Resolution | Description | NaN | Free text description of the resolution. | Max350Text | NaN |
| Resolution | Title | NaN | Abbreviated description of the resolution. | Max350Text | NaN |
| Resolution | Type | NaN | Indicates whether a resolution is ordinary, extraordinary or special. | ResolutionTypeCode | NaN |
| Resolution | ForInformationOnly | NaN | Indicates whether the resolution is listed for information or for voting. | YesNoIndicator | NaN |
| Resolution | SubmittedBySecurityHolder | NaN | Indicates whether the resolution has been submitted by the security holder. | YesNoIndicator | NaN |
| Resolution | ManagementRecommendation | NaN | Indicates how the management of the issuing company wishes the security holders to vote. | VoteInstructionCode | NaN |
| Resolution | NotifyingPartyRecommendation | NaN | Indicates how the notifying party recommends that the security holders vote. | VoteInstructionCode | NaN |
| Resolution | CastVotes | NaN | Specifies whether a resolution is accepted or not and details the number of votes and their status. | Vote | Resolution |
| Resolution | Meeting | NaN | Meeting for which an agenda item is specified. | Meeting | AgendaItem |
| Resolution | VoteOptions | NaN | Vote options allowed at the resolution level. When specified, it supersedes the vote options given for the meeting. | VoteInstructionCode | NaN |
| Resolution | VoteType | NaN | Impact of vote results on an agenda resolution. | VoteTypeCode | NaN |
| Resolution | VotingRightsThresholdForApproval | NaN | Voting rights threshold required in percentage or in quantity to have the resolution approved. | PercentageRate | NaN |
| Resolution | ThresholdBasis | NaN | Nature of the quantity used as a basis to set a threshold for voting on resolutions at general meetings. | ThresholdBasisCode | NaN |
| MeetingStatus | NaN | Status | Status of the instructions related to a meeting. | NaN | NaN |
| MeetingStatus | MeetingResolutionStatus | NaN | Indicates whether the resolution is active or withdrawn. | ResolutionStatusCode | NaN |
| MeetingStatus | InstructionCancellationStatus | NaN | Status of the request for cancellation of an instruction. | CancellationStatusCode | NaN |
| MeetingStatus | Reason | NaN | Specifies the underlying reason for a status of a meeting or related instructions. | MeetingStatusReason | MeetingStatus |
| MeetingStatus | NotificationStatus | NaN | Specifies the status of the related notification. | NotificationStatusCode | NaN |
| MeetingStatus | Meeting | NaN | Meeting for which a status is provided. | Meeting | Status |
| VotingCondition | NaN | NaN | Specifies the different voting types, channels and premium. | NaN | NaN |
| VotingCondition | SecuritiesQuantityRequiredToVote | NaN | Number of holdings required for a vote. | DecimalNumber | NaN |
| VotingCondition | PartialVoteAllowed | NaN | Specifies whether it is allowed to only vote on a part of the entire entitled holding, leaving part of the position un-voted. | YesNoIndicator | NaN |
| VotingCondition | SplitVoteAllowed | NaN | Indicates that the option to give a split instruction, for example, a split voting instruction on a meeting, is allowed. | YesNoIndicator | NaN |
| VotingCondition | VoteLocation | NaN | Electronic address, e-mail or website where a voting ballot can be obtained and/or where a security holder can vote. | ContactPoint | ContactPointForVote |
| VotingCondition | BeneficialOwnerDisclosure | NaN | Indicates whether beneficiary details (eg name and address) must be supplied in order to take part to a meeting. | YesNoIndicator | NaN |
| VotingCondition | IncentivePremium | NaN | Cash premium made available if the securities holder consents or participates to an event. | NaN | NaN |
| VotingCondition | VoteInstructionType | NaN | Identifies the possible types of voting instructions. | VoteInstructionCode | NaN |
| VotingCondition | StandingVotingInstruction | NaN | Indicates whether standing instructions have been defined or not. In this case, the intermediary should cast the votes according to these instructions. | YesNoIndicator | NaN |
| VotingCondition | VotingPremiumAmount | NaN | Amount of additional weight applied to the votes of long term shareholders. | CurrencyAndAmount | NaN |
| VotingCondition | VotingPremiumRate | NaN | Rate of additional weight applied to the votes of long term shareholders. | PercentageRate | NaN |
| VotingCondition | Meeting | NaN | Meeting for which voting conditions are specified. | Meeting | VotingCondition |
| VotingCondition | PreviousInstructionInvalidity | NaN | Indicates whether the previously sent instructions becomes invalid after a market deadline extension. | YesNoIndicator | NaN |
| IncentivePremium | NaN | NaN | Cash premium made available if the securities holder consents or participates to an event. | NaN | NaN |
| IncentivePremium | PerSecurity | NaN | Number of securities giving right to a premium. | Number | NaN |
| IncentivePremium | PerVote | NaN | Number of votes giving right to a premium. | Number | NaN |
| IncentivePremium | PerAttendee | NaN | Indicates that the premium is given per attendee. | YesNoIndicator | NaN |
| IncentivePremium | Description | NaN | Description of the premium. | Max350Text | NaN |
| IncentivePremium | PremiumAmount | NaN | Cash premium paid per security, per vote or per attendee. | CurrencyAndAmount | NaN |
| IncentivePremium | PaymentDate | NaN | Date/time for the payment of the premium. | ISODateTime | NaN |
| IncentivePremium | Meeting | NaN | Meeting for which an incentive premium is specified. | Meeting | IncentivePremium |
| IncentivePremium | CorporateActionDistribution | NaN | CorporateActionDistribution for which an incentive premium is specified. | Distribution | IncentivePremium |
| SecuritiesRegistrationDeadline | NaN | Deadline | Date by which the securities have to be registered. | NaN | NaN |
| SecuritiesRegistrationDeadline | RegistrationDate | NaN | Date at which the voting positions are established (in some countries). | ISODateTime | NaN |
| RegistrationBeneficiary | NaN | MeetingPartyRole | Party in whose name securities are registered. | NaN | NaN |
| PowerOfAttorneyRequirements | NaN | NaN | Specifies the conditions to be filled in to obtain a valid power of attorney. | NaN | NaN |
| PowerOfAttorneyRequirements | LegalRequirement | NaN | Specifies whether the power of attorney needs to be validated by some authority. | PowerOfAttorneyLegalisationCode | NaN |
| PowerOfAttorneyRequirements | OtherDocumentation | NaN | Specifies the documents needed to obtain a valid power of attorney. | Max350Text | NaN |
| PowerOfAttorneyRequirements | PowerOfAttorney | NaN | Power of attorney for which the requirements are provided. | PowerOfAttorney | PowerOfAttorneyRequirements |
| PowerOfAttorneyRequirements | Meeting | NaN | Meeting to which the power of attorney requirements apply. | Meeting | PowerOfAttorneyRequirements |
| CorporateActionAgent | NaN | CorporateActionPartyRole | A firm authorised to act as an intermediary between issuer and shareholders. It takes care of the needs of the shareholders such as reporting, inquiries and regulatory compliance. | NaN | NaN |
| CorporateActionAgent | AgentRole | NaN | Specifies the agent role played by a party in a corporate action process. | AgentRoleCode | NaN |
| MeetingDeadline | NaN | Deadline | Specifies the different deadlines available for the different processes related to meeting attendance, proxy voting and entitlement assessment. | NaN | NaN |
| MeetingParticipationRegistrationDeadline | NaN | MeetingDeadline | Date and time by which the beneficial owner or agent must notify of their intention to participate in the meeting process in order to be allowed to participate in the meeting event. | NaN | NaN |
| AdditionalRight | NaN | NaN | Specifies how the additional rights can be granted to the shareholder. These rights can be exercised at shareholders meetings (for example, the right to ask questions, the right to add items to the agenda or table draft resolutions). | NaN | NaN |
| AdditionalRight | Meeting | NaN | Meeting for which additional rights are specified. | Meeting | AdditionalRight |
| AdditionalRight | Type | NaN | Specifies the additional right type. | AdditionalRightCode | NaN |
| AdditionalRight | AdditionalRightThreshold | NaN | Additional right granted to specify the minimum stake in share capital or cash value or number of security holders required to table resolutions. | Max350Text | NaN |
| AdditionalRight | AdditionalRightThresholdPercentage | NaN | Additional right granted to specify the minimum stake in share capital or cash value or number of security holders required to table resolutions. This minimum is expressed as a percentage. | PercentageRate | NaN |
| MeetingStatusReason | NaN | StatusReason | Specifies the underlying reason for a status of a meeting or related instructions. | NaN | NaN |
| MeetingStatusReason | MeetingCancellationReason | NaN | Specifies the reason for cancelling a meeting. | MeetingCancellationReasonCode | NaN |
| MeetingStatusReason | MeetingStatus | NaN | Status for which a reason is provided. It is derived from the association between StatusReason and Status. | MeetingStatus | Reason |
| MeetingStatusReason | InstructionRejectionReason | NaN | Reason of the rejection of the instruction or of the cancellation request. | RejectionReasonV3Code | NaN |
| MeetingAttendeeRole | NaN | MeetingPartyRole | Security holder who will attend and vote at the meeting in person and/or a person assigned by the security holder to attend the meeting without having any voting rights or taking any action. | NaN | NaN |
| MeetingAttendeeRole | Person | NaN | Specifies the person who is registered to attend a meeting. | Person | MeetingAttendee |
| VoteInstructionRequest | NaN | NaN | Decision of the voting party for one resolution. Several types of decisions can be indicated to allow for split vote specification. | NaN | NaN |
| VoteInstructionRequest | MeetingInstruction | NaN | Meeting instruction which contains a vote instruction. | InstructionForMeeting | VoteInstruction |
| VoteInstructionRequest | VotePerResolution | NaN | Specifies the number of votes to be cast for a specific resolution. | Vote | VoteRequest |
| VoteInstructionRequest | Discretionary | NaN | Number of votes for which decision is left to the party that will exercise the voting right. | Number | NaN |
| VoteInstructionRequest | GlobalVoteInstruction | NaN | Vote instruction per resolution is cast for the entire entitlement. | VoteInstructionCode | NaN |
| VoteInstructionRequest | VoteForMeetingResolution | NaN | Specifies the vote recommendation for resolutions added during the meeting. | VoteInstructionCode | NaN |
| VoteInstructionRequest | VoteExecutionConfirmation | NaN | Indicates that a Vote execution confirmation is requested. | YesNoIndicator | NaN |
| VoteInstructionRequest | RelatedProxyAppointment | NaN | Proxy appointment to which instructions are attached. | ProxyAppointment | Vote |
| InstructionForMeeting | NaN | NaN | Identifies the position of the instructing party and the actions that it wants to take in relation with the meeting. | NaN | NaN |
| InstructionForMeeting | VoteInstruction | NaN | Request to cast detailed voting instructions. | VoteInstructionRequest | MeetingInstruction |
| InstructionForMeeting | RequestedExecutionDate | NaN | Date at which the instruction must be executed. | ISODateTime | NaN |
| InstructionForMeeting | RelatedServicing | NaN | Meeting servicing process which comprises the management of meeting instructions. | MeetingServicing | MeetingInstruction |
| InstructionForMeeting | MeetingAttendance | NaN | Instruction containing the information on the participation of the security holder or of its assigned representative. | MeetingAttendance | RelatedMeeting |
| InstructionForMeeting | ProxyAppointment | NaN | Request to assign a proxy for participation to the meeting. | ProxyAppointment | RelatedMeetingInstruction |
| InstructionForMeeting | MeetingIdentification | NaN | Identification assigned to a general meeting by the party which has notified the meeting. | Max35Text | NaN |
| InstructionForMeeting | SecuritiesRegistration | NaN | Request to register the securities for the meeting. | YesNoIndicator | NaN |
| InstructionForMeeting | BlockingSecurities | NaN | Request to block the securities | YesNoIndicator | NaN |
| InstructionForMeeting | ParticipationRegistration | NaN | Request to register for participation to the meeting. | YesNoIndicator | NaN |
| InstructionForMeeting | SafekeepingAccount | NaN | Account and balance for which the instruction is specified. | SecuritiesAccount | RelatedMeetingInstruction |
| Vote | NaN | NaN | Number of votes assigned to each voting option. | NaN | NaN |
| Vote | VoteRequest | NaN | Request which contains the vote instructions. | VoteInstructionRequest | VotePerResolution |
| Vote | For | NaN | Number of votes in favour of one resolution | Number | NaN |
| Vote | Against | NaN | Number of votes against one resolution | Number | NaN |
| Vote | Abstain | NaN | Number of votes declared abstained for one resolution. | Number | NaN |
| Vote | Withhold | NaN | Number of votes withheld for one resolution | Number | NaN |
| Vote | WithManagement | NaN | Number of votes in line with the votes of the management. | Number | NaN |
| Vote | AgainstManagement | NaN | Number of votes against the voting recommendation of the management. | Number | NaN |
| Vote | Resolution | NaN | Specifies the agenda item on which a vote is/was cast. | Resolution | CastVotes |
| Vote | NoAction | NaN | Number of votes for which no action has been taken. | Number | NaN |
| Vote | Result | NaN | Information on the vote result for a specific resolution. | VoteResult | Vote |
| Vote | TwoYears | NaN | Number of votes in favour of two years for "say on pay" type of resolution. | Number | NaN |
| Vote | OneYear | NaN | Number of votes in favour for one year for "say on pay" type of resolution. | Number | NaN |
| Vote | Withdrawn | NaN | Resolution withdrawn at the meeting. | YesNoIndicator | NaN |
| Vote | ThreeYears | NaN | Number of votes in favour of three years for "say on pay" type of resolution. | Number | NaN |
| Vote | Blank | NaN | Vote is cast as empty but the vote is counted. | Number | NaN |
| Vote | VoteReceiptDateTime | NaN | Date or date and time at which the votes that have been recorded and counted were received. | ISODateTime | NaN |
| AttendanceCard | NaN | NaN | Information about the attendance card which is issued for the requestor, for its underlying client or for the appointed proxy person or meeting attendee when an attendance request is included in the meeting instruction. The instructing party can specify which information must be indicated on the attendance card and to which location the attendance card must be delivered. | NaN | NaN |
| AttendanceCard | AttendanceCardLabelling | NaN | Information to be indicated on the attendance card. | Max105Text | NaN |
| AttendanceCard | MeetingAttendance | NaN | Attendance card which is required to attend the meeting. | MeetingAttendance | AttendanceCard |
| AttendanceCard | DeliveryMethod | NaN | Specifies where the attendance card must be delivered. | DeliveryPlaceCode | NaN |
| AttendanceCard | DeliveryPlace | NaN | Address where the attendance card should be delivered. | ContactPoint | DeliveredAttendanceCard |
| MeetingAttendance | NaN | NaN | Information on the participation of the security holder or of its assigned representative. | NaN | NaN |
| MeetingAttendance | AttendanceCard | NaN | Specifies details linked to the attendance card. | AttendanceCard | MeetingAttendance |
| MeetingAttendance | PercentageOfVotingRights | NaN | Percentage of rights participating to the vote versus total voting rights. | PercentageRate | NaN |
| MeetingAttendance | RelatedMeeting | NaN | Instruction in which the meeting attendance conditions are specified. | InstructionForMeeting | MeetingAttendance |
| VoteResult | NaN | NaN | Specifies whether an agenda item of a general meeting has been accepted or rejected, together with the number of votes. | NaN | NaN |
| VoteResult | Vote | NaN | Number of votes per type of vote and per resolution. | Vote | Result |
| VoteResult | Accepted | NaN | Specifies whether a resolution is accepted or not. | YesNoIndicator | NaN |
| VoteResult | VoteDissemination | NaN | Disemination process through which the results are propagated. | MeetingResultDissemination | VoteResult |
| VoteResult | TotalVotesCast | NaN | Total number of votes cast per resolution. | Number | NaN |
| VoteResult | ModalityOfCounting | NaN | Modality through which the votes that have been recorded and counted were received by the issuer, including whether this is ahead of the meeting or at the meeting. | ModalityOfCountingCode | NaN |
| CorporateActionOptionServicing | NaN | NaN | Option servicing process which calculates the entitlement based on a corporate action option. | NaN | NaN |
| CorporateActionOptionServicing | RelatedOption | NaN | Specifies the option for which an entitlement is calculated | CorporateActionOption | CorporateActionOptionServicing |
| CorporateActionOptionServicing | RelatedServicing | NaN | Process which groups the activities related to corporate action servicing. | CorporateActionServicing | CorporateActionOptionServicing |
| Distribution | NaN | NaN | Distributions in cash and/or securities following a corporate event. | NaN | NaN |
| Distribution | ExercisePeriod | NaN | Period during which the right and/or privilege on an underlying financial instrument may be executed. | DateTimePeriod | ExercisePeriodDistribution |
| Distribution | OfferPeriod | NaN | Period during which an open offer remains valid. | DateTimePeriod | OfferPeriodDistribution |
| Distribution | TradingPeriod | NaN | Period during which a financial instrument is available for trading. | DateTimePeriod | TradingPeriodDistribution |
| Distribution | BlockingPeriod | NaN | Period, set by the issuer, during which the security is blocked, ie, not available for exchange. | DateTimePeriod | BlockingPeriodDistribution |
| Distribution | InterestPeriod | NaN | Period during which interest has accrued. | DateTimePeriod | CashDistribution |
| Distribution | DistributionTax | NaN | Provides the tax description associated with the corporate event. | Tax | RelatedCorporateActionDistribution |
| Distribution | OfferPrice | NaN | Price, determined by the offerer, at which the investor is entitled to take part in an event. | SecuritiesPricing | Distribution |
| Distribution | IncentivePremium | NaN | Cash premium made available to encourage participation by a certain deadline (avoids to have a second call). | IncentivePremium | CorporateActionDistribution |
| Distribution | EffectiveDate | NaN | Date/time at which the event or part of the event, for example, an option, becomes valid and should be processed and/or applied to holdings. | ISODateTime | NaN |
| Distribution | EventConditions | NaN | Conditions that the issuer has placed on the completion of the event, for example, tender percentage required. | Max350Text | NaN |
| Distribution | ExDate | NaN | Date/time as from which trading (including exchange and OTC trading) occurs on the underlying security without the benefit. | ISODateTime | NaN |
| Distribution | GrossRate | NaN | Percentage paid before deductions and/or allowances have been made. | PercentageRate | NaN |
| Distribution | MeetingDate | NaN | Date/time at which the meeting will take place. | ISODateTime | NaN |
| Distribution | NetRate | NaN | Percentage paid after deductions and/or allowances have been made. | PercentageRate | NaN |
| Distribution | NewFaceValue | NaN | New unit value of a debt security. | CurrencyAndAmount | NaN |
| Distribution | NewParValue | NaN | New nominal value of an equity security. | CurrencyAndAmount | NaN |
| Distribution | PaymentDate | NaN | Date/time at which the distribution is due to take place (cash and/or securities). | ISODateTime | NaN |
| Distribution | Dividend | NaN | Dividend per financial instrument. | Dividend | RelatedDistribution |
| Distribution | CorporateActionOption | NaN | Specifies information about the choices offered to the holder of a corporate action. | CorporateActionOptionCode | NaN |
| Distribution | CurrencyOption | NaN | Currency choice given to the investor. | CurrencyCode | NaN |
| Distribution | DecreaseAmount | NaN | Amount by which the issuer devalues a share (in a decrease value event). | CurrencyAndAmount | NaN |
| Distribution | DecreaseRate | NaN | Amount, expressed as a percentage, by which the issuer devalues a share (in a decrease value event). | PercentageRate | NaN |
| Distribution | OfferPriceFixingDate | NaN | Date/time at which an offer price is determined (as compared to its reset date if applicable). | ISODateTime | NaN |
| CashDistribution | NaN | Distribution | Distribution of cash pay-out. | NaN | NaN |
| CashDistribution | DistributionCurrencyExchangeInformation | NaN | Detailed information about the currency exchange in a distribution event. | CurrencyExchange | CurrencyExchangeForCashDistribution |
| CashDistribution | SecuritiesAndCashDistribution | NaN | Distribution for which the cash distribution elements are provided. | SecuritiesAndCashDistribution | CashDistribution |
| CashDistribution | AmortisedRate | NaN | Rate that will be applicable as of the next factor date and defines the outstanding principal of the factored security. | BaseOneRate | NaN |
| CashDistribution | Rate | NaN | Amount of cash, expressed as a percentage, disbursed per financial instrument. | PercentageRate | NaN |
| CashDistribution | CashIndemnityRate | NaN | Ratio of compensation for damage/loss versus value of insured entity | PercentageRate | NaN |
| CashDistribution | DividendReinvestmentIndicator | NaN | Indicates whether a cash dividend can be rolled over into shares of the issuing company. | YesNoIndicator | NaN |
| CashDistribution | InterestAmount | NaN | Amount of interest paid to the principal amount of the financial instrument for a specific period of time. | CurrencyAndAmount | NaN |
| CashDistribution | InterestRate | NaN | Ratio of the amount of interest paid to the principal amount of the financial instrument for a specific period of time. | PercentageRate | NaN |
| CashDistribution | LoyaltyPremiumIndicator | NaN | Indicates whether dividends, in addition to regular dividends, are payable to loyal (time, size, amount) investors. | YesNoIndicator | NaN |
| CashDistribution | PaymentType | NaN | Provides information about the whether the payment will be before or after tax. | PaymentTypeCode | NaN |
| CashDistribution | SelectionDate | NaN | Date/time at which securities are selected for redemption prior to maturity. | ISODateTime | NaN |
| CashDistribution | CashDistributionRate | NaN | Amount, expressed as a percentage, of cash disbursed per financial instrument. | PercentageRate | NaN |
| CashDistribution | CashDistributionAmount | NaN | Amount of cash disbursed per financial instrument. | CurrencyAndAmount | NaN |
| AgentCorporateActionStandingInstruction | NaN | StandingSettlementInstruction | Set-up at the issuer (agent) of a standing instruction originating from the CSD Participants. These standing instructions allow the participant to indicate details for the distribution of the outturn resources of a CA event outside of the CSD. A standing instruction can be accepted or rejected by the issuer (agent) and a CSD participant can amend or cancel a standing instruction. | NaN | NaN |
| AgentCorporateActionStandingInstruction | StandingInstructionType | NaN | Type of standing instruction. | StandingInstructionTypeCode | NaN |
| AgentCorporateActionStandingInstruction | GrossOrNetIndicator | NaN | Indicates whether the payments must always be gross or net. | StandingInstructionGrossNetCode | NaN |
| AgentCorporateActionStandingInstruction | RelatedDeliveryInstructions | NaN | Corporate action delivery instructions which contain settlement standing instructions. | CorporateActionProceedsDeliveryInstruction | CorporateActionStandingInstruction |
| AgentCorporateActionStandingInstruction | Security | NaN | Financial instrument to which the standing instruction applies. | Security | CorporateActionStandingInstructions |
| CollateralStatus | NaN | Status | Specifies the status of the collateral or of an event related to collateral. | NaN | NaN |
| CollateralStatus | ResponseStatus | NaN | Specifies the status of the response to a collateral claim, proposal or substitution proposal. | ResponseStatusCode | NaN |
| CollateralStatus | CollateralManagementCancellationReason | NaN | Specifies the reason for the cancellation of a message. | CollateralManagementCancellationReasonCode | NaN |
| CollateralStatus | SubstitutionStatus | NaN | Provides details about the status of the collateral substitution, either released or returned. | CollateralSubstitutionConfirmationCode | NaN |
| CollateralStatus | InterestRejectionReason | NaN | Provides the interest rejection reason using an ISO 20022 code. | InterestRejectionReasonCode | NaN |
| CollateralStatus | MarginCallResponse | NaN | Specifies whether the margin call request was sent on a non valuation day or was received after notification time. | MarginCallResponseCode | NaN |
| CollateralStatus | Settlement | NaN | Provides the settlement status of the collateral. | SettlementStatusCode | NaN |
| CollateralStatus | CancellationReason | NaN | Provides details about the status of the collateral cancellation. | CancellationReasonCode | NaN |
| CollateralStatus | Collateral | NaN | Collateral for which a status is provided. | Collateral | Status |
| PaymentInitiation | NaN | PaymentExecution | Instruction to pay an amount of money to an ultimate beneficiary, on behalf of an originator. This instruction is the first of the series of instructions which may be used to execute a payment. It is normally sent by the initiating party to the forwarding agent or to the debtor's agent. | NaN | NaN |
| NonDeliverableTrade | NaN | ForeignExchangeTrade | Foreign exchange contract where one of the exchanged amounts is specified in a non-deliverable currency. | NaN | NaN |
| NonDeliverableTrade | SettlementCurrency | NaN | Currency in which a non-deliverable contract is settled. | CurrencyCode | NaN |
| NonDeliverableTrade | FixingConditions | NaN | Set of parameters used to calculate a rate for instance the fixing rate to be applied to a non-deliverable agreement. | FixingCondition | NonDeliverableTrade |
| NonDeliverableTrade | OpeningLeg | NaN | Specifies the opening leg of a non deliverable trade in which the forward rate and amount are specified together with the fixing conditions. | ForeignExchangeTrade | OpeningLegRelatedNonDeliverableTrade |
| NonDeliverableTrade | ClosingLeg | NaN | Specifies the closing leg of a non deliverable trade in which the amount to be settled is the difference in the deliverable currency betweem its original value and the countervalue calculated against the fixing rate. | ForeignExchangeTrade | ClosingLegRelatedNonDeliverableTrade |
| TreasurySettlementPartyRole | NaN | SettlementPartyRole | Role played by a party in the context of the settlement of a treasury trade. | NaN | NaN |
| TreasurySettlementPartyRole | TreasuryTrade | NaN | Identifies the treasury trade for which a party plays a settlement role. | TreasuryTrade | TreasurySettlementPartyRole |
| CurrencyOption | NaN | TreasuryTrade | Right to buy (call) or sell (put) an underlying amount in one currency against another amount in another currency at a predetermined exchange rate, within a specified period of time or at a specified date and time. | NaN | NaN |
| CurrencyOption | CallAmount | NaN | Call amount and currency of a foreign exchange option trade. | ActiveOrHistoricCurrencyAndAmount | NaN |
| CurrencyOption | PutAmount | NaN | Put amount and currency of a foreign exchange option trade. | ActiveOrHistoricCurrencyAndAmount | NaN |
| CurrencyOption | PremiumCalculation | NaN | Specifies the way the premium is calculated. | PremiumCalculation | Option |
| CurrencyOption | OptionDefinition | NaN | Specifies the different parameters used to define an option. | Option | CurrencyOption |
| CurrencyOption | PremiumSettlement | NaN | Specifies the amount of the premium paid by the buyer of the option and its settlement place. | PaymentObligation | PaymentSourceCurrencyOption |
| CurrencyOption | ExercisedOption | NaN | Specifies the trade that may take place to exercise the option. | ForeignExchangeTrade | RelatedOption |
| CurrencyOption | OptionSettlementCurrency | NaN | Currency that must be used to settle the option when it is netted off. | ActiveOrHistoricCurrencyCode | NaN |
| CurrencyOption | StrikeRate | NaN | Fixed exchange rate at which the option contract can be exercised. | BaseOneRate | NaN |
| PremiumCalculation | NaN | NaN | Specifies the amount of a premium on a currency option together with its calculation method. | NaN | NaN |
| PremiumCalculation | Option | NaN | Option for which a premium is calculated. | CurrencyOption | PremiumCalculation |
| PremiumCalculation | PercentageOfCallAmount | NaN | Premium calculation is based on a percentage of the call amount. | PercentageRate | NaN |
| PremiumCalculation | PercentageOfPutAmount | NaN | Premium calculation is based on a percentage of the put amount. | PercentageRate | NaN |
| PremiumCalculation | PointsOfCallAmount | NaN | Premium calculation is based on points of the call amount. | BaseOneRate | NaN |
| PremiumCalculation | PointsOfPutAmount | NaN | Premium calculation is based on points of the put amount. | BaseOneRate | NaN |
| InvoiceFinancingAgreement | NaN | Agreement | Set of characteristics that unambiguously identify an invoice financing agreement. An invoice financing agreement between a factor and its client allows to transfer a payment obligation that exists between the client and a third party from the client to the factor. | NaN | NaN |
| InvoiceFinancingAgreement | Authorisation | NaN | User identification or any user key that allows to check if the financing requestor is allowed to ask for invoice financing. Usage: the content is not of a technical nature, but reflects the organisational structure at the requesting side. The authorisation element can typically be used in case the financing requestor acts on behalf of one or more suppliers. | Max128Text | NaN |
| InvoiceFinancingAgreement | FinancingMethod | NaN | Specifies the financing method related to invoice financing (eg collection mandate). | Max350Text | NaN |
| InvoiceFinancingAgreement | RequestedAmount | NaN | Amount requested by the requestor party, related to a single invoice to be financed. | CurrencyAndAmount | NaN |
| InvoiceFinancingAgreement | RequestedPercentage | NaN | Percentage of the amount requested by the requestor party, related to a single invoice, to be financed. | PercentageRate | NaN |
| InvoiceFinancingAgreement | AppliedPercentage | NaN | The percentage rate applied to calculate the amount financed. | PercentageRate | NaN |
| InvoiceFinancingAgreement | FinancedAmount | NaN | Specifies the amount financed which is derived from the applied percentage and the invoice amount.. | CurrencyAndAmount | NaN |
| InvoiceFinancingAgreement | Identification | NaN | Identifies unambiguously the financing transaction. | Max35Text | NaN |
| InvoiceFinancingAgreement | InvoiceFinancingPartyRole | NaN | Role played by a party in the context of financing an invoice. | InvoiceFinancingPartyRole | InvoiceFinancingTransaction |
| InvoiceFinancingAgreement | InvoiceFinancingStatus | NaN | Status of the invoice financing transaction and of the different requests linked to it. | InvoiceFinancingStatus | InvoiceFinancingTransaction |
| InvoiceFinancingAgreement | Invoice | NaN | Invoice to which is referred financing request. | Invoice | InvoiceFinancingTransaction |
| InvoiceFinancingAgreement | ResultingCashEntry | NaN | Information related to the crediting of the amount financed, such as dates, amount, charges... | CashEntry | RelatedInvoiceFinancingTransaction |
| InvoiceFinancingAgreement | Assignment | NaN | Assignments resulting from an invoice financing agreement. | Assignment | FinancingAgreement |
| FinancingRequestorRole | NaN | InvoiceFinancingPartyRole | Credit party that requests the invoice financing, on behalf of creditor. | NaN | NaN |
| CommercialTrade | NaN | Trade | Commercial details of a trade transaction between a buyer and a seller. | NaN | NaN |
| CommercialTrade | PurchaseAccount | NaN | Specific purchase account for recording debits and credits for accounting purposes. | CashAccount | RelatedCommercialTrade |
| CommercialTrade | PaymentObligation | NaN | Obligation for the buyer to settle the value of the products bought. | PaymentObligation | CommercialTrade |
| CommercialTrade | TotalAcceptedAmount | NaN | Total amount of a trade, that is the sum of the accepted items. | CurrencyAndAmount | NaN |
| CommercialTrade | PartyRole | NaN | Role played by a party in the context of a trade. | CommercialTradePartyRole | CommercialTrade |
| CommercialTrade | TradeSettlement | NaN | Process of settling a commercial trade. | CommercialTradeSettlement | CommercialTrade |
| CommercialTrade | ProductDeliveryObligation | NaN | Obligation for the seller to deliver the products to the buyer. | ProductDeliveryObligation | CommercialTrade |
| CommercialTrade | PurchaseOrder | NaN | Specifies the purchase order related to a commercial trade. | PurchaseOrder | ResultingCommercialTrade |
| CommercialTrade | Documents | NaN | Documents related to a commercial trade transaction. | Document | CommercialTrade |
| CommercialTrade | RelatedUndertaking | NaN | Undertaking related to the commercial trade. | UnderlyingTransaction | CommercialTrade |
| CommercialTrade | TransactionStatus | NaN | Status of a commercial trade processed in a central system. | BaselineStatus | CommercialTrade |
| CommercialTrade | Agreement | NaN | Agreement between trade parties which describes the conditions under which they agree to execute trades amongst themselves. | Agreement | Trade |
| LineItem | NaN | NaN | Unit of information showing the related provision of products and/or services and monetary summations reported as a discrete line item. | NaN | NaN |
| LineItem | FinancialAdjustment | NaN | Modification on the value of goods and / or services taking into account discounts, allowances and charges. | Adjustment | RelatedLineItem |
| LineItem | LogisticsCharge | NaN | Logistics service charge for this line item. | Charges | LogisticsChargeLineItem |
| LineItem | GrossAmount | NaN | Monetary value of the line amount total being reported for this settlement. | CurrencyAndAmount | NaN |
| LineItem | Identification | NaN | Uniquely identifies a line item. | Max35Text | NaN |
| LineItem | InvoicedProduct | NaN | Specifies the product and the quantity for which an invoice is generated. | Product | LineItem |
| LineItem | NetWeight | NaN | Net weight of the physical item which is invoiced. | ProductQuantity | NetWeightRelatedLineItem |
| LineItem | BilledQuantity | NaN | Quantity billed for this line item. | ProductQuantity | BilledQuantityRelatedLineItem |
| LineItem | ChargeFreeQuantity | NaN | Quantity that is free of charge for this line item. | ProductQuantity | ChargeFreeQuantityRelatedLineItem |
| LineItem | MeasureQuantityStartRelatedLineItem | NaN | Line item for which a measure quantity end is specified. | ProductQuantity | MeasureQuantityStart |
| LineItem | MeasureQuantityEndRelatedLineItem | NaN | Line item for which a measure quantity end is specified. | ProductQuantity | MeasureQuantityEnd |
| LineItem | MeasureDateTimeStart | NaN | Date/time on which the clock time measure started for a line item. | ISODateTime | NaN |
| LineItem | MeasureDateTimeEnd | NaN | Date/time on which the clock time measure ended for a line item. | ISODateTime | NaN |
| LineItem | Invoice | NaN | Specifies the invoice in which the line item is included. | Invoice | LineItem |
| LineItem | NetAmount | NaN | Total amount resulting from the gross amount plus freight charges, tax and plus/minus Adjustments. | CurrencyAndAmount | NaN |
| LineItem | Packaging | NaN | Physical packaging of the product. | Packaging | RelatedLineItem |
| LineItem | DeliveryDateTime | NaN | Actual delivery date/time of the products and/or services for this line item. | ISODateTime | NaN |
| LineItem | Charges | NaN | Charges specified for this line item. | Charges | LineItem |
| LineItem | NetPriceCharge | NaN | Allowance or charge applied to the net price. When the charge amount is added (credit) | Charges | NetPriceChargeLineItem |
| LineItem | GrossPriceQuantity | NaN | Quantity and conversion factor on which the gross price is based for this line item product and/or service. | ProductQuantity | GrossPriceQuantityRelatedLineItem |
| LineItem | NetPriceQuantity | NaN | Quantity and conversion factor on which the net price is based for this line item product and/or service. | ProductQuantity | NetPriceQuantityRelatedLineItem |
| LineItem | GrossWeight | NaN | Gross weight of the physical item which is invoiced. | ProductQuantity | GrossWeightRelatedLineItem |
| InvoiceFinancingStatus | NaN | Status | Status of an invoice financing transaction and of the instructions related to the invoice financing. | NaN | NaN |
| InvoiceFinancingStatus | ValidationStatusReason | NaN | The reason for the validation status. | FinancingStatusReasonCode | NaN |
| InvoiceFinancingStatus | ValidationStatus | NaN | The result of the technical validation (e.g. Accepted, Reception error) executed on the request message. | TechnicalValidationStatusCode | NaN |
| InvoiceFinancingStatus | CancellationStatus | NaN | Information on the business status of the cancellation. | TechnicalValidationStatusCode | NaN |
| InvoiceFinancingStatus | CancellationStatusReason | NaN | The reason for the cancellation status. | FinancingStatusReasonCode | NaN |
| InvoiceFinancingStatus | FinancingTransactionStatus | NaN | Specifies the status of the financing request (e.g. financed. not financed). | RequestStatusCode | NaN |
| InvoiceFinancingStatus | CancellationRequestReason | NaN | Further details on the cancellation request information, in an uncoded form. | Max105Text | NaN |
| InvoiceFinancingStatus | InvoiceFinancingTransaction | NaN | Specifies the transaction for which a status is provided. | InvoiceFinancingAgreement | InvoiceFinancingStatus |
| InvoiceFinancingStatus | FinancingStatusReason | NaN | <p>Indicates the reasons that have determined the result of the single request.</p> | FinancingStatusReasonCode | NaN |
| Transport | NaN | NaN | Moving of goods or people from one place to another by vehicle. | NaN | NaN |
| Transport | Incoterms | NaN | Specifies the applicable Incoterm and associated location. | Incoterms | Transport |
| Transport | Identification | NaN | Unique identification of the means of transport, such as the International Maritime Organization number of a vessel. | Max35Text | NaN |
| Transport | Packaging | NaN | Physical packaging of goods for transport. | Packaging | Transport |
| Transport | ArrivalDateTime | NaN | Date and time when the goods reach their destination.. | ISODateTime | NaN |
| Transport | PartialShipment | NaN | Indicates whether or not partial shipments are allowed. | YesNoIndicator | NaN |
| Transport | TransShipment | NaN | Indicates whether or not transshipment of goods is allowed. | YesNoIndicator | NaN |
| Transport | ProductDelivery | NaN | Specifies the delivery parameters of a trade. | ProductDelivery | Routing |
| Transport | PlaceOfDeparture | NaN | Place from where the goods must leave. | Location | DepartureTransportParameters |
| Transport | PlaceOfDestination | NaN | Place where the goods must arrive. | Location | DestinationTransportParameters |
| Transport | TransportCharges | NaN | Charges related to the conveyance of goods. | Charges | Transport |
| Transport | FreightChargesPrepaidOrCollect | NaN | Identifies whether the freight charges associated with the items are "prepaid" or "collect". | FreightChargesCode | NaN |
| Transport | ShipmentDates | NaN | Specifies the shipment date, the earliest shipment date and the latest shipment date. | ShipmentDateRange | RelatedTransport |
| Transport | TransportedGoods | NaN | Goods that are transported. | Goods | Transport |
| Transport | PartyRole | NaN | Specifies each role linked to the transport of goods. | TransportPartyRole | Transport |
| Transport | TransitLocation | NaN | Place through which the goods are transiting. | Location | RelatedTransport |
| Transport | TransportDocuments | NaN | Documents which may be required in relation with the transportation of goods. | Document | Transport |
| Incoterms | NaN | NaN | International commerce terms are a series of international sales terms, published by International Chamber of Commerce (ICC) and widely used in international commercial transactions. These are accepted by governments, legal authorities and practitioners worldwide for the interpretation of most commonly used terms in international trade. Scope of this is limited to matters relating to rights and obligations of the parties to the contract of sale with respect to the delivery of goods sold. They are used to divide transaction costs and responsibilities between buyer and seller and reflect state-of-the-art transportation practices. | NaN | NaN |
| Incoterms | Transport | NaN | Specifies the transport information to which the incoterms apply. | Transport | Incoterms |
| Incoterms | Code | NaN | Specifies the applicable Incoterm by means of a code. | IncotermsCode | NaN |
| Incoterms | Location | NaN | Location where the Incoterms are actioned. | Location | Incoterms |
| Goods | NaN | Product | Good is a physical product that can be delivered to a purchaser and that involves the transfer of ownership from seller to customer. | NaN | NaN |
| Goods | Transport | NaN | Specifies the transport information related to the delivery of goods. | Transport | TransportedGoods |
| Goods | Analysis | NaN | Analysis of the goods, as proven by the trade certificate. | Max70Text | NaN |
| Goods | HealthCheck | NaN | Indicates if the goods have passed the health check. | YesNoIndicator | NaN |
| Goods | PhytosanitaryInspection | NaN | Indicates if the goods have passed the phytosanitary inspection. | YesNoIndicator | NaN |
| Goods | PartyRole | NaN | Role played by a party in the context of producing goods. | GoodsPartyRole | Item |
| ProductDelivery | NaN | ObligationFulfilment | Arrangements for delivery of invoiced products and/or services. | NaN | NaN |
| ProductDelivery | DeliveryPeriod | NaN | Actual delivery period of the products and/or services. | DateTimePeriod | RelatedProductDelivery |
| ProductDelivery | Routing | NaN | Information related to the conveyance of goods. | Transport | ProductDelivery |
| ProductDelivery | TradeSettlement | NaN | Specifies the settlement operation which originates the delivery of a product. | CommercialTradeSettlement | ProductDelivery |
| ProductDelivery | Obligation | NaN | Specifies the obligation which is offset by the delivery of a product. | ProductDeliveryObligation | ProductDeliveryOffset |
| ProductDelivery | TradeCertificate | NaN | Formal document used to record a fact and used as proof of the fact, in the context of a commercial trade transaction. | TradeCertificate | ProductDelivery |
| ProductDelivery | InsuranceCertificate | NaN | Formal document used to record a fact and used as proof of the fact that goods have been insured under an insurance policy. | InsuranceCertificate | ProductDelivery |
| ProductDelivery | Product | NaN | Specifies the type of goods and services linked to the quantity. | Product | Delivery |
| CommercialTradePartyRole | NaN | TradePartyRole | Role played by a party in the context of a trade. | NaN | NaN |
| CommercialTradePartyRole | CommercialTrade | NaN | Identifies the trade for which a party plays a role. | CommercialTrade | PartyRole |
| ShipFrom | NaN | CommercialTradePartyRole | Party from whom the goods are dispatched. | NaN | NaN |
| ShipTo | NaN | CommercialTradePartyRole | Party to whom the goods must be delivered. | NaN | NaN |
| Packaging | NaN | NaN | Physical packaging of goods for transport. | NaN | NaN |
| Packaging | Quantity | NaN | Number of packages for a supply chain trade delivery. | ProductQuantity | RelatedPackaging |
| Packaging | PerPackageUnitQuantity | NaN | Number of units per package for a supply chain trade delivery. | ProductQuantity | PackagingForUnitQuantity |
| Packaging | Transport | NaN | Transport process which uses a specific packaging. | Transport | Packaging |
| Packaging | PackagingName | NaN | Name given to the type of supply chain packaging. For instance Halogenated Resin (PVC). | Max350Text | NaN |
| Packaging | TotalConsignmentQuantity | NaN | Total quantity of packaging units, eg number of boxes, containers, pallets, etc | ProductQuantity | PackagingForConsignmentlQuantity |
| Packaging | TotalVolume | NaN | Total volume of goods shipped, eg number of cubic meters. | ProductQuantity | PackagingForVolume |
| Packaging | TotalWeight | NaN | Total weight of goods shipped, eg number of kg, tons. | ProductQuantity | PackagingForWeight |
| Packaging | RelatedLineItem | NaN | Line item information for the package goods. | LineItem | Packaging |
| Packaging | PackageType | NaN | Code specifying the properties of packaging for the supply chain delivery of goods. | Max4Text | NaN |
| TransportPartyRole | NaN | Role | Role played by a party in the context of transporting goods. | NaN | NaN |
| TransportPartyRole | Transport | NaN | Identifies the transport process for which a party plays a role. | Transport | PartyRole |
| Consignor | NaN | TransportPartyRole | Party responsible for dispatching the goods. | NaN | NaN |
| Consignee | NaN | TransportPartyRole | Party to whom the goods must be delivered. | NaN | NaN |
| CommercialTradeSettlement | NaN | Settlement | Settlement of a commercial trade, that is, the instruction to deliver goods or services against the payment of an amount of money. | NaN | NaN |
| CommercialTradeSettlement | Payment | NaN | Settlement of the payment side of a commercial trade. | Payment | TradeSettlement |
| CommercialTradeSettlement | Invoice | NaN | Specifies for which invoice the settlement takes place. | Invoice | TradeSettlement |
| CommercialTradeSettlement | LetterOfCredit | NaN | Written undertaking by a bank to honour a demand for payment. | LetterOfCredit | CommercialTradeSettlement |
| CommercialTradeSettlement | ProductDelivery | NaN | Delivery of the goods or services to the buyer. | ProductDelivery | TradeSettlement |
| CommercialTradeSettlement | CommercialTrade | NaN | Specifies the commercial trade which is settled. | CommercialTrade | TradeSettlement |
| InvoicerRole | NaN | InvoicePartyRole | Party identified as the liable party on the face of a commercial invoice. | NaN | NaN |
| Allowance | NaN | Adjustment | Amount of money deducted from a price or an amount due. | NaN | NaN |
| Allowance | TotalAllowance | NaN | Algebraical sum of allowances related to the invoice. | CurrencyAndAmount | NaN |
| Allowance | NetPriceAllowance | NaN | Allowance applied to the net price. | CurrencyAndAmount | NaN |
| ProductCharacteristics | NaN | NaN | Identifies the characteristic of a product. | NaN | NaN |
| ProductCharacteristics | Product | NaN | Specifies the product for which characteristics are specified. | Product | Characteristics |
| ProductCharacteristics | Characteristics | NaN | Specifies the characteristic of a product. | Max35Text | NaN |
| ProductCharacteristics | Type | NaN | Specifies the type of product characteristic by means of a code. | ProductCharacteristicsCode | NaN |
| BaselineStatus | NaN | Status | Indicates the status of a baseline. | NaN | NaN |
| BaselineStatus | Status | NaN | Specifies the status of the processing of a baseline. | BaselineStatusCode | NaN |
| BaselineStatus | CommercialTrade | NaN | Commercial trade for which a status is provided. | CommercialTrade | TransactionStatus |
| ShipmentDateRange | NaN | NaN | Specifies a shipment period or a shipment date. | NaN | NaN |
| ShipmentDateRange | LatestShipmentDate | NaN | Latest date whereby the goods must be shipped. | ISODateTime | NaN |
| ShipmentDateRange | RelatedTransport | NaN | Specifies the transport process to which the dates apply. | Transport | ShipmentDates |
| ShipmentDateRange | EarliestShipmentDate | NaN | Earliest date whereby the items must be shipped. | ISODateTime | NaN |
| ShipmentDateRange | ShipmentDate | NaN | Date at which the goods are shipped. | ISODateTime | NaN |
| TransportByAir | NaN | Transport | Information related to the transportation of goods by air. | NaN | NaN |
| TransportByAir | AirportName | NaN | Identifies an airport by means of its IATA identification code. Example: LHR. | Max6Text | NaN |
| TransportByAir | FlightNumber | NaN | Identifies the flight and the carrier. | Max35Text | NaN |
| TransportBySea | NaN | Transport | Information related for the transportation of goods by sea. | NaN | NaN |
| TransportBySea | VesselName | NaN | Name of a vessel. | Max35Text | NaN |
| TransportBySea | VoyageNumber | NaN | Identifies the voyage. | Max35Text | NaN |
| TransportBySea | ChartererName | NaN | Name of the company or individual that acts in the capacity of charterer. | Max70Text | NaN |
| TransportBySea | MasterName | NaN | Name of the master or captain of a vessel. | Max70Text | NaN |
| TransportBySea | OwnerName | NaN | Name of the company or individual that acts in the capacity of owner. | Max70Text | NaN |
| TransportBySea | IMONumber | NaN | International Maritime Organisation identification of a ship. This is a unique seven digit number that is assigned to vessels and aids banks in determining whether a vessel is subject to an order that would not permit a bank to handle a certain transaction under local or international laws. | Exact7NumericText | NaN |
| TransportByRoad | NaN | Transport | Information related to the transportation of goods by road. | NaN | NaN |
| TransportByRail | NaN | Transport | Information related to the transportation of goods by rail. | NaN | NaN |
| TransportByRail | CarriageIdentification | NaN | Identifies the carriage. | Max35Text | NaN |
| TradeCertificate | NaN | Document | Formal document used to record a fact and used as proof of the fact, in the context of a commercial trade transaction. | NaN | NaN |
| TradeCertificate | CertificateType | NaN | Specifies the type of the certificate. | TradeCertificateTypeCode | NaN |
| TradeCertificate | InspectionDate | NaN | Date(s) at which inspection of the goods took place. | DateTimePeriod | TradeCertificate |
| TradeCertificate | TradeCertificatePartyRole | NaN | Role played by a party in the context of issuing a trade certificate. | TradeCertificatePartyRole | TradeCertificate |
| TradeCertificate | ProductDelivery | NaN | Delivery parameters of a trade. | ProductDelivery | TradeCertificate |
| PurchaseOrder | NaN | Order | Document issued by a buyer and containing the details of a purchase, including description of goods, transport information, payment terms, etc. | NaN | NaN |
| PurchaseOrder | TotalAmount | NaN | Line items total amount. | CurrencyAndAmount | NaN |
| PurchaseOrder | ResultingCommercialTrade | NaN | Execution of the purchase order. | CommercialTrade | PurchaseOrder |
| PurchaseOrder | Product | NaN | Specifies the items which are sold by the seller to the buyer in a commercial trade. | Product | PurchaseOrder |
| PurchaseOrder | Identification | NaN | Identification of the purchase order that can be used for reconciliation or to link tasks relating to the commercial trade. | GenericIdentification | RelatedPurchaseOrder |
| InsurancePartyRole | NaN | Role | Role played by a party in the context of insurance. | NaN | NaN |
| InsurancePartyRole | InsuranceCertificate | NaN | Identifies the certificate for which a party plays a role. | InsuranceCertificate | InsurancePartyRole |
| Assured | NaN | InsurancePartyRole | Party that is covered under the assurance policy. | NaN | NaN |
| Assured | AssuredType | NaN | Specifies the type of assured party. | AssuredTypeCode | NaN |
| CollateralAgreement | NaN | Agreement | Agreement between two trading parties that contains information about their relative duties and rights regarding collateral processes. | NaN | NaN |
| CollateralAgreement | BaseCurrency | NaN | Denomination currency. | CurrencyCode | NaN |
| CollateralAgreement | AssociatedMasterAgreement | NaN | Agreement in which the parties agree to most of the terms that will govern collateral transactions. | MasterAgreement | CollateralAgreement |
| CollateralAgreement | StandingSettlementInstructions | NaN | Settlement instructions which must be used for the settlement of collateral unless otherwise specified. | StandingSettlementInstruction | RelatedCollateralAgreement |
| CollateralAgreement | MarginConvention | NaN | Determines how the variation margin requirement will be calculated, either net or gross. | ExposureConventionTypeCode | NaN |
| CollateralAgreement | ExposureTerm | NaN | Specifies the terms used to calculate a risk exposure and its coverage. | ExposureTerm | RelatedCollateralAgreement |
| CollateralAgreement | CallFrequency | NaN | Specifies the frequency at which collateral positions are evaluated and margin calls are issued. | FrequencyCode | NaN |
| CollateralAgreement | Collateral | NaN | Specifies the collateral which is the subject of the agreement. | Collateral | CollateralAgreement |
| CollateralAgreement | RiskCoverage | NaN | Collateral management process which applies the terms agreed in the collateral agreement. | CollateralManagement | AgreedTerms |
| CollateralPartyRole | NaN | Role | Role played by a party in the context of collateral. | NaN | NaN |
| CollateralPartyRole | Collateral | NaN | Specifies the collateral for which a party plays a role. | Collateral | CollateralPartyRole |
| ServicingPartyRole | NaN | CollateralPartyRole | Party that is acting on behalf of another party and that offers collateral management services. | NaN | NaN |
| MarginCall | NaN | NaN | Specifies the calculation and the resulting margin and independent amount needed to cover the risk exposure of one party versus another. | NaN | NaN |
| MarginCall | MarginCallValuationDate | NaN | Close of business date that initiating party is valuing the margin call. | ISODateTime | NaN |
| MarginCall | AgreedAmount | NaN | Specifies the amount which is undisputed. | CurrencyAndAmount | NaN |
| MarginCall | VariationMargin | NaN | Provides the summation of the call amounts for the variation margin and optionally the segregated independent amount. | CurrencyAndAmount | NaN |
| MarginCall | SegregatedIndependentAmount | NaN | Provides the summation of the call amounts for the segregated independent amount only. | CurrencyAndAmount | NaN |
| MarginCall | DefaultFundContribution | NaN | Portion of the participation to the default fund that clearing member must provide. It is the sum of the individual contributions. | DefaultFundContribution | RelatedMarginCall |
| MarginCall | ExpectedVariationMarginType | NaN | Specifies the expected collateral type and direction. | ExpectedCollateralType | VariationMarginRelatedCall |
| MarginCall | ExpectedSegregatedIndependentAmountType | NaN | Specifies the expected collateral type and direction. | ExpectedCollateralType | SegregatedIndependentAmountRelatedCall |
| MarginCall | TotalMarkToMarket | NaN | Net unrealised profit or loss on the value of the netted, gross and failing positions. | CurrencyAndAmount | NaN |
| MarginCall | MarkToMarketNetted | NaN | Unrealised net loss calculated at the participant portfolio level. | CurrencyAndAmount | NaN |
| MarginCall | MarkToMarketGross | NaN | Unrealised net loss calculated in that market/boundary. | CurrencyAndAmount | NaN |
| MarginCall | MarkToMarketFails | NaN | Sum of the unrealised loss without taking profit into consideration. | CurrencyAndAmount | NaN |
| MarginCall | FailsHaircut | NaN | Haircut applied to the absolute value of the participants net positions. Calculation depends on a participants credit rating. | CurrencyAndAmount | NaN |
| MarginCall | InitialMargin | NaN | Margin required for absorbing future market price fluctuations (market risks) occurring between the default of a member and close-out of unsettled securities positions by the CCP. | CurrencyAndAmount | NaN |
| MarginCall | IncreaseCoverage | NaN | Amount added to the requirement amount. Its value is at the discretion of the central clearing counterparty. | CurrencyAndAmount | NaN |
| MarginCall | CollateralisedMarginAccountIndicator | NaN | Used to indicate whether the reported margin account is collateralised or not. If not collateralised, the account is configured for informational reporting. | YesNoIndicator | NaN |
| MarginCall | CollateralMovement | NaN | Movements resulting from the margin call calculation. | CollateralMovement | MarginCall |
| MarginCall | RelatedManagementProcess | NaN | Process which groups the activities related to collateral. | CollateralManagement | MarginCall |
| MarginCall | Security | NaN | Description of the securities related to the margin call. | Security | RelatedMarginCall |
| MarginCall | MarginProduct | NaN | Specifies the underlying product of the margin. | MarginProductCode | NaN |
| MarginCall | MarginType | NaN | Specifies the type of margin, for example, initial margin, variation margin, initial deposit or coupon margin. | MarginTypeCode | NaN |
| MarginCall | TotalMarginAmount | NaN | Total margin requirement (expressed in the reporting currency) that must be provided. This is the total requirement calculated to cover the initial margin and the variation margin. | CurrencyAndAmount | NaN |
| CollateralProposal | NaN | NaN | Specifies collateral proposed to the counterparty. | NaN | NaN |
| CollateralProposal | ProposedCollateralMovement | NaN | Details the movement of collateral that is proposed to be delivered or returned by one of the collateral parties. | CollateralMovement | RelatedCollateralProposal |
| CollateralProposal | ResponseType | NaN | Indicates whether the collateral proposal is an initial or a counter proposal. | CollateralProposalResponseCode | NaN |
| CollateralProposal | Type | NaN | Indicates whether this is an initial or counter proposal. | ProposalTypeCode | NaN |
| CollateralProposal | RelatedManagementProcess | NaN | Process which groups the activities related to collateral. | CollateralManagement | CollateralProposal |
| CollateralMovement | NaN | NaN | Provides the agreed amount and the collateral movement direction. | NaN | NaN |
| CollateralMovement | RelatedCollateralProposal | NaN | Collateral proposal for which collateral movements are detailed. | CollateralProposal | ProposedCollateralMovement |
| CollateralMovement | VariationMargin | NaN | Amount of margin that will be delivered to one party by the other party after rounding, threshold and minimum transfer amount are taken into account. | CurrencyAndAmount | NaN |
| CollateralMovement | SegregatedIndependentAmount | NaN | Amount of margin that will be delivered to one party by the other party after rounding, threshold and minimum transfer amount are taken into account. | CurrencyAndAmount | NaN |
| CollateralMovement | MarginCall | NaN | Magin call which needs to be executed. | MarginCall | CollateralMovement |
| CollateralMovement | SecuritiesCollateralMovement | NaN | Movement of assets in relation with collateral updates. | SecuritiesDeliveryObligation | RelatedCollateralMovement |
| CollateralMovement | CashCollateralMovement | NaN | Movement of assets in relation with collateral updates. | PaymentObligation | RelatedCollateralMovement |
| CollateralMovement | FinancialTransaction | NaN | Financial transaction to which the collateral management is associated. | FinancialTransaction | CollateralMovement |
| MasterAgreement | NaN | Agreement | Agreement which defines the framework of a contract between two trading parties in different domains such as collateral, derivatives, trade.. | NaN | NaN |
| MasterAgreement | CollateralAgreement | NaN | Collateral agreement which is governed by the related master agreement. | CollateralAgreement | AssociatedMasterAgreement |
| MasterAgreement | MasterAgreementType | NaN | Nature of the agreement, eg, ISDA Master Agreement or bilateral agreement. | AgreementFrameworkCode | NaN |
| MasterAgreement | GovernedTrades | NaN | Trades to which the master agreement applies. | Trade | GoverningDocument |
| MasterAgreement | GovernedContract | NaN | Contract which is governed by the master agreement. | Contract | MasterAgreement |
| MasterAgreement | GoverningLaw | NaN | National law under which a non-deliverable contract has been agreed. | CountryCode | NaN |
| CollateralManagement | NaN | NaN | Set of operations relative to the management of collateral, variation margins, default fund participation and independent amount. | NaN | NaN |
| CollateralManagement | CollateralProposal | NaN | Specifies collateral proposed to the counterparty. | CollateralProposal | RelatedManagementProcess |
| CollateralManagement | CollateralValuation | NaN | Provides details about the valuation of each piece of collateral that is posted. | CollateralValuation | RelatedManagementProcess |
| CollateralManagement | FeesAndCommissions | NaN | Specifies the amount of money paid for the provision of financial services. | Adjustment | CollateralManagement |
| CollateralManagement | InterestManagement | NaN | Calculation and request of interest linked to collateral. | CollateralInterestAdministration | CollateralManagement |
| CollateralManagement | DisputeManagement | NaN | Provides the dispute details on the variation margin and/or the segregated independent amount. | DisputeManagement | RelatedManagementProcess |
| CollateralManagement | MarginCall | NaN | Calculation of the variation margin and independent amount needed to cover the risk exposure of one party versus another. | MarginCall | RelatedManagementProcess |
| CollateralManagement | CollateralSubstitution | NaN | Request of a substitution of collateral by specifying the collateral to be returned and proposing the new type(s) of collateral to be delivered. | CollateralSubstitution | RelatedManagementProcess |
| CollateralManagement | RiskToCover | NaN | Risk which is the source of the collateral management processes. | ExposureCalculation | CollateralManagement |
| CollateralManagement | Collateral | NaN | Description of the collateral which is related to the different management processes. | Collateral | CollateralManagement |
| CollateralManagement | AgreedTerms | NaN | Specifies the terms bilaterally agreed by the parties related to the collateral processes. | CollateralAgreement | RiskCoverage |
| CollateralManagement | ClearingSystem | NaN | Clearing system involved in the collateral management process. | ClearingSystem | CollateralManagement |
| Money | NaN | Asset | Currency (banknotes and coins) and demand deposits or 'bank money' (the balance held in checking accounts and savings accounts). | NaN | NaN |
| Money | CashAmount | NaN | Value of the asset specified as a currency and an amount. | CurrencyAndAmount | NaN |
| Deposit | NaN | Money | An arrangement in which a lender gives money or property to a borrower, and the borrower agrees to return the property or repay the money, usually along with interest, at some future point(s) in time. | NaN | NaN |
| Deposit | DepositType | NaN | Specifies whether the deposit is fixed term or call/notice. | DepositTypeCode | NaN |
| Deposit | Interest | NaN | Interest amount linked to a deposit. It is derived from the relationship between AssetHolding and Interest. | Interest | Deposit |
| LetterOfCredit | NaN | Asset | Instrument issued by a bank substituting its name and credit standing for that of its customer. A letter of credit is a written undertaking of the bank, issued for the account of a customer (the applicant), to honour a demand for payment, upon the beneficiary's compliance with the terms and conditions set forth in the undertaking. | NaN | NaN |
| LetterOfCredit | Amount | NaN | Amount of the letter/documentary credit. | ActiveCurrencyAndAmount | NaN |
| LetterOfCredit | Document | NaN | Document which materialises the letter of credit. | Document | LetterOfCredit |
| LetterOfCredit | CommercialTradeSettlement | NaN | Settlement process related to a letter of credit. | CommercialTradeSettlement | LetterOfCredit |
| Guarantee | NaN | Asset | Partial or full coverage of amounts by a party other than the debtor. | NaN | NaN |
| Guarantee | CoveredAmount | NaN | Amount covered by the guarantee. | CurrencyAndAmount | NaN |
| Guarantee | EffectivePeriod | NaN | Period during which the guarantee is valid. | DateTimePeriod | Guarantee |
| Guarantee | GuaranteeType | NaN | Specifies the type of security granted by an organisation with the role as 'guarantor', for example, suretyship. | GuarantyTypeCode | NaN |
| Guarantee | CoveredPercentage | NaN | Amount covered by the guarantee, expressed as a percentage. | PercentageRate | NaN |
| Guarantee | Document | NaN | Document which contains the description of the guarantee. | Document | Guarantee |
| Guarantee | GuaranteedTrade | NaN | Trade which is partially or fully covered by a guarantee. | Trade | Guarantee |
| Guarantee | ExcessAmount | NaN | Amount not covered by the guarantee. | CurrencyAndAmount | NaN |
| Guarantee | GuaranteePartyRole | NaN | Specifies the roles played by a party in the context of guarantees. | GuaranteePartyRole | Guarantee |
| CollateralSubstitution | NaN | NaN | Substitution of collateral by specifying the collateral to be returned and proposing the new type(s) of collateral to be delivered. | NaN | NaN |
| CollateralSubstitution | Type | NaN | Specifies if the collateral that is substituted was posted against the variation margin or the independent amount. | CollateralSubstitutionTypeCode | NaN |
| CollateralSubstitution | AcceptedAmount | NaN | Provides the accepted collateral substitution amount. | CurrencyAndAmount | NaN |
| CollateralSubstitution | RejectedAmount | NaN | Specifies the collateral substitution amount that is rejected. | CurrencyAndAmount | NaN |
| CollateralSubstitution | RelatedManagementProcess | NaN | Process which groups the activities related to collateral. | CollateralManagement | CollateralSubstitution |
| CollateralSubstitution | NewCollateral | NaN | Specifies the collateral which is replacing the returned one. | Collateral | RelatedCollateralSubstitution |
| CollateralBalance | NaN | NaN | Specifies the different values taken into account to calculate the current collateral. | NaN | NaN |
| CollateralBalance | CollateralDescription | NaN | Describes the collateral included in the collateral balance, | Collateral | CollateralBalance |
| CollateralBalance | HeldAmount | NaN | Specifies the collateral currently held. | CurrencyAndAmount | NaN |
| CollateralBalance | PriorAgreed | NaN | Specifies the collateral which has been agreed but is not yet transferred. | CurrencyAndAmount | NaN |
| CollateralBalance | VariationMarginRelatedRiskCalculation | NaN | Risk coverage for which a current variation margin is provided. | ExposureCalculation | CurrentVariationMargin |
| CollateralBalance | InTransit | NaN | Specifies the collateral which is being transferred. | CurrencyAndAmount | NaN |
| CollateralBalance | SegregatedIndependentAmountRelatedRiskCalculation | NaN | Risk coverage for which a collateral balance is provided. | ExposureCalculation | CurrentSegregatedIndependentAmount |
| CollateralBalance | RelatedCollateralInterestManagement | NaN | Collateral interest management for which an opening balance is specified. | CollateralInterestAdministration | OpeningCollateralBalance |
| CollateralBalance | CollateralInterestManagement | NaN | Collateral interest management for which a closing balance is specified. | CollateralInterestAdministration | ClosingCollateralBalance |
| ExposureCalculation | NaN | NaN | Description of the calculation of the amounts representing the risk that needs to be covered, together with the calculation of the existing coverage. | NaN | NaN |
| ExposureCalculation | TotalCollateralCurrentValue | NaN | Total value of the collateral derived from the sum of the current independent amounts and variation margins held, agreed and in transit. | CurrencyAndAmount | NaN |
| ExposureCalculation | TotalExposedAmount | NaN | The sum of the exposures of all transactions which are in favour of a Party. That is, all transactions which would have an amount payable by the counterparty if they were being terminated. | CurrencyAndAmount | NaN |
| ExposureCalculation | CurrentIndependentAmount | NaN | Amount applied as an add-on to the exposure usually intended to cover a possible increase in exposure before the next valuation date. | IndependentAmount | RelatedRiskCalculation |
| ExposureCalculation | CurrentVariationMargin | NaN | Provides details about the collateral held, in transit or that still needs to be agreed by both parties, against the variation margin. | CollateralBalance | VariationMarginRelatedRiskCalculation |
| ExposureCalculation | CurrentSegregatedIndependentAmount | NaN | Provides details about the collateral held, in transit or that still needs to be agreed by both parties, against the segregated independent amount only. | CollateralBalance | SegregatedIndependentAmountRelatedRiskCalculation |
| ExposureCalculation | VariationMarginAmountRequirement | NaN | Amount of expected margin required by any of the parties of the margin calculation. | MarginAmountRequirement | VariationMarginAmountRequirementCalculation |
| ExposureCalculation | SegregatedAmountRequirement | NaN | Margin requirements for the segregated independent amount. | MarginAmountRequirement | SegregatedAmountRequirementCalculation |
| ExposureCalculation | CollateralManagement | NaN | Specifies the collateral management actions resulting from the calculation of the risk. | CollateralManagement | RiskToCover |
| ExposureCalculation | CounterpartyRisk | NaN | Calculation of the exposure amount that one party has vis-a-vis one counterparty or a central system, based on its credit risk. | CounterpartyRisk | ExposureCalculation |
| ExposureCalculation | TransactionRisk | NaN | Calculation of the exposure amount that one party has vis-a-vis one counterparty or a central system, based on the transactions that are not yet settled. | TransactionRisk | ExposureCalculation |
| ExposureCalculation | TotalCollateralAfterHaircut | NaN | Collateral currently received (+)/delivered (-) in the base currency. This amount is after the haircut has been applied. | CurrencyAndAmount | NaN |
| DisputeManagement | NaN | NaN | Provides the dispute details on the variation margin and/or the segregated independent amount. | NaN | NaN |
| DisputeManagement | DisputedAmount | NaN | Disputed amount. | CurrencyAndAmount | NaN |
| DisputeManagement | DisputeDate | NaN | Date of dispute. | ISODate | NaN |
| DisputeManagement | DisputeResolutionType | NaN | Specifies the type of dispute that is to be resolved regarding the disputed collateral amount. | DisputeResolutionTypeCode | NaN |
| DisputeManagement | RelatedManagementProcess | NaN | Process which groups the activities related to collateral. | CollateralManagement | DisputeManagement |
| IndependentAmount | NaN | NaN | Amount applied as an add-on to the exposure usually intended to cover a possible increase in exposure before the next valuation date. | NaN | NaN |
| IndependentAmount | RelatedRiskCalculation | NaN | Risk coverage for which an independent amount is provided. | ExposureCalculation | CurrentIndependentAmount |
| IndependentAmount | IndependentAmountPerTrade | NaN | Independent amounts that are related to specific trades or groups of trades. | CurrencyAndAmount | NaN |
| IndependentAmount | IndependentAmountValueAtRisk | NaN | Portfolio level independent amount which reflects portfolio change over a short time period using statistical techniques such as volatility and risk factor correlations. | CurrencyAndAmount | NaN |
| IndependentAmount | IndependentAmountNetOpenPosition | NaN | Portfolio level independent amount related to FX net open position, i.e. to the difference between assets and liabilities in a particular currency. This may be measured on a per currency basis or the position of all currencies when calculated in base currency. | CurrencyAndAmount | NaN |
| IndependentAmountTerm | NaN | ExposureTerm | Defines the specific terms used to calculate an independent amount. | NaN | NaN |
| IndependentAmountTerm | Convention | NaN | Determines how the independent amount was applied in the calculation. It is either: - Before threshold, effectively acting as an add on to exposure, - After threshold where the amount is an add on to the credit support amount and forms part of the variation margin requirement, - Segregated where it is treated independently of variation margin for segregation purposes.Defines the specific terms used to calculate an independent amount. | IndependentAmountConventionTypeCode | NaN |
| VariationMarginTerm | NaN | ExposureTerm | Defines the specific terms used to calculate a variation margin. | NaN | NaN |
| VariationMarginTerm | ThresholdAmount | NaN | Amount of unsecured exposure a counterparty will accept before issuing a margin call in the base currency. | CurrencyAndAmount | NaN |
| VariationMarginTerm | ThresholdType | NaN | Defines whetherthe threshold is applied on an unsecured or security basis. | ThresholdTypeCode | NaN |
| MarginAmountRequirement | NaN | NaN | Amount of expected margin required by any of the parties of the margin calculation. | NaN | NaN |
| MarginAmountRequirement | VariationMarginAmountRequirementCalculation | NaN | Exposure valuation which takes into account amount requirements. | ExposureCalculation | VariationMarginAmountRequirement |
| MarginAmountRequirement | DeliverMarginAmount | NaN | Amount of new Variation Margin that will be delivered to one party by the other party after rounding, threshold and minimum transfer amount are taken into account. | CurrencyAndAmount | NaN |
| MarginAmountRequirement | ReturnMarginAmount | NaN | Amount of new Variation Margin that will be recalled to one party from the other party after rounding, threshold and minimum transfer amount are taken into account. | CurrencyAndAmount | NaN |
| MarginAmountRequirement | SegregatedAmountRequirementCalculation | NaN | Exposure valuation which takes into account amount requirements. | ExposureCalculation | SegregatedAmountRequirement |
| MarginAmountRequirement | IntraDayMarginCall | NaN | Total aggregate value of collateral called intraday, excluding repayments. | CurrencyAndAmount | NaN |
| MarginAmountRequirement | PeakInitialMarginLiability | NaN | Peak increase in initial margin liability for the account during the day. | CurrencyAndAmount | NaN |
| MarginAmountRequirement | AggregatePeakLiability | NaN | Peak intraday liability (sum of increase in initial margin relative to end of day plus sum of decrease in variation margin relative to end of day) for a margin account during the day. Liabilities are shown as positive integers. | CurrencyAndAmount | NaN |
| MarginAmountRequirement | PeakVariationMarginLiability | NaN | Peak loss uncollateralised variation margin liability on the margin account during the day. | CurrencyAndAmount | NaN |
| DefaultFundContribution | NaN | NaN | Portion of the participation to the default fund that clearing member must provide. It is the sum of the individual contributions. | NaN | NaN |
| DefaultFundContribution | RelatedMarginCall | NaN | Margin call for which a contribution to a default fund is specified. | MarginCall | DefaultFundContribution |
| DefaultFundContribution | DefaultFund | NaN | Management of the assets posted by participants in a clearing fund that can be used in the event of a default by a participant to compensate non-defaulting participants for losses they suffer due to this default. | DefaultFund | Contribution |
| DefaultFundContribution | ExcessOrDeficitAmount | NaN | Excess amount that the CCP will restitute to the Clearing member OR deficit to be provided by the member for the guarantee fund. | CurrencyAndAmount | NaN |
| DefaultFundContribution | ContributionAccount | NaN | Sub account segregated by the central counterparty on the basis of trading venues/products or other attributes. | Account | DefaultFundContribution |
| DefaultFundContribution | AmountDirection | NaN | Specifies whether the amount is a deficit (debit) or an excess (credit). | DebitCreditCode | NaN |
| ExpectedCollateralType | NaN | NaN | Expected collateral type. | NaN | NaN |
| ExpectedCollateralType | VariationMarginRelatedCall | NaN | Call for which a variation margin type is specified. | MarginCall | ExpectedVariationMarginType |
| ExpectedCollateralType | Delivery | NaN | Type of collateral that will be delivered. | CollateralTypeCode | NaN |
| ExpectedCollateralType | Return | NaN | Type of collateral that will be returned. | CollateralTypeCode | NaN |
| ExpectedCollateralType | SegregatedIndependentAmountRelatedCall | NaN | Call for which a segregated independent amount type is specified. | MarginCall | ExpectedSegregatedIndependentAmountType |
| PortfolioValuation | NaN | NaN | Valuation information of the portfolio. | NaN | NaN |
| PortfolioValuation | TotalPortfolioValue | NaN | Total value of the portfolio. It is derived from the sum of the values of the asset holdings, of the unrealised gain/loss and of the liabilities. | CurrencyAndAmount | NaN |
| PortfolioValuation | TotalBookValue | NaN | Net asset on balance sheet - total portfolio value minus or plus the unrealised gain or loss. | CurrencyAndAmount | NaN |
| PortfolioValuation | TotalReceipts | NaN | Total receipts attributable to the portfolio. | CurrencyAndAmount | NaN |
| PortfolioValuation | TotalDisbursements | NaN | Total disbursements attributable to the portfolio. | CurrencyAndAmount | NaN |
| PortfolioValuation | IncomeReceived | NaN | Income attributable to the portfolio. | CurrencyAndAmount | NaN |
| PortfolioValuation | ExpensesPaid | NaN | Expenses attributable to the portfolio | CurrencyAndAmount | NaN |
| PortfolioValuation | Portfolio | NaN | Specifies the portfolio for which a valuation is calculated. | Portfolio | Valuation |
| PortfolioValuation | ValuationPeriod | NaN | Period for which the valuation is calculated. | DateTimePeriod | RelatedPortfolioValuation |
| BuyIn | NaN | ObligationFulfilment | Process in which the buyer/CCP repurchases shares of stock because the seller either failed to deliver the shares or did not deliver them in a timely fashion. The seller has to make up the price difference if the new shares are more expensive than originally agreed to. | NaN | NaN |
| BuyIn | SecuritiesCompensation | NaN | Securities bought in a buy-in process. | SecuritiesQuantity | RelatedBuyIn |
| BuyIn | BuyinDate | NaN | Date at which the buy-in occurs. | ISODate | NaN |
| BuyIn | BuyInPrice | NaN | Provides the price of the buy-in. | SecuritiesPricing | RelatedBuyIn |
| BuyIn | Fees | NaN | Fees related to a cash compensation or to a securities compensation in a buy-in process | ActiveCurrencyAndAmount | NaN |
| BuyIn | CashCompensation | NaN | In case securities are not available to be bought-in by the buyer/CCP, a cash compensation is required from the seller. It is derived from the association ResultingObligation between ObligationFulfillment and Obligation. | PaymentObligation | PaymentSourceBuyIn |
| BuyIn | RelatedSecuritiesClearingProcess | NaN | Clearing process which includes the buy-in. | SecuritiesClearing | BuyIn |
| ThirdPartyRole | NaN | SystemPartyRole | Party that can use the facilities of a system through one of its members. | NaN | NaN |
| NonClearingMemberRole | NaN | ThirdPartyRole | Party that is involved in a trade but which must clear the trade through a member of an exchange's clearing corporation. | NaN | NaN |
| DefaultFund | NaN | NaN | Assets posted by participants in a clearing fund that can be used in the event of a default by a participant to compensate non-defaulting participants for losses they suffer due to this default. | NaN | NaN |
| DefaultFund | TotalAmount | NaN | Total amount required by the Clearing Member to participate to the Default Fund. | ActiveCurrencyAndAmount | NaN |
| DefaultFund | Contribution | NaN | Contribution information for a default fund. | DefaultFundContribution | DefaultFund |
| DefaultFund | ClearingSystem | NaN | Clearing system for which assets are posted by participants in the default fund. | ClearingSystem | DefaultFund |
| SidePocket | NaN | NaN | Separate account containing illiquid assets of a hedge fund portfolio. Only the present participants in the hedge fund will be entitled to a share of it. | NaN | NaN |
| SidePocket | SidePocketInclusionIndicator | NaN | Indicates whether the investor wants to participate in the optional side pocket. | YesNoIndicator | NaN |
| SidePocket | SidePocketIdentification | NaN | Identifies the side pocket. Type of account used in hedge funds to separate illiquid assets from other more liquid investments. Once an asset is designated for inclusion in a side pocket, new investors do not share in it, and when existing investors redeem from the hedge fund, they remain as investors in the side pocket until it is liquidated. | Max35Text | NaN |
| SidePocket | InvestmentAccount | NaN | Investment account which contains the liquid assets of a hedge fund. | InvestmentAccount | SidePocket |
| SidePocket | SidePocketQuantity | NaN | Quantity of the side pocket. | SecuritiesQuantity | SidePocket |
| CollateralInterestAdministration | NaN | InterestManagement | Calculation and request of interest linked to collateral. | NaN | NaN |
| CollateralInterestAdministration | CollateralManagement | NaN | Collateral processes that interest management is part of. | CollateralManagement | InterestManagement |
| CollateralInterestAdministration | ClosingCollateralBalance | NaN | Specifies the opening collateral balance for the calculation of interest. | CollateralBalance | CollateralInterestManagement |
| CollateralInterestAdministration | OpeningCollateralBalance | NaN | Specifies the opening collateral balance for the calculation of interest. | CollateralBalance | RelatedCollateralInterestManagement |
| ClearingExceptionPartyRole | NaN | TradePartyRole | Identifies the party that is exempt from a clearing obligation. | NaN | NaN |
| ReportingPartyRole | NaN | Role | Party responsible for providing regulatory reports. | NaN | NaN |
| ReportingPartyRole | RegulatoryReport | NaN | Report provided by the reporting party. | RegulatoryReport | ReportingPartyRole |
| MatchingSystem | NaN | System | System which compares two sets of data and provides the comparison result to its users. | NaN | NaN |
| Garnishment | NaN | PaymentObligation | Legal process whereby the debtor pays another party than the creditor to settle a debt due by the creditor to that other party. | NaN | NaN |
| Penalty | NaN | Adjustment | Fee charged when the conditions of a contract are not met. | NaN | NaN |
| Penalty | PenaltyBasisAmount | NaN | Amount used as a basis to calculate the penalty amount. | CurrencyAndAmount | NaN |
| AccountEntry | NaN | CreditInstrument | Amount of money debited or credited on the books of an account servicer. | NaN | NaN |
| ShareholderRegister | NaN | NaN | Contains a list of owners and the quantity of securities they own. | NaN | NaN |
| ShareholderRegister | Identification | NaN | Uniquely identifies the shareholder registry. | Max35Text | NaN |
| ShareholderRegister | Entry | NaN | Number of securities issued by the same entity and registered by owner. | DecimalNumber | NaN |
| WarrantAgent | NaN | AssetPartyRole | Entity appointed by the issuer to process the exercising of warrants, sometimes responsible for the issuance of the warrants into the market. | NaN | NaN |
| LegalRepresentative | NaN | Role | Person that is officially and legally mandated to represent the organisation. Depending on legislation, the legal representative(s) might for instance be assigned by the Board, identified in the by-laws of the organisation, be publicly announced in the official journal of a country. | NaN | NaN |
| CapitalValue | NaN | NaN | Value of the capital. | NaN | NaN |
| CapitalValue | Capital | NaN | Capital for which a value is provided. | NaN | NaN |
| Capital | NaN | NaN | Amount of money targeted to be raised through the issuance of a security. | NaN | NaN |
| Capital | AssetIssuance | NaN | Issued asset. | Issuance | CapitalRaised |
| Capital | Date | NaN | Date/time at which capital amount was recorded. | ISODateTime | NaN |
| Capital | Type | NaN | Specifies the type of capital. | CapitalTypeCode | NaN |
| Capital | Amount | NaN | Capital expressed as a currency and amount. | CurrencyAndAmount | NaN |
| Capital | Unit | NaN | Capital expressed as a number of units. | DecimalNumber | NaN |
| SchemeOwner | NaN | InformationPartyRole | Description of the owner of a code scheme, for example, International Standards Organization. | NaN | NaN |
| Cashier | NaN | CardPaymentPartyRole | Cashier who carried out the payment card transaction. | NaN | NaN |
| Cashier | ShiftNumber | NaN | Identifies the shift of the cashier. | Max2NumericText | NaN |
| Reconciliation | NaN | NaN | Process of matching different documents submitted by parties to a trade. | NaN | NaN |
| Reconciliation | System | NaN | System which provides the reconciliation process. | System | Reconciliation |
| Reconciliation | Document | NaN | Document submitted in a reconciliation process. | Document | Reconciliation |
| Reconciliation | ReconciledTrades | NaN | Trades which are reconciled with entries in an account. | Trade | Reconciliation |
| Reconciliation | Account | NaN | Account for which a reconciliation process is performed. | Account | Reconciliation |
| SSIDatabaseProvider | NaN | SettlementPartyRole | Provider of a standing settlement instruction (SSI) database. | NaN | NaN |
| SSIDatabaseProvider | StandingSettlementDatabase | NaN | Settlement instruction database information which is provided. | StandingSettlementInstruction | SSIDatabaseProvider |
| PortfolioManagerRole | NaN | AssetPartyRole | Party responsible for investing another party's assets and for managing the day-to-day operations. | NaN | NaN |
| LocalSettlementAgentRole | NaN | SecuritiesSettlementPartyRole | Party which holds securities and settles trades for non-resident customers. The customers' securities are held in one omnibus account or in sub accounts at the local central securities depository. | NaN | NaN |
| ChequePartyRole | NaN | Role | Role played by a party in the context of a payment by cheque. | NaN | NaN |
| ChequePartyRole | Cheque | NaN | Identifies the cheque for which a party plays a role. | Cheque | ChequePartyRole |
| Payee | NaN | ChequePartyRole | Party that receives funds as required by a transaction. | NaN | NaN |
| Liquidity | NaN | NaN | Ability of a financial instrument to be easily traded and converted to cash, at conditions that do not affect its price. | NaN | NaN |
| Liquidity | Quantity | NaN | Quantity of a financial instrument for which liquidity range details are provided. | SecuritiesQuantity | Liquidity |
| Liquidity | ListTrading | NaN | List trading process for which liquidity data is provided. | ListTrading | Liquidity |
| Liquidity | IndicatorType | NaN | Type of liquidity measure, of a financial instrument, on a market. | LiquidityIndicatorTypeCode | NaN |
| Liquidity | Upper | NaN | Upper liquidity indicator, represented as a percentage of the average trade daily volume. | PercentageRate | NaN |
| Liquidity | Lower | NaN | Lower liquidity indicator, represented as a percentage of the average trade daily volume. | PercentageRate | NaN |
| Liquidity | Value | NaN | Market value of the securities position for which liquidity details are provided. | CurrencyAndAmount | NaN |
| Liquidity | WeightedAverageLiquidity | NaN | Indicates the overall weighted average liquidity expressed as a percentage of average daily volume. | PercentageRate | NaN |
| SecuritiesOrderParameters | NaN | NaN | Parameters of the transfer of a financial instrument. | NaN | NaN |
| SecuritiesOrderParameters | MinimumQuantity | NaN | Minimum quantity of financial instrument to be bought or sold if the entire order cannot be executed. | SecuritiesQuantity | MinimumQuantityOrderParameters |
| SecuritiesOrderParameters | MatchIncrement | NaN | Allows orders to specify a minimum quantity that applies to every execution. (one execution could be for multiple counter-orders). The order may still fill against smaller orders, but the cumulative quantity of the execution must be in multiples of the MatchIncrement. | SecuritiesQuantity | MatchIncrementOrderParameters |
| SecuritiesOrderParameters | PegInstructions | NaN | Additional instructions if the order is pegged. | SecuritiesPegOrderInstruction | Order |
| SecuritiesOrderParameters | PreviousClosingPrice | NaN | Previous closing price of security. | SecuritiesPricing | RelatedOrder |
| SecuritiesOrderParameters | AutoRouting | NaN | Indicates whether an automatic routing system is involved. | AutoRoutingCode | NaN |
| SecuritiesOrderParameters | CorporateActionOptionIndicator | NaN | Indicates the possible options or choices available to account owner (for investment funds). | IncomePreferenceCode | NaN |
| SecuritiesOrderParameters | ExecutionTimeLimit | NaN | Indicates from/until when an order must be executed. | ExecutionTimeLimitCode | NaN |
| SecuritiesOrderParameters | PreAllocationConditionIndicator | NaN | Indicates the conditions that apply to a pre-allocation. | Max16Text | NaN |
| SecuritiesOrderParameters | PriorityIndicator | NaN | Indicates the execution priority of the trade. | PriorityCode | NaN |
| SecuritiesOrderParameters | RequestedDealCurrency | NaN | Currency in which a trade should be executed. | CurrencyCode | NaN |
| SecuritiesOrderParameters | OrderHandlingInstruction | NaN | Specifies instructions for order handling on the broker trading floor. | TradingFloorOrderHandlingCode | NaN |
| SecuritiesOrderParameters | StockLocateRequired | NaN | Indicates whether the broker is to locate the stock in conjunction with a short sell order.This information is mandatory in case of short sales. When executed, the report will then mention the securities location. | YesNoIndicator | NaN |
| SecuritiesOrderParameters | WorkingIndicator | NaN | Indicates if the order is currently being worked. For open outcry markets this indicates that the order is being worked in the crowd. For electronic markets it indicates that the order has transitioned from a contingent order to a market order. | YesNoIndicator | NaN |
| SecuritiesOrderParameters | BookPriorityIndicator | NaN | Indicates if a Cancel/Replace has caused an order to lose book priority. | BookPriorityIndicatorCode | NaN |
| SecuritiesOrderParameters | MaxPriceLevels | NaN | Allows an order to specify a maximum number of price levels to trade through. | Number | NaN |
| SecuritiesOrderParameters | PreTradeAnonymity | NaN | Allows trader to explicitly request anonymity or disclosure in pre-trade market data feeds. Anonymity is relevant in markets where counterparties are regularly disclosed in order depth feeds. Disclosure is relevant when counterparties are not normally visible. | YesNoIndicator | NaN |
| SecuritiesOrderParameters | GoodTillBooking | NaN | For partially good till orders, the specification of whether to book each execution, or to accumulate the executions. | GoodTillBookingInstructionCode | NaN |
| SecuritiesOrderParameters | ManualOrderIndicator | NaN | Indicates if the order was initially received manually (as opposed to electronically). | YesNoIndicator | NaN |
| SecuritiesOrderParameters | DirectedOrder | NaN | Indicates if the customer directed this order to a specific execution venue (Y) or not (N). | YesNoIndicator | NaN |
| SecuritiesOrderParameters | ReceivedDepartment | NaN | Identifies the Broker / Dealer Department that first took the order. | Max35Text | NaN |
| SecuritiesOrderParameters | CustomerHandlingInstruction | NaN | Codes that apply special information that the Broker / Dealer needs to report, as specified by the customer. | CustomerHandlingInstructionsCode | NaN |
| SecuritiesOrderParameters | ProcessCode | NaN | Used to identify soft trades at order entry. | CommissionTypeV2Code | NaN |
| SecuritiesOrderParameters | RelatedSecuritiesOrder | NaN | Securities order for which parameters are specified. | SecuritiesOrder | OrderExecutionParameters |
| Quote | NaN | NaN | Indicates whether the quote details are indicated as an offer, a bid or a mid of a security, commodity, currency (the latter being an average of the offer and the bid). | NaN | NaN |
| Quote | MaximumQuantity | NaN | Specifies the maximum quantity of the financial instrument. | SecuritiesQuantity | MaximumQuantityRelatedQuote |
| Quote | Quantity | NaN | Quantity of a Financial Instrument. | SecuritiesQuantity | QuantityRelatedQuote |
| Quote | MinimumQuantity | NaN | Specifies the minimal quantity of the financial instrument. | SecuritiesQuantity | MinimumQuantityRelatedQuote |
| Quote | PartyRole | NaN | Specifies each role played by a party in a quotation process. | InformationPartyRole | Quote |
| Quote | RelatedNegotiation | NaN | Negotiation process during which quotes are provided. | Negotiation | Quote |
| Quote | QuotedRate | NaN | Exchange rate specified in a quote. | CurrencyExchange | CurrencyExchangeForSecuritiesQuote |
| Quote | PreviousClosingPrice | NaN | Previous closing price of the financial instrument - Useful for verifying its identification. | SecuritiesPricing | PreviousClosingPriceRelatedQuote |
| Quote | RequestedPrice | NaN | Is used to specify the desired currency of the quoted price when they differ from the normal trading currency of the instrument being quote requested. | SecuritiesPricing | RequestedPriceRelatedQuote |
| Quote | Price | NaN | Indicates the price of the instrument, applicable to the quote. | SecuritiesPricing | PriceRelatedQuote |
| Quote | MarketPrice | NaN | Used by markets to indicate the current best bid and offer. | SecuritiesPricing | MarketPriceRelatedQuote |
| Quote | MidSideQuoteVariable | NaN | Quote details for which mid information is provided. | SecuritiesQuoteVariable | MidSide |
| Quote | BidSideQuoteVariable | NaN | Quote details for which bid information is provided. | SecuritiesQuoteVariable | BidSide |
| Quote | OfferSideQuoteVariable | NaN | Quote details for which offer information is provided. | SecuritiesQuoteVariable | OfferSide |
| Quote | SecurityQuoteVariable | NaN | Proposition of price for a financial instrument. | SecuritiesQuoteVariable | RelatedQuote |
| Quote | QuoteSwap | NaN | Characteristics and conditions, quoted by the seller, by which a borrower can exchange one type of fund for another. | FinancialInstrumentSwap | RelatedQuote |
| Quote | ValidUntilDateTime | NaN | Expresses the validity date and time of the Quote. | ISODateTime | NaN |
| Quote | Currency | NaN | Can be used to specify the desired currency of the quoted price that may differ from the normal trading currency of the instrument being quote requested. | CurrencyCode | NaN |
| Quote | Status | NaN | Provide the status for the quote. | QuoteStatus | RelatedQuote |
| Quote | QuotedSecurity | NaN | Security specified in a quote. | Security | Quote |
| PairOff | NaN | ObligationFulfilment | Transaction is paired off and netted against one or more previous transactions. | NaN | NaN |
| PairOff | PairedOffQuantity | NaN | Quantity of financial instruments to be paired-off. | SecuritiesQuantity | Pairoff |
| PairOff | RelatedSecuritiesSettlement | NaN | Trade settlement process which is the source of the pair off. | SecuritiesSettlement | PairOff |
| SecuritiesAndCashDistribution | NaN | Distribution | Characteristics for a mixed cash and securities distribution event. | NaN | NaN |
| SecuritiesAndCashDistribution | IntermediateToUnderlyingDenominator | NaN | Quantity of interim securities awarded for a given quantity of underlying shares. | SecuritiesQuantity | IntermediateToUnderlyingDenominatorDistributionInformation |
| SecuritiesAndCashDistribution | MaximumHolding | NaN | Indicates the maximum quantity of financial instrument that must be held in order to be entitled to take part in the event. | SecuritiesQuantity | MaximumHoldingDistributionInformation |
| SecuritiesAndCashDistribution | MaximumExercisableQuantity | NaN | Indicates the maximum quantity of financial instrument that may be exercised in the event. | SecuritiesQuantity | MaximumExercisableQuantityDistributionInformation |
| SecuritiesAndCashDistribution | MinimumExercisableQuantity | NaN | Minimum quantity of securities that must be exercised. | SecuritiesQuantity | MinimumExercisableQuantityDistributionInformation |
| SecuritiesAndCashDistribution | DistributedToUnderlyingDenominator | NaN | Quantity of new securities that will be derived by the exercise of a given quantity of intermediate securities. | SecuritiesQuantity | DistributedToUnderlyingDenominatorDistributionInformation |
| SecuritiesAndCashDistribution | IntermediateToUnderlyingNumerator | NaN | Quantity of interim securities awarded for a given quantity of underlying shares. | SecuritiesQuantity | IntermediateToUnderlyingNumeratorDistributionInformation |
| SecuritiesAndCashDistribution | MinimumHolding | NaN | Indicates the minimum quantity of financial instrument that must be held in order to be entitled to take part in the event. | SecuritiesQuantity | MinimumHoldingDistributionInformation |
| SecuritiesAndCashDistribution | DistributedToUnderlyingNumerator | NaN | Quantity of new securities that will be derived by the exercise of a given quantity of intermediate securities. | SecuritiesQuantity | DistributedToUnderlyingNumeratorDistributionInformation |
| SecuritiesAndCashDistribution | SecuritiesDistribution | NaN | Securities distribution elements of a cash and securities distribution process. | SecuritiesDistribution | SecuritiesAndCashDistribution |
| SecuritiesAndCashDistribution | CashDistribution | NaN | Cash distribution elements of a cash and securities distribution process. | CashDistribution | SecuritiesAndCashDistribution |
| SecuritiesDistribution | NaN | Distribution | Characteristics for a securities distribution event. | NaN | NaN |
| SecuritiesDistribution | MaximumHolding | NaN | Indicates the maximum quantity of financial instrument that must be held in order to be entitled to take part in the event. | SecuritiesQuantity | MaximumHoldingRelatedSecuritiesDistribution |
| SecuritiesDistribution | IntermediateToUnderlyingNumerator | NaN | The quantity of interim securities awarded for a given quantity of underlying shares. | SecuritiesQuantity | IntermediateToUnderlyingNumeratorRelatedSecuritiesDistribution |
| SecuritiesDistribution | IntermediateToUnderlyingDenominator | NaN | The quantity of interim securities awarded for a given quantity of underlying shares. | SecuritiesQuantity | IntermediateToUnderlyingDenominatorRelatedSecuritiesDistribution |
| SecuritiesDistribution | DistributedToUnderlyingDenominator | NaN | Quantity of new securities that will be derived by the exercise of a given quantity of intermediate securities. | SecuritiesQuantity | DistributedToUnderlyingDenominatorRelatedSecuritiesDistribution |
| SecuritiesDistribution | DistributedToUnderlyingNumerator | NaN | Quantity of new securities that will be derived by the exercise of a given quantity of intermediate securities. | SecuritiesQuantity | DistributedToUnderlyingNumeratorRelatedSecuritiesDistribution |
| SecuritiesDistribution | MinimumHolding | NaN | Indicates the minimum quantity of financial instrument that must be held in order to be entitled to take part in the event. | SecuritiesQuantity | MinimumHoldingRelatedSecuritiesDistribution |
| SecuritiesDistribution | CashFractionsPrice | NaN | Price paid by the issuer for the remaining fraction. | SecuritiesPricing | CashFractionsPriceRelatedSecuritiesDistribution |
| SecuritiesDistribution | SubscriptionPrice | NaN | The amount of money required per unit for the purchase of an instrument. | SecuritiesPricing | SuscriptionPriceRelatedSecuritiesDistribution |
| SecuritiesDistribution | ReinvestmentPrice | NaN | Price at which a cash disbursement will be reinvested into a security. | SecuritiesPricing | ReinvestmentPriceRelatedSecuritiesDistribution |
| SecuritiesDistribution | IntermediateSecurityExpiryDate | NaN | Date/time at which a privilege or an intermediate security is no longer available. | ISODateTime | NaN |
| SecuritiesDistribution | TradingAvailabilityDate | NaN | Date/time at which a security starts or resumes trading. | ISODateTime | NaN |
| SecuritiesDistribution | OfferExpiryDate | NaN | Date/time at which a privilege or a security is no longer available. | ISODateTime | NaN |
| SecuritiesDistribution | OversubscriptionRate | NaN | Rate of oversubscription allowed by the issuer. | PercentageRate | NaN |
| SecuritiesDistribution | OversubscriptionAmount | NaN | Amount of oversubscription allowed by the issuer. | CurrencyAndAmount | NaN |
| SecuritiesDistribution | ReinvestmentAmount | NaN | Amount at which a cash disbursement will be reinvested into a security. | CurrencyAndAmount | NaN |
| SecuritiesDistribution | ReinvestmentRate | NaN | Rate at which a cash disbursement will be reinvested into a security. | BaseOneRate | NaN |
| SecuritiesDistribution | LoyalityPremiumIndicator | NaN | Dividend, in addition to regular dividends, payable to loyal (time, size, amount) investors. | YesNoIndicator | NaN |
| SecuritiesDistribution | OversubscriptionIndicator | NaN | Indicates that the event permits the holder to subscribe to more securities than the underlying position allows. | YesNoIndicator | NaN |
| SecuritiesDistribution | RenounceableIndicator | NaN | Indicates whether the intermediate securities held by the beneficial owner or agent can be sold. | YesNoIndicator | NaN |
| SecuritiesDistribution | DecimalPrecision | NaN | Indicates the number of digits to the right of the decimal point. | Number | NaN |
| SecuritiesDistribution | ReinvestmentType | NaN | Specifies whether the investment will be net or gross. | PaymentTypeCode | NaN |
| SecuritiesDistribution | RevocableIndicator | NaN | Action or event can be reversed at anytime, or otherwise annulled. | YesNoIndicator | NaN |
| SecuritiesDistribution | SecuritiesAndCashDistribution | NaN | Distribution for which the cash distribution elements are provided. | SecuritiesAndCashDistribution | SecuritiesDistribution |
| SecuritiesDistribution | FractionTreatment | NaN | Specifies how the fractions will be treated. | RoundingDirectionCode | NaN |
| SecuritiesDistribution | IntermediateSecurityDistributionIndicator | NaN | Indicates whether there will be a distribution of intermediate securities or privilege. | YesNoIndicator | NaN |
| Sponsor | NaN | SecuritiesPartyRole | The party that advises a company on how to issue new shares or bonds. | NaN | NaN |
| FundPromoter | NaN | FundManagerRole | Fund Promoter | NaN | NaN |
| ProxyAgent | NaN | MeetingPartyRole | Party appointed to organise the issuer meeting. Also called vote tabulator. | NaN | NaN |
| PortfolioStrategy | NaN | NaN | Rough allocation of the portfolio. | NaN | NaN |
| PortfolioStrategy | Portfolio | NaN | Portfolio for which a strategy is specified. | Portfolio | Strategy |
| PortfolioStrategy | InclusionIndicator | NaN | Indicates whether the referred strategy is included. | YesNoIndicator | NaN |
| PortfolioStrategy | MinimumInvestmentAmount | NaN | Minimum amount that has to be invested in the specified strategy. | CurrencyAndAmount | NaN |
| PortfolioStrategy | MinimumInvestmentRate | NaN | Minimum percentage that has to be invested in the specified strategy. | PercentageRate | NaN |
| PortfolioStrategy | MaximumInvestmentAmount | NaN | Maximum amount that may be invested in the specified strategy. | CurrencyAndAmount | NaN |
| PortfolioStrategy | MaximumInvestmentRate | NaN | Maximum percentage that may be invested in the specified strategy. | PercentageRate | NaN |
| PortfolioStrategy | EffectivePeriod | NaN | Period during which the investment guideline is valid. | NaN | NaN |
| PortfolioStrategy | DistributionPolicy | NaN | Income policy relating to the fund, ie, if income is paid out or retained in the fund. | DistributionPolicyCode | NaN |
| PortfolioStrategy | Description | NaN | Free text description of the investment guideline, for example, rating requirements. | Max2000Text | NaN |
| PortfolioStrategy | Definition | NaN | Definition of the portfolio strategy. | PortfolioStrategyDefinition | Strategy |
| JurisdictionStrategy | NaN | PortfolioStrategy | Strategy is jurisdiction based. | NaN | NaN |
| JurisdictionStrategy | Jurisdiction | NaN | Jurisdiction (country, county, state, province, city) of the investment. | Jurisdiction | AssociatedStrategy |
| AttendanceConfirmationDeadline | NaN | MeetingDeadline | Date and time by which the beneficial owner or agent must notify of their intention to participate in a meeting. | NaN | NaN |
| Auditor | NaN | InvestmentFundPartyRole | Party in charge of examining and verifying a fund's financial and accounting records as well as supporting documents. | NaN | NaN |
| BondCounsel | NaN | SecuritiesPartyRole | Attorney who prepares the legal opinion concerning a municipal bond issue. | NaN | NaN |
| PortfolioBenchmark | NaN | NaN | Security or other price against which the performance of the portfolio is evaluated. | NaN | NaN |
| PortfolioBenchmark | Index | NaN | Specifies the index which may be used for decomposition. | Index | PortfolioBenchmark |
| PortfolioBenchmark | Portfolio | NaN | Portfolio to which the benchmark applies. | Portfolio | Benchmark |
| PortfolioBenchmark | BenchmarkWeight | NaN | Instrument weighting in the benchmark for the portfolio. | PercentageRate | NaN |
| PortfolioBenchmark | MaximumDeviation | NaN | Maximum allowable deviation from the benchmark. | PercentageRate | NaN |
| PortfolioBenchmark | MinimumDeviation | NaN | Minimum allowable deviation from the benchmark. | PercentageRate | NaN |
| PortfolioBenchmark | EffectivePeriod | NaN | Period during which the instrument is used as a benchmark for the portfolio. | NaN | NaN |
| PortfolioBenchmark | Description | NaN | Free text description of the benchmark used to determine the performance of a portfolio. | Max350Text | NaN |
| PortfolioBenchmark | Approver | NaN | Party who is the supervised entity endorsing the benchmark. | PartyIdentificationInformation | RelatedApprovedBenchmark |
| PortfolioBenchmark | Administrator | NaN | Party who is administrating the benchmark. | PartyIdentificationInformation | RelatedAdministratedBenchmark |
| CentralClearingCounterpartyRole | NaN | SettlementPartyRole | Infrastructure that may be a component of a clearing house and which facilitates clearing and settlement for its members by standing between the buyer and the seller. It may net transactions and it substitutes itself as settlement counterparty for each position. | NaN | NaN |
| CentralClearingCounterpartyRole | System | NaN | Specifies the system which plays a role in the clearing of securities. | ClearingSystem | CentralClearingCounterparty |
| TerminalManagerRole | NaN | SystemPartyRole | Identifies the party which is the terminal manager (TM) to contact for the maintenance. | NaN | NaN |
| TerminalManagerRole | TerminalManagementSystem | NaN | Identifies the system for which a party plays the terminal manager role. | TerminalManagementSystem | TerminalManagerRole |
| MarketClaimCounterparty | NaN | CorporateActionPartyRole | Party that has reimbursed the account owner with funds to which they were legally entitled. | NaN | NaN |
| CorporateActionOfferor | NaN | CorporateActionPartyRole | Provides the entity making the offer and that is different from the issuing company. | NaN | NaN |
| MeetingServicing | NaN | CorporateActionServicing | Services which consists in notifying the investor or its agent of a meeting, in validating and relaying its instructions and in calculating its entitlement based on its holdings. | NaN | NaN |
| MeetingServicing | MeetingSpecification | NaN | Meeting for which services are provided. | Meeting | MeetingServicing |
| MeetingServicing | MeetingNotice | NaN | Service which consists in notifying the investor of a meeting. It may contain details of the meeting as defined by the agent in addition to the details defined by the issuer. | MeetingNotice | RelatedServicing |
| MeetingServicing | MeetingEntitlement | NaN | Calculation of the entitlementbased on the balance in the account. | MeetingEntitlement | RelatedServicing |
| MeetingServicing | MeetingInstruction | NaN | Service which consists in validating, calculating and transferring the investor's instruction. | InstructionForMeeting | RelatedServicing |
| MeetingServicing | MeetingResultDissemination | NaN | Service which consists in distributing the results of the meeting to the investor. | MeetingResultDissemination | RelatedServicing |
| MeetingResultDissemination | NaN | NaN | Provides information on the voting results of a shareholders meeting. | NaN | NaN |
| MeetingResultDissemination | RelatedServicing | NaN | Meeting servicing process which comprises the dissemination of the results. | MeetingServicing | MeetingResultDissemination |
| MeetingResultDissemination | VoteResult | NaN | Specifies whether a resolution is accepted and the number of votes which were cast. | VoteResult | VoteDissemination |
| CardIssuer | NaN | CardPaymentPartyRole | Party that issues a payment card, as expressed by a numeric identification of the card issuer according to ISO/IEC 7812-1. | NaN | NaN |
| CaseCreator | NaN | InvestigationPartyRole | Party who initiates the case. | NaN | NaN |
| CentralSecuritiesDepositoryRole | NaN | DepositoryRole | An infrastructure that, holds or controls, the holding of physical or dematerialised financial instruments belonging to all, or a large portion of, the investors in a securities market. This effects the centralised transfer of ownership of such securities by entries on its books and records. The depository may delegate custody to another entity (custodian). | NaN | NaN |
| ChargeAgent | NaN | ChargePartyRole | Party that takes the transaction charges or to which the transaction charges are due. | NaN | NaN |
| ChargeBearer | NaN | ChargePartyRole | Party(ies) liable for a charge associated with the transfer of cash. | NaN | NaN |
| ChargeRecipient | NaN | ChargePartyRole | Party entitled to the amount of money resulting from a charge. | NaN | NaN |
| ClaimsAgent | NaN | InsurancePartyRole | Party where claims under the insurance policy have to be addressed. | NaN | NaN |
| ClearingPlace | NaN | SettlementPartyRole | Infrastructure that may be a component of a clearing house and which facilitates clearing and settlement for its members by standing between the buyer and the seller. It may net transactions and it substitutes itself as settlement counterparty for each position. | NaN | NaN |
| CollectionAgent | NaN | SecuritiesPartyRole | Additional party appointed to collect payment or securities on behalf of the issuer. | NaN | NaN |
| CommissionPartyRole | NaN | Role | Role played by a party in the context of a payment of commission. | NaN | NaN |
| CommissionPartyRole | Commission | NaN | Identifies the commission for which a party plays a role. | Commission | CommissionPartyRole |
| CommissionRecipient | NaN | CommissionPartyRole | Party entitled to the amount of money resulting from a commission. | NaN | NaN |
| ContraClearingFirm | NaN | SettlementPartyRole | Party that is the clearing firm of the counterparty in a trade. | NaN | NaN |
| ContraFirm | NaN | SecuritiesTradePartyRole | Party that is the counterparty in a trade. | NaN | NaN |
| CorrespondentClearingFirm | NaN | SettlementPartyRole | Firm that is going to carry the position on their books at another clearinghouse (exchanges). | NaN | NaN |
| CustodianRole | NaN | SecuritiesPartyRole | The party that safekeeps and administers assets on behalf of the owner. | NaN | NaN |
| CustodianRole | InvestmentFund | NaN | Fund for which a custodian is specified. | InvestmentFund | Custodian |
| DataSetInitiator | NaN | CardPaymentPartyRole | Initiator of a data set. | NaN | NaN |
| DeliverersCustodian | NaN | SecuritiesSettlementPartyRole | Party that acts on behalf of the seller of securities when the seller does not have a direct relationship with the delivering agent. | NaN | NaN |
| DeliverersIntermediary | NaN | SecuritiesSettlementPartyRole | Party that the deliverer's custodian uses to effect the delivery of a security, when the deliverer's custodian does not have a direct relationship with the delivering agent. | NaN | NaN |
| DeliveringAgent | NaN | SecuritiesSettlementPartyRole | Party that delivers securities to the receiving agent at the place of settlement. For example, a central securities depository. | NaN | NaN |
| DeliveringDepositoryRole | NaN | DeliveringSettlementParty | Organisation holding securities to enable book entry transfer of securities. Such an organisation may also carry out centralised comparison and transaction processing such as clearing and settlement of securities. The physical securities may be immobilised by the depository, or securities may be dematerialised (so that they exist only as electronic records). It is also responsible for compliance of the portfolio with legal ratios etc. The depository may delegate custody to another entity (custodian). | NaN | NaN |
| DeterminationAgent | NaN | SecuritiesPartyRole | Party that determines a parameter on which a calculation is based. For example, fixing of a reference rate. | NaN | NaN |
| DirectMember | NaN | SystemMemberRole | Financial institution or member of a system having full rights to the system specifications. | NaN | NaN |
| DocumentSignatory | NaN | DocumentPartyRole | Person who binds himself or herself, or the entity he or she is authorized to represent, by his or her signature on the document. | NaN | NaN |
| Drawee | NaN | ChequePartyRole | Financial institution on which a cheque is drawn, ie, the financial institution that services the account of the entity that issued the cheque. | NaN | NaN |
| Drawer | NaN | ChequePartyRole | Account owner that issues a cheque ordering the drawee bank to pay a specific amount, upon demand, to the payee. | NaN | NaN |
| EnteringFirm | NaN | SecuritiesOrderPartyRole | Broker that has recorded or reported an execution of a trade. When an entering firm that is not a party to a trade enters the trade into a trade recording system, any inquiries can be directed to the appropriate source. | NaN | NaN |
| ETCServiceProvider | NaN | SecuritiesTradePartyRole | Party that provides electronic trade confirmation services to its clients. For example, trade and allocation matching. | NaN | NaN |
| ExecutingTrader | NaN | SecuritiesTradePartyRole | Trader that executes a trade for an organisation. | NaN | NaN |
| ExecutingTrader | ExecutingBroker | NaN | Executing broker which employs the trade | ExecutingBrokerRole | ExecutingTrader |
| SecuritiesTradeSystemRole | NaN | SecuritiesTradePartyRole | Role played by a system in the context of a securities trade. | NaN | NaN |
| ExecutionDestination | NaN | SecuritiesTradePartyRole | Destination for the execution, as defined by an institution when an order is entered. | NaN | NaN |
| ForwardingAgentRole | NaN | PaymentPartyRole | Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain for execution. | NaN | NaN |
| FundAccountantRole | NaN | InvestmentFundPartyRole | Party that keeps accounting records of available assets and liabilities of a fund. It calculates dealing prices, the net asset value (NAV) of the fund, and may provide fund performance and tax data. Can be sub-contracted by the fund administrator. | NaN | NaN |
| FundAdministratorRole | NaN | InvestmentFundPartyRole | Party in charge of financial accounting, net asset value (NAV) calculation, management and performance fee calculation. Can also be in charge of orders centralisation and registration. | NaN | NaN |
| FundOrderDesk | NaN | InvestmentFundPartyRole | Principal entity appointed by the fund to which orders should be submitted. | NaN | NaN |
| FundOrderDesk | MainFundOrderDeskIndicator | NaN | Indicates whether the fund order desk is the principal entity appointed by the fund to which orders should be submitted. | YesNoIndicator | NaN |
| FundOrderDesk | MainFundOrderDeskAccount | NaN | Settlement details for the main fund order desk as defined in the prospectus of the investment fund class. | InvestmentAccount | AccountForInvestmentFundProcessing |
| GiverRole | NaN | CollateralPartyRole | Party which provides the collateral. A party can be both a taker and a giver in a collateral relationship. | NaN | NaN |
| GiveUpClearingFirm | NaN | SettlementPartyRole | Firm to which the trade is given up (carries the position that results from a trade). | NaN | NaN |
| GoodsPartyRole | NaN | Role | Role played by a party in the context of handling goods. | NaN | NaN |
| GoodsPartyRole | Item | NaN | Item produced by the manufacturer. | Goods | PartyRole |
| GuarantorRole | NaN | GuaranteePartyRole | Legal entity, other than the issuer, who gives a guarantee. The guarantor becomes liable in case of default. | NaN | NaN |
| GuarantorRole | Position | NaN | Rank of this guarantor. | positiveInteger | NaN |
| GuaranteeBeneficiary | NaN | GuaranteePartyRole | Party that is the beneficiary of the guarantee. | NaN | NaN |
| IndirectMember | NaN | ThirdPartyRole | Financial institution or member of a system having limited rights to the system specifications. | NaN | NaN |
| InitiatingPartyRole | NaN | PaymentPartyRole | Party initiating the payment to an agent. In the payment context, this can either be the debtor (in a credit transfer), the creditor (in a direct debit), or a party that initiates the payment on behalf of the debtor or creditor. In the context of treasury, the party that instructs the trading party to execute a treasury deal on its behalf. | NaN | NaN |
| InstructingReimbursementAgent | NaN | CashSettlementInstructionPartyRole | Specifies the agent through which the instructing agent will reimburse the instructed agent.Usage: If the instructing and instructed agents have the same reimbursement agent, then only InstructingReimbursementAgent must be used. | NaN | NaN |
| Insurer | NaN | InsurancePartyRole | Insurance company that issues a particular insurance policy to an assured party. | NaN | NaN |
| InvestmentAdvisor | NaN | AssetPartyRole | The party that provides investment guidance at a fee. | NaN | NaN |
| LeadUnderwriter | NaN | SecuritiesPartyRole | Main party that is awarded the mandate by a borrower to raise money via a new issue. The lead manager guarantees the liquidity of the deal, arranges the syndication of the issue and undertakes a major underwriting and distribution commitment. Also called Lead Manager. | NaN | NaN |
| LegalAdvisor | NaN | SecuritiesPartyRole | A party that provides legal advice for a fee. | NaN | NaN |
| LocalBroker | NaN | Broker | Party paid a commission following the execution of a trade, as directed by the investment manager. | NaN | NaN |
| MandateIssuer | NaN | MandatePartyRole | Issuer of the mandate. | NaN | NaN |
| ObligorBank | NaN | CommercialTradePartyRole | Bank that has to pay under a payment obligation contracted between two financial institutions related to the financing of a commercial transaction. | NaN | NaN |
| OrderOriginationFirm | NaN | SecuritiesOrderPartyRole | Firm that originates or submits the original order for execution. | NaN | NaN |
| OrderOriginationTrader | NaN | SecuritiesOrderPartyRole | Identifies the trader at the order origination firm that submitted the order. | NaN | NaN |
| PayingAgentRole | NaN | NaN | Additional party appointed to distribute payment or securities on behalf of the issuer. | NaN | NaN |
| PayingAgentRole | CommissionAmount | NaN | Amount of paying/sub-paying agent commission. | CurrencyAndAmount | NaN |
| PlacementAgent | NaN | InvestmentFundPartyRole | Party that helps hedge funds to refine their strategy. May also introduce partners such as fund of funds, pension funds, insurance companies and family offices. | NaN | NaN |
| PlaceOfRegistry | NaN | SecuritiesPartyRole | Location at which records of ownership are maintained for a financial instrument, and at which ownership changes must be recorded. | NaN | NaN |
| PlaceOfSettlement | NaN | SecuritiesSettlementPartyRole | Place where settlement of securities occurs. | NaN | NaN |
| PlaceOfSettlement | SettlementMarket | NaN | Identifies the market for the settlement. | TradingMarket | RelatedPlaceOfSettlement |
| POIManufacturer | NaN | CardPaymentPartyRole | Manufacturer or the software, hardware or system of the POI component. | NaN | NaN |
| PrimaryPlaceOfDeposit | NaN | SecuritiesPartyRole | Specifies the primary place of deposit for the securities. | NaN | NaN |
| PrincipalCollectionAgent | NaN | SecuritiesPartyRole | Main party appointed to collect payment or securities on behalf of the issuer. | NaN | NaN |
| PrincipalPayingAgent | NaN | SecuritiesPartyRole | Main party appointed to distribute payment or securities on behalf of the issuer. | NaN | NaN |
| ProxyAssignerRole | NaN | MeetingPartyRole | Party entitled to appoint a proxy. | NaN | NaN |
| QualifiedForeignIntermediary | NaN | TradePartyRole | Foreign financial institution that has been authorised by local authorities to act as account management institution in the country. | NaN | NaN |
| QualifiedForeignIntermediary | Country | NaN | Specifies the country in which the intermediary is qualified. | CountryCode | NaN |
| QuoteOriginator | NaN | InformationPartyRole | Originator of the quote. | NaN | NaN |
| QuoteOriginator | QuoteOriginatorType | NaN | Identifies in what capacity(role) the originator of the quote is acting. | OriginatorRoleCode | NaN |
| QuoteRequestor | NaN | InformationPartyRole | Requestor of the quote | NaN | NaN |
| QuoteRequestor | RequestorEligibility | NaN | Identifies if the requestor of the quote is an elligible counterparty. | EligibilityCode | NaN |
| QuotingInstitution | NaN | InformationPartyRole | Source of the quote, party that proposes a rate. | NaN | NaN |
| ReceiversCustodian | NaN | SecuritiesSettlementPartyRole | Party that acts on behalf of the buyer of securities when the buyer does not have a direct relationship with the receiving agent. | NaN | NaN |
| ReceiversIntermediary | NaN | SecuritiesSettlementPartyRole | Party that the receiver's custodian uses to effect the receipt of a security, when the receiver's custodian does not have a direct relationship with the receiver agent. | NaN | NaN |
| ReceivingDepositoryRole | NaN | ReceivingSettlementParty | Organisation holding securities to enable book entry transfer of securities. These organisations may also carry out centralised comparison and transaction processing such as clearing and settlement of securities. The physical securities may be immobilised by the depository, or securities may be dematerialised (so that they exist only as electronic records). Also responsible for compliance of the portfolio with legal ratios etc. The depository may delegate custody to another entity (custodian). | NaN | NaN |
| RecipientBank | NaN | CommercialTradePartyRole | Bank that will be paid under a payment obligation contracted between two financial institutions related to the financing of a commercial transaction. | NaN | NaN |
| RemarketingAgent | NaN | SecuritiesPartyRole | The party in charge of a remarketing event. | NaN | NaN |
| RightsHolder | NaN | MeetingPartyRole | Owner of voting rights. | NaN | NaN |
| CounterpartyRisk | NaN | NaN | Calculation of the exposure amount that one party has vis-a-vis one counterparty or a central system, based on its credit risk. | NaN | NaN |
| CounterpartyRisk | Party | NaN | Specifies which role played by a party was taken into consideration for the risk calculation, for instance clearing member role. | Role | CounterpartyRisk |
| CounterpartyRisk | ExposedAmount | NaN | The amount which needs to be covered for the counterparty risk. | ActiveCurrencyAndAmount | NaN |
| CounterpartyRisk | ExposureCalculation | NaN | Specifies the exposure for which the risk is calculated on a counterparty basis. | ExposureCalculation | CounterpartyRisk |
| CounterpartyRisk | SecureMarketValue | NaN | The market value of the financial instruments being used to secure the facility. | ActiveCurrencyAndAmount | NaN |
| CounterpartyRisk | LiquidResourceValue | NaN | Amount of liquid resources available to meet liquid requirements. | ActiveCurrencyAndAmount | NaN |
| SecurityCertificateIssuerRole | NaN | SecurityCertificatePartyRole | Party that issues security certificates. | NaN | NaN |
| SellerBank | NaN | TradePartyRole | Financial institution of the seller. | NaN | NaN |
| SponsoringFirm | NaN | SecuritiesOrderPartyRole | Member of an exchange that is sponsoring an entering entity to send orders to the exchange. The sponsoring member firm permits sponsorees to enter orders directly to the exchange via automated means. | NaN | NaN |
| StockExchange | NaN | TradePartyRole | Party that identifies the stock exchange. | NaN | NaN |
| StockExchange | Market | NaN | Market for which the stock exchange system operates. | TradingMarket | StockExchange |
| SystemAdministratorRole | NaN | SystemPartyRole | Party that administers a system. | NaN | NaN |
| TakerRole | NaN | CollateralPartyRole | Party which receives the collateral. A party can be both a taker and a giver in a collateral relationship. | NaN | NaN |
| TaxRecipient | NaN | TaxPartyRole | Party that receives the tax. The recipient of, and the party entitled to, the tax may be two different parties. | NaN | NaN |
| ThirdReimbursementAgent | NaN | CashSettlementInstructionPartyRole | Specifies the branch of the instructed agent where the amount of money will be made available when different from the instructed reimbursement agent. | NaN | NaN |
| TradeCertificatePartyRole | NaN | Role | Role played by a party in the context of issuing trade certificates. | NaN | NaN |
| TradeCertificatePartyRole | TradeCertificate | NaN | Specifies the trade certificate issued by a party. | TradeCertificate | TradeCertificatePartyRole |
| TradingBranch | NaN | TreasuryTradingParty | Specifies the branch of the trading party with which the deal was done. | NaN | NaN |
| TransferAgentRole | NaN | InvestmentFundPartyRole | Party appointed by a fund management company. It updates records of investor accounts to reflect the daily investor purchases, redemptions, switches, transfers, and re-registrations. It ensures the timely settlement of transactions, and may provide tax information to the investor and/or to its intermediaries. It may calculate, collect, and rebate commissions. It prepares and distributes confirmations reflecting transactions, resulting in unit or cash account movements to the investor or the investor's intermediary. It responds to inquiries concerning account status, and processes the income distribution. | NaN | NaN |
| TreasurySettlementSystem | NaN | System | Centralised system in which a central party settles treasury trades between members. | NaN | NaN |
| TreasurySettlementSystem | SystemRole | NaN | Specifies the role played by the treasury settlement system. | TreasurySettlementSystemRole | System |
| TreasurySettlementSystemRole | NaN | TreasurySettlementPartyRole | System involved in the settlement chain of one leg of a treasury trade. | NaN | NaN |
| TreasurySettlementSystemRole | System | NaN | Specifies the system which plays a role in the settlement of a treasury trade. | TreasurySettlementSystem | SystemRole |
| TripartyAgent | NaN | CollateralPartyRole | Agent which acts as an intermediary between two parties for the administration of tri-party collateral transactions. | NaN | NaN |
| UnderwriterRole | NaN | SecuritiesPartyRole | The party that forms, together with the lead underwriter, a syndicate of co-lead managers, co-managers and underwriters in order to raise money for a borrower via a new issue. | NaN | NaN |
| VotingPartyRole | NaN | MeetingPartyRole | Party that has indicated its voting decision on one agenda item or on the entirety of the agenda. | NaN | NaN |
| AcceptorRole | NaN | CardPaymentPartyRole | Entity accepting payment related cards. | NaN | NaN |
| AccountInformationRecipientRole | NaN | AccountPartyRole | Party that is entitled by the account owner to receive information about movements in the account. | NaN | NaN |
| AccountingAgent | NaN | SecuritiesTradePartyRole | Party in charge of the accounting tasks. | NaN | NaN |
| AuthorisedAccountModifier | NaN | AccountPartyRole | Authorised sender of a message related to the life cycle of an account. | NaN | NaN |
| BillTo | NaN | CommercialTradePartyRole | Party to be invoiced for the purchase. | NaN | NaN |
| BuyerBank | NaN | TradePartyRole | Financial institution of the buyer. | NaN | NaN |
| QuoteStatus | NaN | Status | Status of a quote and if required, the rejection reason. | NaN | NaN |
| QuoteStatus | Status | NaN | Identifies the status of a quote acknowledgement. | QuoteStatusCode | NaN |
| QuoteStatus | RejectionReason | NaN | Reason why the quote is rejected. | RejectionReasonV3Code | NaN |
| QuoteStatus | RelatedQuote | NaN | Quote for wich the status is provided. | Quote | Status |
| VoluntaryCorporateAction | NaN | CorporateActionEvent | Participation in the corporate action is voluntary. To take part in the event, the account owner must provide its instructions. | NaN | NaN |
| PowerOfAttorney | NaN | Mandate | Document that transfers specific rights from a party to another party. | NaN | NaN |
| PowerOfAttorney | AuthorisedParty | NaN | Party which is the holder of the power of attorney. | Party | PowerOfAttorney |
| PowerOfAttorney | PowerOfAttorneyRequirements | NaN | Describes the requirements relative to the power of attorney. | PowerOfAttorneyRequirements | PowerOfAttorney |
| PowerOfAttorney | AuthorisedAccount | NaN | Specifies the securities account on which the power of attorney applies. | SecuritiesAccount | RelatedPowerOfAttorney |
| VoteRegistrationDeadline | NaN | MeetingDeadline | Date/time by which the beneficial owner or agent must notify of their intention to participate in a meeting. | NaN | NaN |
| ProductDeliveryObligation | NaN | Obligation | Obligation for the seller to deliver goods or services to the buyer. | NaN | NaN |
| ProductDeliveryObligation | ProductDeliveryOffset | NaN | Fulfilment of a product delivery obligation through the delivery of goods and services. It is derived from the association between Obligation and Obligation fulfillment. | ProductDelivery | Obligation |
| ProductDeliveryObligation | CommercialTrade | NaN | Specifies the trade which originates the obligation to deliver a specific product. | CommercialTrade | ProductDeliveryObligation |
| AdditionalRightDeadline | NaN | MeetingDeadline | Date and time by which security holders can propose amendments or new resolutions. | NaN | NaN |
| VoteRevocabilityDeadline | NaN | MeetingDeadline | Specifies the different deadlines available for revoking a casted vote. | NaN | NaN |
| ProxyAppointmentDeadline | NaN | MeetingDeadline | Date by which the information on proxy assignment must be received. | NaN | NaN |
| ResolutionProposalDeadline | NaN | MeetingDeadline | Date and time by which security holders can propose amendments or new resolutions. | NaN | NaN |
| VoteDeadline | NaN | MeetingDeadline | Date and time by which the vote instructions should be submitted. | NaN | NaN |
| VoteWithPremiumDeadline | NaN | MeetingDeadline | Specifies the different deadlines available for submitting vote instructions to take advantage of the premium. | NaN | NaN |
| TransactionRisk | NaN | NaN | Calculation of the exposure amount that one party has vis-a-vis one counterparty or a central system, based on the transactions that are not yet settled. | NaN | NaN |
| TransactionRisk | Obligation | NaN | Specifies the obligations used to calculate the transaction risk. Specifies the quantity of securities and/or the cash amounts that have to be taken into account to calculate the exposure of one trading party versus one of its counterparties. | Obligation | TransactionRisk |
| TransactionRisk | ExposedAmount | NaN | The sum of the exposures of all transactions which are in favour of a Party. That is, all transactions which would have an amount payable by the counterparty if they were being terminated. | ActiveCurrencyAndAmount | NaN |
| TransactionRisk | ExposureCalculation | NaN | Specifies the exposure for which the risk is calculated on a transaction basis. | ExposureCalculation | TransactionRisk |
| CashLoanDeposit | NaN | Deposit | Agreement for a temporary transfer of cash from its owner (the lender) to a borrower who promises to return it according to the terms of the agreement, usually with interest for its use. | NaN | NaN |
| AccountLink | NaN | NaN | Defines the link between the accounts held with a market infrastructure. | NaN | NaN |
| AccountLink | CashAccount | NaN | Cash account linked to a securities account. | CashAccount | AccountLink |
| AccountLink | ValidityPeriod | NaN | Defines the period when the securities account is linked to the cash account. | DateTimePeriod | RelatedAccountLink |
| AccountLink | SecuritiesAccount | NaN | Securities account linked to a cash account. | SecuritiesAccount | AccountLink |
| AccountLink | MarketInfrastructure | NaN | Specifies the market infrastructure where the accounts are held. | MarketInfrastructure | AccountLink |
| AccountLink | CashSettlementIndicator | NaN | Specifies whether market infrastructure can use the link between the securities account and the market infrastructure dedicated cash account for the settlement of the cash leg of a settlement instruction. | YesNoIndicator | NaN |
| AccountLink | CollateralisationIndicator | NaN | Specifies whether market infrastructure can use the securities, earmarked as collateral and held on the securities account, for auto-collateralisation operations on the linked market infrastructure dedicated cash account. | YesNoIndicator | NaN |
| AccountLink | DefaultIndicator | NaN | Specifies whether created account link is set as default for settlement. | YesNoIndicator | NaN |
| Netting | NaN | ObligationFulfilment | Offset of payables against receivables to reduce credit exposure to a counterparty. | NaN | NaN |
| Netting | AverageDealPrice | NaN | Average price of the netted trades. | Price | Netting |
| Netting | RelatedSecuritiesClearingProcess | NaN | Clearing process which includes the netting. | SecuritiesClearing | Netting |
| Netting | NetPositionAmount | NaN | Calculated position. | ActiveCurrencyAndAmount | NaN |
| Netting | AmountDirection | NaN | Specifies whether the amount is a debit or a credit. | DebitCreditCode | NaN |
| Netting | NetQuantity | NaN | Calculated net quantity of securities. | SecuritiesQuantity | Netting |
| Netting | PositionAmount | NaN | Intra-position amount. | CurrencyAndAmount | NaN |
| Rollover | NaN | ObligationFulfilment | Process whereby a financial instrument is reinvested at maturity. | NaN | NaN |
| Rollover | SecuritiesSettlement | NaN | Trade settlement process which is the source of the rollover. | SecuritiesSettlement | Rollover |
| SecuritiesClearing | NaN | Clearing | Process of settling securities through a central system. | NaN | NaN |
| SecuritiesClearing | SecuritiesSettlement | NaN | Settlement process performed as part of the securities clearing. | SecuritiesSettlement | SecuritiesClearing |
| SecuritiesClearing | BuyIn | NaN | Buy-in process performed as part of the securities clearing. | BuyIn | RelatedSecuritiesClearingProcess |
| SecuritiesClearing | Novation | NaN | Novation process performed as part of the securities clearing. | Novation | SecuritiesClearing |
| SecuritiesClearing | Netting | NaN | Netting process performed as part of the securities clearing. | Netting | RelatedSecuritiesClearingProcess |
| Novation | NaN | ObligationFulfilment | Act of either replacing an obligation to perform with a new obligation, or replacing a party to an agreement with a new party. | NaN | NaN |
| Novation | SecuritiesClearing | NaN | Clearing process to which the novation is related. | SecuritiesClearing | Novation |
| Novation | NovationStatus | NaN | Provides the novation status for the transaction. | NovationStatusCode | NaN |
| MandatoryCorporateAction | NaN | CorporateActionEvent | Corporate action that will result in only one possibility for account holders. The shareholder is just a passive beneficiary of these actions. | NaN | NaN |
| Carrier | NaN | TransportPartyRole | Identifies the party that is responsible for the conveyance of the goods from one place to another. | NaN | NaN |
| Manufacturer | NaN | GoodsPartyRole | Manufacturer of the goods. | NaN | NaN |
| DuplicateCase | NaN | InvestigationResolution | Outcome that results in closing a case as duplicate because the same issue has been reported by another party. | NaN | NaN |
| DuplicateCase | DuplicatedCase | NaN | Identifies the original case. | InvestigationCase | DuplicateCaseResolution |
| DuplicateCase | RelatedCaseResolution | NaN | Investigation case information which is duplicate. | PaymentInvestigationCaseResolution | DuplicateCase |
| BulkPayment | NaN | Payment | Payment which contains a series of other payments which have been grouped under specific criteria. A bulk payment can only contain individual payments of the same type (credit transfer or direct debit). | NaN | NaN |
| BulkPayment | Groups | NaN | Indicates that a bulk payment groups several individual payments of the same type (credit transfer or direct debit). | IndividualPayment | BulkPayment |
| CashDelivery | NaN | CreditInstrument | Amount of money representing a value paid by an agent bank to a creditor. | NaN | NaN |
| CashDelivery | CashAmount | NaN | Amount of money to be physically delivered. | ActiveCurrencyAndAmount | NaN |
| CashDelivery | RelatedBankingTransaction | NaN | Describes the type of transaction associated with a cash delivery. | BankingTransaction | CashDelivery |
| ComponentSecurity | NaN | NaN | Security which forms a component of another security, for example, underlying. | NaN | NaN |
| ComponentSecurity | SeparationPeriod | NaN | Period during which the related security can (optional) or must (mandatory) be separated. | DateTimePeriod | ComponentSecurity |
| ComponentSecurity | Security | NaN | Security for which a component security is specified. | Security | ComponentSecurity |
| ComponentSecurity | SeparationChoice | NaN | Defines if the separation of the security is optional or mandatory. | ChoiceCode | NaN |
| ComponentSecurity | QuantityNumerator | NaN | Number of related securities for the exercise. | BaseOneRate | NaN |
| ComponentSecurity | QuantityDenominator | NaN | Number of held securities for the exercise. | BaseOneRate | NaN |
| ComponentSecurity | SeparationDate | NaN | Date/time at which the related security can (optional) or must (mandatory) be separated. | ISODateTime | NaN |
| FinancialInstrumentSwap | NaN | NaN | Characteristics and conditions by which a borrower can exchange one type of financial instrument for another. | NaN | NaN |
| FinancialInstrumentSwap | Maturity | NaN | Range of time during which a swap is in effect. | DateTimePeriod | FinancialInstrumentSwap |
| FinancialInstrumentSwap | SpotSell | NaN | Details of the spot leg of the sell-side of a swap. | SecuritiesSwapLeg | SpotSellSwap |
| FinancialInstrumentSwap | SpotBuy | NaN | Details of the spot leg of the buy-side of a swap. | SecuritiesSwapLeg | SpotBuySwap |
| FinancialInstrumentSwap | ForwardBuyBack | NaN | Details of the forward leg of a swap that has been sold and is being returned, ie, bought back. | SecuritiesSwapLeg | ForwardBuyBackSwap |
| FinancialInstrumentSwap | ForwardSellBack | NaN | Details of the forward leg of a swap that has been bought and is being returned, ie, sold back. | SecuritiesSwapLeg | ForwardSellBackSwap |
| FinancialInstrumentSwap | RelatedQuote | NaN | Quote related to a swap. | Quote | QuoteSwap |
| FinancialInstrumentSwap | ForwardSellBackFrequency | NaN | Frequency at which the sold financial instrument is being returned. | FrequencyCode | NaN |
| FinancialInstrumentSwap | ForwardBuyBackFrequency | NaN | Frequency at which the bought financial instrument is being returned. | FrequencyCode | NaN |
| FinancialInstrumentSwap | InterestComputation | NaN | Method used to compute the accrued interest of a financial instrument. | InterestComputationMethodCode | NaN |
| BuyOrSellIndicationOfInterest | NaN | NaN | Intention to buy or sell a financial Instrument. | NaN | NaN |
| BuyOrSellIndicationOfInterest | NegotiationDetails | NaN | Negotiation details associated with an indication of interest. | Negotiation | IndicationOfInterest |
| BuyOrSellIndicationOfInterest | Organisations | NaN | Organisations to be included from the targeted list of firms, managed by the vendor, receiving indications. | Organisation | RelatedIndicationOfInterest |
| BuyOrSellIndicationOfInterest | RelativeSize | NaN | Indicates a quantity in relative size. | RelativeSizeCode | NaN |
| BuyOrSellIndicationOfInterest | Price | NaN | Indicates the price of the instrument, applicable to the indication of interest. | NaN | NaN |
| BuyOrSellIndicationOfInterest | QualityIndication | NaN | Indicates the relative quality of the indication of interest. | QualityIndicationCode | NaN |
| BuyOrSellIndicationOfInterest | NaturalIndicator | NaN | Indicates whether or not the indication of interest is the result of an existing agency order or a facilitation position resulting from an agency order, not from principal trading or order solicitation activity. | TrueFalseIndicator | NaN |
| BuyOrSellIndicationOfInterest | Qualifier | NaN | Qualifies the use of the indication of interest. | QualifierCode | NaN |
| BuyOrSellIndicationOfInterest | NumberOfLegs | NaN | In case of multilegs indication of interest, indicates number of instrumentLeg repeating group . | Number | NaN |
| BuyOrSellIndicationOfInterest | SpreadToBenchmark | NaN | Indicates the spread to benchmark details of an indication of interest. | Spread | RelatedIndicationOfInterest |
| BuyOrSellIndicationOfInterest | SwapSpread | NaN | Indicates the swap spread details of an indication of interest. | Spread | IndicationOfInterest |
| BuyOrSellIndicationOfInterest | TwoLegTransaction | NaN | Securities Financing is the process of lending or borrowing cash or securities against securities or cash collateral. It aims at optimising liquidity, support a trading strategy, or increase settlement efficiency. | SecuritiesFinancing | RelatedIndicationOfInterest |
| BuyOrSellIndicationOfInterest | RoutingType | NaN | Indicates if the type of routing is allowed or blocked. | RoutingTypeCode | NaN |
| BuyOrSellIndicationOfInterest | OrganisationListName | NaN | Name of the organisation list. | Max35Text | NaN |
| OrganisationStrategy | NaN | PortfolioStrategy | Strategy is organisation based. | NaN | NaN |
| OrganisationStrategy | Organisation | NaN | Strategy is organisation based. | Organisation | Strategy |
| SecuritiesPegOrderInstruction | NaN | NaN | Instructions specific to pegged orders, which consist in an investor buying large amounts of the underlying asset of a derivative it holds. | NaN | NaN |
| SecuritiesPegOrderInstruction | Offset | NaN | Amount (signed) added to the peg for a pegged order. | CurrencyAndAmount | NaN |
| SecuritiesPegOrderInstruction | PriceType | NaN | Defines the type of peg. | PegTypeCode | NaN |
| SecuritiesPegOrderInstruction | MoveType | NaN | Describes whether peg is static/fixed or floats. | MoveTypeCode | NaN |
| SecuritiesPegOrderInstruction | OffsetType | NaN | Type of peg offset. | OffsetTypeCode | NaN |
| SecuritiesPegOrderInstruction | LimitType | NaN | Specifies nature of resulting pegged price. | Max35Text | NaN |
| SecuritiesPegOrderInstruction | Scope | NaN | The scope of "related to" price of the peg (for example, local, global etc). | PriceProtectionScopeCode | NaN |
| SecuritiesPegOrderInstruction | OffsetSign | NaN | Indicates whether the offset should be added to or subtracted from the peg for a pegged order. | PlusOrMinusIndicator | NaN |
| SecuritiesPegOrderInstruction | Order | NaN | Order which is pegged. | SecuritiesOrderParameters | PegInstructions |
| SecuritiesPegOrderInstruction | RoundDirection | NaN | If the calculated peg price is not a valid tick price, specifies how to round the price. | RoundingParameters | RelatedPegOrderInstruction |
| SecuritiesRegulatoryDetails | NaN | NaN | Information related to order and required for regulatory purposes. | NaN | NaN |
| SecuritiesRegulatoryDetails | OrderRestrictions | NaN | Classification and restrictions linked to an order (for regulatory purpose). | OrderClassificationCode | NaN |
| SecuritiesRegulatoryDetails | BrokerSolicitedTrade | NaN | Indicates whether the trading party has suggested to his client to buy/sell a financial instrument or whether the investor acts on its own without advice from its trading party. | YesNoIndicator | NaN |
| SecuritiesRegulatoryDetails | RelatedOrder | NaN | Order for which legal parameters are provided. | SecuritiesOrder | LegalParameters |
| AnalyticsCalculation | NaN | NaN | Characteristics related to the analytics. | NaN | NaN |
| AnalyticsCalculation | SecuritiesPricing | NaN | Pricing for which an analytics calculation is specified. | SecuritiesPricing | AnalyticsCalculation |
| AnalyticsCalculation | Value | NaN | Result of the defined analytics calculation. | AnalyticsValue | AnalyticsCalculation |
| AnalyticsCalculation | CalculationType | NaN | Specifies the type of calculation. | CalculationTypeCode | NaN |
| AnalyticsCalculation | ValueDate | NaN | Date/time on which the calculation is based. For example: valuation on October 1 (price date) based on price of September 19 ( value date). | ISODateTime | NaN |
| AnalyticsCalculation | ValuePeriod | NaN | Period on which the calculation is based. | NaN | NaN |
| AnalyticsCalculation | EstimatedInterestRate | NaN | Estimated per annum ratio of interest paid to the principal amount of the financial instrument for a specific period of time. | PercentageRate | NaN |
| AnalyticsCalculation | VariableRateValueDate | NaN | Date/time as of which the variable rate is valid. | ISODateTime | NaN |
| DurationCalculation | NaN | NaN | Calculation of the price sensitivity of a fixed-income security to a change in interest rates. | NaN | NaN |
| DurationCalculation | RelatedSecuritiesPricing | NaN | Securities pricing for which a duration calculation is specified. | SecuritiesPricing | DurationCalculation |
| DurationCalculation | VariableInterest | NaN | Variable interest used for the calculation. | VariableInterest | DurationCalculation |
| DurationCalculation | Years | NaN | Result of the duration calculation measured in number of years. | Number | NaN |
| DurationCalculation | CalculationType | NaN | Specifies the type of calculation. | CalculationTypeCode | NaN |
| DurationCalculation | ValueDate | NaN | Date/time on which the calculation is based, eg, valuation on October 1 (price date) based on price of September 19 ( value date). | ISODateTime | NaN |
| DurationCalculation | ValuePeriod | NaN | Period on which the calculation is based. | NaN | NaN |
| LifeCalculation | NaN | NaN | Estimate of the number of terms to maturity, taking the possibility of early payments into account. | NaN | NaN |
| LifeCalculation | SecuritiesPricing | NaN | Securities pricing for which a life calculation is specified. | SecuritiesPricing | LifeCalculation |
| LifeCalculation | VariableInterest | NaN | Variable interest used for the calculation. | VariableInterest | LifeCalculation |
| LifeCalculation | Years | NaN | Result of the life calculation measured in number of years. | Number | NaN |
| LifeCalculation | CalculationType | NaN | Specifies the type of calculation. | CalculationTypeCode | NaN |
| LifeCalculation | ValueDate | NaN | Date/time on which the calculation is based, for example, valuation on October 1 (price date) based on price of September 19 ( value date). | ISODateTime | NaN |
| LifeCalculation | ValuePeriod | NaN | Period on which the calculation is based. | NaN | NaN |
| Entitlement | NaN | Security | Financial instrument providing the holder the privilege to subscribe to or to receive specific assets on terms specified. | NaN | NaN |
| Entitlement | StrikePrice | NaN | Predetermined price at which the holder buys or sells the underlying assets. | SecuritiesPricing | Entitlement |
| Entitlement | CoveredIndicator | NaN | Indicates whether the underlying security is owned by the writer of the entitlement. | YesNoIndicator | NaN |
| Entitlement | OptionStyle | NaN | Specifies how an option can be exercised. | OptionStyleCode | NaN |
| Entitlement | OptionType | NaN | Specifies whether it is a call option (right to purchase a specific underlying asset) or a put option (right to sell a specific underlying asset). | OptionTypeCode | NaN |
| Entitlement | CappedValue | NaN | Limit on the pay-out on the expiration of the entitlement. The positive difference between the cap value and the strike price is the maximum amount that would be paid off at expiration. | CurrencyAndAmount | NaN |
| Entitlement | CappedIndicator | NaN | Indicates whether an entitlement is capped. | YesNoIndicator | NaN |
| Discretion | NaN | NaN | Indicates on an order that the trader wishes to display one price in the market but will accept trades at another price. | NaN | NaN |
| Discretion | RelatedOrderExecution | NaN | Order instruction for which a discretion is specified. | SecuritiesOrderExecutionInstruction | OrderPriceStrategy |
| Discretion | Offset | NaN | Amount added to the 'related to' price. | CurrencyAndAmount | NaN |
| Discretion | OffsetSign | NaN | Indicates whether the offset should be added or subtracted from the related price. | PlusOrMinusIndicator | NaN |
| Discretion | RelatedPriceType | NaN | Identify the type of price an offset is related to. The offset can either be added or subtracted. | TypeOfDiscretionPriceCode | NaN |
| Discretion | MoveType | NaN | Describes whether discretion price is static/fixed or floats. | MoveTypeCode | NaN |
| Discretion | LimitType | NaN | Specifies the nature of the resulting discretion price (e.g. or better limit, strict limit etc). | Max35Text | NaN |
| Discretion | RoundDirection | NaN | If the calculated discretion price is not a valid tick price, specifies how to round the price (e.g. to be more or less aggressive) | Max35Text | NaN |
| Discretion | Scope | NaN | The scope of "related to" price of the discretion (e.g. local, global etc) | PriceProtectionScopeCode | NaN |
| Discretion | OffsetType | NaN | Describes the type of Discretion Offset . | OffsetTypeCode | NaN |
| DisclosedListTrading | NaN | ListTrading | List trading by which the buy-side details the exact stocks and sizes to be traded and the sell-side offers the buy-side a two-way price, to buy or to sell the indicated stocks. All sell-side firms see all of the stocks and quantities in the portfolio during the bidding phase regardless of whether or not they win the business. | NaN | NaN |
| DisclosedListTrading | DisclosedListTradingAccount | NaN | Securities account used for the trade of a disclosed list of securities, eg, in basket or program trading. | SecuritiesAccount | DisclosedListTrading |
| DisclosedListTrading | BuyAmount | NaN | Total trade value for which a party is willing to purchase financial instruments. | CurrencyAndAmount | NaN |
| DisclosedListTrading | SellAmount | NaN | Total trade value for which a party is willing to sell financial instruments. | CurrencyAndAmount | NaN |
| DisclosedListTrading | RequestedSettlementDateCode | NaN | Requested date of trade settlement in coded form (eg, trade date +1). | SettlementDateCode | NaN |
| SecuritiesQuoteVariable | NaN | NaN | Proposition of price for a financial instrument. | NaN | NaN |
| SecuritiesQuoteVariable | Qualifier | NaN | Qualifies the use of the quote. | QualifierCode | NaN |
| SecuritiesQuoteVariable | Type | NaN | Indicates the scenario in which the quote is (requested to be) used (ie, indicative, firm, restricted tradeable or counter). | QuoteTypeCode | NaN |
| SecuritiesQuoteVariable | QuoteTradingSession | NaN | Details of a specific trading session associated with a quote. | TradingSession | Quote |
| SecuritiesQuoteVariable | LegSwapType | NaN | Indicates that the sell-side is requested to calculate the quantity based on the opposite leg and is used instead of giving a quantity. | LegSwapTypeCode | NaN |
| SecuritiesQuoteVariable | PriceType | NaN | Initiator can specify the price type the quote needs to be quoted at. If not specified, the respondent has option to specify how quote is quoted. | PriceValueTypeCode | NaN |
| SecuritiesQuoteVariable | MidSide | NaN | Indicates that the quote details are indicated as a mid of a security, commodity, currency (an average of the offer and the bid). | Quote | MidSideQuoteVariable |
| SecuritiesQuoteVariable | BidSide | NaN | Indicates that the quote details are indicated as a bid of a security, commodity, currency. | Quote | BidSideQuoteVariable |
| SecuritiesQuoteVariable | OfferSide | NaN | Indicates that the quote details are indicated as an offer of a security, commodity, currency. | Quote | OfferSideQuoteVariable |
| SecuritiesQuoteVariable | RelatedQuote | NaN | Quote parameters related to a security quote. | Quote | SecurityQuoteVariable |
| SecuritiesQuoteVariable | SecuritiesOrder | NaN | Preliminary information on conditions of the order, specified in the quote (request). | SecuritiesOrder | Quote |
| SecuritiesQuoteVariable | Commission | NaN | Commission associated with a quote. | Commission | RelatedQuote |
| ExchangeForPhysicalTrade | NaN | NaN | Technique whereby a position in the underlying is traded for a futures position in the physical commodity markets. | NaN | NaN |
| ExchangeForPhysicalTrade | OutsideIndex | NaN | Unexpected divergence between the price behaviour of an underlying position or portfolio and the price behaviour of a hedging position or benchmark. | PercentageRate | NaN |
| ExchangeForPhysicalTrade | FairValue | NaN | Difference between the value of a future and the value of the underlying equities after allowing for the discounted cash flows associated with the underlying stocks. | CurrencyAndAmount | NaN |
| ExchangeForPhysicalTrade | ValueForFutures | NaN | Value of a futures position involved in an Exchange For Physical trade. | CurrencyAndAmount | NaN |
| ExchangeForPhysicalTrade | OutMainCountryIndex | NaN | Accepted value of stocks composing an index located outside its country of origin. | CurrencyAndAmount | NaN |
| ExchangeForPhysicalTrade | SecuritiesOrder | NaN | Order for which parameters for exchange for physical trading are specified. | SecuritiesOrder | ExchangeForPhysicalTrade |
| OrderBook | NaN | NaN | Record of orders to buy and sell a financial instrument. | NaN | NaN |
| OrderBook | Order | NaN | Instruction to a broker or dealer to buy or sell a specific security. | SecuritiesOrder | RelatedOrderBook |
| OrderBook | PriceTimePriority | NaN | Priority given to an order based on its price and/or time specification. | Max16Text | NaN |
| CrossTrade | NaN | SecuritiesOrder | Transaction where either the buy-broker and the sell-broker are the same, or the buy-broker and the sell-broker belong to the same firm. | NaN | NaN |
| CrossTrade | BuySideOrder | NaN | Buyside order details. | SecuritiesOrder | BuySideRelatedCrossTrade |
| CrossTrade | SellSideOrder | NaN | Sell side order details. | SecuritiesOrder | SellSideRelatedCrossTrade |
| CrossTrade | ExecutionType | NaN | Identifies the type of execution of a cross trade. | CrossTradeExecutionCode | NaN |
| CrossTrade | CrossType | NaN | Type of cross being submitted to a market. | CrossTypeCode | NaN |
| CrossTrade | Prioritisation | NaN | Indicates whether one side or the other of a cross order should be prioritized. The definition of prioritization depends on the market. In some markets prioritization means which side of the cross order is applied to the market first. In other markets, prioritization may mean that the prioritized side is fully executed (sometimes referred to as the side being protected). | PrioritisationCode | NaN |
| SecuritiesSwapLeg | NaN | NaN | Contains the details of one of the legs of a swap, both in time (spot versus [partial] forward details) and the side (sell versus buy). | NaN | NaN |
| SecuritiesSwapLeg | Amount | NaN | Contains the currency and amount of a buy or sell leg of a swap for the spot or the forward. | CurrencyAndAmount | NaN |
| SecuritiesSwapLeg | Benchmark | NaN | Contains the benchmark used for a buy or sell leg of a swap for the spot or the forward. | BenchmarkCurveNameCode | NaN |
| SecuritiesSwapLeg | CurvePoint | NaN | Identifies a point on a benchmark curve. | Max256Text | NaN |
| SecuritiesSwapLeg | BenchmarkYield | NaN | Contains the yield against a benchmark for a buy or sell leg of a swap for the spot or the forward. | PercentageRate | NaN |
| SecuritiesSwapLeg | BenchmarkOffset | NaN | Contains the offset in basis points against a benchmark for a buy or sell leg of a swap for the spot or the forward. | BaseOneRate | NaN |
| SecuritiesSwapLeg | SpotSellSwap | NaN | Swap for which a spot sell leg is specified. | FinancialInstrumentSwap | SpotSell |
| SecuritiesSwapLeg | SpotBuySwap | NaN | Swap for which a spot buy leg is specified. | FinancialInstrumentSwap | SpotBuy |
| SecuritiesSwapLeg | ForwardBuyBackSwap | NaN | Swap for which a forward buy back leg is specified. | FinancialInstrumentSwap | ForwardBuyBack |
| SecuritiesSwapLeg | ForwardSellBackSwap | NaN | Swap for which a forward sell back leg is specified. | FinancialInstrumentSwap | ForwardSellBack |
| NonDisclosedListTrading | NaN | ListTrading | List trading by which the buy-side provides details to the sell-side information about the sector, country, index and potential market impact of the financial instrument to be bought or sold. Using this information, the sell-side firms bid for the trade. | NaN | NaN |
| NonDisclosedListTrading | BidByCurrency | NaN | Identifies a type of bid based on a common characteristic (the currency) of all securities of a list. | CountryCode | NaN |
| NonDisclosedListTrading | BidBySector | NaN | Identifies a type of bid based on a common characteristic (the sector) of all securities of a list. | Max140Text | NaN |
| NonDisclosedListTrading | BidByIndex | NaN | Identifies a type of bid based on a common characteristic (the index) of all securities of a list. | Max140Text | NaN |
| NonDisclosedListTrading | NumberOfBidders | NaN | Indicates the total number of bidders participating to a list trade. | Number | NaN |
| NonDisclosedListTrading | SideValue | NaN | Indicates the monetary value in either direction (buy or sell) without revealing whether it is the intention to buy or sell. | CurrencyAndAmount | NaN |
| Curve | NaN | NaN | Describes a benchmark curve. | NaN | NaN |
| Curve | Currency | NaN | Identifies the currency used for the benchmark curve. | CurrencyCode | NaN |
| Curve | Name | NaN | Identifies the name of the benchmark curve. | BenchmarkCurveNameCode | NaN |
| Curve | Point | NaN | Identifies a point on a benchmark curve. The point can be stated via a combination of maturity month/year and coupon. | Max256Text | NaN |
| Curve | Spread | NaN | Spread for which a benchmark curve is specified. | Spread | BenchmarkCurve |
| AnalyticsValue | NaN | NaN | Value given to a price analytic. | NaN | NaN |
| AnalyticsValue | Amount | NaN | Analytics expressed as a currency and value. | CurrencyAndAmount | NaN |
| AnalyticsValue | Rate | NaN | Analytics expressed as a rate. | PercentageRate | NaN |
| AnalyticsValue | NumberOfYears | NaN | Analytics expressed as a number of years. | Number | NaN |
| AnalyticsValue | AnalyticsCalculation | NaN | Analytics calculation for which an analytics value is specified. | AnalyticsCalculation | Value |
| PaymentSchedule | NaN | NaN | Schedule for partial payments of an issue. | NaN | NaN |
| PaymentSchedule | Date | NaN | Date/time at which the partial payment is to be done. | ISODateTime | NaN |
| PaymentSchedule | Amount | NaN | Amount of the partial payment. | CurrencyAndAmount | NaN |
| PaymentSchedule | Rate | NaN | Partial payment expressed as a rate. | PercentageRate | NaN |
| PortfolioStrategyDefinition | NaN | NaN | Additional information on the definition of the strategy. | NaN | NaN |
| PortfolioStrategyDefinition | Strategy | NaN | Stategy attached to the portfolio. | PortfolioStrategy | Definition |
| PortfolioStrategyDefinition | Name | NaN | Name of the defined strategy. | Max350Text | NaN |
| PortfolioStrategyDefinition | Description | NaN | Free text description of the strategy definition. | Max350Text | NaN |
| PortfolioStrategyDefinition | EffectivePeriod | NaN | Period during which the defined strategy is valid. | NaN | NaN |
| SectorStrategy | NaN | PortfolioStrategy | Strategy is sector based. | NaN | NaN |
| SectorStrategy | Sector | NaN | Sector of business of the organisation, for example, pharmaceutical. | Sector | Strategy |
| CurrencyStrategy | NaN | PortfolioStrategy | Strategy is currency based. | NaN | NaN |
| CurrencyStrategy | Currency | NaN | Currency of the investment. | CurrencyCode | NaN |
| AssetClassStrategy | NaN | PortfolioStrategy | Strategy is asset class based. | NaN | NaN |
| AssetClassStrategy | AssetClass | NaN | Strategy based on asset classes. | AssetClassification | Strategy |
| MarketInfrastructure | NaN | Role | Multilateral system among participating institutions, including the operator of the system, used for the purposes of clearing, settling, or recording payments, securities, derivatives or other financial transactions. | NaN | NaN |
| MarketInfrastructure | AccountLink | NaN | Defines the link between the accounts held with a market infrastructure. | AccountLink | MarketInfrastructure |
| CarrierAgent | NaN | TransportPartyRole | Carrier's agent (for example, shipping company) that acts on behalf of the carrier and may be the issuer of transport documents. | NaN | NaN |
| CreditNote | NaN | FinancialDocument | Monetary instrument issued by a seller that allows a buyer to purchase an item or service from that seller on a future date. | NaN | NaN |
| PersonProfile | NaN | NaN | Information to support Know Your Customer (KYC) processes. | NaN | NaN |
| PersonProfile | ForeignStatusCertification | NaN | Specifies if documentary evidence has been provided for the foreign resident. | ProvidedCode | NaN |
| PersonProfile | EmployeeTerminationIndicator | NaN | Indicates if the employment of the person has been terminated. | YesNoIndicator | NaN |
| PersonProfile | KnowYourCustomerCheckType | NaN | Specifies the type of due diligence checks carried out on a party. For definitions of ordinary, simple and enhanced know your customer checks, local market regulations should be consulted. | KnowYourCustomerCheckTypeCode | NaN |
| PersonProfile | RiskLevel | NaN | Specifies the customerâ€™s money laundering risk. | RiskLevelCode | NaN |
| PersonProfile | Person | NaN | Person for which the profile parameters are described. | Person | PersonProfile |
| PersonProfile | PoliticalExposureType | NaN | Specifies if due diligence checks on the political exposure of the investor have been carried out and whether these checks are national or foreign. (A politically exposed person is someone who has been entrusted with a prominent public function, or an individual who is closely related to such a person.) | PoliticalExposureTypeCode | NaN |
| PersonProfile | CustomerConductClassification | NaN | Assessment of the customerâ€™s behaviour at the time of the account opening application. | ConductClassificationCode | NaN |
| PersonProfile | FamilyMedicalInsuranceIndicator | NaN | Indicates if the person has family medical insurance coverage available. | YesNoIndicator | NaN |
| PersonProfile | ProfileCertification | NaN | Information to support the Know Your Customer processes. | PrivateCertificate | Person |
| PersonProfile | SourceOfWealth | NaN | Indicates the main sources of the money. | Max140Text | NaN |
| PersonProfile | SalaryRange | NaN | Specifies the level of salary. | Max35Text | NaN |
| PersonProfile | PoliticallyExposedStatus | NaN | Status of the politically exposed person. | PoliticallyExposedPersonStatusCode | NaN |
| InvoiceStatus | NaN | Status | Status of the invoice or of the billing process. | NaN | NaN |
| InvoiceStatus | Invoice | NaN | Invoice for which a status is provided. | Invoice | InvoiceStatus |
| Reinvestment | NaN | NaN | Parameters of the reinvestment of the income on the fund. | NaN | NaN |
| Reinvestment | RelatedinvestmentAccountService | NaN | Investment account services which include reinvestment information. | InvestmentAccountService | Reinvestment |
| Reinvestment | InvestmentFundClass | NaN | Investment fund class which is the fund in which the income must be reinvested. | InvestmentFundClass | Reinvestment |
| Reinvestment | Percentage | NaN | Percentage on the income on the fund to be reinvested. | PercentageRate | NaN |
| DeliveryNote | NaN | Document | Document which is a proof of delivery of the product. | NaN | NaN |
| AmountAndPeriod | NaN | NaN | Relates an amount to a period of time. | NaN | NaN |
| AmountAndPeriod | Period | NaN | Period related to an amount. | DateTimePeriod | Amount |
| AmountAndPeriod | Amount | NaN | Amount of this period. | CurrencyAndAmount | NaN |
| NotificationReceiver | NaN | DocumentPartyRole | Identifies the party (to be) notified of the content of a document. | NaN | NaN |
| Market | NaN | NaN | Context or geographic environment in which trading parties execute trades. | NaN | NaN |
| Market | Trade | NaN | Trade executed in a market. | Trade | Market |
| Market | Jurisdiction | NaN | Jurisdiction of the governing law for the trades on this market, for example, City of NY, County of NY, State of NY, regulatory SEC. | Jurisdiction | RelatedMarket |
| Market | Country | NaN | Country in which a market operates. | Country | Market |
| Market | GeographicalEnvironment | NaN | Geographic zone in which the cash transfer is executed, from the perspective of the forwarding or first agent, eg, domestic or international. | GeographicalEnvironmentCode | NaN |
| Market | Identification | NaN | Identifies the market by name, id and/or code. | PartyIdentificationInformation | IdentifiedMarket |
| Assessment | NaN | Document | Assessment for the components of a system. | NaN | NaN |
| Assessment | AssessmentType | NaN | Type of assessment. | POIComponentAssessmentCode | NaN |
| Assessment | System | NaN | System for which an assessment is produced. | System | Assessment |
| Assessment | ExpiryDate | NaN | Date when the assessment expires. | ISODateTime | NaN |
| Assessment | DeliveryDate | NaN | Date when the assessment document was delivered. | ISODateTime | NaN |
| Evidence | NaN | NaN | Element such as signature that can be used to prove a fact. | NaN | NaN |
| Evidence | RelatedDocument | NaN | Document which is used as a proof of evidence. | Document | Evidence |
| NotifyingParty | NaN | DocumentPartyRole | Identifies the party that notifies the content of a document to a third party. | NaN | NaN |
| GuaranteePartyRole | NaN | Role | Role played by a party in the context of guarantees. | NaN | NaN |
| GuaranteePartyRole | Guarantee | NaN | Guarantee for which a party plays a role. | Guarantee | GuaranteePartyRole |
| Order | NaN | NaN | Order placed by an investor to buy or sell an asset at a price specified or not. | NaN | NaN |
| Order | Trade | NaN | Agreement between two parties to buy and sell assets. | Trade | Order |
| Order | MasterIdentification | NaN | Unique and unambiguous identifier for a group of individual orders, as assigned by the instructing party. This identifier links the individual orders together. | Max35Text | NaN |
| BankingTransaction | NaN | NaN | Transaction executed by the client of a financial institution from/to the account serviced by the financial institution, such as mortgage payment. | NaN | NaN |
| BankingTransaction | PaymentObligation | NaN | Payment obligation resulting from a banking transaction. | PaymentObligation | BankingTransaction |
| BankingTransaction | FinancialTransaction | NaN | Financial transaction to which the banking transaction is associated. | FinancialTransaction | BankingTransaction |
| BankingTransaction | CashDelivery | NaN | Specifies the cash which is delivered by a financial institution. | CashDelivery | RelatedBankingTransaction |
| BankingTransaction | CashDeposit | NaN | Specifies the cash which is received by a financial institution. | CashDeposit | RelatedBankingTransaction |
| SecuritiesTransaction | NaN | SecuritiesTrade | Exchange of securities. | NaN | NaN |
| SecuritiesTransaction | ReplacedAmount | NaN | Specifies the amount requested to be replaced or actually replaced. | CurrencyAndAmount | NaN |
| RepurchaseAgreement | NaN | SecuritiesFinancing | Sale of securities together with an agreement for the seller to buy back the securities at a later date. A repo is equivalent to a spot sale combined with a forward contract. For the seller of the security it is a repo; for the buyer of the security it is a reverse repurchase agreement. | NaN | NaN |
| RepurchaseAgreement | PaymentObligation | NaN | Obligation covered by a repurchase agreement. | PaymentObligation | RepurchaseAgreement |
| Assignment | NaN | NaN | Transfer by one party to a third party of its receivables. | NaN | NaN |
| Assignment | PaymentObligation | NaN | Payment obligations included in an assignment. | PaymentObligation | RelatedAssignment |
| Assignment | FinancingAgreement | NaN | Invoice financing agreement which creates a payment obligation. | InvoiceFinancingAgreement | Assignment |
| FinancialTransaction | NaN | NaN | Process which includes the order, the execution, the settlement of trades in the financial domain. | NaN | NaN |
| FinancialTransaction | CorporateActionDistribution | NaN | Distribution of the proceeds of a CA event. | CorporateActionDistribution | FinancialTransaction |
| FinancialTransaction | InterestManagement | NaN | Management of interest which consists into calculating the interest, requesting its payment or distributing the interest proceeds. | InterestManagement | FinancialTransaction |
| FinancialTransaction | Trade | NaN | Agreement between two parties to buy and sell assets. | Trade | FinancialTransaction |
| FinancialTransaction | CollateralMovement | NaN | Collateral in or out as a result of collateral management. | CollateralMovement | FinancialTransaction |
| FinancialTransaction | BankingTransaction | NaN | Transaction executed by the client of a financial institution from/to the account serviced by the financial institution, such as mortgage payment. | BankingTransaction | FinancialTransaction |
| FinancialTransaction | RegulatoryReport | NaN | Information related to a trade and that has to be reported to a regulatory authority. | RegulatoryReport | ReportedTransaction |
| OrganisationHierarchy | NaN | NaN | Description of the structure of a company. | NaN | NaN |
| OrganisationHierarchy | Organisation | NaN | Specifies the organisation which plays a specific role in the company structure. | Organisation | OrganisationHierarchy |
| FinancialDocument | NaN | Document | Type of document used in relation with financial transactions. | NaN | NaN |
| IndividualInvestor | NaN | InvestmentAccountPartyRole | Individual person which makes investment decisions in relation with its investment account. | NaN | NaN |
| LocalDepositoryRole | NaN | DepositoryRole | Place where securities are deposited, that is company, bank or institution that holds and facilitates the exchange of securities at a local/national level. | NaN | NaN |
| SystematicInternaliser | NaN | SecuritiesTradePartyRole | Firm which deals on its own account by executing client orders outside a regulated market or a multi-lateral trading facility, against its own books or against orders from other clients. | NaN | NaN |
| DepositoryRole | NaN | SecuritiesPartyRole | Place where securities are deposited, that is company, bank or institution that holds and facilitates the exchange of securities. | NaN | NaN |
| FinancialProduct | NaN | Product | Product offered by a financial institution to its customers. | NaN | NaN |
| CorporateActionDeadline | NaN | Deadline | Time constraints for processing corporate actions. | NaN | NaN |
| CorporateActionDeadline | RevocabilityPeriod | NaN | Period during which the shareholder can revoke, change or withdraw its instruction. | NaN | NaN |
| CorporateActionDeadline | ProtectDate | NaN | Last date a holder can request to defer delivery of securities pursuant to a notice of guaranteed delivery or other required documentation. | ISODateTime | NaN |
| CorporateActionDeadline | TradingSuspendedDate | NaN | Date on which trading of a security is suspended as the result of an event. | ISODateTime | NaN |
| CorporateActionDeadline | ThirdPartyDeadline | NaN | Date/Time by which the account owner must instruct directly another party, for example to provide documentation to an issuer agent. | ISODateTime | NaN |
| CorporateActionDeadline | CertificationDeadline | NaN | Deadline by which the beneficial ownership of securities must be declared. | ISODateTime | NaN |
| CorporateActionDeadline | DeadlineToSplit | NaN | Deadline by which instructions must be received to split securities, that is, of physical certificates. | ISODateTime | NaN |
| CorporateActionDeadline | SpecialExDate | NaN | Date/time as from which 'special processing' can start to be used by participants for that event. Special processing is a means of marking a transaction, that would normally be traded ex or cum, as being traded cum or ex respectively, for example, a transaction dealt 'special' after the ex date would result in the buyer being eligible for the entitlement. This is typically used in the UK and Irish markets. | ISODateTime | NaN |
| CorporateActionDeadline | DeadlineForTaxBreakdownInstruction | NaN | Date until which tax breakdown instructions will be accepted. | ISODateTime | NaN |
| CorporateActionDeadline | EarlyClosingDate | NaN | First possible early closing date of an offer if different from the expiry date. | ISODateTime | NaN |
| CorporateActionDeadline | RecordDate | NaN | Date at which the positions are struck to note which parties will receive the entitlement. | ISODateTime | NaN |
| CorporateActionDeadline | CoverExpirationDate | NaN | Last day a holder can deliver the securities that it had previously protected. | ISODateTime | NaN |
| CorporateActionDeadline | ElectionToCounterpartyDeadline | NaN | Deadline by which an entitled holder needs to advise their counterparty to a transaction of their election for a corporate action event. | ISODateTime | NaN |
| CorporateActionDeadline | ExpiryDate | NaN | Date on which the offer terminates. | ISODateTime | NaN |
| CorporateActionDeadline | EarlyThirdPartyDeadline | NaN | Date/Time set by the issuer agent as a first early deadline by which the account owner must instruct directly another party, possibly giving the holder eligibility to incentives. For example, to provide documentation to an issuer agent. | ISODateTime | NaN |
| CorporateActionDeadline | DepositoryCoverExpirationDate | NaN | The last date/tiime that a participant of the depository can deliver securities that it had elected on and/or previously protected. | ISODateTime | NaN |
| CorporateActionDeadline | ResponseDeadline | NaN | Date on which the account servicer has set as the deadline to respond, with instructions, to an outstanding event. This time is dependent on the reference time zone of the account servicer as specified in an SLA. | ISODateTime | NaN |
| CorporateActionDeadline | ConsentExpirationDate | NaN | Last date on which a holder can consent to the changes sought by the corporation. | ISODateTime | NaN |
| CorporateActionDeadline | RegistrationDeadline | NaN | Date on which instructions to register or registration details will be accepted. | ISODateTime | NaN |
| CorporateActionDeadline | StockLendingDeadline | NaN | Date or date and time that the account servicer has set as the deadline to respond with instructions to an event for which the underlying security is out on loan. | ISODateTime | NaN |
| CorporateActionDeadline | ConsentRecordDate | NaN | Date used by the offeror to determine the beneficiary eligible to participate in a consent based on the registered owner of the securities, eg, beneficial owner of consent record. The consent record date qualifier is used to indicate that a record date only applies to a certain part of the offer, not the entire offer. The consent record date is used to indicate that a record date only applies to a certain part of the offer, not the entire offer. | ISODateTime | NaN |
| CorporateActionDeadline | EarlyResponseDeadline | NaN | Date/time that the account servicer has set as the deadline to respond, with instructions, to an outstanding event, giving the holder eligibility to incentives. This time is dependent on the reference time zone of the account servicer as specified in an SLA. | ISODateTime | NaN |
| CorporateActionDeadline | GuaranteedParticipationDate | NaN | Last date/time by which a buying counterparty to a trade can be sure that it will have the right to participate in an event. | ISODateTime | NaN |
| PaymentTerms | NaN | NaN | Specifies the payment terms of the obligation. | NaN | NaN |
| PaymentTerms | Amount | NaN | Specifies that the payment terms apply to an amount. | CurrencyAndAmount | NaN |
| PaymentTerms | Percentage | NaN | Specifies that the payment conditions apply to a percentage of the amount due. | PercentageRate | NaN |
| PaymentTerms | PaymentPeriod | NaN | Period to which the payment terms apply. | DateTimePeriod | RelatedPaymentTerms |
| PaymentTerms | RelatedPaymentObligation | NaN | Payment obligation for which payment terms are specified. | PaymentObligation | PaymentTerms |
| PaymentTerms | PaymentTime | NaN | Specifies the time of the payment relative to an event such as product delivery or receipt of invoice. | PaymentTimeCode | NaN |
| PaymentTerms | RelatedPaymentScheduleType | NaN | Related type of the payment schedule provided in the contract. | RegisteredContract | PaymentScheduleType |
| PaymentTerms | RelatedLoan | NaN | Schedule for the payment of the interests due on the related loan. | Loan | InterestPaymentsSchedule |
| Tranche | NaN | NaN | One of a number of related assets offered as part of the same transaction. The detachment point less the attachment point represents the maximum loss. | NaN | NaN |
| Tranche | Asset | NaN | Specifies the asset for which tranche information is reported. | Asset | Tranche |
| Tranche | DetachmentPoint | NaN | Point beyond which losses do not affect the tranche. | BaseOneRate | NaN |
| Tranche | AttachmentPoint | NaN | The attachment point defines the amount of subordination a tranche enjoys. | BaseOneRate | NaN |
| AllocationPartyRole | NaN | TradePartyRole | Party which instructs the trade allocation to the executing party. | NaN | NaN |
| CorporateInvestor | NaN | InvestmentAccountPartyRole | Corporate that makes investment decisions in relation with its investment account. | NaN | NaN |
| Investor | NaN | InvestmentAccountPartyRole | Party which makes investment decisions in relation with its investment account. | NaN | NaN |
| Investor | NewIssuePermission | NaN | Indicates whether the investor permits its beneficial owners to participate in profits and losses attributed to new issue securities. | YesNoIndicator | NaN |
| Investor | DeMinimusApplicable | NaN | Determine if the investor is covered by the "de minimis" exemption. | Max35Text | NaN |
| Investor | Restricted | NaN | Indicates whether the investor is eligible to participate in the profits and losses from a new issue. | YesNoIndicator | NaN |
| Investor | RestrictedPersonReason | NaN | Reason for the restricted person. | Max350Text | NaN |
| PercentageAndPeriod | NaN | NaN | Relates a percentage to a period of time. | NaN | NaN |
| PercentageAndPeriod | Period | NaN | Period related to percentage. | DateTimePeriod | Percentage |
| PercentageAndPeriod | Percentage | NaN | Percentage rate. | PercentageRate | NaN |
| InterestManagement | NaN | NaN | Management of interest which consists into calculating the interest, requesting its payment or distributing the interest proceeds. | NaN | NaN |
| InterestManagement | InterestCalculation | NaN | Calculation parameters used to obtain the interest amount. | InterestCalculation | RelatedInterestManagement |
| InterestManagement | FinancialTransaction | NaN | Financial transaction to which the order belongs. | FinancialTransaction | InterestManagement |
| InterestManagement | Interest | NaN | Interest information used in the interest management process. | Interest | RelatedInterestManagement |
| InterestManagement | PaymentObligation | NaN | Payment information for the settlement of interest or payment obligation to which interest charges are attached. | PaymentObligation | Interest |
| SecuritiesOptionTrade | NaN | SecuritiesTrade | Process of buying or selling an option which has securities as underlying asset. | NaN | NaN |
| SecuritiesOptionTrade | Option | NaN | Specifies the different parameters of the option. | Option | SecuritiesOptionTrade |
| Position | NaN | NaN | Specifies the status of trades and their value inside a system. | NaN | NaN |
| Position | NetQuantity | NaN | Specifies the net quantity position of the trade legs of one member within the system. | SecuritiesQuantity | Position |
| Position | NetPositionAmount | NaN | Specifies the net position amount of the trade legs of one member within the system. | CurrencyAndAmount | NaN |
| Position | System | NaN | System for which trades position is specified. | System | TradesPosition |
| Position | Price | NaN | Price applied to the position. | SecuritiesPricing | RelatedPosition |
| Position | SecuritiesSettlement | NaN | Information related to the settlement of the position. | SecuritiesSettlement | Position |
| Position | InitialPositionAmount | NaN | Specifies the position at the beginning of a reporting period. | CurrencyAndAmount | NaN |
| Household | NaN | NaN | Specifies the members of a household in relation with the ownership of an account. | NaN | NaN |
| Household | Member | NaN | Identifies the member of a household. | Person | Household |
| ManagedAccountProduct | NaN | FinancialProduct | Product which provides guidance to investors to manage their portfolios. | NaN | NaN |
| ManagedAccountProduct | Account | NaN | Account which is the object of the managed account product. | Account | ManagedAccountProduct |
| ManagedAccountProduct | InvestmentAccountContract | NaN | Contract which manages the investment account that is related to the products offered. | InvestmentAccountContract | ModeledAccount |
| SystemReferenceDataResponsible | NaN | SystemPartyRole | Party responsible for the maintenance of other parties reference data. | NaN | NaN |
| FinancialService | NaN | Service | Services provided by a financial institution to its clients. | NaN | NaN |
| Pledgee | NaN | SecuritiesPartyRole | Organisation used as the pledgee for the securities. | NaN | NaN |
| Pledgee | PledgeeType | NaN | Specifies the type of pledgee. | PledgeeTypeCode | NaN |
| Pledgee | SecuritiesBalance | NaN | Balance which is held by a pledgee. | SecuritiesBalance | Pledgee |
| CustodyService | NaN | FinancialService | A service in which a financial institution holds securities on behalf of the client. Custody provides an investor a place to store assets. Assets in custody are not fungible for the brokerage because they remain on the client's name. | NaN | NaN |
| FATCAStatus | NaN | NaN | Foreign Account Tax Compliance Act (FATCA) status and the status source of the investor. | NaN | NaN |
| FATCAStatus | FATCAStatus | NaN | Foreign Account Tax Compliance Act (FATCA) status of the investor. | FATCAStatusCode | NaN |
| FATCAStatus | FATCASourceStatus | NaN | Source of the Foreign Account Tax Compliance Act (FATCA) status. | FATCASourceStatusCode | NaN |
| FATCAStatus | InvestmentAccountParty | NaN | Foreign Account Tax Compliance Act (FATCA) status linked to an investment account and played by a party in that context. | InvestmentAccountPartyRole | FATCAStatus |
| FATCAStatus | FATCAReportingDate | NaN | Date provided by the account owner to inform the account servicer of the date on which the holdings must be reported before the account is subsequently closed. | ISODate | NaN |
| ATMTotal | NaN | NaN | Current totals of the ATM. | NaN | NaN |
| ATMTotal | ATMBalance | NaN | Total balance of the ATM including reject cassette, but excluding the retract cassette. | ImpliedCurrencyAndAmount | NaN |
| ATMTotal | Currency | NaN | Currency of the totals. | CurrencyCode | NaN |
| ATMTotal | ATMCurrentNumber | NaN | Total number of units for non-valued media, excluding reject cassette. | Number | NaN |
| ATMTotal | ATMBalanceNumber | NaN | Total number of units for non-valued media, including reject cassette. | Number | NaN |
| ATMTotal | ATMCurrent | NaN | Available amount for dispense in the ATM. | ImpliedCurrencyAndAmount | NaN |
| ATMTotal | RelatedCardPayment | NaN | Related payments representing the current totals of the ATM. | CardPayment | ATMTotal |
| RegisteredContract | NaN | Contract | Contract registered for regulatory purpose by a registration agent for the journaling of payments made against the contract. | NaN | NaN |
| RegisteredContract | Certificate | NaN | Certificate against which all transactions in the scope of the regulatory requirements are registered. | GenericIdentification | RelatedCertificate |
| RegisteredContract | ContractBalance | NaN | Contract balance on date of contract registration. | CashBalance | RelatedRegisteredContract |
| RegisteredContract | ReportingParty | NaN | Party which must register the contract for regulatory reporting reasons. | RegulatoryReportingRole | RelatedReportingParty |
| RegisteredContract | Identification | NaN | Unique and unambiguous identification of the registered contract. | Max35Text | NaN |
| RegisteredContract | DeliveryDate | NaN | Provides the date for the delivery of the registered contract. | ISODate | NaN |
| RegisteredContract | RegistrationAgent | NaN | Agent which is in charge of the registration of the contract. | RegulatoryReportingRole | RelatedRegistrationAgent |
| RegisteredContract | ReceivingParty | NaN | Party which receives support information about the registered contract. | RegulatoryReportingRole | RelatedReceivingParty |
| RegisteredContract | Priority | NaN | Priority requested for the registered contract. | PriorityCode | NaN |
| RegisteredContract | RegistrationDate | NaN | Provides the date for the registration of the registered contract. | ISODate | NaN |
| RegisteredContract | ClosureReason | NaN | Reason of closure of the contract. | StatusReason | RelatedClosureReason |
| RegisteredContract | ClosureDate | NaN | Date of closure of the contract. | ISODate | NaN |
| RegisteredContract | PaymentScheduleType | NaN | Type of the payment schedule provided in the contract. | PaymentTerms | RelatedPaymentScheduleType |
| RegisteredContract | SubmissionDate | NaN | Provides the date for the submission of the registered contract. | ISODate | NaN |
| RegisteredContract | SendingParty | NaN | Party which sends support information about the registered contract. | RegulatoryReportingRole | RelatedSendingParty |
| RegisteredContract | DeliveryMethod | NaN | Provides the communication method for the delivery of the registered contract. | CommunicationMethodCode | NaN |
| RegisteredContract | SubmissionMethod | NaN | Provides the communication method for the submission of the registered contract. | CommunicationMethodCode | NaN |
| RegisteredContract | RelatedPayment | NaN | Provides the payment related of the registered contract. | Payment | ContractRegistration |
| RegisteredContract | Attachment | NaN | Documents provided as attachments to the registered contract. | Document | RelatedContract |
| Loan | NaN | Debt | Act of provding an amount of money, a property or other material goods to a another party in exchange for future repayment of the principal amount along with interest or other finance charges. | NaN | NaN |
| Loan | PrincipalAmount | NaN | Amount of money borrowed, or part of that amount which remains unpaid (excluding interest). | CurrencyAndAmount | NaN |
| Loan | InterestPaymentsSchedule | NaN | Schedule for the payment of the interests due on the loan. | PaymentTerms | RelatedLoan |
| Loan | IntraCompanyLoanIndicator | NaN | Loan is an intra-company loan. | YesNoIndicator | NaN |
| RegulatoryReportingRole | NaN | Role | Party which plays a role for regulatory reporting. | NaN | NaN |
| RegulatoryReportingRole | RelatedReportingParty | NaN | Related party which must register the contract for regulatory reporting reasons. | RegisteredContract | ReportingParty |
| RegulatoryReportingRole | RelatedRegistrationAgent | NaN | Related agent which is in charge of the registration of the contract. | RegisteredContract | RegistrationAgent |
| RegulatoryReportingRole | RelatedReceivingParty | NaN | Related party which receives support information about the registered contract. | RegisteredContract | ReceivingParty |
| RegulatoryReportingRole | RelatedSendingParty | NaN | Related Party which sends support information about the registered contract. | RegisteredContract | SendingParty |
| CreditDefaultSwap | NaN | Swaps | Credit default swap is a particular type of swap designed to transfer the credit exposure of fixed income products between two or more parties. | NaN | NaN |
| CreditDefaultSwap | RollDate | NaN | Roll date of the underlying asset as established by the asset issuer. | ISODate | NaN |
| CreditDefaultSwap | RollMonth | NaN | Roll month of the underlying asset as established by the asset issuer. | ISOYearMonth | NaN |
| CreditDefaultSwap | Series | NaN | Series number of the composition of the derivative if applicable. | Number | NaN |
| Swaps | NaN | Derivative | Derivative contract through which two parties exchange financial instruments. | NaN | NaN |
| Swaps | SovereignIssuer | NaN | Issuer is a national government within a given country. | NaN | NaN |
| Swaps | Obligation | NaN | Specific underlying debt upon which a swap is based. | NaN | NaN |
| Commodity | NaN | Asset | Basic good used in commerce that is interchangeable with other commodities of the same type. Commodities are most often used as inputs in the production of other goods or services. The quality of a given commodity may differ slightly, but it is essentially uniform across producers. When they are traded on an exchange, commodities must also meet specified minimum standards, also known as a basis grade. | NaN | NaN |
| Commodity | BaseProduct | NaN | Basic category of the commodity, such as agricultural or metal. | AssetClassProductTypeCode | NaN |
| Commodity | DetailedSubProduct | NaN | Further detailed description of the basic resources, such as aluminium, iron ore or wheat | AssetClassDetailedSubProductTypeCode | NaN |
| Commodity | SubProduct | NaN | Basic resources and agricultural products such as non-precious metal or grain. | AssetClassSubProductTypeCode | NaN |
| CRSStatus | NaN | NaN | Common Reporting Standard (CRS) status and the status source of the investor. | NaN | NaN |
| CRSStatus | CRSStatus | NaN | Common Reporting Standard (CRS) status of the investor. | CRSStatusCode | NaN |
| CRSStatus | ExceptionalReportingCountry | NaN | Reporting country for the CRS status when there is an exception at the country level. | CountryCode | NaN |
| CRSStatus | CRSSourceStatus | NaN | Source of the Common Reporting Standard (CRS) status expressed as a code. | CRSSourceStatusCode | NaN |
| CRSStatus | CRSReportingDate | NaN | Date provided by the account owner to inform the account servicer of the date on which the holdings must be reported before the account is subsequently closed. | ISODate | NaN |
| CRSStatus | InvestmentAccountParty | NaN | Common Reporting Standard (CRS) status linked to an investment account and played by a party in that context. | InvestmentAccountPartyRole | CRSStatus |
| AccountSwitching | NaN | CashAccountService | The Account Switch Service support the guaranteed switch of a customerâ€™s account and the transfer of payments arrangements associated with the account from one payment institution to another payment institution. | NaN | NaN |
| AccountSwitching | SwitchReceivedDateTime | NaN | Date and time that the request was received by the central switch service. | ISODateTime | NaN |
| AccountSwitching | SwitchDate | NaN | Date on which the account switch is expected to have completed. The value is the same as the targeted switch date if the switch completes in the expected timeline. | ISODate | NaN |
| AccountSwitching | SwitchStatus | NaN | State of the account switch at the time the message is sent. | SwitchStatusCode | NaN |
| AccountSwitching | UniqueReferenceNumber | NaN | Unique number that provides unique and unambiguous identification of the account switch. | Max35Text | NaN |
| AccountSwitching | SwitchType | NaN | Indicates whether the account switch is a full switch or a partial switch. | SwitchTypeCode | NaN |
| AccountSwitching | BalanceTransferWindow | NaN | Identifies the processing window in which the balance transfer will be processed on the day of the account switch. | BalanceTransferWindowCode | NaN |
| CappedLimit | NaN | NaN | Limits of the capped drawdown. | NaN | NaN |
| CappedLimit | IncomeCurrentPeriod | NaN | Income taken in the current income year. | CurrencyAndAmount | NaN |
| CappedLimit | StartDate | NaN | Start date of current reference period | ISODate | NaN |
| CappedLimit | IncomeLimitCurrentPeriod | NaN | Income limit for the current period. | CurrencyAndAmount | NaN |
| CappedLimit | RelatedDrawdown | NaN | Details of a drawdown tranche. | Drawdown | CappedLimit |
| CappedLimit | IncomeLimitNextPeriod | NaN | Income limit for the next income year. | CurrencyAndAmount | NaN |
| CorporateActionProtectProcess | NaN | NaN | Provides detailed information on protect and cover protect instructions. | NaN | NaN |
| CorporateActionProtectProcess | ProtectDate | NaN | Date at which the protect instruction was created and used for cover protect validation. | ISODate | NaN |
| CorporateActionProtectProcess | TransactionIdentification | NaN | Unique reference of the protect transaction assigned by the depository and used for cover protect validation. | Max15Text | NaN |
| CorporateActionProtectProcess | ProtectSafekeepingAccount | NaN | Account which submitted the original protect instruction used for cover protect instructions whereby one safekeeping account is covering on behalf of another safekeeping account. | Max35Text | NaN |
| CorporateActionProtectProcess | ProtectTransactionStatus | NaN | Status of the protect transaction. | DTCInstructionStatusCode | NaN |
| CorporateActionProtectProcess | UncoveredProtectQuantity | NaN | Remaining quantity of protect instruction which has not been covered. | SecuritiesQuantity | RelatedCorporateActionProtectProcess |
| CorporateActionProtectProcess | RelatedCorporateActionElection | NaN | Related election on wich the provided details informations refers to. | CorporateActionElection | ProtectProcess |
| CorporateActionProtectProcess | TransactionType | NaN | Indicates whether the instruction is a protect or a cover protect instruction. | ReorganisationTransactionTypeCode | NaN |
| PaymentTracker | NaN | NaN | Specifies the agent specific tracking system information of a payment transaction. | NaN | NaN |
| PaymentTracker | Agent | NaN | Identification of an agent in the tracker. | FinancialInstitution | RelatedPaymentTracker |
| PaymentTracker | ChargesAmount | NaN | Transaction charges to be paid by the charge bearer. | CurrencyAndAmount | NaN |
| PaymentTracker | ChargeBearer | NaN | Specifies which party/parties will bear the charges associated with the processing of the payment transaction. | ChargeBearerTypeCode | NaN |
| PaymentTracker | ExchangeRateData | NaN | Provides details of the rate and the currencies used in the foreign exchange. | CurrencyExchange | RelatedPaymentTracker |
| TaxEfficientProduct | NaN | NaN | Characteristics of a tax efficient product. | NaN | NaN |
| TaxEfficientProduct | EstimatedValue | NaN | Estimated value of the assets of the tax efficient product to be transferred. | NaN | NaN |
| TaxEfficientProduct | PreviousYears | NaN | Investment plans issued during previous years. | ISOYear | NaN |
| TaxEfficientProduct | CurrentInvestmentAmount | NaN | Amount of money invested. | CurrencyAndAmount | NaN |
| TaxEfficientProduct | Amount | NaN | Bonus paid out or withdrawn. | CurrencyAndAmount | NaN |
| TaxEfficientProduct | UnusedTaxDeduction | NaN | Unused tax deduction amount. | CurrencyAndAmount | NaN |
| TaxEfficientProduct | TaxCalculationBase | NaN | Amount of money from which the tax deduction is calculated. | CurrencyAndAmount | NaN |
| TaxEfficientProduct | LowestInvestedAmountCurrentYear | NaN | Lowest investment amount in the current year, used to calculate a tax deduction amount. | CurrencyAndAmount | NaN |
| TaxEfficientProduct | InvestorTaxReference | NaN | Identification of the investor as assigned by a tax authority. | NaN | NaN |
| TaxEfficientProduct | RelatedInvestmentPlan | NaN | Investment plan to what the characteristics of the tax efficient product relate to. | InvestmentPlan | TaxEfficientProduct |
| TaxEfficientProduct | TaxEfficientProductType | NaN | Type of tax efficient product, for example, an individual savings account (ISA) in the UK. | TaxEfficientProductTypeCode | NaN |
| TaxEfficientProduct | AmountType | NaN | Specifies if it is a Bonus paid out or Withdrawn. | TaxWrapperAmountTypeCode | NaN |
| TaxEfficientProduct | InvestmentsToFollowValue | NaN | Value of the investments to follow. | NaN | NaN |
| TaxEfficientProduct | InvestorTaxReferenceType | NaN | Identification of the type of investor as assigned by a tax authority. | PersonIdentificationTypeCode | NaN |
| TaxEfficientProduct | CurrentYearSubscription | NaN | Amounts already subscribed for the current year. | SubscriptionExecution | TaxEfficientProduct |
| Drawdown | NaN | NaN | Details of a drawdown tranche. | NaN | NaN |
| Drawdown | BeneficiaryType | NaN | Information about the recipient of the drawdown, when not the original pension holder. | BeneficiaryTypeCode | NaN |
| Drawdown | CrystallisedUnitsNumber | NaN | Number of units crystallised. | DecimalNumber | NaN |
| Drawdown | CrystallisationAmount | NaN | Amount that was originally designated for crystallisation. | CurrencyAndAmount | NaN |
| Drawdown | DrawdownStatus | NaN | Drawdown status of the pension. | DrawdownStatusCode | NaN |
| Drawdown | EventType | NaN | Type of crystallisation event. | DrawdownEventTypeCode | NaN |
| Drawdown | TrancheType | NaN | Type of drawdown tranche. | DrawdownTypeCode | NaN |
| Drawdown | PercentageOfTotalTransferValue | NaN | Percentage of the total transfer value covered by the drawdown. | PercentageRate | NaN |
| Drawdown | ApplicableRules | NaN | Specifies the rules that are applicable to the drawdown. For example, in the UK market, the pre-A-day rule that was introduced on 6 April 2006.) | ApplicableRulesCode | NaN |
| Drawdown | CappedLimit | NaN | Limits of the capped drawdown. | CappedLimit | RelatedDrawdown |
| Drawdown | Beneficiary | NaN | Information about the recipient of the drawdown, when not the original pension holder. | NaN | NaN |
| Drawdown | TriggeredDate | NaN | Date on which the drawdown was triggered when the drawdown type is flexible. | ISODate | NaN |
| Drawdown | EventDate | NaN | Date on which the crystallisation event was triggered. | ISODate | NaN |
| Drawdown | DrawdownAmount | NaN | Amount that was originally designated for drawdown. | CurrencyAndAmount | NaN |
| Drawdown | Pension | NaN | Attributes of a pension. | Pension | Drawdown |
| Drawdown | LifetimeAllowance | NaN | Percentage of the lifetime allowance (LTA) used. | PercentageRate | NaN |
| Drawdown | DrawdownTrancheIdentification | NaN | Reference of the drawdown. | NaN | NaN |
| Drawdown | NumberOfDrawdownTranches | NaN | Number of drawdown tranches. | Number | NaN |
| Pension | NaN | NaN | Attributes of a pension. | NaN | NaN |
| Pension | ValueOfPensionPolicy | NaN | Value of the pension policy, plan or scheme. | NaN | NaN |
| Pension | RelatedInvestmentPlan | NaN | Plan that allows investors to schedule periodical investments or divestments, according to pre-defined criteria. | InvestmentPlan | Pension |
| Pension | EstimatedValue | NaN | Estimated value of the pension policy, plan or scheme. | NaN | NaN |
| Pension | TransferScope | NaN | Scope of the pension policy, plan or scheme transfer. | PensionTransferScopeCode | NaN |
| Pension | Drawdown | NaN | Details of a drawdown tranche. | Drawdown | Pension |
| Pension | PensionOrderType | NaN | Type of order attached to the pension policy, plan or scheme. | PensionOrderTypeCode | NaN |
| Pension | RetirementAge | NaN | Age at which the pension policy, plan or scheme holder retires. | DecimalNumber | NaN |
| Pension | Identification | NaN | Identification of the pension policy, plan or scheme. | NaN | NaN |
| Pension | Type | NaN | Type of pension policy, plan or scheme. | PensionSchemeTypeCode | NaN |
| Pension | TaxFreeCashAmount | NaN | Amount of cash that is tax free. | NaN | NaN |
| Pension | LumpSumType | NaN | Type of lump sum paid to a member of the pension policy, plan or scheme. | LumpSumTypeCode | NaN |
| Pension | TaxReference | NaN | Tax reference issued to the pension policy, plan or scheme by a central organisation. | PersonIdentificationTypeCode | NaN |
| Pension | ClientLifetimeAllowanceProtection | NaN | Indicates whether the client has any lifetime allowance protection. | YesNoIndicator | NaN |
| CollateralReinvestment | NaN | NaN | Provides details on the type of the cash reinvestment in a given currency and on the cash reinvestment rate. | NaN | NaN |
| CollateralReinvestment | CashReinvestmentRate | NaN | Average interest rate received on cash collateral reinvestment by the lender for reinvestment of cash collateral. | PercentageRate | NaN |
| CollateralReinvestment | ReinvestedCashType | NaN | Provides details on the type of the cash reinvestment in a given currency. | ReinvestmentTypeCode | NaN |
| CollateralReinvestment | FundingSourceType | NaN | Information on type of funding sources used as funding to finance a margin loans. | FundingSourcesTypeCode | NaN |
| CollateralReinvestment | RelatedCollateral | NaN | Provides details on the collateral of the cash reinvestment. | Collateral | CollateralReinvestment |
| AdditionalLEIAttributes | NaN | NaN | Additional LEI attributes belonging to the LEI of an organisation. | NaN | NaN |
| AdditionalLEIAttributes | RelationshipType | NaN | Unique code designating the specific category of a directional relationship between two legal entities. | Max35Text | NaN |
| AdditionalLEIAttributes | RelationshipStatus | NaN | Status of the legal entities' relationship itself: ACTIVE or INACTIVE. | Max35Text | NaN |
| AdditionalLEIAttributes | RelatedOrganisationIdentification | NaN | Identification of the organisation for wich the LEI attributes belongs to. | OrganisationIdentification | AdditionalLEIAttributes |
| AdditionalLEIAttributes | ManagingLOU | NaN | LEI of the LEI Issuer that is responsible for administering this LEI Record. | LEIIdentifier | NaN |
| CreditTransferMandate | NaN | Mandate | Authorisation in favour of the creditor agent given by the creditor to initiate a credit transfer from its own account. | NaN | NaN |
| CreditTransferMandate | Reason | NaN | Reason for the setup of the credit transfer mandate. | Max70Text | NaN |
| CreditTransferMandate | FirstPaymentDate | NaN | Date of the first payment of a recurrent credit transfer as per the mandate. | ISODateTime | NaN |
| CreditTransferMandate | DateOfVerification | NaN | Date on which the credit transfer mandate has been verified. | ISODateTime | NaN |
| CreditTransferMandate | FinalPaymentDate | NaN | Date of the final payment of a recurrent credit transfer as per the mandate. | ISODateTime | NaN |
| CreditTransferMandate | Signature | NaN | Additional security provisions, such as a digital signature, as provided by the debtor. | Max10KBinary | NaN |
| ActivationService | NaN | NaN | Specifies the attributes for an activation. | NaN | NaN |
| ActivationService | DedicatedActivation | NaN | Unique, one-time code that a creditor may require from a debtor for activation purposes, and which is known only by the creditor and the debtor. | Max35Text | NaN |
| ActivationService | EndDate | NaN | Date and time at which the debtor activation will be deactivated. | ISODateTime | NaN |
| ActivationService | StartDate | NaN | Date and time at which the debtor activation will be activated. | ISODateTime | NaN |
| ActivationService | OriginalActivation | NaN | Specifies the attributes of the original activation. | ActivationService | RelatedActivation |
| ActivationService | RelatedActivation | NaN | Specifies the attributes of the activation. | ActivationService | OriginalActivation |
| ActivationService | RelatedElectronicInvoiceProcessingService | NaN | Related creditor's EIPP provider address to which the debtor activation has to be delivered. | ElectronicInvoiceProcessingService | DebtorActivation |
| EnrolmentVisibility | NaN | NaN | Specifies the details of the visibility of the creditor enrolment as shown to the debtors. | NaN | NaN |
| EnrolmentVisibility | EndDate | NaN | End date when the information will be shown to the debtors. | ISODateTime | NaN |
| EnrolmentVisibility | RelatedEnrolmentService | NaN | Provides the creditor enrolment as shown to the debtors of the details of the visibility. | EnrolmentService | Visibility |
| EnrolmentVisibility | LimitedVisibility | NaN | Indicates whether the information is shown to the debtors or not. | TrueFalseIndicator | NaN |
| EnrolmentVisibility | StartDate | NaN | Start date when the information will be shown to the debtors. | ISODateTime | NaN |
| EnrolmentService | NaN | NaN | Specifies the service details for the enrolment. | NaN | NaN |
| EnrolmentService | ServiceActivationLink | NaN | Web page link provided by the Creditor, intended to the Debtors, to proceed to activation when servicing messages can not be used. | Max2048Text | NaN |
| EnrolmentService | ServiceActivationAllowed | NaN | Define the acceptance of activation requests through the scheme. | TrueFalseIndicator | NaN |
| EnrolmentService | EndDate | NaN | End date when the creditor enrolment becomes effective. | ISODateTime | NaN |
| EnrolmentService | UltimateCreditor | NaN | Ultimate party to which an amount of money is due. | Organisation | RelatedUltimateCreditrorEnrolmentService |
| EnrolmentService | Visibility | NaN | Provides the details of the visibility of the creditor enrolment as shown to the debtors. | EnrolmentVisibility | RelatedEnrolmentService |
| EnrolmentService | ServiceDescriptionLink | NaN | Information web page, as provided by the creditor, to which the debtor can be linked for further information (Universal Resource Locator - URL). | Max2048Text | NaN |
| EnrolmentService | StartDate | NaN | Start date when the creditor enrolment becomes effective. | ISODateTime | NaN |
| EnrolmentService | Creditor | NaN | Party to which an amount of money is due. | Organisation | RelatedCreditrorEnrolmentService |
| EnrolmentService | OriginalEnrolment | NaN | Specifies the service details for the original enrolment. | EnrolmentService | RelatedEnrolment |
| EnrolmentService | RelatedElectronicInvoiceProcessingService | NaN | Specifies the details service for the enrolment. | ElectronicInvoiceProcessingService | CreditorEnrolment |
| EnrolmentService | RelatedEnrolment | NaN | Specifies the service details for the enrolment. | EnrolmentService | OriginalEnrolment |
| ElectronicInvoiceProcessingService | NaN | AccountService | Specifies the attributes for the electronic invoice processing. | NaN | NaN |
| ElectronicInvoiceProcessingService | RelatedInvoice | NaN | Specifies the details for the invoice for the service. | Invoice | RelatedElectronicInvoiceProcessingService |
| ElectronicInvoiceProcessingService | ElectronicInvoiceSolutionProvider | NaN | Organisation servicing the e-invoicing for the debtor. | ElectronicInvoiceServiceProvider | RelatedElectronicInvoiceSolutionService |
| ElectronicInvoiceProcessingService | CreditorEnrolment | NaN | Specifies the details for the enrolment of the service. | EnrolmentService | RelatedElectronicInvoiceProcessingService |
| ElectronicInvoiceProcessingService | ElectronicInvoiceDirectoryProvider | NaN | Organisation servicing the e-invoicing for the debtor. | ElectronicInvoiceServiceProvider | RelatedElectronicInvoiceDirectoryService |
| ElectronicInvoiceProcessingService | DebtorActivation | NaN | Creditor's EIPP provider address to which the debtor activation has to be delivered. | ActivationService | RelatedElectronicInvoiceProcessingService |
| ElectronicInvoiceProcessingService | ProcessingStatus | NaN | Specifies the status and the reason of the processing service. | ElectronicInvoiceServiceStatus | RelatedElectronicinvoiceProcessingService |
| ElectronicInvoiceServiceProvider | NaN | Role | Organisation servicing the e-invoicing for the debtor. | NaN | NaN |
| ElectronicInvoiceServiceProvider | RelatedElectronicInvoiceSolutionService | NaN | Service related to the e-invoicing of the debtor organisation. | ElectronicInvoiceProcessingService | ElectronicInvoiceSolutionProvider |
| ElectronicInvoiceServiceProvider | ServiceStatus | NaN | Specifies the status and the reason of the enrolment request. | ElectronicInvoiceServiceStatus | StatusReasonOriginator |
| ElectronicInvoiceServiceProvider | RelatedElectronicInvoiceDirectoryService | NaN | Service related to the e-invoicing of the debtor organisation. | ElectronicInvoiceProcessingService | ElectronicInvoiceDirectoryProvider |
| ElectronicInvoiceServiceStatus | NaN | NaN | Specifies the status and the reason of the enrolment request. | NaN | NaN |
| ElectronicInvoiceServiceStatus | ServiceStatus | NaN | Provides detailed information on the acceptance result. | ServiceRequestStatusCode | NaN |
| ElectronicInvoiceServiceStatus | ActivationStatusReason | NaN | Provides detailed information on the activation result. | Max35Text | NaN |
| ElectronicInvoiceServiceStatus | EnrolmentStatusReason | NaN | Specifies the status reason for the enrolment request. | ExternalCreditorEnrolmentCancellationReasonCode | NaN |
| ElectronicInvoiceServiceStatus | StatusReasonOriginator | NaN | Specifies the provider of the enrolment request for wich the status and the reason are provided. | ElectronicInvoiceServiceProvider | ServiceStatus |
| ElectronicInvoiceServiceStatus | RelatedElectronicinvoiceProcessingService | NaN | Specifies the processing service of the status and the reason. | ElectronicInvoiceProcessingService | ProcessingStatus |
| CountrySubdivisionIdentification | NaN | NaN | Identification code and name to identify a name of a unit resulting from the division of a country, dependency, or other area of special geopolitical interest contained in ISO 3166-1, on the basis of country names obtained from the United Nations (ISO 3166-2: Country subdivision code). | NaN | NaN |
| CountrySubdivisionIdentification | Code | NaN | Code to identify a name of a unit resulting from the division of a country, dependency, or other area of special geopolitical interest contained in ISO 3166-1, on the basis of country names obtained from the United Nations (ISO 3166-2: Country subdivision code). | CountrySubDivisionCode | NaN |
| CountrySubdivisionIdentification | Name | NaN | Name to identify a code of a unit resulting from the division of a country, dependency, or other area of special geopolitical interest contained in ISO 3166-1, on the basis of country names obtained from the United Nations (ISO 3166-2: Country subdivision code). | Max35Text | NaN |
| CountrySubDivision | NaN | NaN | Sub division of a nation with its own government. | NaN | NaN |
| CountrySubDivision | Country | NaN | Nation with its own government. | Country | SubDivision |
| CountrySubDivision | Province | NaN | A territory governed as an administrative or political unit of a country. | NaN | NaN |
| CountrySubDivision | Region | NaN | Identification of an administrative division of a country, state, or territory. | NaN | NaN |
| CountrySubDivision | County | NaN | Identifier of a county. | NaN | NaN |
| CountrySubDivision | DistrictSubDivision | NaN | Identification of a sub-division of a district. | NaN | NaN |
| CountrySubDivision | State | NaN | Organised political community or area forming a part of a federation. | NaN | NaN |
| CountrySubDivision | District | NaN | Name of a district, for example, a part of a town or region. | NaN | NaN |
| DigitalWallet | NaN | SecuritiesAccount | Digital account where digital assets or digital tokens can be stored and where an entry is made. | NaN | NaN |
| DigitalWallet | DigitalAssetIdentifier | NaN | The Digital Token Identifier (DTI) is an 8 character code assigned to fungible digital assets which uses distributed ledger technology for its issuance, storage, exchange, record of ownership or transaction validation and is not a currency (ISO 4217) as described in ISO 24165 â€“ DTI. | DTI2021Identifier | NaN |
| PostTradeRiskReduction | NaN | NaN | Multilateral portfolio compression but also rebalancing and other types of risk mitigating techniques used in the market. | NaN | NaN |
| PostTradeRiskReduction | Structurer | NaN | Identification of the structurer of the post trade risk reduction identifier. | Organisation | RelatedPostTradeRiskReduction |
| PostTradeRiskReduction | Technique | NaN | Indicator of a type of a post trade risk reduction operation for the purpose of reporting. | RiskReductionServiceCode | NaN |
| PostTradeRiskReduction | PTRRIdentifier | NaN | Identification of the post trade risk reduction. | TradeIdentification | RelatedPostTradeRiskReduction |
| PostTradeRiskReduction | RelatedDerivativeEvent | NaN | Derivative event for which the risk has been reduced. | DerivativeEvent | PostTradeRiskReduction |
| PostTradeRiskReduction | ServiceProvider | NaN | Service provider for the post trade risk reduction. | AccountServicerRole | RelatedPTRR |
| DerivativeEvent | NaN | NaN | Event which has an impact on the life cycle of the derivative contract. | NaN | NaN |
| DerivativeEvent | EventIdentifier | NaN | Identification of the derivative event. | TradeIdentification | RelatedEventIdentifier |
| DerivativeEvent | RelatedDerivative | NaN | Derivative for which the event has been triggered. | Derivative | Event |
| DerivativeEvent | TimeStamp | NaN | Indicates the time stamp of a derivative event. | ISODateTime | NaN |
| DerivativeEvent | PostTradeRiskReduction | NaN | Means to reduce risks in the derivatives market. | PostTradeRiskReduction | RelatedDerivativeEvent |
| DerivativeEvent | Type | NaN | Classification of the derivative event type | DerivativeEventTypeCode | NaN |
| EnergyDelivery | NaN | NaN | Information related to energy commodities delivery attributes. | NaN | NaN |
| EnergyDelivery | PointOrZone | NaN | Identification of delivery/interconnection point or zone as a code. | EICIdentifier | NaN |
| EnergyDelivery | Capacity | NaN | Specifies delivery capacity. | LongDecimalNumber | NaN |
| EnergyDelivery | Interval | NaN | Specifies delivery intervals. | DecimalNumber | NaN |
| EnergyDelivery | RelatedEnergy | NaN | Specifies corresponding energy delivery. | Energy | Delivery |
| Energy | NaN | Commodity | Energy related commodities. | NaN | NaN |
| Energy | WeekDay | NaN | Specifies energy week days. | WeekDayCode | NaN |
| Energy | LoadType | NaN | Specifies the energy delivery profile. | EnergyLoadTypeCode | NaN |
| Energy | Delivery | NaN | Specifies energy delivery. | EnergyDelivery | RelatedEnergy |
| Energy | Duration | NaN | Specifies energy duration details. | DurationTypeCode | NaN |
| Energy | Price | NaN | Specifies corresponding energy. | Price | RelatedEnergy |
| Energy | QuantityUnit | NaN | Specifies energy quanity units. | QuantityCode | NaN |
| Energy | InterConnectionPoint | NaN | Specifies the energy delivery profile. | EICIdentifier | NaN |
| Energy | Date | NaN | Specifies date related to energy. | ISODate | NaN |
| ExecutingPerson | NaN | SecuritiesOrderPartyRole | Identification of the person or algorithm within the member or participant of the trading venue who is respon sible for the execution of the transaction resulting from the order. | NaN | NaN |
| InvestmentDecisionPerson | NaN | SecuritiesOrderPartyRole | Identification of the person or the algorithm within the member or participant of the trading venue who is responsible for the investment decision. | NaN | NaN |
| NonExecutingBroker | NaN | SecuritiesOrderPartyRole | Member or participant of the trading venue who routed the order on behalf of and in the name of another member or participant of the trading venue. | NaN | NaN |

## Traces
| Message Component Name | Message Element Name | Type Trace To | Is Technical | Trace To Business Component | Trace To Element | Trace Path |
| --- | --- | --- | --- | --- | --- | --- |
| AccountIdentification4Choice | IBAN | NaN | False | AccountIdentification | IBAN | IBAN |
| AccountIdentification4Choice | Other | AccountIdentification | False | AccountIdentification | IBAN | IBAN |
| AccountSchemeName1Choice | NaN | NaN | False | Scheme | NaN | NaN |
| AccountSchemeName1Choice | Code | NaN | False | Scheme | Code | Code |
| AccountSchemeName1Choice | Proprietary | NaN | False | Scheme | Code | Code |
| AddressType3Choice | NaN | NaN | True | NaN | NaN | NaN |
| AddressType3Choice | Code | NaN | True | NaN | NaN | NaN |
| AddressType3Choice | Proprietary | GenericIdentification | True | NaN | NaN | NaN |
| AdviceType1 | NaN | NaN | False | PaymentProcessing | NaN | NaN |
| AdviceType1 | CreditAdvice | NaN | False | PaymentProcessing | AdviceType | AdviceType |
| AdviceType1 | DebitAdvice | NaN | False | PaymentProcessing | AdviceType | AdviceType |
| AdviceType1Choice | NaN | NaN | True | NaN | NaN | NaN |
| AdviceType1Choice | Code | NaN | True | NaN | NaN | NaN |
| AdviceType1Choice | Proprietary | NaN | True | NaN | NaN | NaN |
| AmendmentInformationDetails15 | NaN | NaN | False | DirectDebitMandate | NaN | NaN |
| AmendmentInformationDetails15 | OriginalCreditorAgent | Organisation | False | Organisation | OrganisationIdentification | RelatedDirectDebit/PartyRole/(as CreditorAgentRole)/Player/(as FinancialInstitution)/OrganisationIdentification |
| AmendmentInformationDetails15 | OriginalCreditorAgentAccount | CashAccount | False | PaymentPartyRole | CashAccount | RelatedDirectDebit/PartyRole/(as CreditorAgentRole)/CashAccount |
| AmendmentInformationDetails15 | OriginalCreditorSchemeIdentification | PartyIdentificationInformation | False | Party | Identification | RelatedDirectDebit/PartyRole/(as CreditorRole)/Player/(as Party)/Identification |
| AmendmentInformationDetails15 | OriginalDebtor | PartyIdentificationInformation | False | Party | Identification | RelatedDirectDebit/PartyRole/(as DebtorRole)/Player/(as Party)/Identification |
| AmendmentInformationDetails15 | OriginalDebtorAccount | CashAccount | False | PaymentPartyRole | CashAccount | RelatedDirectDebit/PartyRole/(as DebtorRole)/CashAccount |
| AmendmentInformationDetails15 | OriginalDebtorAgent | Organisation | False | Organisation | OrganisationIdentification | RelatedDirectDebit/PartyRole/(as DebtorAgentRole)/Player/(as FinancialInstitution)/OrganisationIdentification |
| AmendmentInformationDetails15 | OriginalDebtorAgentAccount | CashAccount | False | PaymentPartyRole | CashAccount | RelatedDirectDebit/PartyRole/(as DebtorAgentRole)/CashAccount |
| AmendmentInformationDetails15 | OriginalFinalCollectionDate | NaN | False | DirectDebitMandate | FinalCollectionDate | FinalCollectionDate |
| AmendmentInformationDetails15 | OriginalFrequency | NaN | False | Mandate | Frequency | Frequency |
| AmendmentInformationDetails15 | OriginalMandateIdentification | NaN | False | Mandate | MandateIdentification | MandateIdentification |
| AmendmentInformationDetails15 | OriginalReason | NaN | False | Agreement | Description | Document/Agreement/Description |
| AmendmentInformationDetails15 | OriginalTrackingDays | NaN | False | Mandate | TrackingDays | TrackingDays |
| AmountType4Choice | NaN | NaN | False | Payment | NaN | NaN |
| AmountType4Choice | EquivalentAmount | Payment | False | Payment | EquivalentAmount | EquivalentAmount |
| AmountType4Choice | InstructedAmount | NaN | False | Payment | InstructedAmount | InstructedAmount |
| Authorisation1Choice | NaN | NaN | True | NaN | NaN | NaN |
| Authorisation1Choice | Code | NaN | True | NaN | NaN | NaN |
| Authorisation1Choice | Proprietary | NaN | True | NaN | NaN | NaN |
| BranchAndFinancialInstitutionIdentification8 | NaN | NaN | False | Organisation | NaN | NaN |
| BranchAndFinancialInstitutionIdentification8 | BranchIdentification | OrganisationIdentification | False | Organisation | OrganisationIdentification | Branch/OrganisationIdentification |
| BranchAndFinancialInstitutionIdentification8 | FinancialInstitutionIdentification | OrganisationIdentification | False | Organisation | OrganisationIdentification | (as FinancialInstitution)/OrganisationIdentification |
| BranchData5 | NaN | NaN | False | OrganisationIdentification | NaN | NaN |
| BranchData5 | Identification | NaN | False | GenericIdentification | Identification | OtherIdentification/Identification |
| BranchData5 | LEI | NaN | True | NaN | NaN | NaN |
| BranchData5 | Name | NaN | False | PartyName | Name | OrganisationName/Name |
| BranchData5 | PostalAddress | PostalAddress | False | NaN | NaN | IdentifiedParty/ContactPoint/(as PostalAddress) |
| CashAccount40 | NaN | NaN | False | CashAccount | NaN | NaN |
| CashAccount40 | Currency | NaN | False | Account | BaseCurrency | BaseCurrency |
| CashAccount40 | Identification | AccountIdentification | False | Account | Identification | Identification |
| CashAccount40 | Name | NaN | False | AccountIdentification | Name | Identification/Name |
| CashAccount40 | Proxy | AccountIdentification | False | Account | Identification | Identification |
| CashAccount40 | Type | CashAccount | False | CashAccount | CashAccountType | CashAccountType |
| CashAccountType2Choice | NaN | NaN | False | CashAccount | NaN | NaN |
| CashAccountType2Choice | Code | NaN | False | CashAccount | CashAccountType | CashAccountType |
| CashAccountType2Choice | Proprietary | NaN | False | CashAccount | CashAccountType | CashAccountType |
| CategoryPurpose1Choice | NaN | NaN | False | Payment | NaN | NaN |
| CategoryPurpose1Choice | Code | NaN | False | PaymentProcessing | CategoryPurpose | PaymentExecution/ProcessingInstructions/CategoryPurpose |
| CategoryPurpose1Choice | Proprietary | NaN | False | PaymentProcessing | CategoryPurpose | PaymentExecution/ProcessingInstructions/CategoryPurpose |
| Charges16 | NaN | NaN | False | Charges | NaN | NaN |
| Charges16 | Agent | Organisation | False | NaN | NaN | ChargesPartyRole/(as ChargeAgent)/Player/(as Organisation)/OrganisationIdentification |
| Charges16 | Amount | NaN | False | Adjustment | Amount | Amount |
| Charges16 | Type | Charges | False | Charges | ChargeType | ChargeType |
| ChargeType3Choice | NaN | NaN | False | Charges | NaN | NaN |
| ChargeType3Choice | Code | NaN | False | Charges | ChargeType | ChargeType |
| ChargeType3Choice | Proprietary | GenericIdentification | False | Charges | ChargeType | ChargeType |
| Cheque19 | NaN | NaN | False | ChequeIssue | NaN | NaN |
| Cheque19 | ChequeFrom | PartyIdentificationInformation | False | Party | Identification | Cheque/ChequePartyRole/Player/(as Party)/Identification |
| Cheque19 | ChequeMaturityDate | NaN | False | Cheque | MaturityDate | Cheque/MaturityDate |
| Cheque19 | ChequeNumber | NaN | False | CreditInstrument | CreditInstrumentIdentification | CreditInstrumentIdentification |
| Cheque19 | ChequeType | NaN | False | Cheque | ChequeType | Cheque/Type |
| Cheque19 | DeliverTo | PartyIdentificationInformation | False | ChequeIssue | DeliverTo | DeliverTo |
| Cheque19 | DeliveryMethod | ChequeIssue | False | ChequeIssue | DeliveryMethod | DeliveryMethod |
| Cheque19 | FormsCode | NaN | False | Cheque | FormsCode | Cheque/FormsCode |
| Cheque19 | InstructionPriority | NaN | False | Payment | Priority | RelatedPayment/Priority |
| Cheque19 | MemoField | NaN | False | Cheque | MemoField | Cheque/MemoField |
| Cheque19 | PrintLocation | NaN | False | ChequeIssue | PrintLocation | PrintLocation |
| Cheque19 | RegionalClearingZone | NaN | False | Cheque | RegionalClearingZone | Cheque/RegionalClearingZone |
| Cheque19 | Signature | NaN | False | NaN | NaN | Cheque/Evidence/(as Signature) |
| ChequeDeliveryMethod1Choice | NaN | NaN | False | ChequeIssue | NaN | NaN |
| ChequeDeliveryMethod1Choice | Code | NaN | False | ChequeIssue | DeliveryMethod | DeliveryMethod |
| ChequeDeliveryMethod1Choice | Proprietary | NaN | False | ChequeIssue | DeliveryMethod | DeliveryMethod |
| ClearingSystemIdentification2Choice | NaN | NaN | False | CashClearingSystem | NaN | NaN |
| ClearingSystemIdentification2Choice | Code | NaN | False | CashClearingSystem | Identification | Identification |
| ClearingSystemIdentification2Choice | Proprietary | NaN | False | CashClearingSystem | Identification | Identification |
| ClearingSystemIdentification3Choice | NaN | NaN | False | CashClearingSystem | NaN | NaN |
| ClearingSystemIdentification3Choice | Code | NaN | False | CashClearingSystem | Identification | Identification |
| ClearingSystemIdentification3Choice | Proprietary | NaN | False | CashClearingSystem | Identification | Identification |
| ClearingSystemMemberIdentification2 | NaN | NaN | False | CashClearingSystemMember | NaN | NaN |
| ClearingSystemMemberIdentification2 | ClearingSystemIdentification | CashClearingSystem | False | CashClearingSystem | Identification | ClearingMember/Player/(as CashClearingSystem)/Identification |
| ClearingSystemMemberIdentification2 | MemberIdentification | NaN | False | GenericIdentification | Identification | OrganisationIdentification/OtherIdentification/Identification |
| Contact13 | NaN | NaN | False | PersonIdentification | NaN | NaN |
| Contact13 | Department | NaN | False | PostalAddress | Department | IdentifiedParty/ContactPoint/(as PostalAddress)/Department |
| Contact13 | EmailAddress | NaN | False | ElectronicAddress | EmailAddress | Person/ContactPoint/(as ElectronicAddress)/EmailAddress |
| Contact13 | EmailPurpose | NaN | True | NaN | NaN | NaN |
| Contact13 | FaxNumber | NaN | False | PhoneAddress | FaxNumber | Person/ContactPoint/(as PhoneAddress)/FaxNumber |
| Contact13 | JobTitle | NaN | False | Person | BusinessFunctionTitle | Person/BusinessFunctionTitle |
| Contact13 | MobileNumber | NaN | False | PhoneAddress | MobileNumber | Person/ContactPoint/(as PhoneAddress)/MobileNumber |
| Contact13 | Name | NaN | False | PartyName | Name | PersonName/Name |
| Contact13 | NamePrefix | NaN | False | PersonName | NamePrefix | PersonName/NamePrefix |
| Contact13 | Other | ContactPoint | False | PartyIdentificationInformation | OtherIdentification | OtherIdentification |
| Contact13 | PhoneNumber | NaN | False | PhoneAddress | PhoneNumber | Person/ContactPoint/(as PhoneAddress)/PhoneNumber |
| Contact13 | PreferredMethod | NaN | False | Party | ContactPoint | Person/ContactPoint |
| Contact13 | Responsibility | NaN | False | Person | Profession | Person/Profession |
| Contact13 | URLAddress | NaN | False | ElectronicAddress | URLAddress | Person/ContactPoint/(as ElectronicAddress)/URLAddress |
| CreditorReferenceInformation3 | NaN | NaN | False | PaymentIdentification | NaN | NaN |
| CreditorReferenceInformation3 | Reference | NaN | False | PaymentIdentification | CreditorReference | CreditorReference |
| CreditorReferenceInformation3 | Type | Document | True | NaN | NaN | NaN |
| CreditorReferenceType2Choice | NaN | NaN | False | Document | NaN | NaN |
| CreditorReferenceType2Choice | Code | NaN | False | Document | Type | Type |
| CreditorReferenceType2Choice | Proprietary | NaN | False | Document | Type | Type |
| CreditorReferenceType3 | NaN | NaN | False | Document | NaN | NaN |
| CreditorReferenceType3 | CodeOrProprietary | Document | False | NaN | NaN | . |
| CreditorReferenceType3 | Issuer | NaN | False | NaN | NaN | PartyRole/(as DocumentIssuer) |
| CreditTransferMandateData1 | NaN | NaN | False | CreditTransferMandate | NaN | NaN |
| CreditTransferMandateData1 | DateOfSignature | NaN | False | Agreement | DateSigned | DateSigned |
| CreditTransferMandateData1 | DateOfVerification | NaN | False | CreditTransferMandate | DateOfVerification | DateOfVerification |
| CreditTransferMandateData1 | ElectronicSignature | NaN | False | CreditTransferMandate | Signature | Signature |
| CreditTransferMandateData1 | FinalPaymentDate | NaN | False | CreditTransferMandate | FinalPaymentDate | FinalPaymentDate |
| CreditTransferMandateData1 | FirstPaymentDate | NaN | False | CreditTransferMandate | FirstPaymentDate | FirstPaymentDate |
| CreditTransferMandateData1 | Frequency | NaN | False | Mandate | Frequency | Frequency |
| CreditTransferMandateData1 | MandateIdentification | NaN | False | Mandate | MandateIdentification | MandateIdentification |
| CreditTransferMandateData1 | Reason | NaN | False | CreditTransferMandate | Reason | Reason |
| CreditTransferMandateData1 | Type | Mandate | False | Mandate | MandatePaymentType | MandatePaymentType |
| CreditTransferTransaction61 | NaN | NaN | False | CreditTransfer | NaN | NaN |
| CreditTransferTransaction61 | Amount | Payment | False | Payment | InstructedAmount | InstructedAmount |
| CreditTransferTransaction61 | ChargeBearer | NaN | False | Charges | BearerType | Adjustments/(as Charges)/BearerType |
| CreditTransferTransaction61 | ChequeInstruction | ChequeIssue | False | NaN | NaN | CreditMethod/(as ChequeIssue) |
| CreditTransferTransaction61 | Creditor | PartyIdentificationInformation | False | Party | Identification | PartyRole/(as CreditorRole)/Player/(as Party)/Identification |
| CreditTransferTransaction61 | CreditorAccount | CashAccount | False | PaymentPartyRole | CashAccount | PartyRole/(as CreditorRole)/CashAccount |
| CreditTransferTransaction61 | CreditorAgent | Organisation | False | Organisation | OrganisationIdentification | PartyRole/(as CreditorAgentRole)/Player/(as FinancialInstitution)/OrganisationIdentification |
| CreditTransferTransaction61 | CreditorAgentAccount | CashAccount | False | PaymentPartyRole | CashAccount | PartyRole/(as CreditorAgentRole)/CashAccount |
| CreditTransferTransaction61 | ExchangeRateInformation | CurrencyExchange | False | Payment | CurrencyExchange | CurrencyExchange |
| CreditTransferTransaction61 | InstructionForCreditorAgent | Payment | False | Payment | InstructionForCreditorAgent | InstructionForCreditorAgent |
| CreditTransferTransaction61 | InstructionForDebtorAgent | Payment | False | Payment | InstructionForDebtorAgent | InstructionForDebtorAgent |
| CreditTransferTransaction61 | IntermediaryAgent1 | Organisation | False | Organisation | OrganisationIdentification | PartyRole/(as IntermediaryAgentRole)/Player/(as FinancialInstitution)/OrganisationIdentification |
| CreditTransferTransaction61 | IntermediaryAgent1Account | CashAccount | False | PaymentPartyRole | CashAccount | PartyRole/(as IntermediaryAgentRole)/CashAccount |
| CreditTransferTransaction61 | IntermediaryAgent2 | Organisation | False | Organisation | OrganisationIdentification | PartyRole/(as IntermediaryAgentRole)/Player/(as FinancialInstitution)/OrganisationIdentification |
| CreditTransferTransaction61 | IntermediaryAgent2Account | CashAccount | False | PaymentPartyRole | CashAccount | PartyRole/(as IntermediaryAgentRole)/CashAccount |
| CreditTransferTransaction61 | IntermediaryAgent3 | Organisation | False | Organisation | OrganisationIdentification | PartyRole/(as IntermediaryAgentRole)/Player/(as FinancialInstitution)/OrganisationIdentification |
| CreditTransferTransaction61 | IntermediaryAgent3Account | CashAccount | False | PaymentPartyRole | CashAccount | PartyRole/(as IntermediaryAgentRole)/CashAccount |
| CreditTransferTransaction61 | MandateRelatedInformation | CreditTransferMandate | False | MandatePartyRole | Mandate | PartyRole/Player/(as Party)/Role/(as MandatePartyRole)/Mandate |
| CreditTransferTransaction61 | PaymentIdentification | PaymentIdentification | False | Payment | PaymentRelatedIdentifications | PaymentRelatedIdentifications |
| CreditTransferTransaction61 | PaymentTypeInformation | PaymentProcessing | False | PaymentExecution | ProcessingInstructions | PaymentExecution/ProcessingInstructions |
| CreditTransferTransaction61 | Purpose | PaymentObligation | False | PaymentObligation | Purpose | PaymentObligation/Purpose |
| CreditTransferTransaction61 | RegulatoryReporting | RegulatoryReport | False | FinancialTransaction | RegulatoryReport | PaymentObligation/Trade/FinancialTransaction/RegulatoryReport |
| CreditTransferTransaction61 | RelatedRemittanceInformation | ContactPoint | False | PaymentObligation | RemittanceLocation | PaymentObligation/RemittanceLocation |
| CreditTransferTransaction61 | RemittanceInformation | Document | False | PaymentObligation | AssociatedDocument | PaymentObligation/AssociatedDocument |
| CreditTransferTransaction61 | SupplementaryData | NaN | True | NaN | NaN | NaN |
| CreditTransferTransaction61 | Tax | Tax | False | Payment | TaxOnPayment | TaxOnPayment |
| CreditTransferTransaction61 | UltimateCreditor | PartyIdentificationInformation | False | Party | Identification | PaymentObligation/PartyRole/(as UltimateCreditorRole)/Player/(as Party)/Identification |
| CreditTransferTransaction61 | UltimateDebtor | PartyIdentificationInformation | False | Party | Identification | PaymentObligation/PartyRole/(as UltimateDebtorRole)/Player/(as Party)/Identification |
| CurrencyExchange13 | NaN | NaN | False | CurrencyExchange | NaN | NaN |
| CurrencyExchange13 | ExchangeRate | NaN | False | CurrencyExchange | ExchangeRate | ExchangeRate |
| CurrencyExchange13 | SourceCurrency | NaN | False | CurrencyExchange | SourceCurrency | SourceCurrency |
| CurrencyExchange13 | TargetCurrency | NaN | False | CurrencyExchange | TargetCurrency | TargetCurrency |
| CurrencyExchange13 | UnitCurrency | NaN | False | CurrencyExchange | UnitCurrency | UnitCurrency |
| DateAndDateTime2Choice | NaN | NaN | True | NaN | NaN | NaN |
| DateAndDateTime2Choice | Date | NaN | True | NaN | NaN | NaN |
| DateAndDateTime2Choice | DateTime | NaN | True | NaN | NaN | NaN |
| DateAndPlaceOfBirth1 | NaN | NaN | False | Person | NaN | NaN |
| DateAndPlaceOfBirth1 | BirthDate | NaN | False | Person | BirthDate | BirthDate |
| DateAndPlaceOfBirth1 | CityOfBirth | NaN | False | PostalAddress | TownName | PlaceOfBirth/Address/TownName |
| DateAndPlaceOfBirth1 | CountryOfBirth | NaN | False | Country | Code | PlaceOfBirth/Address/Country/Code |
| DateAndPlaceOfBirth1 | ProvinceOfBirth | NaN | False | CountrySubDivision | Province | PlaceOfBirth/Address/Country/SubDivision/Province |
| DateAndType1 | NaN | NaN | True | NaN | NaN | NaN |
| DateAndType1 | Date | NaN | True | NaN | NaN | NaN |
| DateAndType1 | Type | NaN | True | NaN | NaN | NaN |
| DatePeriod2 | NaN | NaN | True | NaN | NaN | NaN |
| DatePeriod2 | FromDate | NaN | False | DateTimePeriod | FromDateTime | FromDateTime |
| DatePeriod2 | ToDate | NaN | False | DateTimePeriod | ToDateTime | ToDateTime |
| DateType2Choice | NaN | NaN | True | NaN | NaN | NaN |
| DateType2Choice | Code | NaN | True | NaN | NaN | NaN |
| DateType2Choice | Proprietary | NaN | True | NaN | NaN | NaN |
| DirectDebitTransaction12 | NaN | NaN | False | DirectDebit | NaN | NaN |
| DirectDebitTransaction12 | CreditorSchemeIdentification | PartyIdentificationInformation | False | Party | Identification | PartyRole/(as CreditorRole)/Player/(as Party)/Identification |
| DirectDebitTransaction12 | MandateRelatedInformation | DirectDebitMandate | False | DirectDebit | DirectDebitMandate | DirectDebitMandate |
| DirectDebitTransaction12 | PreNotificationDate | NaN | False | DirectDebit | PreNotificationDate | PreNotificationDate |
| DirectDebitTransaction12 | PreNotificationIdentification | NaN | False | DirectDebit | PreNotificationIdentification | PreNotificationIdentification |
| DirectDebitTransactionInformation32 | NaN | NaN | False | DirectDebit | NaN | NaN |
| DirectDebitTransactionInformation32 | ChargeBearer | NaN | False | Charges | BearerType | Adjustments/(as Charges)/BearerType |
| DirectDebitTransactionInformation32 | Debtor | PartyIdentificationInformation | False | Party | Identification | PartyRole/(as DebtorRole)/Player/(as Party)/Identification |
| DirectDebitTransactionInformation32 | DebtorAccount | CashAccount | False | PaymentPartyRole | CashAccount | PartyRole/(as DebtorRole)/CashAccount |
| DirectDebitTransactionInformation32 | DebtorAgent | Organisation | False | Organisation | OrganisationIdentification | PartyRole/(as DebtorAgentRole)/Player/(as FinancialInstitution)/OrganisationIdentification |
| DirectDebitTransactionInformation32 | DebtorAgentAccount | CashAccount | False | PaymentPartyRole | CashAccount | PartyRole/(as DebtorAgentRole)/CashAccount |
| DirectDebitTransactionInformation32 | DirectDebitTransaction | DirectDebit | False | NaN | NaN | . |
| DirectDebitTransactionInformation32 | InstructedAmount | NaN | False | Payment | InstructedAmount | InstructedAmount |
| DirectDebitTransactionInformation32 | InstructionForCreditorAgent | NaN | False | Payment | InstructionForCreditorAgent | InstructionForCreditorAgent |
| DirectDebitTransactionInformation32 | PaymentIdentification | PaymentIdentification | False | Payment | PaymentRelatedIdentifications | PaymentRelatedIdentifications |
| DirectDebitTransactionInformation32 | PaymentTypeInformation | PaymentProcessing | False | Payment | PaymentExecution | PaymentExecution |
| DirectDebitTransactionInformation32 | Purpose | PaymentObligation | False | PaymentProcessing | CategoryPurpose | PaymentExecution/ProcessingInstructions/CategoryPurpose |
| DirectDebitTransactionInformation32 | RegulatoryReporting | RegulatoryReport | False | FinancialTransaction | RegulatoryReport | PaymentObligation/Trade/FinancialTransaction/RegulatoryReport |
| DirectDebitTransactionInformation32 | RelatedRemittanceInformation | ContactPoint | False | Document | PlaceOfStorage | PaymentObligation/AssociatedDocument/PlaceOfStorage |
| DirectDebitTransactionInformation32 | RemittanceInformation | Document | False | PaymentObligation | AssociatedDocument | PaymentObligation/AssociatedDocument |
| DirectDebitTransactionInformation32 | SupplementaryData | NaN | True | NaN | NaN | NaN |
| DirectDebitTransactionInformation32 | Tax | Tax | False | Payment | TaxOnPayment | TaxOnPayment |
| DirectDebitTransactionInformation32 | UltimateCreditor | PartyIdentificationInformation | False | Party | Identification | PaymentObligation/PartyRole/(as UltimateCreditorRole)/Player/(as Party)/Identification |
| DirectDebitTransactionInformation32 | UltimateDebtor | PartyIdentificationInformation | False | Party | Identification | PaymentObligation/PartyRole/(as UltimateDebtorRole)/Player/(as Party)/Identification |
| DocumentAdjustment1 | NaN | NaN | False | Adjustment | NaN | NaN |
| DocumentAdjustment1 | AdditionalInformation | NaN | True | NaN | NaN | NaN |
| DocumentAdjustment1 | Amount | NaN | False | Adjustment | Amount | Amount |
| DocumentAdjustment1 | CreditDebitIndicator | NaN | False | Adjustment | Direction | Direction |
| DocumentAdjustment1 | Reason | NaN | False | Adjustment | Reason | Reason |
| DocumentAmount1 | NaN | NaN | False | Adjustment | NaN | NaN |
| DocumentAmount1 | Amount | NaN | False | Adjustment | Amount | Amount |
| DocumentAmount1 | Type | Discount | False | NaN | NaN | (as Discount)/. |
| DocumentAmountType1Choice | NaN | NaN | False | Discount | NaN | NaN |
| DocumentAmountType1Choice | Code | NaN | False | Discount | DiscountType | DiscountType |
| DocumentAmountType1Choice | Proprietary | NaN | True | NaN | NaN | NaN |
| DocumentLineIdentification1 | NaN | NaN | False | Document | NaN | NaN |
| DocumentLineIdentification1 | Number | NaN | True | NaN | NaN | NaN |
| DocumentLineIdentification1 | RelatedDate | NaN | False | Document | IssueDate | IssueDate |
| DocumentLineIdentification1 | Type | Document | False | Document | Type | Type |
| DocumentLineInformation2 | NaN | NaN | False | Document | NaN | NaN |
| DocumentLineInformation2 | Amount | Document | False | Document | Amount | Amount |
| DocumentLineInformation2 | Description | NaN | False | NaN | NaN | . |
| DocumentLineInformation2 | Identification | Document | False | GenericIdentification | Identification | DocumentIdentification/Identification |
| DocumentLineType1 | NaN | NaN | False | Document | NaN | NaN |
| DocumentLineType1 | CodeOrProprietary | Document | False | NaN | NaN | . |
| DocumentLineType1 | Issuer | NaN | False | GenericIdentification | Identification | PartyRole/(as DocumentIssuer)/Player/(as Party)/Identification/OtherIdentification/Identification |
| DocumentLineType1Choice | NaN | NaN | False | Document | NaN | NaN |
| DocumentLineType1Choice | Code | NaN | False | Document | Type | Type |
| DocumentLineType1Choice | Proprietary | NaN | False | Document | Type | Type |
| DocumentType1 | NaN | NaN | False | Document | NaN | NaN |
| DocumentType1 | CodeOrProprietary | Document | False | NaN | NaN | . |
| DocumentType1 | Issuer | NaN | False | NaN | NaN | PartyRole/(as DocumentIssuer) |
| DocumentType2Choice | NaN | NaN | False | Document | NaN | NaN |
| DocumentType2Choice | Code | NaN | False | Document | Type | Type |
| DocumentType2Choice | Proprietary | NaN | False | Document | Type | Type |
| EquivalentAmount2 | NaN | NaN | False | Payment | NaN | NaN |
| EquivalentAmount2 | Amount | NaN | False | Payment | EquivalentAmount | EquivalentAmount |
| EquivalentAmount2 | CurrencyOfTransfer | NaN | False | Payment | CurrencyOfTransfer | CurrencyOfTransfer |
| ExchangeRate1 | NaN | NaN | False | CurrencyExchange | NaN | NaN |
| ExchangeRate1 | ContractIdentification | NaN | False | TradeIdentification | Identification | CurrencyExchangeForForeignExchangeTrade/TradeRelatedIdentifications/Identification |
| ExchangeRate1 | ExchangeRate | NaN | False | CurrencyExchange | ExchangeRate | ExchangeRate |
| ExchangeRate1 | RateType | NaN | False | CurrencyExchange | RateType | RateType |
| ExchangeRate1 | UnitCurrency | NaN | False | CurrencyExchange | UnitCurrency | UnitCurrency |
| FinancialIdentificationSchemeName1Choice | NaN | NaN | False | Scheme | NaN | NaN |
| FinancialIdentificationSchemeName1Choice | Code | NaN | False | Scheme | Code | Code |
| FinancialIdentificationSchemeName1Choice | Proprietary | NaN | False | Scheme | Code | Code |
| FinancialInstitutionIdentification23 | NaN | NaN | False | OrganisationIdentification | NaN | NaN |
| FinancialInstitutionIdentification23 | BICFI | NaN | False | OrganisationIdentification | BICFI | BICFI |
| FinancialInstitutionIdentification23 | ClearingSystemMemberIdentification | CashClearingSystemMember | False | OrganisationIdentification | ClearingSystemMemberIdentificationType | ClearingSystemMemberIdentificationType |
| FinancialInstitutionIdentification23 | LEI | NaN | True | NaN | NaN | NaN |
| FinancialInstitutionIdentification23 | Name | NaN | False | PartyName | Name | OrganisationName/Name |
| FinancialInstitutionIdentification23 | Other | OrganisationIdentification | False | NaN | NaN | . |
| FinancialInstitutionIdentification23 | PostalAddress | PostalAddress | False | NaN | NaN | Organisation/ContactPoint/(as PostalAddress) |
| Frequency36Choice | NaN | NaN | True | NaN | NaN | NaN |
| Frequency36Choice | Period | NaN | True | NaN | NaN | NaN |
| Frequency36Choice | PointInTime | NaN | True | NaN | NaN | NaN |
| Frequency36Choice | Type | NaN | True | NaN | NaN | NaN |
| FrequencyAndMoment1 | NaN | NaN | True | NaN | NaN | NaN |
| FrequencyAndMoment1 | PointInTime | NaN | True | NaN | NaN | NaN |
| FrequencyAndMoment1 | Type | NaN | True | NaN | NaN | NaN |
| FrequencyPeriod1 | NaN | NaN | True | NaN | NaN | NaN |
| FrequencyPeriod1 | CountPerPeriod | NaN | True | NaN | NaN | NaN |
| FrequencyPeriod1 | Type | NaN | True | NaN | NaN | NaN |
| Garnishment4 | NaN | NaN | False | Garnishment | NaN | NaN |
| Garnishment4 | Date | NaN | False | Trade | TradeDateTime | Trade/TradeDateTime |
| Garnishment4 | EmployeeTerminationIndicator | NaN | False | PersonProfile | EmployeeTerminationIndicator | PartyRole/Player/(as Person)/PersonProfile/EmployeeTerminationIndicator |
| Garnishment4 | FamilyMedicalInsuranceIndicator | NaN | False | PersonProfile | FamilyMedicalInsuranceIndicator | PartyRole/Player/(as Person)/PersonProfile/FamilyMedicalInsuranceIndicator |
| Garnishment4 | Garnishee | PartyIdentificationInformation | False | NaN | NaN | PaymentOffset/PaymentObligation/PartyRole/(as UltimateDebtorRole) |
| Garnishment4 | GarnishmentAdministrator | PartyIdentificationInformation | False | Party | Identification | PaymentOffset/PartyRole/(as CreditorAgentRole)/Player/(as Party)/Identification |
| Garnishment4 | ReferenceNumber | NaN | False | Tax | Identification | PaymentOffset/TaxOnPayment/Identification |
| Garnishment4 | RemittedAmount | NaN | False | Document | RemittedAmount | AssociatedDocument/RemittedAmount |
| Garnishment4 | Type | Document | False | PaymentObligation | AssociatedDocument | AssociatedDocument |
| GarnishmentType1 | NaN | NaN | False | Document | NaN | NaN |
| GarnishmentType1 | CodeOrProprietary | Document | False | NaN | NaN | . |
| GarnishmentType1 | Issuer | NaN | False | NaN | NaN | PartyRole/(as DocumentIssuer) |
| GarnishmentType1Choice | NaN | NaN | False | Document | NaN | NaN |
| GarnishmentType1Choice | Code | NaN | False | Document | Type | Type |
| GarnishmentType1Choice | Proprietary | NaN | False | Document | Type | Type |
| GenericAccountIdentification1 | NaN | NaN | False | AccountIdentification | NaN | NaN |
| GenericAccountIdentification1 | Identification | NaN | False | GenericIdentification | Identification | ProprietaryIdentification/Identification |
| GenericAccountIdentification1 | Issuer | NaN | False | NaN | NaN | ProprietaryIdentification/PartyRole/(as IdentificationIssuerRole) |
| GenericAccountIdentification1 | SchemeName | Scheme | False | GenericIdentification | Scheme | ProprietaryIdentification/Scheme |
| GenericFinancialIdentification1 | NaN | NaN | False | OrganisationIdentification | NaN | NaN |
| GenericFinancialIdentification1 | Identification | NaN | False | GenericIdentification | Identification | OtherIdentification/Identification |
| GenericFinancialIdentification1 | Issuer | NaN | False | NaN | NaN | OtherIdentification/PartyRole/(as IdentificationIssuerRole) |
| GenericFinancialIdentification1 | SchemeName | Scheme | False | GenericIdentification | Scheme | OtherIdentification/Scheme |
| GenericIdentification3 | NaN | NaN | False | GenericIdentification | NaN | NaN |
| GenericIdentification3 | Identification | NaN | False | GenericIdentification | Identification | Identification |
| GenericIdentification3 | Issuer | NaN | False | NaN | NaN | PartyRole/(as IdentificationIssuerRole) |
| GenericIdentification30 | NaN | NaN | False | GenericIdentification | NaN | NaN |
| GenericIdentification30 | Identification | NaN | False | GenericIdentification | Identification | Identification |
| GenericIdentification30 | Issuer | NaN | False | NaN | NaN | PartyRole/(as IdentificationIssuerRole) |
| GenericIdentification30 | SchemeName | NaN | False | Scheme | NameShort | Scheme/NameShort |
| GenericOrganisationIdentification3 | NaN | NaN | False | OrganisationIdentification | NaN | NaN |
| GenericOrganisationIdentification3 | Identification | NaN | False | GenericIdentification | Identification | OtherIdentification/Identification |
| GenericOrganisationIdentification3 | Issuer | NaN | False | NaN | NaN | OtherIdentification/PartyRole/(as IdentificationIssuerRole) |
| GenericOrganisationIdentification3 | SchemeName | OrganisationIdentification | False | GenericIdentification | Scheme | OtherIdentification/Scheme |
| GenericPersonIdentification2 | NaN | NaN | False | PersonIdentification | NaN | NaN |
| GenericPersonIdentification2 | Identification | NaN | False | GenericIdentification | Identification | OtherIdentification/Identification |
| GenericPersonIdentification2 | Issuer | NaN | False | NaN | NaN | OtherIdentification/PartyRole/(as IdentificationIssuerRole) |
| GenericPersonIdentification2 | SchemeName | PersonIdentification | False | GenericIdentification | Scheme | OtherIdentification/Scheme |
| GroupHeader114 | NaN | NaN | False | Payment | NaN | NaN |
| GroupHeader114 | Authorisation | NaN | True | NaN | NaN | NaN |
| GroupHeader114 | ControlSum | NaN | True | NaN | NaN | NaN |
| GroupHeader114 | CreationDateTime | NaN | False | PaymentExecution | CreationDate | PaymentExecution/CreationDate |
| GroupHeader114 | ForwardingAgent | Organisation | False | Organisation | OrganisationIdentification | PartyRole/(as ForwardingAgentRole)/Player/(as FinancialInstitution)/OrganisationIdentification |
| GroupHeader114 | InitiatingParty | PartyIdentificationInformation | False | Party | Identification | PartyRole/(as InitiatingPartyRole)/Player/(as Party)/Identification |
| GroupHeader114 | InitiationSource | NaN | True | NaN | NaN | NaN |
| GroupHeader114 | MessageIdentification | NaN | False | PaymentIdentification | ExecutionIdentification | PaymentRelatedIdentifications/ExecutionIdentification |
| GroupHeader114 | NumberOfTransactions | NaN | True | NaN | NaN | NaN |
| GroupHeader118 | NaN | NaN | False | Payment | NaN | NaN |
| GroupHeader118 | Authorisation | NaN | True | NaN | NaN | NaN |
| GroupHeader118 | ControlSum | NaN | True | NaN | NaN | NaN |
| GroupHeader118 | CreationDateTime | NaN | False | PaymentExecution | CreationDate | PaymentExecution/CreationDate |
| GroupHeader118 | ForwardingAgent | Organisation | False | Organisation | OrganisationIdentification | PartyRole/(as ForwardingAgentRole)/Player/(as FinancialInstitution)/OrganisationIdentification |
| GroupHeader118 | InitiatingParty | PartyIdentificationInformation | False | Party | Identification | PartyRole/(as InitiatingPartyRole)/Player/(as Party)/Identification |
| GroupHeader118 | MessageIdentification | NaN | False | PaymentIdentification | ExecutionIdentification | PaymentRelatedIdentifications/ExecutionIdentification |
| GroupHeader118 | NumberOfTransactions | NaN | True | NaN | NaN | NaN |
| GroupHeader124 | NaN | NaN | False | Payment | NaN | NaN |
| GroupHeader124 | Authorisation | NaN | True | NaN | NaN | NaN |
| GroupHeader124 | ControlSum | NaN | True | NaN | NaN | NaN |
| GroupHeader124 | CreationDateTime | NaN | False | PaymentExecution | CreationDate | PaymentExecution/CreationDate |
| GroupHeader124 | CreditorAgent | Organisation | False | Organisation | OrganisationIdentification | PartyRole/(as CreditorAgentRole)/Player/(as FinancialInstitution)/OrganisationIdentification |
| GroupHeader124 | DebtorAgent | Organisation | False | Organisation | OrganisationIdentification | PartyRole/(as DebtorAgentRole)/Player/(as FinancialInstitution)/OrganisationIdentification |
| GroupHeader124 | ForwardingAgent | Organisation | False | Organisation | OrganisationIdentification | PartyRole/(as ForwardingAgentRole)/Player/(as FinancialInstitution)/OrganisationIdentification |
| GroupHeader124 | GroupReversal | NaN | True | NaN | NaN | NaN |
| GroupHeader124 | InitiatingParty | PartyIdentificationInformation | False | Party | Identification | PartyRole/(as InitiatingPartyRole)/Player/(as Party)/Identification |
| GroupHeader124 | MessageIdentification | NaN | False | PaymentIdentification | ExecutionIdentification | PaymentRelatedIdentifications/ExecutionIdentification |
| GroupHeader124 | NumberOfTransactions | NaN | True | NaN | NaN | NaN |
| GroupHeader128 | NaN | NaN | False | Payment | NaN | NaN |
| GroupHeader128 | CreationDateTime | NaN | False | PaymentExecution | CreationDate | PaymentExecution/CreationDate |
| GroupHeader128 | CreditorAgent | Organisation | False | Organisation | OrganisationIdentification | PartyRole/(as CreditorAgentRole)/Player/(as FinancialInstitution)/OrganisationIdentification |
| GroupHeader128 | DebtorAgent | Organisation | False | Organisation | OrganisationIdentification | PartyRole/(as DebtorAgentRole)/Player/(as FinancialInstitution)/OrganisationIdentification |
| GroupHeader128 | ForwardingAgent | Organisation | False | Organisation | OrganisationIdentification | PartyRole/(as ForwardingAgentRole)/Player/(as FinancialInstitution)/OrganisationIdentification |
| GroupHeader128 | InitiatingParty | PartyIdentificationInformation | False | Party | Identification | PartyRole/(as InitiatingPartyRole)/Player/(as Party)/Identification |
| GroupHeader128 | MessageIdentification | NaN | False | PaymentIdentification | ExecutionIdentification | PaymentRelatedIdentifications/ExecutionIdentification |
| InstructionForCreditorAgent3 | NaN | NaN | False | Payment | NaN | NaN |
| InstructionForCreditorAgent3 | Code | NaN | False | Payment | InstructionForCreditorAgent | InstructionForCreditorAgent |
| InstructionForCreditorAgent3 | InstructionInformation | NaN | True | NaN | NaN | NaN |
| InstructionForDebtorAgent1 | NaN | NaN | False | Payment | NaN | NaN |
| InstructionForDebtorAgent1 | Code | NaN | False | Payment | InstructionForCreditorAgent | InstructionForCreditorAgent |
| InstructionForDebtorAgent1 | InstructionInformation | NaN | True | NaN | NaN | NaN |
| LocalInstrument2Choice | NaN | NaN | False | PaymentProcessing | NaN | NaN |
| LocalInstrument2Choice | Code | NaN | False | PaymentProcessing | LocalInstrument | LocalInstrument |
| LocalInstrument2Choice | Proprietary | NaN | False | PaymentProcessing | LocalInstrument | LocalInstrument |
| MandateClassification1Choice | NaN | NaN | False | Payment | NaN | NaN |
| MandateClassification1Choice | Code | NaN | False | PaymentProcessing | CategoryPurpose | PaymentExecution/ProcessingInstructions/CategoryPurpose |
| MandateClassification1Choice | Proprietary | NaN | False | PaymentProcessing | CategoryPurpose | PaymentExecution/ProcessingInstructions/CategoryPurpose |
| MandateRelatedData3Choice | NaN | NaN | True | NaN | NaN | NaN |
| MandateRelatedData3Choice | CreditTransferMandate | CreditTransferMandate | True | NaN | NaN | NaN |
| MandateRelatedData3Choice | DirectDebitMandate | DirectDebitMandate | True | NaN | NaN | NaN |
| MandateRelatedInformation16 | NaN | NaN | False | DirectDebitMandate | NaN | NaN |
| MandateRelatedInformation16 | AmendmentIndicator | NaN | False | Mandate | Amendment | Amendment |
| MandateRelatedInformation16 | AmendmentInformationDetails | DirectDebitMandate | False | NaN | NaN | . |
| MandateRelatedInformation16 | DateOfSignature | NaN | False | Agreement | DateSigned | DateSigned |
| MandateRelatedInformation16 | ElectronicSignature | NaN | False | NaN | NaN | Document/Evidence/(as ElectronicSignature) |
| MandateRelatedInformation16 | FinalCollectionDate | NaN | False | DirectDebitMandate | FinalCollectionDate | FinalCollectionDate |
| MandateRelatedInformation16 | FirstCollectionDate | NaN | False | DirectDebitMandate | FirstCollectionDate | FirstCollectionDate |
| MandateRelatedInformation16 | Frequency | NaN | False | Mandate | Frequency | Frequency |
| MandateRelatedInformation16 | MandateIdentification | NaN | False | Mandate | MandateIdentification | MandateIdentification |
| MandateRelatedInformation16 | Reason | NaN | False | Agreement | Description | Document/Agreement/Description |
| MandateRelatedInformation16 | TrackingDays | NaN | False | Mandate | TrackingDays | TrackingDays |
| MandateSetupReason1Choice | NaN | NaN | True | NaN | NaN | NaN |
| MandateSetupReason1Choice | Code | NaN | True | NaN | NaN | NaN |
| MandateSetupReason1Choice | Proprietary | NaN | True | NaN | NaN | NaN |
| MandateTypeInformation2 | NaN | NaN | False | Mandate | NaN | NaN |
| MandateTypeInformation2 | CategoryPurpose | Payment | False | PaymentProcessing | CategoryPurpose | (as DirectDebitMandate)/MandatePaymentType/CategoryPurpose |
| MandateTypeInformation2 | Classification | Payment | False | DirectDebitMandate | Classification | (as DirectDebitMandate)/Classification |
| MandateTypeInformation2 | LocalInstrument | PaymentProcessing | False | Mandate | MandatePaymentType | (as DirectDebitMandate)/MandatePaymentType |
| MandateTypeInformation2 | ServiceLevel | ServiceLevel | False | PaymentProcessing | ServiceLevel | (as DirectDebitMandate)/MandatePaymentType/ServiceLevel |
| NameAndAddress18 | NaN | NaN | False | PartyIdentificationInformation | NaN | NaN |
| NameAndAddress18 | Address | PostalAddress | False | NaN | NaN | IdentifiedParty/ContactPoint/(as PostalAddress) |
| NameAndAddress18 | Name | NaN | False | PartyName | Name | PartyName/Name |
| NumberOfTransactionsPerStatus5 | NaN | NaN | True | NaN | NaN | NaN |
| NumberOfTransactionsPerStatus5 | DetailedControlSum | NaN | True | NaN | NaN | NaN |
| NumberOfTransactionsPerStatus5 | DetailedNumberOfTransactions | NaN | True | NaN | NaN | NaN |
| NumberOfTransactionsPerStatus5 | DetailedStatus | NaN | True | NaN | NaN | NaN |
| OrganisationIdentification39 | NaN | NaN | False | OrganisationIdentification | NaN | NaN |
| OrganisationIdentification39 | AnyBIC | NaN | False | OrganisationIdentification | AnyBIC | AnyBIC |
| OrganisationIdentification39 | LEI | NaN | True | NaN | NaN | NaN |
| OrganisationIdentification39 | Other | OrganisationIdentification | False | PartyIdentificationInformation | OtherIdentification | OtherIdentification |
| OrganisationIdentificationSchemeName1Choice | NaN | NaN | False | OrganisationIdentification | NaN | NaN |
| OrganisationIdentificationSchemeName1Choice | Code | NaN | False | Scheme | Code | OtherIdentification/Scheme/Code |
| OrganisationIdentificationSchemeName1Choice | Proprietary | NaN | False | Scheme | Code | OtherIdentification/Scheme/Code |
| OriginalGroupHeader20 | NaN | NaN | False | PaymentExecution | NaN | NaN |
| OriginalGroupHeader20 | OriginalCreationDateTime | NaN | False | PaymentExecution | CreationDate | CreationDate |
| OriginalGroupHeader20 | OriginalMessageIdentification | NaN | False | PaymentIdentification | ExecutionIdentification | Payment/PaymentRelatedIdentifications/ExecutionIdentification |
| OriginalGroupHeader20 | OriginalMessageNameIdentification | NaN | True | NaN | NaN | NaN |
| OriginalGroupHeader20 | ReversalReasonInformation | StatusReason | False | Payment | PaymentStatus | Payment/PaymentStatus |
| OriginalGroupHeader22 | NaN | NaN | False | PaymentExecution | NaN | NaN |
| OriginalGroupHeader22 | GroupStatus | NaN | False | PaymentStatus | Status | Payment/PaymentStatus/Status |
| OriginalGroupHeader22 | NumberOfTransactionsPerStatus | NaN | True | NaN | NaN | NaN |
| OriginalGroupHeader22 | OriginalControlSum | NaN | True | NaN | NaN | NaN |
| OriginalGroupHeader22 | OriginalCreationDateTime | NaN | False | PaymentExecution | CreationDate | CreationDate |
| OriginalGroupHeader22 | OriginalMessageIdentification | NaN | False | PaymentIdentification | ExecutionIdentification | Payment/PaymentRelatedIdentifications/ExecutionIdentification |
| OriginalGroupHeader22 | OriginalMessageNameIdentification | NaN | True | NaN | NaN | NaN |
| OriginalGroupHeader22 | OriginalNumberOfTransactions | NaN | True | NaN | NaN | NaN |
| OriginalGroupHeader22 | StatusReasonInformation | PaymentStatus | False | Status | StatusReason | Payment/PaymentStatus/StatusReason |
| OriginalPaymentInstruction50 | NaN | NaN | False | Payment | NaN | NaN |
| OriginalPaymentInstruction50 | BatchBooking | NaN | True | NaN | NaN | NaN |
| OriginalPaymentInstruction50 | OriginalControlSum | NaN | True | NaN | NaN | NaN |
| OriginalPaymentInstruction50 | OriginalNumberOfTransactions | NaN | True | NaN | NaN | NaN |
| OriginalPaymentInstruction50 | OriginalPaymentInformationIdentification | NaN | False | TradeIdentification | Identification | PaymentRelatedIdentifications/Identification |
| OriginalPaymentInstruction50 | PaymentInformationReversal | NaN | True | NaN | NaN | NaN |
| OriginalPaymentInstruction50 | ReversalPaymentInformationIdentification | NaN | False | PaymentIdentification | InstructionIdentification | PaymentRelatedIdentifications/InstructionIdentification |
| OriginalPaymentInstruction50 | ReversalReasonInformation | StatusReason | False | Status | StatusReason | PaymentStatus/StatusReason |
| OriginalPaymentInstruction50 | TransactionInformation | Payment | False | NaN | NaN | NaN |
| OriginalPaymentInstruction51 | NaN | NaN | False | Payment | NaN | NaN |
| OriginalPaymentInstruction51 | NumberOfTransactionsPerStatus | NaN | True | NaN | NaN | NaN |
| OriginalPaymentInstruction51 | OriginalControlSum | NaN | True | NaN | NaN | NaN |
| OriginalPaymentInstruction51 | OriginalNumberOfTransactions | NaN | True | NaN | NaN | NaN |
| OriginalPaymentInstruction51 | OriginalPaymentInformationIdentification | NaN | False | TradeIdentification | Identification | PaymentRelatedIdentifications/Identification |
| OriginalPaymentInstruction51 | PaymentInformationStatus | NaN | False | PaymentStatus | Status | PaymentStatus/Status |
| OriginalPaymentInstruction51 | StatusReasonInformation | PaymentStatus | False | Status | StatusReason | PaymentStatus/StatusReason |
| OriginalPaymentInstruction51 | TransactionInformationAndStatus | Payment | False | NaN | NaN | . |
| OriginalTransactionReference42 | NaN | NaN | False | Payment | NaN | NaN |
| OriginalTransactionReference42 | Amount | Payment | False | Payment | InstructedAmount | InstructedAmount |
| OriginalTransactionReference42 | Creditor | PartyIdentificationInformation | False | Party | Identification | PartyRole/(as CreditorRole)/Player/(as Party)/Identification |
| OriginalTransactionReference42 | CreditorAccount | CashAccount | False | PaymentPartyRole | CashAccount | PartyRole/(as CreditorRole)/CashAccount |
| OriginalTransactionReference42 | CreditorAgent | Organisation | False | Party | Identification | PartyRole/(as CreditorAgentRole)/Player/(as Party)/Identification |
| OriginalTransactionReference42 | CreditorAgentAccount | CashAccount | False | PaymentPartyRole | CashAccount | PartyRole/(as CreditorAgentRole)/CashAccount |
| OriginalTransactionReference42 | CreditorSchemeIdentification | PartyIdentificationInformation | False | Party | Identification | PartyRole/(as CreditorRole)/Player/(as Party)/Identification |
| OriginalTransactionReference42 | Debtor | PartyIdentificationInformation | False | Party | Identification | PartyRole/(as DebtorRole)/Player/(as Party)/Identification |
| OriginalTransactionReference42 | DebtorAccount | CashAccount | False | PaymentPartyRole | CashAccount | PartyRole/(as DebtorRole)/CashAccount |
| OriginalTransactionReference42 | DebtorAgent | Organisation | False | Party | Identification | PartyRole/(as DebtorAgentRole)/Player/(as Party)/Identification |
| OriginalTransactionReference42 | DebtorAgentAccount | CashAccount | False | PaymentPartyRole | CashAccount | PartyRole/(as DebtorAgentRole)/CashAccount |
| OriginalTransactionReference42 | InterbankSettlementAmount | NaN | False | CashSettlement | InterbankSettlementAmount | PaymentExecution/(as PaymentInstruction)/SettlementInstruction/InterbankSettlementAmount |
| OriginalTransactionReference42 | InterbankSettlementDate | NaN | False | CashSettlement | InterbankSettlementDate | PaymentExecution/(as PaymentInstruction)/SettlementInstruction/InterbankSettlementDate |
| OriginalTransactionReference42 | MandateRelatedInformation | NaN | False | NaN | NaN | (as DirectDebit)/DirectDebitMandate |
| OriginalTransactionReference42 | PaymentMethod | NaN | False | CreditInstrument | Method | CreditMethod/Method |
| OriginalTransactionReference42 | PaymentTypeInformation | PaymentProcessing | False | PaymentExecution | ProcessingInstructions | PaymentExecution/ProcessingInstructions |
| OriginalTransactionReference42 | Purpose | PaymentObligation | False | PaymentObligation | Purpose | PaymentObligation/Purpose |
| OriginalTransactionReference42 | RemittanceInformation | Document | False | PaymentObligation | AssociatedDocument | PaymentObligation/AssociatedDocument |
| OriginalTransactionReference42 | RequestedCollectionDate | NaN | False | Obligation | RequestedSettlementDate | ObligationOffset/RequestedSettlementDate |
| OriginalTransactionReference42 | RequestedExecutionDate | NaN | False | Obligation | RequestedSettlementDate | ObligationOffset/RequestedSettlementDate |
| OriginalTransactionReference42 | SettlementInformation | CashSettlement | False | PaymentInstruction | SettlementInstruction | PaymentExecution/(as PaymentInstruction)/SettlementInstruction |
| OriginalTransactionReference42 | UltimateCreditor | PartyIdentificationInformation | False | Party | Identification | PaymentObligation/PartyRole/(as UltimateCreditorRole)/Player/(as Party)/Identification |
| OriginalTransactionReference42 | UltimateDebtor | PartyIdentificationInformation | False | Party | Identification | PaymentObligation/PartyRole/(as UltimateDebtorRole)/Player/(as Party)/Identification |
| OtherContact1 | NaN | NaN | False | ContactPoint | NaN | NaN |
| OtherContact1 | ChannelType | NaN | True | NaN | NaN | NaN |
| OtherContact1 | Identification | NaN | False | ContactPoint | Identification | Identification |
| Party50Choice | NaN | NaN | False | PartyIdentificationInformation | NaN | NaN |
| Party50Choice | Agent | Organisation | False | NaN | NaN | IdentifiedParty/(as FinancialInstitution) |
| Party50Choice | Party | PartyIdentificationInformation | False | NaN | NaN | . |
| Party52Choice | NaN | NaN | False | PartyIdentificationInformation | NaN | NaN |
| Party52Choice | OrganisationIdentification | OrganisationIdentification | False | NaN | NaN | (as OrganisationIdentification) |
| Party52Choice | PrivateIdentification | PersonIdentification | False | NaN | NaN | (as PersonIdentification) |
| PartyIdentification272 | NaN | NaN | False | PartyIdentificationInformation | NaN | NaN |
| PartyIdentification272 | ContactDetails | PersonIdentification | False | Party | ContactPoint | IdentifiedParty/ContactPoint |
| PartyIdentification272 | CountryOfResidence | NaN | False | Country | Code | IdentifiedParty/Residence/Address/Country/Code |
| PartyIdentification272 | Identification | PartyIdentificationInformation | False | NaN | NaN | . |
| PartyIdentification272 | Name | NaN | False | PartyName | Name | PartyName/Name |
| PartyIdentification272 | PostalAddress | PostalAddress | False | NaN | NaN | IdentifiedParty/ContactPoint/(as PostalAddress) |
| PaymentIdentification6 | NaN | NaN | False | PaymentIdentification | NaN | NaN |
| PaymentIdentification6 | EndToEndIdentification | NaN | False | PaymentIdentification | EndToEndIdentification | EndToEndIdentification |
| PaymentIdentification6 | InstructionIdentification | NaN | False | PaymentIdentification | InstructionIdentification | Payment/PaymentRelatedIdentifications/InstructionIdentification |
| PaymentIdentification6 | UETR | NaN | False | PaymentIdentification | UETR | UETR |
| PaymentInitiationSource1 | NaN | NaN | True | NaN | NaN | NaN |
| PaymentInitiationSource1 | Name | NaN | True | NaN | NaN | NaN |
| PaymentInitiationSource1 | Provider | NaN | True | NaN | NaN | NaN |
| PaymentInitiationSource1 | Version | NaN | True | NaN | NaN | NaN |
| PaymentInstruction44 | NaN | NaN | False | PaymentInstruction | NaN | NaN |
| PaymentInstruction44 | BatchBooking | NaN | True | NaN | NaN | NaN |
| PaymentInstruction44 | ChargeBearer | NaN | False | Charges | BearerType | Payment/Adjustments/(as Charges)/BearerType |
| PaymentInstruction44 | ChargesAccount | CashAccount | False | Charges | ChargesDebitAccount | Payment/Adjustments/(as Charges)/BearerType |
| PaymentInstruction44 | ChargesAccountAgent | Organisation | False | Organisation | OrganisationIdentification | Payment/Adjustments/(as Charges)/ChargesPartyRole/(as ChargeAccountAgent)/Player/(as Organisation)/OrganisationIdentification |
| PaymentInstruction44 | ControlSum | NaN | True | NaN | NaN | NaN |
| PaymentInstruction44 | CreditTransferTransactionInformation | CreditTransfer | False | NaN | NaN | Payment/(as CreditTransfer) |
| PaymentInstruction44 | Debtor | PartyIdentificationInformation | False | Party | Identification | Payment/PartyRole/(as DebtorRole)/Player/(as Party)/Identification |
| PaymentInstruction44 | DebtorAccount | CashAccount | False | PaymentPartyRole | CashAccount | Payment/PartyRole/(as DebtorRole)/CashAccount |
| PaymentInstruction44 | DebtorAgent | Organisation | False | Organisation | OrganisationIdentification | Payment/PartyRole/(as DebtorAgentRole)/Player/(as Organisation)/OrganisationIdentification |
| PaymentInstruction44 | DebtorAgentAccount | CashAccount | False | PaymentPartyRole | CashAccount | Payment/PartyRole/(as DebtorAgentRole)/CashAccount |
| PaymentInstruction44 | InstructionForDebtorAgent | NaN | False | Payment | InstructionForDebtorAgent | Payment/InstructionForDebtorAgent |
| PaymentInstruction44 | NumberOfTransactions | NaN | True | NaN | NaN | NaN |
| PaymentInstruction44 | PaymentInformationIdentification | NaN | False | TradeIdentification | Identification | Payment/PaymentRelatedIdentifications/Identification |
| PaymentInstruction44 | PaymentMethod | NaN | False | CreditInstrument | Method | Payment/CreditMethod/Method |
| PaymentInstruction44 | PaymentTypeInformation | PaymentProcessing | False | PaymentExecution | ProcessingInstructions | ProcessingInstructions |
| PaymentInstruction44 | PoolingAdjustmentDate | NaN | False | Payment | PoolingAdjustmentDate | Payment/PoolingAdjustmentDate |
| PaymentInstruction44 | RequestedAdviceType | PaymentProcessing | True | NaN | NaN | NaN |
| PaymentInstruction44 | RequestedExecutionDate | NaN | False | PaymentExecution | RequestedExecutionDate | RequestedExecutionDate |
| PaymentInstruction44 | UltimateDebtor | PartyIdentificationInformation | False | Party | Identification | Payment/PaymentObligation/PartyRole/Player/(as Party)/Identification |
| PaymentInstruction45 | NaN | NaN | False | PaymentInstruction | NaN | NaN |
| PaymentInstruction45 | BatchBooking | NaN | True | NaN | NaN | NaN |
| PaymentInstruction45 | ChargeBearer | NaN | False | Charges | BearerType | Payment/Adjustments/(as Charges)/BearerType |
| PaymentInstruction45 | ChargesAccount | CashAccount | False | Charges | ChargesDebitAccount | Payment/Adjustments/(as Charges)/BearerType |
| PaymentInstruction45 | ChargesAccountAgent | Organisation | False | Organisation | OrganisationIdentification | Payment/Adjustments/(as Charges)/ChargesPartyRole/(as ChargeAccountAgent)/Player/(as Organisation)/OrganisationIdentification |
| PaymentInstruction45 | ControlSum | NaN | True | NaN | NaN | NaN |
| PaymentInstruction45 | Creditor | PartyIdentificationInformation | False | Party | Identification | Payment/PartyRole/(as CreditorRole)/Player/(as Party)/Identification |
| PaymentInstruction45 | CreditorAccount | CashAccount | False | PaymentPartyRole | CashAccount | Payment/PartyRole/(as CreditorRole)/CashAccount |
| PaymentInstruction45 | CreditorAgent | Organisation | False | Party | Identification | Payment/PartyRole/(as CreditorAgentRole)/Player/(as Party)/Identification |
| PaymentInstruction45 | CreditorAgentAccount | CashAccount | False | PaymentPartyRole | CashAccount | Payment/PartyRole/(as CreditorAgentRole)/CashAccount |
| PaymentInstruction45 | CreditorSchemeIdentification | PartyIdentificationInformation | False | Party | Identification | Payment/PartyRole/(as CreditorRole)/Player/(as Party)/Identification |
| PaymentInstruction45 | DirectDebitTransactionInformation | DirectDebit | False | NaN | NaN | Payment/(as DirectDebit) |
| PaymentInstruction45 | NumberOfTransactions | NaN | True | NaN | NaN | NaN |
| PaymentInstruction45 | PaymentInformationIdentification | NaN | False | TradeIdentification | Identification | Payment/PaymentRelatedIdentifications/Identification |
| PaymentInstruction45 | PaymentMethod | NaN | False | CreditInstrument | Method | Payment/CreditMethod/Method |
| PaymentInstruction45 | PaymentTypeInformation | PaymentProcessing | False | PaymentExecution | ProcessingInstructions | ProcessingInstructions |
| PaymentInstruction45 | RequestedAdviceType | PaymentProcessing | True | NaN | NaN | NaN |
| PaymentInstruction45 | RequestedCollectionDate | NaN | False | PaymentExecution | RequestedExecutionDate | RequestedExecutionDate |
| PaymentInstruction45 | UltimateCreditor | PartyIdentificationInformation | False | Party | Identification | Payment/PaymentObligation/PartyRole/(as UltimateCreditorRole)/Player/(as Party)/Identification |
| PaymentReversalReason10 | NaN | NaN | False | StatusReason | NaN | NaN |
| PaymentReversalReason10 | AdditionalInformation | NaN | False | StatusReason | Reason | Reason |
| PaymentReversalReason10 | Originator | PartyIdentificationInformation | False | Party | Identification | Status/PartyRole/(as StatusOriginator)/Player/(as Party)/Identification |
| PaymentReversalReason10 | Reason | PaymentStatus | False | NaN | NaN | . |
| PaymentTransaction156 | NaN | NaN | False | Payment | NaN | NaN |
| PaymentTransaction156 | ChargeBearer | NaN | False | Charges | BearerType | Adjustments/(as Charges)/BearerType |
| PaymentTransaction156 | OriginalEndToEndIdentification | NaN | False | PaymentIdentification | EndToEndIdentification | PaymentRelatedIdentifications/EndToEndIdentification |
| PaymentTransaction156 | OriginalInstructedAmount | NaN | False | Payment | InstructedAmount | InstructedAmount |
| PaymentTransaction156 | OriginalInstructionIdentification | NaN | False | PaymentIdentification | InstructionIdentification | PaymentRelatedIdentifications/InstructionIdentification |
| PaymentTransaction156 | OriginalTransactionReference | Payment | False | NaN | NaN | . |
| PaymentTransaction156 | OriginalUETR | NaN | False | PaymentIdentification | UETR | PaymentRelatedIdentifications/UETR |
| PaymentTransaction156 | ReversalIdentification | NaN | True | NaN | NaN | NaN |
| PaymentTransaction156 | ReversalReasonInformation | StatusReason | False | Status | StatusReason | PaymentStatus/StatusReason |
| PaymentTransaction156 | ReversedInstructedAmount | NaN | False | Payment | InstructedAmount | InstructedAmount |
| PaymentTransaction156 | SupplementaryData | NaN | True | NaN | NaN | NaN |
| PaymentTransaction160 | NaN | NaN | False | Payment | NaN | NaN |
| PaymentTransaction160 | AcceptanceDateTime | NaN | False | PaymentExecution | AcceptanceDateTime | PaymentExecution/AcceptanceDateTime |
| PaymentTransaction160 | AccountServicerReference | NaN | False | Entry | AccountServicerTransactionIdentification | CreditMethod/(as BookEntry)/CashEntry/AccountServicerTransactionIdentification |
| PaymentTransaction160 | ChargesInformation | Charges | False | NaN | NaN | Adjustments/(as Charges)/BearerType |
| PaymentTransaction160 | ClearingSystemReference | NaN | False | PaymentIdentification | ClearingSystemReference | PaymentRelatedIdentifications/ClearingSystemReference |
| PaymentTransaction160 | OriginalEndToEndIdentification | NaN | False | PaymentIdentification | EndToEndIdentification | PaymentRelatedIdentifications/EndToEndIdentification |
| PaymentTransaction160 | OriginalInstructionIdentification | NaN | False | PaymentIdentification | InstructionIdentification | PaymentRelatedIdentifications/InstructionIdentification |
| PaymentTransaction160 | OriginalTransactionReference | Payment | False | NaN | NaN | . |
| PaymentTransaction160 | OriginalUETR | NaN | False | PaymentIdentification | UETR | PaymentRelatedIdentifications/UETR |
| PaymentTransaction160 | StatusIdentification | NaN | True | NaN | NaN | NaN |
| PaymentTransaction160 | StatusReasonInformation | PaymentStatus | False | Status | StatusReason | PaymentStatus/StatusReason |
| PaymentTransaction160 | SupplementaryData | NaN | True | NaN | NaN | NaN |
| PaymentTransaction160 | TrackerData | PaymentTracker | False | NaN | NaN | PaymentExecution/CurrencyExchange/RelatedPaymentTracker/. |
| PaymentTransaction160 | TransactionStatus | NaN | False | Payment | PaymentStatus | PaymentStatus |
| PaymentTypeInformation26 | NaN | NaN | False | PaymentProcessing | NaN | NaN |
| PaymentTypeInformation26 | CategoryPurpose | Payment | False | PaymentProcessing | CategoryPurpose | CategoryPurpose |
| PaymentTypeInformation26 | InstructionPriority | NaN | False | PaymentProcessing | Priority | Priority |
| PaymentTypeInformation26 | LocalInstrument | PaymentProcessing | False | PaymentProcessing | LocalInstrument | LocalInstrument |
| PaymentTypeInformation26 | ServiceLevel | ServiceLevel | False | PaymentProcessing | ServiceLevel | ServiceLevel |
| PaymentTypeInformation27 | NaN | NaN | False | PaymentProcessing | NaN | NaN |
| PaymentTypeInformation27 | CategoryPurpose | Payment | False | PaymentProcessing | CategoryPurpose | CategoryPurpose |
| PaymentTypeInformation27 | ClearingChannel | NaN | False | PaymentProcessing | ClearingChannel | ClearingChannel |
| PaymentTypeInformation27 | InstructionPriority | NaN | False | PaymentProcessing | Priority | Priority |
| PaymentTypeInformation27 | LocalInstrument | PaymentProcessing | False | PaymentProcessing | LocalInstrument | NaN |
| PaymentTypeInformation27 | SequenceType | NaN | False | PaymentProcessing | SequenceType | NaN |
| PaymentTypeInformation27 | ServiceLevel | ServiceLevel | False | PaymentProcessing | ServiceLevel | ServiceLevel |
| PaymentTypeInformation29 | NaN | NaN | False | PaymentProcessing | NaN | NaN |
| PaymentTypeInformation29 | CategoryPurpose | Payment | False | PaymentProcessing | CategoryPurpose | CategoryPurpose |
| PaymentTypeInformation29 | InstructionPriority | NaN | False | PaymentProcessing | Priority | Priority |
| PaymentTypeInformation29 | LocalInstrument | PaymentProcessing | False | PaymentProcessing | LocalInstrument | NaN |
| PaymentTypeInformation29 | SequenceType | NaN | False | PaymentProcessing | SequenceType | NaN |
| PaymentTypeInformation29 | ServiceLevel | ServiceLevel | False | PaymentProcessing | ServiceLevel | ServiceLevel |
| PersonIdentification18 | NaN | NaN | False | PersonIdentification | NaN | NaN |
| PersonIdentification18 | DateAndPlaceOfBirth | Person | False | PersonIdentification | Person | Person |
| PersonIdentification18 | Other | PersonIdentification | False | PartyIdentificationInformation | OtherIdentification | OtherIdentification |
| PersonIdentificationSchemeName1Choice | NaN | NaN | False | PersonIdentification | NaN | NaN |
| PersonIdentificationSchemeName1Choice | Code | NaN | False | Scheme | Code | OtherIdentification/Scheme/Code |
| PersonIdentificationSchemeName1Choice | Proprietary | NaN | False | Scheme | NameShort | OtherIdentification/Scheme/NameShort |
| PostalAddress27 | NaN | NaN | False | PostalAddress | NaN | NaN |
| PostalAddress27 | AddressLine | NaN | True | NaN | NaN | NaN |
| PostalAddress27 | AddressType | NaN | False | PostalAddress | AddressType | AddressType |
| PostalAddress27 | BuildingName | NaN | False | PostalAddress | BuildingName | BuildingName |
| PostalAddress27 | BuildingNumber | NaN | False | PostalAddress | StreetBuildingIdentification | StreetBuildingIdentification |
| PostalAddress27 | CareOf | NaN | False | PostalAddress | CareOf | CareOf |
| PostalAddress27 | Country | NaN | False | Country | Code | Country/Code |
| PostalAddress27 | CountrySubDivision | NaN | False | CountrySubDivision | State | Country/SubDivision/State |
| PostalAddress27 | Department | NaN | False | PostalAddress | Department | Department |
| PostalAddress27 | DistrictName | NaN | False | CountrySubDivision | District | Country/SubDivision/District |
| PostalAddress27 | Floor | NaN | False | PostalAddress | Floor | Floor |
| PostalAddress27 | PostBox | NaN | False | PostalAddress | PostOfficeBox | PostOfficeBox |
| PostalAddress27 | PostCode | NaN | False | PostalAddress | PostCodeIdentification | PostCodeIdentification |
| PostalAddress27 | Room | NaN | False | PostalAddress | SuiteIdentification | SuiteIdentification |
| PostalAddress27 | StreetName | NaN | False | PostalAddress | StreetName | StreetName |
| PostalAddress27 | SubDepartment | NaN | False | PostalAddress | SubDepartment | SubDepartment |
| PostalAddress27 | TownLocationName | NaN | False | NaN | NaN | Country/SubDivision/DistrictSubDivision/. |
| PostalAddress27 | TownName | NaN | False | PostalAddress | TownName | TownName |
| PostalAddress27 | UnitNumber | NaN | False | PostalAddress | UnitNumber | UnitNumber |
| ProxyAccountIdentification1 | NaN | NaN | False | AccountIdentification | NaN | NaN |
| ProxyAccountIdentification1 | Identification | NaN | False | GenericIdentification | Identification | ProprietaryIdentification/Identification |
| ProxyAccountIdentification1 | Type | Scheme | False | GenericIdentification | Scheme | ProprietaryIdentification/Scheme |
| ProxyAccountType1Choice | NaN | NaN | False | Scheme | NaN | NaN |
| ProxyAccountType1Choice | Code | NaN | False | Scheme | Code | Code |
| ProxyAccountType1Choice | Proprietary | NaN | False | Scheme | Code | Code |
| Purpose2Choice | NaN | NaN | False | PaymentObligation | NaN | NaN |
| Purpose2Choice | Code | NaN | False | PaymentObligation | Purpose | Purpose |
| Purpose2Choice | Proprietary | NaN | False | PaymentObligation | Purpose | Purpose |
| ReferredDocumentInformation8 | NaN | NaN | False | Document | NaN | NaN |
| ReferredDocumentInformation8 | LineDetails | Document | False | NaN | NaN | . |
| ReferredDocumentInformation8 | Number | NaN | False | GenericIdentification | Identification | DocumentIdentification/Identification |
| ReferredDocumentInformation8 | RelatedDate | NaN | False | Document | IssueDate | IssueDate |
| ReferredDocumentInformation8 | Type | Document | False | Document | Type | Type |
| RegulatoryAuthority2 | NaN | NaN | False | RegulatoryAuthorityRole | NaN | NaN |
| RegulatoryAuthority2 | Country | NaN | False | Country | Code | Country/Code |
| RegulatoryAuthority2 | Name | NaN | False | PartyName | Name | Player/(as Party)/Identification/PartyName/Name |
| RegulatoryReporting3 | NaN | NaN | False | RegulatoryReport | NaN | NaN |
| RegulatoryReporting3 | Authority | RegulatoryAuthorityRole | False | RegulatoryReport | Authority | Authority |
| RegulatoryReporting3 | DebitCreditReportingIndicator | NaN | False | RegulatoryReport | DebitCreditReportingIndicator | DebitCreditReportingIndicator |
| RegulatoryReporting3 | Details | RegulatoryReport | False | NaN | NaN | . |
| RemittanceAmount4 | NaN | NaN | False | Document | NaN | NaN |
| RemittanceAmount4 | AdjustmentAmountAndReason | Adjustment | False | Payment | Adjustments | PaymentObligation/PaymentOffset/Adjustments |
| RemittanceAmount4 | RemittanceAmountAndType | Adjustment | False | Document | Amount | Amount |
| RemittanceInformation22 | NaN | NaN | False | Document | NaN | NaN |
| RemittanceInformation22 | Structured | Document | False | NaN | NaN | . |
| RemittanceInformation22 | Unstructured | NaN | False | NaN | NaN | . |
| RemittanceLocation8 | NaN | NaN | False | ContactPoint | NaN | NaN |
| RemittanceLocation8 | RemittanceIdentification | NaN | True | NaN | NaN | NaN |
| RemittanceLocation8 | RemittanceLocationDetails | ContactPoint | False | NaN | NaN | . |
| RemittanceLocationData2 | NaN | NaN | False | ContactPoint | NaN | NaN |
| RemittanceLocationData2 | ElectronicAddress | NaN | False | NaN | NaN | (as ElectronicAddress) |
| RemittanceLocationData2 | Method | NaN | False | PaymentObligation | RemittanceDeliveryMethod | RemittanceRelatedPayment/RemittanceDeliveryMethod |
| RemittanceLocationData2 | PostalAddress | PartyIdentificationInformation | False | NaN | NaN | (as PostalAddress) |
| ReversalReason4Choice | NaN | NaN | False | PaymentStatus | NaN | NaN |
| ReversalReason4Choice | Code | NaN | False | PaymentStatus | TransactionRejectionReason | TransactionRejectionReason |
| ReversalReason4Choice | Proprietary | NaN | False | PaymentStatus | TransactionRejectionReason | TransactionRejectionReason |
| ServiceLevel8Choice | NaN | NaN | False | ServiceLevel | NaN | NaN |
| ServiceLevel8Choice | Code | NaN | False | ServiceLevel | Code | Code |
| ServiceLevel8Choice | Proprietary | NaN | False | NaN | NaN | . |
| SettlementInstruction15 | NaN | NaN | False | CashSettlement | NaN | NaN |
| SettlementInstruction15 | ClearingSystem | CashClearingSystem | False | NaN | NaN | PartyRole/(as SettlementInstructionSystemRole) |
| SettlementInstruction15 | InstructedReimbursementAgent | Organisation | False | NaN | NaN | PartyRole/(as InstructedReimbursementAgent) |
| SettlementInstruction15 | InstructedReimbursementAgentAccount | CashAccount | False | CashSettlementInstructionPartyRole | CashAccount | PartyRole/(as InstructedReimbursementAgent)/CashAccount |
| SettlementInstruction15 | InstructingReimbursementAgent | Organisation | False | Organisation | OrganisationIdentification | PartyRole/(as InstructingReimbursementAgent)/Player/(as FinancialInstitution)/OrganisationIdentification |
| SettlementInstruction15 | InstructingReimbursementAgentAccount | CashAccount | False | CashSettlementInstructionPartyRole | CashAccount | PartyRole/(as InstructingReimbursementAgent)/CashAccount |
| SettlementInstruction15 | SettlementAccount | CashAccount | False | CashSettlement | SettlementAccount | SettlementAccount |
| SettlementInstruction15 | SettlementMethod | NaN | False | CashSettlement | SettlementMethod | SettlementMethod |
| SettlementInstruction15 | ThirdReimbursementAgent | Organisation | False | Party | Identification | PartyRole/(as ThirdReimbursementAgent) |
| SettlementInstruction15 | ThirdReimbursementAgentAccount | CashAccount | False | CashSettlementInstructionPartyRole | CashAccount | PartyRole/(as ThirdReimbursementAgent)/CashAccount |
| StatusReason6Choice | NaN | NaN | False | StatusReason | NaN | NaN |
| StatusReason6Choice | Code | NaN | False | StatusReason | Reason | Reason |
| StatusReason6Choice | Proprietary | NaN | False | StatusReason | Reason | Reason |
| StatusReasonInformation14 | NaN | NaN | False | PaymentStatus | NaN | NaN |
| StatusReasonInformation14 | AdditionalInformation | NaN | False | Status | StatusDescription | StatusDescription |
| StatusReasonInformation14 | Originator | PartyIdentificationInformation | False | Party | Identification | PartyRole/(as StatusOriginator)/Player/(as Party)/Identification |
| StatusReasonInformation14 | Reason | StatusReason | False | Status | StatusReason | StatusReason |
| StructuredRegulatoryReporting3 | NaN | NaN | False | RegulatoryReport | NaN | NaN |
| StructuredRegulatoryReporting3 | Amount | NaN | False | RegulatoryReport | Amount | Amount |
| StructuredRegulatoryReporting3 | Code | NaN | False | RegulatoryReport | Code | Code |
| StructuredRegulatoryReporting3 | Country | NaN | False | Country | Code | Authority/Country/Code |
| StructuredRegulatoryReporting3 | Date | NaN | False | RegulatoryReport | Date | Date |
| StructuredRegulatoryReporting3 | Information | NaN | False | RegulatoryReport | Description | Description |
| StructuredRegulatoryReporting3 | Type | NaN | False | RegulatoryReport | Type | Type |
| StructuredRemittanceInformation18 | NaN | NaN | False | Document | NaN | NaN |
| StructuredRemittanceInformation18 | AdditionalRemittanceInformation | NaN | False | NaN | NaN | . |
| StructuredRemittanceInformation18 | CreditorReferenceInformation | PaymentIdentification | False | PaymentIdentification | CreditorReference | PaymentObligation/PaymentOffset/PaymentRelatedIdentifications/CreditorReference |
| StructuredRemittanceInformation18 | GarnishmentRemittance | Garnishment | False | NaN | NaN | PaymentObligation/(as Garnishment) |
| StructuredRemittanceInformation18 | Invoicee | PartyIdentificationInformation | False | NaN | NaN | (as Invoice)/InvoicePartyRole/(as InvoiceeRole) |
| StructuredRemittanceInformation18 | Invoicer | PartyIdentificationInformation | False | Party | Identification | (as Invoice)/InvoicePartyRole/(as InvoicerRole)/Player/(as Party)/Identification |
| StructuredRemittanceInformation18 | ReferredDocumentAmount | Document | False | Document | Amount | Amount |
| StructuredRemittanceInformation18 | ReferredDocumentInformation | Document | False | NaN | NaN | . |
| StructuredRemittanceInformation18 | TaxRemittance | Tax | False | Payment | TaxOnPayment | PaymentObligation/PaymentOffset/TaxOnPayment |
| SupplementaryData1 | NaN | NaN | True | NaN | NaN | NaN |
| SupplementaryData1 | Envelope | NaN | True | NaN | NaN | NaN |
| SupplementaryData1 | PlaceAndName | NaN | True | NaN | NaN | NaN |
| TaxAmount3 | NaN | NaN | False | Tax | NaN | NaN |
| TaxAmount3 | Details | Tax | True | NaN | NaN | NaN |
| TaxAmount3 | Rate | NaN | False | Tax | Rate | NaN |
| TaxAmount3 | TaxableBaseAmount | NaN | False | Tax | TaxableBaseAmount | NaN |
| TaxAmount3 | TotalAmount | NaN | False | Tax | Amount | NaN |
| TaxAuthorisation1 | NaN | NaN | False | TaxPartyRole | NaN | NaN |
| TaxAuthorisation1 | Name | NaN | False | PartyName | Name | NaN |
| TaxAuthorisation1 | Title | NaN | False | Person | BusinessFunctionTitle | NaN |
| TaxData1 | NaN | NaN | False | Tax | NaN | NaN |
| TaxData1 | AdministrationZone | NaN | False | Tax | AdministrationZone | AdministrationZone |
| TaxData1 | Creditor | TaxPartyRole | False | NaN | NaN | PartyRole/(as CreditSideTaxDebtor) |
| TaxData1 | Date | NaN | False | Tax | TaxDate | TaxDate |
| TaxData1 | Debtor | TaxPartyRole | False | NaN | NaN | PartyRole/(as DebitSideTaxDebtor) |
| TaxData1 | Method | NaN | False | Tax | Method | Method |
| TaxData1 | Record | TaxRecord | False | Tax | Record | Record |
| TaxData1 | ReferenceNumber | NaN | False | Tax | Identification | Identification |
| TaxData1 | SequenceNumber | NaN | True | NaN | NaN | NaN |
| TaxData1 | TotalTaxableBaseAmount | NaN | False | Tax | TaxableBaseAmount | TaxableBaseAmount |
| TaxData1 | TotalTaxAmount | NaN | False | Tax | Amount | Amount |
| TaxData1 | UltimateDebtor | TaxPartyRole | False | Party | Identification | RelatedPaymentSettlement/PaymentObligation/PartyRole/Player/(as Party)/Identification |
| TaxParty1 | NaN | NaN | False | TaxPartyRole | NaN | NaN |
| TaxParty1 | RegistrationIdentification | NaN | False | PartyIdentificationInformation | TaxIdentificationNumber | Player/(as Party)/Identification/TaxIdentificationNumber |
| TaxParty1 | TaxIdentification | NaN | False | PartyIdentificationInformation | TaxIdentificationNumber | Player/(as Party)/Identification/TaxIdentificationNumber |
| TaxParty1 | TaxType | NaN | False | NaN | NaN | (as TaxPayer) |
| TaxParty2 | NaN | NaN | False | TaxPartyRole | NaN | NaN |
| TaxParty2 | Authorisation | TaxPartyRole | False | NaN | NaN | . |
| TaxParty2 | RegistrationIdentification | NaN | False | PartyIdentificationInformation | TaxIdentificationNumber | Player/(as Party)/Identification/TaxIdentificationNumber |
| TaxParty2 | TaxIdentification | NaN | False | PartyIdentificationInformation | TaxIdentificationNumber | Player/(as Party)/Identification/TaxIdentificationNumber |
| TaxParty2 | TaxType | NaN | False | NaN | NaN | (as TaxPayer) |
| TaxPeriod3 | NaN | NaN | False | TaxPeriod | NaN | NaN |
| TaxPeriod3 | FromToDate | NaN | False | TaxPeriod | FromToDate | NaN |
| TaxPeriod3 | Type | NaN | False | TaxPeriod | Type | NaN |
| TaxPeriod3 | Year | NaN | False | TaxPeriod | Year | NaN |
| TaxRecord3 | NaN | NaN | False | TaxRecord | NaN | NaN |
| TaxRecord3 | AdditionalInformation | NaN | True | NaN | NaN | NaN |
| TaxRecord3 | Category | NaN | False | TaxRecord | Category | Category |
| TaxRecord3 | CategoryDetails | NaN | True | NaN | NaN | NaN |
| TaxRecord3 | CertificateIdentification | NaN | False | Tax | CertificateIdentification | Tax/CertificateIdentification |
| TaxRecord3 | DebtorStatus | NaN | False | TaxRecord | Status | Status |
| TaxRecord3 | FormsCode | NaN | False | TaxRecord | FormsCode | FormsCode |
| TaxRecord3 | Period | TaxPeriod | False | TaxRecord | Period | Period |
| TaxRecord3 | TaxAmount | Tax | False | TaxRecord | Tax | Tax |
| TaxRecord3 | Type | NaN | False | TaxRecord | TaxRecordType | TaxRecordType |
| TaxRecordDetails3 | NaN | NaN | False | Tax | NaN | NaN |
| TaxRecordDetails3 | Amount | NaN | False | Tax | Amount | NaN |
| TaxRecordDetails3 | Period | TaxPeriod | True | NaN | NaN | NaN |
| TrackerData7 | NaN | NaN | False | PaymentTracker | NaN | NaN |
| TrackerData7 | ConfirmedAmount | NaN | False | PaymentTracker | ChargesAmount | ChargesAmount |
| TrackerData7 | ConfirmedDate | NaN | False | CurrencyExchange | QuotationDate | ExchangeRateData/QuotationDate |
| TrackerData7 | TrackerRecord | PaymentTracker | False | NaN | NaN | . |
| TrackerRecord5 | NaN | NaN | False | PaymentTracker | NaN | NaN |
| TrackerRecord5 | Agent | Organisation | False | PaymentTracker | Agent | Agent |
| TrackerRecord5 | ChargeBearer | NaN | False | PaymentTracker | ChargeBearer | ChargeBearer |
| TrackerRecord5 | ChargesAmount | NaN | False | PaymentTracker | ChargesAmount | ChargesAmount |
| TrackerRecord5 | ExchangeRateData | CurrencyExchange | False | PaymentTracker | ExchangeRateData | ExchangeRateData |

## PaymentsInitiation
|
|  |