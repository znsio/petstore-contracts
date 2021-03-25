Feature: Petstore SOAP API
	Background:
		Given type Request
		"""
		<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
			<SOAP-ENV:Header/>
			<SOAP-ENV:Body>(RequestPayload)</SOAP-ENV:Body>
		</SOAP-ENV:Envelope>
		"""
		Given type Response
		"""
		<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
			<SOAP-ENV:Header/>
			<SOAP-ENV:Body>(ResponsePayload)</SOAP-ENV:Body>
		</SOAP-ENV:Envelope>
		"""
		When POST /ws
		And request-body (Request)
		Then status 200
		And response-body (Response)

	Scenario Outline: Get Pet Info
		* type RequestPayload
		"""
		<ns2:GetPetRequest xmlns:ns2="http://qontract.run/petstore/api">
			<ns2:id>(number)</ns2:id>
		</ns2:GetPetRequest>
		"""
		* type ResponsePayload
		"""
		<ns2:GetPetResponse xmlns:ns2="http://qontract.run/petstore/api">
			<ns2:id>(number)</ns2:id>
			<ns2:name>(string)</ns2:name>
			<ns2:type>(string)</ns2:type>
			<ns2:status>(string)</ns2:status>
		</ns2:GetPetResponse>
		"""

		Examples:
		| id |
		| 1  |

	Scenario Outline: Add Pet
		* type RequestPayload
		"""
		<ns2:AddPetRequest xmlns:ns2="http://qontract.run/petstore/api">
			<ns2:name>(string)</ns2:name>
			<ns2:type>(string)</ns2:type>
			<ns2:status>(string)</ns2:status>
		</ns2:AddPetRequest>
		"""
		* type ResponsePayload
		"""
		<ns2:AddPetResponse xmlns:ns2="http://qontract.run/petstore/api">
			<ns2:id>(number)</ns2:id>
		</ns2:AddPetResponse>
		"""

		Examples:
		| name   | type | status    |
		| Archie | dog  | available |

	Scenario Outline: Search Pets
		* type RequestPayload
		"""
		<ns2:SearchRequest xmlns:ns2="http://qontract.run/petstore/api">
			<ns2:name>(string)</ns2:name>
			<ns2:type>(string)</ns2:type>
			<ns2:status>(string)</ns2:status>
		</ns2:SearchRequest>
		"""
		* type Pet
		"""
		<ns2:Pet>
			<ns2:id>(number)</ns2:id>
			<ns2:name>(string)</ns2:name>
			<ns2:type>(string)</ns2:type>
			<ns2:status>(string)</ns2:status>
		</ns2:Pet>
		"""
		* type ResponsePayload
		"""
		<ns2:SearchResponse xmlns:ns2="http://qontract.run/petstore/api">(Pet*)</ns2:SearchResponse>
		"""

		Examples:
		| name   | type | status    |
		| Archie |      |           |
		|        | dog  |           |
		|        |      | available |
